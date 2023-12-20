Running locally (1):

docker build -t channels-backend-api .

docker run -it -p 8001:80 --env-file .env channels-backend-api

Running locally (2):

docker pull --platform linux/x86_64/v8 therealsangwoohan/channels-backend-api

docker run -it -p 8001:80 --env-file .env therealsangwoohan/channels-backend-api