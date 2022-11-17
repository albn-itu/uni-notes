// Server takes the role of Bob

use std::sync::Mutex;

use tonic::{
    transport::{
        server::{TlsConnectInfo},
        Identity, Server, ServerTlsConfig, Certificate,
    }, 
    Request, Response, Status
};

use communication::communication_server::{Communication, CommunicationServer};
use communication::{InitPedersenRequest, InitPedersenReply};
use communication::{SendCommitmentRequest, SendCommitmentReply};
use communication::{SendPedersenRequest, SendPedersenReply};

pub mod communication {
    tonic::include_proto!("communication"); // The string specified here must match the proto package name
}

use crate::messages::handle_request;
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
        let request_data = handle_request(request);
        
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
        let request_data = handle_request(request);

        let mut state = self.state.lock().unwrap();
        state.c = request_data.c;

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
        let request_data = handle_request(request);
        let state = self.state.lock().unwrap();

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

pub async fn get_tls() -> Result<ServerTlsConfig, Box<dyn std::error::Error>> {
    let ca_cert = tokio::fs::read("data/ca-cert.pem").await?;
    let server_cert = tokio::fs::read("data/server-cert.pem").await?;
    let server_key = tokio::fs::read("data/server-key.pem").await?;

    let ca = Certificate::from_pem(ca_cert);
    let id = Identity::from_pem(server_cert, server_key);

    let tls = ServerTlsConfig::new()
        .identity(id)
        .client_ca_root(ca);

    Ok(tls)
}

pub async fn run(listen: String) -> Result<(), Box<dyn std::error::Error>> {
    let addr = listen.parse()?;
    let communication = MyCommunication::default();

    let tls = get_tls().await?;

    Server::builder()
        .tls_config(tls)?
        .add_service(CommunicationServer::new(communication))
        .serve(addr)
        .await?;

    Ok(())
}
