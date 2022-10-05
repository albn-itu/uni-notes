use clap::Parser;
mod server;
mod client;

#[derive(Parser, Debug)]
#[command(author, version, about, long_about = None)]
struct Args {
   #[arg(short, long)]
   listen: Option<String>,

   #[arg(short, long)]
   connect: Option<String>,
}

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let args = Args::parse();

    if args.listen.is_some() && args.connect.is_none() {
        server::run(args.listen.unwrap()).await?;
    } else if args.listen.is_none() && args.connect.is_some() {
        client::run(args.connect.unwrap()).await?;
    } else {
        eprintln!("You must supply exactly one of connect or listen.");
        std::process::exit(1);
    }

    Ok(())
}
