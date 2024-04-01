#!/bin/bash
# script that sends a DELETE req to URL passed as the first arg and displays the body of the res
curl -s -X "DELETE" "$1"
