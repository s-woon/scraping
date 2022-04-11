import pandas as pd
import requests
import csv
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.ticker as mticker
from matplotlib import font_manager
from bs4 import BeautifulSoup

url = "https://search.daum.net/search?w=tot&q=%EC%97%AD%EB%8C%80%EA%B4%80%EA%B0%9D%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"
data = requests.get(url)
movie_list = []

mpl.rcParams['axes.unicode_minus'] = False
font_path = '/usr/share/fonts/truetype/nanum/NanumGothic.ttf'
font_name = font_manager.FontProperties(fname=font_path).get_name()
plt.rcParams["font.family"] = font_name

if data.status_code != requests.codes.ok:
    print("접속실패")
    exit()

html = BeautifulSoup(data.text, "html.parser")

movies = html.select('ol.movie_list > li')
for movie in movies:
    temp = []
    temp.append(movie.select_one('.info_tit').text.strip())
    temp.append(movie.select_one('.score .rate').text.strip())
    cont_data = movie.select('.dl_comm > .cont')
    temp.append(cont_data[0].text.strip())
    temp.append(cont_data[1].text.strip("명").replace(",",""))
    movie_list.append(temp)

with open('movie.csv', 'w', encoding='UTF-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Title', 'Score', 'Open_date', 'Total'])
    writer.writerows(movie_list)

df = pd.read_csv('movie.csv')  # 파일 df에 담기
df_name = df['Title']  # df에서 제목값을 df_name에 담기
df_total = df['Total']  # df에서 누적관객수를 df_total에 담기
df_score = df['Score']

# plt.figure(figsize=(20, 14))  # 그림 사이즈 지정(가로 14인치, 세로 5인치)
# plt.get_current_fig_manager().full_screen_toggle()  # 전체화면
#
# plt.subplot(2, 1, 1)
# plt.gca().yaxis.set_major_formatter(mticker.FormatStrFormatter('%.lf 명'))
# plt.title('누적 관객수')
# plt.plot(df_name, df_total, color='green')  # x, y
# plt.xticks(rotation='80')
#
# plt.subplot(2, 1, 2)
# plt.gca().yaxis.set_major_formatter(mticker.FormatStrFormatter('%.1lf 점'))
# plt.title('평점')
# plt.plot(df_name, df_score, color='steelblue')
# plt.xticks(rotation='80')

fig = plt.figure(figsize=(20, 20))
plt.title('역대 흥행 영화')
ax1 = fig.add_subplot()
# ax1 = fig.plot(fig)
plt.xticks(rotation='80')

# ax1 = df[['Title', 'Total']]

ax1.plot(df_name, df_total, color='green')  # x, y
plt.gca().yaxis.set_major_formatter(mticker.FormatStrFormatter('%.lf 명'))
ax1.set_xlabel('영화')
ax1.set_ylabel('누적관객', color='green')
ax1.tick_params(axis='y', labelcolor='green')

ax2 = ax1.twinx()
ax2.plot(df_name, df_score, color='blue')
plt.gca().yaxis.set_major_formatter(mticker.FormatStrFormatter('%.1lf 점'))
ax2.set_ylabel('평점', color='blue')
ax2.tick_params(axis='y', labelcolor='blue')

ax1.set_ylim(6000000, 18000000)
ax2.set_ylim(5.0, 10.0)

plt.show()




