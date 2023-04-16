import os
import requests

token = os.environ['JUNBOT_TOKEN']
chat_id = os.environ['CHAT_ID']

# get global ip address
ip = requests.get("https://api.ipify.org").text
# print(ip)

requests.get("https://api.telegram.org/bot"+token+"/sendmessage?chat_id="+chat_id+"&text="+ip)