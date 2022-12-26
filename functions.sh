#!/bin/bash

# get power of a to b
pow() {
echo $(($1**$2))
}

# Defining a timestamp function

print_log() {
        local txt=$@ 
        echo "[$(date +%F-%R)] $@"
 }

print_log $@

