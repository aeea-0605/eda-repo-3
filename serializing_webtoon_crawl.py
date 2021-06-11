import time
import pickle
import numpy as np
import pandas as pd
import requests
import urllib.parse
from bs4 import BeautifulSoup


# 웹툰의 장르를 갖고오는 함수
def get_genre(link):
    response = requests.get(link)
    dom = BeautifulSoup(response.content, 'html.parser')

    return dom.find('span', 'genre').text.replace(',','')


# webtoon_df 생성 및 숫자를 요일로 변환할 dictionary 변수생성
day_of_week = {1:"mon", 2:"tue", 3:"wed", 4:"thu", 5:"fri", 6:"sat", 7:"sun"}
webtoon_df = pd.DataFrame(columns=['day', 'rank', 'title', 'link', 'genre', 'star', 'img', 'person', 'date'])

# 2021년 연재중인 인기순 요일별 웹툰 크롤링
base_url = 'https://comic.naver.com/'
url = 'https://comic.naver.com/webtoon/weekday.nhn'
headers = {'cookie': f'{Request Cookie}'}

for day in range(1, 8):
    print()
    print('{} webtoon crawling..'.format(day_of_week[day]))
    response = requests.get(url)
    dom = BeautifulSoup(response.content, 'html.parser')
    condition = '#content > div.list_area.daily_all > div:nth-of-type({}) > div > ul > li'.format(day)
    elements = dom.select(condition)

    for idx, element in enumerate(elements):
        print(idx+1, end=' ')
        title = element.find_all('a', 'title')[0].text
        link = urllib.parse.urljoin(base=base_url, url=element.select_one('a').get('href'), allow_fragments=True)

        response = requests.get(link)
        dom = BeautifulSoup(response.content, 'html.parser')

        title_id = link.split("Id=")[1].split('&')[0]
        number = int(str(dom.find('td', 'title').a).split('no=')[1].split('&')[0])
        while number:
            detail_url = 'https://comic.naver.com/webtoon/detail.nhn?titleId={}&no={}&weekday={}'.format(title_id, number, day_of_week[day])
            response = requests.get(detail_url, headers=headers)
            dom = BeautifulSoup(response.content, 'html.parser')

            img = dom.select('#comic_view_area > div.wt_viewer > img')
            star = float(dom.select('#topPointTotalNumber')[0].text)
            person = int(dom.select('#topTotalStarPoint > span.pointTotalPerson > em')[0].text)
            date = dom.select('#sectionContWide > div.tit_area > div.vote_lst > dl.rt > dd.date')[0].text

            data = {
                'day': day_of_week[day],
                'rank': idx+1,
                'title': title,
                'link': link,
                'genre': get_genre(link),
                'star': star,
                'img': len(img),
                'person': person,
                'date': date

            }
            webtoon_df.loc[len(webtoon_df)] = data
            number -= 1


# 크롤링한 데이터프레임 pickle로 저장
with open('datas/every_weekly_webtoon.pkl', 'wb') as f:
    pickle.dump(webtoon_df, f)
