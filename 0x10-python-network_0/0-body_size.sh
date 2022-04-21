#!/bin/bash
# Curls request and display bytes received
curl -w '%{size_download}\n' -so /dev/null "$1"
