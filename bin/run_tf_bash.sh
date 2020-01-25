#!/bin/bash
docker run \
    -it \
    -v $PWD:/tmp \
    -w /tmp \
    -u $(id -u):$(id -g) \
    tensorflow/tensorflow:latest-gpu-jupyter \
    bash
