import requests

from bs4 import BeautifulSoup

word = input()
url = input()

r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')

p2 = soup.find_all('p')

for para in p2:
    if word in para.text:
        print(para.text)
        break
