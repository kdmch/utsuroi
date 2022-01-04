import random
import datetime
import re
import twitter
import json
from requests_oauthlib import OAuth1Session
import imgtrans as ic
import sys
import base64

apikey   = 'your api-key'
apisec   = 'your api-key secret'
token    = 'access token'
tokens   = 'access token secret'
flag     = False
twitter  = OAuth1Session(apikey, apisec, token, tokens)

url      = 'https://api.twitter.com/1.1/account/update_profile_image.json'
reqsave  = -1
interval = 10
reserved =  0 #run at the optional time
quality  = 25 #quality of icon.jpg
filepath = 'mitori.png'
filepath_another = 'mitoriwink.png'


print('running')

while True:
  now = datetime.datetime.now()
  m   = now.minute
  if (m % interval) and (m != reserved):
    flag = False

  if ((not (m % interval)) or (m == reserved)) and (not flag):
    verify = twitter.get('https://api.twitter.com/1.1/account/verify_credentials.json')
    print(verify)

    if not(random.randint(0,9)):
      ic.iconhsv('img/'+filepath_another,quality)
    else:
      ic.iconhsv('img/'+filepath,quality)
    
    with open('img/processed.jpg', 'rb') as f:
      img = base64.b64encode(f.read()).decode('utf-8')
    
    params  = {'image': img, 'include_entities': False, 'skip_status': True}
    req     = twitter.post(url, params=params)
    reqsave = req.status_code
    flag    = True

    print(img[0:5])
    print(len(img))
    print((now.hour+9)%24, m)
    if req.status_code == 200:
      print('200 updated!')
    else:
      print('%d failed.' % req.status_code)
