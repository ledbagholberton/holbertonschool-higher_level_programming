#!/bin/bash
#Put a JSON file
curl -L --request PUT -d "user_id=98" -H "origin:HolbertonSchool" $1
