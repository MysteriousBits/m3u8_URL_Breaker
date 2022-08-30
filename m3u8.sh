#!/bin/bash

if (($# > 0))
then
    curl -s $1 | grep -o -m 1 '\bhttp.*.m3u8\b'
else 
    echo "Usage: ./m3u8.sh <URL>"
fi
