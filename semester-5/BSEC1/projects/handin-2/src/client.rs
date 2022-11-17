// Client takes the role of Alice

use std::panic::UnwindSafe;

use tonic::transport::Identity;
use tonic::transport::{Certificate, ClientTlsConfig, Channel};

use communication::communication_client::CommunicationClient;
use communication::InitPedersenRequest;
use communication::SendCommitmentRequest;
use communication::SendPedersenRequest;

pub mod communication {
    tonic::include_proto!("communication");
}

use crate::pedersen::gen_data;
use crate::messages::handle_response;

pub async fn create_client(connect: String) -> Result<Channel, Box<dyn std::error::Error>> {
    let ca_cert = tokio::fs::read("data/ca-cert.pem").await?;
    let client_cert = tokio::fs::read("data/client-cert.pem").await?;
    let client_key = tokio::fs::read("data/client-key.pem").await?;

    let ca = Certificate::from_pem(ca_cert);
    let id = Identity::from_pem(client_cert, client_key);

    let tls = ClientTlsConfig::new()
        .identity(id)
        .ca_certificate(ca)
        .domain_name("bob.com");

    Ok(Channel::builder(connect.parse::<tonic::transport::Uri>().unwrap())
        .tls_config(tls)?
        .connect()
        .await?)
}

pub async fn run(connect: String) -> Result<(), Box<dyn std::error::Error>> {
    let channel = create_client(connect).await?;
    let mut client = CommunicationClient::new(channel);

    let pedersen_data = gen_data();

    let init_request = tonic::Request::new(InitPedersenRequest {
        h: pedersen_data.h,
        g: pedersen_data.g,
        p: pedersen_data.p,
    });

    handle_response(client.init_pedersen(init_request).await?);

    let dice_roll = crate::dice::gen() ;
    let (r, c) = crate::pedersen::com(dice_roll, pedersen_data, None);
    let commit_request = tonic::Request::new(SendCommitmentRequest { c });
    let commit_response = handle_response(client.send_commitment(commit_request).await?);
    let bobs_dice_roll = commit_response.m as crate::dice::Dice;

    let pedersen_request = tonic::Request::new(SendPedersenRequest { 
        r, 
        m: dice_roll as u64
    });
    handle_response(client.send_pedersen(pedersen_request).await?);

    println!("Dice roll result: {}", crate::dice::xor(dice_roll, bobs_dice_roll));

    Ok(())
}
