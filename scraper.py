# country code -> country
# us -> United State
# india -> India
# brazil -> Brazil
# france -> France
# russia -> Russia
# uk -> United Kingdom
# turkey -> Turkey
# italy -> Italy
# spain -> Spain
# germany -> Germany
# pakistan ->	Pakistan
# bangladesh -> Bangladesh
# nepal -> Nepal
# sri-lanka -> Sri Lanka
# china -> China
# afghanistan -> Afghanistan


con = input("Enter country code (Please enter a valid code otherwise it will not work) : ")
while(con != 'india' and con != 'us' and con != 'brazil' and con != 'france' and con != 'rassia' and con != 'uk' and con != 'turkey' and con != 'france' and con != 'itly' and con != 'spain'
and con != 'germany' and con != 'pakistan' and con != 'bangladesh' and con != 'nepal' and con != 'sri-lanka' and con != 'china' and con != 'afganistan'):
  con = input("you have enter wrong country code (Please enter a valid code otherwise it will not work) : ")
print(con)


# referece from https://www.dataquest.io/blog/web-scraping-python-using-beautiful-soup/
import requests
from bs4 import BeautifulSoup

# https://www.worldometers.info/coronavirus/#countries

URL = 'https://www.worldometers.info/coronavirus/country/{country}/'.format(country = con)
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

last_upd = soup.find(attrs={"style" : "font-size:13px; color:#999; text-align:center"})
last_time = list(last_upd)[0].split(':')
last_upd_time_tit = last_time[0]
last_upd_time = last_time[1].strip() +':' + last_time[2]
#print(last_upd_time_tit)
#print(last_upd_time)

results = soup.find_all('div', id='maincounter-wrap')
#print(results)

#print(results[0])

cor_cas1 = list(list(results[0])[1])[0].strip(':')
cor_cas = cor_cas1.split()[1]

cor_cas_data = list(list(list(results[0])[3])[1])[0].strip()

#print(results[1])

det_tit = list(list(results[1])[1])[0].strip(':')
det_data = list(list(list(results[1])[3])[1])[0]
rec = list(results[2])
#print(rec)

rec_title = list(rec[1])[0].strip(':')
#print(rec_title)

rec_data = list(list(rec[3])[1])[0]
#print(rec_data)

data = { cor_cas: cor_cas_data, rec_title: rec_data, det_tit: det_data , last_upd_time_tit: last_upd_time  }
#print(data)

import json
# this will return json string
json_object = json.dumps(data)
# this will return dict
json_object_dic = json.loads(json_object)
print(json_object) 

json_obj = {}
json_obj[con] = []
json_obj[con].append(data)
#Write the object to file.
with open('covid_{coun}.json'.format(last = last_upd_time, coun = con),'w') as jsonFile:
    json.dump(json_obj, jsonFile)