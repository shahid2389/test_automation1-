import requests, urllib3
from urllib.parse import urlsplit, parse_qs
import base64
import json
#>>>
#//>>> url = "http://www.example.org/default.html?ct=32&op=92&item=98"
#>>> query = urlsplit(url).query
#>>> params = parse_qs(query)

url = 'https://captivemgr.o2wifi.net.uk/redirector/gf?switch_url=https://wlc.welcome.o2wifi.co.uk/login.html&ap_mac=00:a6:ca:6c:c4:90&client_mac=84-B1-53-E1-BD-8C&wlan=O2%20Wifi&redirect=www.msftconnecttest.com/redirect'
response = requests.get(url)
#jsonRes = response.json()
#print(jsonRes['title'] , jsonRes['body'], sep=':')
#print(response.text)
#print(response.url)

rp1 = response.url

query = urlsplit(rp1).query
params = parse_qs(query)
sessionT = params.get('i')
#rint(str(sessionT))
sessionT = str(sessionT)

print(base64.b64decode(sessionT))
url2 = 'https://captive.o2wifi.co.uk/api/register'
sessionTdecode = base64.b64decode(sessionT)
#print(sessionTdecode)
sessionTdecode = sessionTdecode.decode('utf-8')
print(sessionTdecode)
data1 = {'version': '1', 'session_token': sessionTdecode,'form_id':'','button_id':''}
#print(data1['session)
#postR = requests.post(url2, json= data1)
postR = requests.post(url2, json= {'version': '1', 'session_token': data1['session_token'] ,'form_id':'','button_id':''})
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
r = requests.post(url,  data=json.dumps(data1), headers=headers)
jsonres = postR.json()
#print(jsonres)

jsondict = (json.loads(jsonres))
print('page0r',jsondict)
#print(jsondict['state_instance']['session_token'])
#print(jsondict['session_token'])
#datafield = {'countryCode':'44','mpn':'07791792000','userAgent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}

p1req= {'version': jsondict['state_instance']['version'] ,
               'session_token': jsondict['state_instance']['session_token'] ,
                'state_id':'enterMpn' ,
                'form_id':'enterMpnForm' ,
                'button_id':'submitMpn',
                 'data':{
                     'countryCode':'44',
                     'mpn':'07791792000',
                     'userAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
                 }
        }


              #  'data[countryCode]':'44',
               # 'data[mpn]':'07791792000',
                #'data[userAgent]':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}


#print(p1req)
p1reqjson = json.dumps(p1req)
#print(p1reqjson)
p1postr = requests.post(url2, json=p1req)
#print(p1postr)
jsonres2 = p1postr.json()
jsondict2 = json.loads(jsonres2)
print('page1r',jsondict2)
print(jsondict2['state_instance']['session_token'])

p2reqdata = {'version' : jsondict2['state_instance']['version'],
         'session_token': jsondict2['state_instance']['session_token'],
         'state_id':'verifyCode',
         'form_id': 'enterConfirmationCodeForm',
         'button_id': 'submitConfirmationCode',
         'data':{
             'confirmationCode': '0812', }
             }

p2postr = requests.post(url2, json=p2reqdata)
jsonres3 = p2postr.json()
jsondict3 = json.loads(jsonres3)
print('page2r', jsondict3)

furtherdata = {'version':jsondict3['state_instance']['version'],
               'session_token': jsondict3['state_instance']['session_token'],
               'state_id':'furtherDetails',
               'form_id':'enterFurtherDetailsForm',
               'button_id':'submitFurtherDetails',
               'data':{
                   'title':'Mr',
               'forename':'auto',
               'surname':'test',
               'email':'shahid.hussain@telefonica.com',
               'dob': '1990-01-01',
               'postcode':'hp111gh',}
               #'optin': 'false',}
               }

furtherdetailpostr = requests.post(url2, json=furtherdata)
jsonres4 = furtherdetailpostr.json()
jsondict4 = json.loads(jsonres4)
print(jsondict4)
