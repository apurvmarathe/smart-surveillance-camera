import requests
def send_email():
 return requests.post(
       'https://api.mailgun.net/v3/xxxxx/messages',
       auth=("api","xxxxx"),
       files=[("attachment",("ss.jpg",open("ss.jpg","rb").read()))],
       data={"from":"xxxxx",
              "to":"xxxx",
              "subject":"Intruder Alert",
              "text":"Alert! Person in restricted premises"})
