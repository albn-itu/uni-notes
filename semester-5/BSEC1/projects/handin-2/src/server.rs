// Server takes the role of Bob

use std::sync::Mutex;

use tonic::{transport::Server, Request, Response, Status};

use communication::communication_server::{Communication, CommunicationServer};
use communication::{InitPedersenRequest, InitPedersenReply};
use communication::{SendCommitmentRequest, SendCommitmentReply};
use communication::{SendPedersenRequest, SendPedersenReply};

pub mod communication {
    tonic::include_proto!("communication"); // The string specified here must match the proto package name
}

use crate::pedersen::PedersenInitData;

#[derive(Debug, Default)]
pub struct State {
    pub connected: bool,
    pub pedersen_init_data: PedersenInitData,
    pub c: u64,
    pub dice_roll: crate::dice::Dice,
}

#[derive(Debug, Default)]
pub struct MyCommunication {
    pub state: Mutex<State>,
}

#[tonic::async_trait]
impl Communication for MyCommunication {
    async fn init_pedersen(
        &self,
        request: Request<InitPedersenRequest>,
    ) -> Result<Response<InitPedersenReply>, Status> {
        println!("Got a InitPedersen request: {:?}", request);

        let request_data = request.into_inner();
        
        let mut state = self.state.lock().unwrap();
        state.pedersen_init_data = PedersenInitData {
            h: request_data.h,
            g: request_data.g,
            p: request_data.p,
        };

        let reply = InitPedersenReply {
            ack: true
        };

        Ok(Response::new(reply))
    }

    async fn send_commitment(
        &self,
        request: Request<SendCommitmentRequest>,
    ) -> Result<Response<SendCommitmentReply>, Status> {
        println!("Got SendCommitment request: {:?}", request);

        let mut state = self.state.lock().unwrap();
        state.c = request.into_inner().c;

        let dice_roll = crate::dice::gen();
        state.dice_roll = dice_roll;

        let reply = SendCommitmentReply {
            m: dice_roll as u64
        };

        Ok(Response::new(reply))
    }

    async fn send_pedersen(
        &self,
        request: Request<SendPedersenRequest>,
    ) -> Result<Response<SendPedersenReply>, Status> {
        println!("Got SendPedersen request: {:?}", request);

        let state = self.state.lock().unwrap();
        let request_data = request.into_inner();

        let (_, c) = crate::pedersen::com(request_data.m as u8, state.pedersen_init_data, Some(request_data.r));

        if c != state.c {
            println!("{} and {} doesn not match", c, state.c);

            return Err(Status::new(tonic::Code::Unauthenticated, "c and state.c does not match"));
        }
        
        println!("Dice game finished: {}", crate::dice::xor(request_data.m as u8, state.dice_roll));

        let reply = SendPedersenReply {
            ack: true
        };

        Ok(Response::new(reply))
    }}

pub async fn run(listen: String) -> Result<(), Box<dyn std::error::Error>> {
    let addr = listen.parse()?;
    let communication = MyCommunication::default();

    Server::builder()
        .add_service(CommunicationServer::new(communication))
        .serve(addr)
        .await?;

    Ok(())
}
