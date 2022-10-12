// Client takes the role of Alice

use communication::communication_client::CommunicationClient;
use communication::InitPedersenRequest;
use communication::SendCommitmentRequest;
use communication::SendPedersenRequest;

pub mod communication {
    tonic::include_proto!("communication");
}

use crate::pedersen::gen_data;
use crate::messages::handle_response;

pub async fn run(connect: String) -> Result<(), Box<dyn std::error::Error>> {
    let mut client = CommunicationClient::connect(connect).await?;

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
