#!/bin/bash
#Send a POST with variable 
curl -s --request POST 0.0.0.0:5000/route_6 --data "email='hr@holbertonschool.com'&subject='I will always be here for PLD'"
