// Client takes the role of Alice

use communication::communication_client::CommunicationClient;
use communication::InitPedersenRequest;
use communication::SendCommitmentRequest;
use communication::SendPedersenRequest;

pub mod communication {
    tonic::include_proto!("communication");
}

use crate::pedersen::gen_data;

pub async fn run(connect: String) -> Result<(), Box<dyn std::error::Error>> {
    let mut client = CommunicationClient::connect(connect).await?;

    let pedersen_data = gen_data();

    let init_request = tonic::Request::new(InitPedersenRequest {
        h: pedersen_data.h,
        g: pedersen_data.g,
        p: pedersen_data.p,
    });

    println!("InitPedersen: RESPONSE={:?}", client.init_pedersen(init_request).await?);

    let dice_roll = crate::dice::gen() ;
    let (r, c) = crate::pedersen::com(dice_roll, pedersen_data, None);
    let commit_request = tonic::Request::new(SendCommitmentRequest { c });
    let commit_response = client.send_commitment(commit_request).await?;
    println!("SendCommitment: RESPONSE={:?}", commit_response);
    let bobs_dice_roll = commit_response.into_inner().m as crate::dice::Dice;

    let pedersen_request = tonic::Request::new(SendPedersenRequest { 
        r, 
        m: dice_roll as u64
    });
    println!("SendPedersen: RESPONSE={:?}", client.send_pedersen(pedersen_request).await?);

    println!("Dice roll result: {}", crate::dice::xor(dice_roll, bobs_dice_roll));

    Ok(())
}
