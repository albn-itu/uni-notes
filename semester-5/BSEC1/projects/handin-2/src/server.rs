// Server takes the role of Bob

use tonic::{transport::Server, Request, Response, Status};

use communication::communication_server::{Communication, CommunicationServer};
use communication::{PedersenInitRequest, PedersenInitReply};

pub mod communication {
    tonic::include_proto!("communication"); // The string specified here must match the proto package name
}

use crate::pedersen::PedersenInitData;

#[derive(Debug, Default)]
pub struct MyCommunication {
    pedersen_init_data: PedersenInitData,
}

#[tonic::async_trait]
impl Communication for MyCommunication {
    async fn init_pedersen(
        &mut self,
        request: Request<PedersenInitRequest>,
    ) -> Result<Response<PedersenInitReply>, Status> {
        println!("Got a request: {:?}", request);

        let request_data = request.into_inner();

        self.pedersen_init_data = PedersenInitData {
            h: request_data.h,
            g: request_data.g,
            p: request_data.p,
        };

        let reply = PedersenInitReply {
            ack: true
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
