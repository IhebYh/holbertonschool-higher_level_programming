#!/usr/bin/env bash
curl -w '%{size_download}\n' -so /dev/null "$1"
