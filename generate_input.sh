#!/bin/sh

mkdir -p ./input/0
mkdir -p ./input/1

for i in `seq -w 0 25`; do
    ./bin/graph_generator ./input/0/$i 0 $i
    ./bin/graph_generator ./input/1/$i 1 $i
done
