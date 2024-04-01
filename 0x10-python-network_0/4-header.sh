#!/bin/bash
# script that takes in URL as arg, sends a GET req to the URL, and displays the body of the res
curl -s -H "X-School-User-Id: 98" "$1"
