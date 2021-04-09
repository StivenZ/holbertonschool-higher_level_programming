#!/bin/bash
# Display all methods from a request Option
curl -is -X OPTIONS $1 | sed -n "/Allow:/p" | cut -d ' ' -f2-
