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
  <a href="https://t.me/plumberpc">
    <img src="https://img.shields.io/badge/telegram-🔔-green.svg" />
  </a>  
</p>

<p align="center">Like Postman, just for GRPC</p>
<p align="center">Thanks <a href="https://github.com/warmuuh/milkman">Milkman</a> and <a href="https://github.com/uw-labs/bloomrpc">Bloom</a> for inpiration.</p>

## About
...

## ⚡ Important

> This version doesn't support import proto files or protosets yet (will be).  
> You can use it only with servers, which support reflection API.

## Features
...

### Requirenments

- Docker

## Build and launch 🚀

- download last version build
- install it
- use `docker pull pashkatrick/plumber-api`
- and `docker run ...`

Create or set data to your .env ([example](https://github.com/pashkatrick/Plumber/blob/tcp-move/env-example), [details](https://pypi.org/project/python-decouple/#usage)), and after that:

```
- python3 app.py
```

You can use second instanse of termial, to execute first test command:

```bash
zerorpc tcp://localhost:1111 test
```
