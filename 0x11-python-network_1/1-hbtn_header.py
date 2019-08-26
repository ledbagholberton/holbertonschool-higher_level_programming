#!/usr/bin/python3
"""request a specific header """
import urllib.request
import sys

url = sys.argv[1]
try:
    with urllib.request.urlopen(url) as response:
        html = response.getheader("X-Request-Id")
    print(html)
except:
    pass
