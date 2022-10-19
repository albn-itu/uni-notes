#!/bin/bash

rm *.pem

function generate_and_sign_cert {
  # Generate private key for the cert
  openssl genrsa -out $1-key.pem 2048

  # Create a CSR (Certificate Signing Request) using the generated key.
  openssl req -new \
    -key $1-key.pem \
    -out $1-csr.pem \
    -subj "/C=DK/ST=Copenhagen/L=Copenhagen/O=$2 Incorporated/OU=$2/CN=$2.com"

  # Generate a new certificate, based on our private key and sign it using the CA
  openssl x509 -req -days 365 -sha256 \
    -out $1-cert.pem \
    -extfile $1.conf \
    -in $1-csr.pem \
    -CA ca-cert.pem \
    -CAkey ca-key.pem \
    -CAcreateserial
}

# Generate a private key and certificate for the CA (Certificate Authority)
# These will be used to selfsign our certificates
openssl req -x509 -sha256 -newkey rsa:4096 -days 365 -nodes \
  -keyout ca-key.pem \
  -out ca-cert.pem \
  -subj "/C=DK/ST=Copenhagen/L=Copenhagen/O=Bob Incorporated/OU=Bob/CN=bob.com"

generate_and_sign_cert server bob
generate_and_sign_cert client alice
