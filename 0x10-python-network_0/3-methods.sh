#!/bin/bash
#Take in a URL and displays http methods
curl -sI "$1" | grep Allow | cut -d' ' -f2-
