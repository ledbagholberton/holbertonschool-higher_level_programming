#!/bin/bash
#Send a delete request to an address
curl -s -I $1 | tail -n 4 | head -n 1 | cut -b 8-
