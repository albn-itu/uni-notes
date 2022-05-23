docker run \
  --name dsv-data-mongo \
  -v /home/goose/Documents/Uni/semester-4/ise/exercises/data/mongo:/data/db \
  -v /home/goose/Documents/Uni/semester-4/ise/exercises/data:/tmp/hostData \
  -p 8027:27017 \
  -d \
  mongo:latest

