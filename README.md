[![Python application test with Github Actions](https://github.com/ThanatPay/build-NLP-project/actions/workflows/main.yml/badge.svg)](https://github.com/ThanatPay/build-NLP-project/actions/workflows/main.yml)
# build-NLP-project
This repo for build nlp project

## Create command line Interface for python file
create file python file `touch wikiphrases.py` and add `#!/usr/bin/env python` to first line in python file for giving an env runs python

run this to allow executing file as program, leaves you with the exact same result as the command in terminal.
```
chmod +x wikiphrases.py
```
run `./wikiphrases.py ` in terminal to run python file

## Create web service
build Dockerfile and FastAPI to create web service.

## Deploy with Elastic Container Registry (ECR)
push a container into ECR repo for trigger a build with AWS App runner. 