#!/bin/bash

args=""
i=1;
for arg in "$@" 
do
    args="$args $arg";
    i=$((i + 1));
done
env/bin/python3 pi_gpio-config.py $args