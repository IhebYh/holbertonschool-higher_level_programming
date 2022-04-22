#!/bin/bash
# send a post a req with json 
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
