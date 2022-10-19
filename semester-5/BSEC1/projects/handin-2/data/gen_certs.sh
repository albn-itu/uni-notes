#!/bin/bash

rm *.pem

# Generate CA (Certificate Authority) private key
openssl genrsa 2048 > ca-key.pem

# Generate the x509 certificate for the CA
openssl req -new -x509 -nodes -days 365000 \
   -subj "/C=DK/ST=Copenhagen/L=Copenhagen/O=Bob Incorporated/OU=Bob/CN=bob.com" \
   -key ca-key.pem \
   -out ca-cert.pem

# Generate a private key for the server (-newkey) and create a CSR (Certificate Signing Request) for the server 
openssl req -newkey rsa:2048 -nodes \
   -subj "/C=DK/ST=Copenhagen/L=Copenhagen/O=Bob Incorporated/OU=Bob/CN=bob.com" \
   -keyout server-key.pem \
   -out server-req.pem

# Use the CA to create, sign and approve the servers public key certificate
openssl x509 -req -days 365000 -set_serial 01 \
   -in server-req.pem \
   -out server-cert.pem \
   -CA ca-cert.pem \
   -CAkey ca-key.pem

# Generate a private key for the client (-newkey) and create a CSR (Certificate Signing Request) for the client
openssl req -newkey rsa:2048 -nodes \
   -subj "/C=DK/ST=Copenhagen/L=Copenhagen/O=Bob Incorporated/OU=Bob/CN=bob.com" \
   -keyout client-key.pem \
   -out client-req.pem

# Use the CA to create, sign and approve the clients public key certificate
openssl x509 -req -days 365000 -set_serial 01 \
   -in client-req.pem \
   -out client-cert.pem \
   -CA ca-cert.pem \
   -CAkey ca-key.pem

