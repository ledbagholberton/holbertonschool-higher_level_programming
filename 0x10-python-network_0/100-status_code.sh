#!/bin/bash
#Get the status code w/o pipes
curl -sI $1 -o /dev/null -w '%{http_code}\n'
