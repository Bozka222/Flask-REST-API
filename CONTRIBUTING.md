# Contributing

## How to run Docker file locally

On third row add `EXPOSE 5000` or any other port on which you want to run app.
Change command with CMD `["flask", "run", "--host", "0.0.0.0"]`

Build docker image with:  
`docker build -t <IMAGE_NAME> .`  
Run docker container with:  
`docker run -dp 5000:5000 -w /app -v "$(pwd):/app" <IMAGE_NAME>`

Or just use:  
`docker run -dp 5000:5000 -w /app -v "$(pwd):/app" <IMAGE_NAME> sh  -c "flask run --host 0.0.0.0"`

Docker compose command:  
`docker compose up`  
`docker compose up --build --force-recreate --no-deps web`  
`docker compose up --build --force-recreate --no-deps db`

## How to migrate database
`flask db init`  
`flask db migrate`  
`flask db upgrade`

## Locally run docker compose and local postgres db inside it
Send HTTP requests to:  
http://127.0.0.1:5000

## Deployment is on render.com with docker and postgres db
https://flask-rest-api-0pb1.onrender.com