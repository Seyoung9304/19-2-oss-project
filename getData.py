#!usr/bin/env python

import urllib.request
import json
import pandas
import requests
import urllib
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import firestore
from urllib.parse import quote_plus
from selenium import webdriver
from bs4 import BeautifulSoup


def print_restaurant_name_google(name):
    baseurl = 'https://www.google.co.kr/search?q='
    plusurl = name
    url = baseurl + quote_plus(plusurl)
    driver = webdriver.Chrome()
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    try:
        r = soup.select('.Ob2kfd') #정보가 우측에 단독으로 나오는 경우
        l = soup.select('.rllt__details.lqhpac') #정보가 리스트로 나오는 경우
        # print(type(r))
        for i in r:
            print("Google score: " + i.select_one('.Aq14fc').text)
            driver.close()
            return i.select_one('.Aq14fc').text
        for j in l:
            print("Google score: " + j.select_one('.BTtC6e').text)
            driver.close()
            return j.select_one('.BTtC6e').text
        return 0
    except:
        print("No data or error!")
        return 0


def print_restaurant_name_siksin(name):
    url = 'https://www.siksinhot.com/search?keywords=' + name
    r = requests.get(url)
    html = r.content
    soup = BeautifulSoup(html, 'html.parser')
    try:
        foundstore = soup.find(class_='store').text
        print("식신 found: " + foundstore)
        foundstar = soup.find(class_='score').text
        print("식신 score: " + foundstar)
        if name == foundstore:
            return foundstar
        else:
            return 0 #찾은 결과가 없거나 실제 원하는 데이터가 아닐 경우
    except:
        print("No data or error!")
        return 0


# firebase 인증 및 초기화
cred = credentials.Certificate('./mykey.json')
firebase_admin.initialize_app(cred)

db = firestore.client()
doc_ref = db.collection(u'data')
# ref = db.reference()
siname = ["가평군", "고양시", "과천시", "광주시", "김포시", "남양주시", "동두천시", "부천시", "성남시", "수원시", "시흥시", "안산시", "안성시", "안양시", "양주시",
          "여주시", "연천군", "오산시", "용인시", "의왕시", "의정부시", "이천시", "평택시", "파주시", "포천시", "하남시", "화성시"]
for names in siname:

    name = urllib.parse.quote(names)
    url = 'https://openapi.gg.go.kr/PlaceThatDoATasteyFoodSt?KEY=30c8bab88c6249babce184a75ce9be0f&Type=json&SIGUN_NM=' + name
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    data = []
    storename = []

    if rescode == 200:
        response_body = response.read()
        dict = json.loads(response_body.decode('utf-8'))
        try:
            for i in dict['PlaceThatDoATasteyFoodSt'][1]['row']:
                data.append([i['RESTRT_NM'], i['TASTFDPLC_TELNO'], i['REFINE_ROADNM_ADDR'], i['REFINE_WGS84_LAT'],
                             i['REFINE_WGS84_LOGT'], i['REPRSNT_FOOD_NM']])
                storename.append(i['RESTRT_NM'])

                scores = []

                scores.append(float(print_restaurant_name_google(i['RESTRT_NM'])))
                scores.append(float(print_restaurant_name_siksin(i['RESTRT_NM'])))

                sum = 0
                nonzerocnt = 0
                for k in scores:
                    if k != 0:
                        sum += k
                        nonzerocnt += 1
                if nonzerocnt != 0:
                    avg = sum / nonzerocnt
                    doc_ref.document(i['RESTRT_NM']).set({
                        u'si': names,
                        u'score': avg,
                        u'storename': i['RESTRT_NM'],
                        u'telno': i['TASTFDPLC_TELNO'],
                        u'address': i['REFINE_ROADNM_ADDR'],
                        u'longitude': i['REFINE_WGS84_LOGT'],
                        u'latitude': i['REFINE_WGS84_LAT'],
                        u'menu': i['REPRSNT_FOOD_NM']
                    })
                # 맛집 기본정보 업데이트
        except:
            print(dict['RESULT']['MESSAGE'])
    else:
        print("Error Code:" + rescode)
