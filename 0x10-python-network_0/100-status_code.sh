#!/bin/bash
# script that sends a req to URL passed as an arg, and displays only the status code of the res
curl -s -L -o /dev/null -s -w "%{http_code}" "$1"
