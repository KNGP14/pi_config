#!/bin/bash

args=""
i=1;
for arg in "$@" 
do
    args="$args $arg";
    i=$((i + 1));
done
venv/bin/python3 pi_config.py $args