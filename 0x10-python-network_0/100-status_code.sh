#!/bin/bash
#Get the status code w/o pipes
curl -o /tmp/null -sIw '%{http_code}\n' $1
