#!/bin/bash

while :; do
    { echo -e "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: 12\r\n\r\nHello, World!"; } | nc -l -p 8080
done
