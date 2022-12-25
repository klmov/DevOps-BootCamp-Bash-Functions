#!/bin/bash

# Defining a timestamp function

print_log() {
        local txt=$@ 
        echo "[$(date +%F-%R)] $@"
 }

print_log $@

