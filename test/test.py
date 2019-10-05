# -*- coding: utf-8 -*-

from requests import post

r = post(url='http://127.0.0.1:5000/testsuit',data={'userId':'Robert'})
print(r.status_code)
print(r.json())