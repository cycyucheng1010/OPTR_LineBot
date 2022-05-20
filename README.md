# OPTR_LineBot
## pip install
* Django
* line-bot-sdk
## server
* ssh root@172.104.80.191
## command
* run django server```python3 manage.py runserver &```
* run ngrok and get log(route: /root/) ```ngrok http 8000 --log=stdout > ngrok.log &```
## domain name : check /root/ngrok.log
