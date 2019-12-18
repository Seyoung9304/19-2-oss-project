import urllib.request
import json
import pandas
import requests
import urllib
from urllib.parse import quote_plus
from selenium import webdriver
from bs4 import BeautifulSoup

def print_restaurant_name_google(name):
    result = [[], []]
    #name = urllib.parse.quote(name)
    baseurl = 'https://www.google.co.kr/search?q='
    plusurl = name
    url = baseurl + quote_plus(plusurl)
    print(url)

    driver = webdriver.Chrome()
    driver.get(url)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    r = soup.select('.Ob2kfd')
    # print(type(r))
    for i in r:
        print(i.select_one('.Aq14fc').text)
        print()

    driver.close()



def print_restaurant_name_siksin(name):
    result = [[], []]
    #name = urllib.parse.quote(name)
    url = 'https://www.siksinhot.com/search?keywords='+name
    print(url)
    r = requests.get(url)
    html = r.content
    soup = BeautifulSoup(html, 'html.parser')
    foundstore = soup.find(class_='store')
    print(foundstore)
    foundstar = soup.find(class_='score')
    print(foundstar)



name = urllib.parse.quote(input("경기도 시/군 명을 입력해주세요 : "))
url = 'https://openapi.gg.go.kr/PlaceThatDoATasteyFoodSt?KEY=30c8bab88c6249babce184a75ce9be0f&Type=json&SIGUN_NM='+name
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
            data.append([i['RESTRT_NM'], i['TASTFDPLC_TELNO'], i['REFINE_ROADNM_ADDR'], i['REFINE_WGS84_LAT'], i['REFINE_WGS84_LOGT']])
            storename.append(i['RESTRT_NM'])
        for i in storename:
            print_restaurant_name_siksin(i)
            print_restaurant_name_google(i)
        #print(data)
        #print(storename)
        #frame = pandas.DataFrame(data)
        #frame.to_csv(r'C:\Users\wogus\PycharmProjects\untitled1\data.csv',header=False, index=False)
    except: #예외처리 : 오류 메시지출력
        print(dict['RESULT']['MESSAGE'])
else:
    print("Error Code:" + rescode)
