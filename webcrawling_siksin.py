
"""
with urllib.request.urlopen("https://www.diningcode.com/list.php?query=%EA%B2%BD%EA%B8%B0%EB%8F%84%EB%A7%9B%EC%A7%91") as response:
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
"""

"""
import urllib.request
import urllib.parse
import requests
import urllib
from bs4 import BeautifulSoup


def print_restaurant_star(name):
    result = [[], []]
    #rname = urllib.parse.quote(name)
    url = 'https://www.google.co.kr/search?q='+name
    print(url)
    req = requests.get(url)
    html = req.content
    soup = BeautifulSoup(html, 'html.parser')
    found = soup.find_all("g-review-stars")
    print(found)
    star = soup.select('g-review-stars')
    print(star)
    #result.append(star.text.strip())
    #print(result)


name = '청년밥상'
print_restaurant_star(name)
"""

import requests
import urllib
from bs4 import BeautifulSoup


def print_stock_price(name):
    result = [[], []]
    #name = urllib.parse.quote(name)
    url = 'https://www.siksinhot.com/search?keywords='+name
    print(url)
    r = requests.get(url)
    html = r.content
    soup = BeautifulSoup(html, 'html.parser')
    print(soup)
    found = soup.find_all("g-review-stars")
    print(found)
    star = soup.select('g-review-stars')
    print(star)
    #result.append(star.text.strip())

    #print(result)


name='청년밥상'
print_stock_price(name)