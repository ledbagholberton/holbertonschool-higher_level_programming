#!/bin/bash
#Get the status code w/o pipes
curl -o /dev/null -sIw '%{http_code}\n' $1
