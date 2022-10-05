use tonic::{transport::Server, Request, Response, Status};

use communication::communication_server::{Communication, CommunicationServer};
use communication::{HelloRequest, HelloReply};

pub mod communication {
    tonic::include_proto!("communication"); // The string specified here must match the proto package name
}

#[derive(Debug, Default)]
pub struct MyCommunication {}

#[tonic::async_trait]
impl Communication for MyCommunication {
    async fn say_hello(
        &self,
        request: Request<HelloRequest>,
    ) -> Result<Response<HelloReply>, Status> {
        println!("Got a request: {:?}", request);

        let reply = communication::HelloReply {
            message: format!(r#"Hello {}!"#, request.into_inner().name)
        };

        Ok(Response::new(reply))
    }
}

pub async fn run(listen: String) -> Result<(), Box<dyn std::error::Error>> {
    let addr = listen.parse()?;
    let communication = MyCommunication::default();

    Server::builder()
        .add_service(CommunicationServer::new(communication))
        .serve(addr)
        .await?;

    Ok(())
}
