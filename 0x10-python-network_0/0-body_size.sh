#!/bin/bash
# curl a request with the body size in bytes
curl -sI $1 | sed -n "/Content-Length/p" | cut -d " " -f 2
