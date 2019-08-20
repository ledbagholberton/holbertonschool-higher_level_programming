#!/bin/bash
#Count lenght of answer to http
curl -s $1 | wc -c
