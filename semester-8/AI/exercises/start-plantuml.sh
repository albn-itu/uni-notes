#!/usr/bin/env bash

sudo systemctl start docker
docker run -d -p 8080:8080 plantuml/plantuml-server:jetty --name plantuml-server
