
"""
with urllib.request.urlopen("https://www.diningcode.com/list.php?query=%EA%B2%BD%EA%B8%B0%EB%8F%84%EB%A7%9B%EC%A7%91") as response:
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
"""


import urllib
import requests
from bs4 import BeautifulSoup


def print_restaurant_star(name):
    result = [[],[]]
    #name = urllib.parse.quote(name)
    url = 'https://www.google.co.kr/search?q='+name
    print(url)
    req = requests.get(url)
    html = req.content
    soup=BeautifulSoup(html, 'html.parser')
    found=soup.find_all("g-review-stars") #html flag
    print(found)

name='청년밥상'
print_restaurant_star(name)
