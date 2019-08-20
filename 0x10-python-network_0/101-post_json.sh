#!/bin/bash
#Put a JSON file
curl -X POST -H "Content-Type: application/json" -d @$2 $1
