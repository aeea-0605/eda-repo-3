import time
import pickle
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup


yearly_webtoon_df = pd.DataFrame(columns=['year', 'title', 'link', 'genre', 'star', 'img', 'person', 'date'])
headers = {'cookie': f'{Request Cookie}'}

for year in range(2005, 2021):
    print()
    print(year)
    base_url = 'https://comic.naver.com/'
    url = 'https://comic.naver.com/webtoon/period.nhn?period={}'.format(year)

    response = requests.get(url)
    dom = BeautifulSoup(response.content, 'html.parser')
    elements = dom.select('#content > div.list_area.daily_img > ul > li')

    for idx, element in enumerate(elements):
        print(idx+1, end=' ')
        title = element.select_one('dl > dt > a').text.replace('.','')
        link = urllib.parse.urljoin(base=base_url, url=element.select_one('dl > dt > a').get('href'), allow_fragments=True)
        title_id = link.split("Id=")[1].split('&')[0]

        response = requests.get(link)
        dom = BeautifulSoup(response.content, 'html.parser')

        number = int(str(dom.find('td', 'title').a).split('no=')[1].split('&')[0])
        while number:
            detail_url = 'https://comic.naver.com/webtoon/detail.nhn?titleId={}&no={}'.format(title_id, number)
            response = requests.get(detail_url, headers=headers)
            dom = BeautifulSoup(response.content, 'html.parser')

            img = dom.select('#comic_view_area > div.wt_viewer > img')
            try:
                star = float(dom.select_one('#topPointTotalNumber').text)
            except:
                number -= 1
                continue
            person = int(dom.select('#topTotalStarPoint > span.pointTotalPerson > em')[0].text)
            date = dom.find('dd', 'date').text

            data = {
                'year': year,
                'title': title,
                'link': link,
                'genre': get_genre(link),
                'star': star,
                'img': len(img),
                'person': person,
                'date': date
            }
            yearly_webtoon_df.loc[len(yearly_webtoon_df)] = data
            number -= 1


with open('datas/every_yearly_webtoon.pkl', 'wb') as f:
    pickle.dump(yearly_webtoon_df, f)

print('end')