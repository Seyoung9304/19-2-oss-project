from bs4 import BeautifulSoup

import urllib.request
import urllib.parse


with urllib.request.urlopen("https://www.diningcode.com/list.php?query=%EA%B2%BD%EA%B8%B0%EB%8F%84%EB%A7%9B%EC%A7%91") as response:
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')


