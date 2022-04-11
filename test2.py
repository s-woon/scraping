import urllib.request
from bs4 import BeautifulSoup
import csv

hdr = { 'User-Agent' : 'Mozilla/5.0'}
url = 'https://www.melon.com/chart/'

req = urllib.request.Request(url, headers=hdr)
html = urllib.request.urlopen(req).read()
soup = BeautifulSoup(html, 'html.parser')

lst50 = soup.select('.lst50, .lst100')


melonList = []
for i in lst50:
    print(i)
    temp = []
    temp.append(i.select_one('.rank').text)
    temp.append(i.select_one('.ellipsis.rank01').a.text)
    temp.append(i.select_one('.ellipsis.rank02').a.text)
    temp.append(i.select_one('.ellipsis.rank03').a.text)
    # temp.append(i.select_one('div > button > span.cnt > #text').text)
    # melonList.append(temp)
    break
#lst50 > td:nth-child(8) > div > button > span.cnt
print(temp)
# print(type(temp[4]))


# with open('melon100.csv', 'w', encoding='ANSI', newline='') as f:
#     writer = csv.writer(f)
#     writer.writerow(['순위', '아티스트', '곡명', '앨범'])
#     writer.writerows(melonList)