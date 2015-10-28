#! /bin/bash
# Andrei Stoica 100554214

k=$1
m=$2
filename=$3

head -n -$m $filename | tail -n +$k
