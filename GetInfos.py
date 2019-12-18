#!usr/bin/env python

import urllib.request
import json
import pandas
import requests
import urllib
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
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
        r = soup.select('.Ob2kfd')
        # print(type(r))
        for i in r:
            print("Google score: " + i.select_one('.Aq14fc').text)
        driver.close()
    except:
        print("No data or error!")


def print_restaurant_name_siksin(name):
    url = 'https://www.siksinhot.com/search?keywords=' + name
    r = requests.get(url)
    html = r.content
    soup = BeautifulSoup(html, 'html.parser')

    foundstore = soup.find(class_='store').text
    print("식신 found: " + foundstore)
    foundstar = soup.find(class_='score').text
    print("식신 score: " + foundstar)


# firebase 인증 및 초기화
cred = credentials.Certificate('mykey.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://oss-d85b6.firebaseio.com/'
})

ref = db.reference()

name = urllib.parse.quote(input("경기도 시/군 명을 입력해주세요 : "))
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
                         i['REFINE_WGS84_LOGT']])
            storename.append(i['RESTRT_NM'])
        for i in storename:
            print("---------------------------------")
            print("Search for " + i + ":")
            print_restaurant_name_siksin(i)
            print_restaurant_name_google(i)
    except:
        print(dict['RESULT']['MESSAGE'])
else:
    print("Error Code:" + rescode)

"""
    const
    firebaseConfig = {
        apiKey: "AIzaSyBp9qZ87OMBpMgsql2Ty4bYY9HlyHOmPk0",
        authDomain: "oss-d85b6.firebaseapp.com",
        databaseURL: "https://oss-d85b6.firebaseio.com",
        projectId: "oss-d85b6",
        storageBucket: "oss-d85b6.appspot.com",
        messagingSenderId: "177361667729",
        appId: "1:177361667729:web:d51c9f369f1afed5eb6130",
        measurementId: "G-5BGT9PMBCZ"
    };
"""
