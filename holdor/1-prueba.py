#!/usr/bin/python3
"""
<form method="post">
<input type="text" name="id" />
<input type="submit" name="holdthedoor" />
</form>
>>> payload = {'key1': 'value1', 'key2': 'value2'}
>>> r = requests.post("http://httpbin.org/post", data=payload)
keys={'text':'lol rofl'}
r=requests.post("http://127.0.0.1/abc.php/POST",params=keys)
"""
import requests

r = requests.get('http://158.69.76.135/level0.php')
print(r.text[0:500])
payload = {'id' : '1789', 'holdthedoor' : 'envio'}
for i in range (1):
    r = requests.post('http://158.69.76.135/level0.php', data=payload)
    print(r.headers)
