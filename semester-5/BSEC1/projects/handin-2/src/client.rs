use communication::communication_client::CommunicationClient;
use communication::HelloRequest;

pub mod communication {
    tonic::include_proto!("communication");
}

pub async fn run(connect: String) -> Result<(), Box<dyn std::error::Error>> {
    let mut client = CommunicationClient::connect(connect).await?;

    let request = tonic::Request::new(HelloRequest {
        name: "Tonic".into(),
    });

    let response = client.say_hello(request).await?;

    println!("RESPONSE={:?}", response);

    Ok(())
}
