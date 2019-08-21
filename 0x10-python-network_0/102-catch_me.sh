#!/bin/bash
#Put a JSON file
curl -sLX PUT -d "user_id=98" -H "origin:HolbertonSchool" $1
