// Client takes the role of Alice

use communication::communication_client::CommunicationClient;
use communication::PedersenInitRequest;

pub mod communication {
    tonic::include_proto!("communication");
}

use crate::pedersen::gen_data;

pub async fn run(connect: String) -> Result<(), Box<dyn std::error::Error>> {
    let mut client = CommunicationClient::connect(connect).await?;

    let pedersen_data = gen_data();

    let request = tonic::Request::new(PedersenInitRequest {
        h: pedersen_data.h,
        g: pedersen_data.g,
        p: pedersen_data.p,
    });

    let response = client.init_pedersen(request).await?;

    println!("RESPONSE={:?}", response);

    Ok(())
}
