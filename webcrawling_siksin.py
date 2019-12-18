
import requests
import urllib
from bs4 import BeautifulSoup


def print_restaurant_name(name):
    result = [[], []]
    #name = urllib.parse.quote(name)
    url = 'https://www.siksinhot.com/search?keywords='+name
    print(url)
    r = requests.get(url)
    html = r.content
    soup = BeautifulSoup(html, 'html.parser')
    """print(soup)"""
    foundstore = soup.find_all(class_='store')
    print(foundstore)
    foundstar = soup.find_all(class_='score')
    print(foundstar)


name = '청년밥상'
print_restaurant_name(name)
