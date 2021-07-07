# SlashURL

This is a Node.JS web application powered by Express that provides the main functionality that you'd expect from a URL Shortener service.

## Features
  - Fast
  - Lightweight
  - Minimalistic
  - REST API microservice

## Setup


Clone this repo to your desktop and run `npm install` to install all the dependencies.

You might want to look into `config.js` to make change the port you want to use and any other required


### Build Image Using `Dockerfile`

```shell
docker build -t  node-url-shortner:v1
```

### Deploy Using `docker-compose` in Bridge Network

```shell
docker-compose -f docker-compose-bridge-network.yaml up -d
```


### Deploy In Mesh Network

```shell
docker stack deploy -f docker-compose-mesh-deploy.yaml 
```



### Tech Used

SlashURL uses a number of open source projects to work properly:

* [node.js] - evented I/O for the backend
* [Express] - fast node.js network app framework
* [MongoDB] - cross-platform document oriented database
* [Redis] - open source in-memory database
* [Twitter Bootstrap] - great UI boilerplate for modern web apps
* [jQuery] - duh



Open another terminal and get to the project folder.
Install the dependencies and start the server.

```sh
$ npm install -d
$ npm start
```
You can also use [Nodemon](https://nodemon.io/) using ```nodemon app.js``` instead of npm start every time you make changes in the project.
