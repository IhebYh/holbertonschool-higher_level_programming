#!/bin/bash
#get status code from http header
curl -so /dev/null --write-out "%{http_code}" "$1"
