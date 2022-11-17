use tonic::{Response, Request};

pub fn handle_response<T: std::fmt::Debug>(response: Response<T>) -> T {
    let metadata = response.metadata().clone();
    let date = metadata.get("date").unwrap();
    let code = metadata.get("grpc-status").unwrap();
    let data = response.into_inner();

    println!("[{:?}][Code: {:?}] {:?}", date, code, data);

    data
}

pub fn handle_request<T: std::fmt::Debug>(request: Request<T>) -> T {
    let date = chrono::Local::now();
    let data = request.into_inner();

    println!("[{}] {:?}", date, data);

    data
}
