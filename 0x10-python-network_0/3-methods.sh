#!/bin/bash
#Send a delete request to an address
curl -s -I --request GET $1 | tail -n 5 | head -n 1 | cut -b 8-
