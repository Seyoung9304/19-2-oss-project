import urllib.request
import json
import pandas

name = urllib.parse.quote(input("경기도 시/군 명을 입력해주세요 : "))
url = 'https://openapi.gg.go.kr/PlaceThatDoATasteyFoodSt?KEY=30c8bab88c6249babce184a75ce9be0f&Type=json&SIGUN_NM='+name
request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
rescode = response.getcode()
data = []

if(rescode==200):
    response_body = response.read()
    dict = json.loads(response_body.decode('utf-8'))
    try:
        for i in dict['PlaceThatDoATasteyFoodSt'][1]['row']:
            data.append([i['RESTRT_NM'], i['TASTFDPLC_TELNO'], i['REFINE_ROADNM_ADDR'], i['REFINE_WGS84_LAT'], i['REFINE_WGS84_LOGT']])
        frame = pandas.DataFrame(data)
        frame.to_csv(r'C:\Users\wogus\PycharmProjects\untitled1\data.csv',header=False, index=False)
    except: #예외처리 : 오류 메시지출력
        print(dict['RESULT']['MESSAGE'])
else:
    print("Error Code:" + rescode)