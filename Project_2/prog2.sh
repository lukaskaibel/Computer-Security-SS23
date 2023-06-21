#! /bin/bash
gcc -o prog2 prog2.c -Wall -g -fno-stack-protector -z execstack
./prog2
./prog2 "Parker"

