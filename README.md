<p align="center">
  <img src="./assets/api_logo.png" width="150"/>
</p>
<h1 align="center">Plumber API</h1>

<p align="center">
  <a href="https://github.com/pashkatrick/Plumber-API"><img src="https://img.shields.io/badge/Made%20with-Python-1f425f.svg" />  
  <a href="https://github.com/pashkatrick/Plumber"><img src="https://img.shields.io/badge/Build%20with-Electron-1f425f.svg" />
  <a href="https://pshktrck.ru/plumber/">
    <img src="https://img.shields.io/badge/changelog-👈-green.svg" />
  </a>
  <a href="https://t.me/pashkatwit">
    <img src="https://img.shields.io/badge/telegram-🔔-green.svg" />
  </a>  
</p>

## About
That's an API for main project [Plumber RPC](https://github.com/pashkatrick/Plumber-API) which in turn is a GUI for [GRPCurl](https://github.com/fullstorydev/grpcurl). 

## ⚡ Important

> This version doesn't support import proto files or protosets yet (will be).  
> You can use it only with servers, which support reflection API.

### Requirenments

- Docker

## Get Started 🚀

- `docker pull pashkatrick/plumber-api`
- `docker run --rm -it -p 3535:3535/tcp pashkatrick/plumber-api`
- or 
- `docker run --rm -it -p 3636:3636/tcp pashkatrick/plumber-api --http:http --http`  
(if you wanna postman collab)

## Features Basic
...

## Features HTTP
**/list** - getting list of available service methods  
**/template** - getteing gRPC message template  
**/send** - sending message  
 
