# 네이버 웹툰 크롤링을 통한 탐색적 데이터 분석 (EDA) 🎨
---
## 1. 개요
<br/>

#### 1-1. 프로젝트 목적
네이버 웹툰 크롤링을 통해 EDA를 하는 것이 주 목적이며, 기술 통계와 시각화를 통해 가설에 대한 결론 도출 및 웹툰의 분포와 장르별 특징, 데이터를 깊게 들여다보며 색다른 인사이트를 찾는 것입니다.



#### 1-2. 프로젝트 목표
- 웹툰시장의 추이 및 장르별 분포와 특징을 시각화하여 인사이트 도출
- 순위가 높은 웹툰에 영향을 끼친 요인 파악
- 평가지표간에 서로 어떠한 영향을 보이는지 파악
- 그 외 EDA를 통한 발견하지 못한 인사이트 도출

#### 1-3. 기술적 목표
- GET방식과 BeautifulSoup을 통해 정적페이지 크롤링 및 Try Except문을 이용해 특정회차에 대한 예외처리
- pandas, sklearn을 통해 raw data의 전처리 및 분석을 위한 파생변수를 생성 및 데이터셋을 pickle파일을 통해 관리
- matplotlib, seaborn을 통해 다양한 그래프로 데이터를 시각화

#### 1-4. 데이터셋 및 가설
- 데이터셋
- Naver Webtton Crawling ([naver webtoon page link](https://comic.naver.com/index.nhn))
    + 2021년 인기순 연재웹툰 (32242 rows)
    + 2005 ~ 2021 연도별 웹툰 (331255 rows)
```
row : 한 회차에 대한 웹툰 정보
columns
    - title : 웹툰 제목
    - genre : 웹툰 장르
    - star : 해당 회차의 평점 (평가지표)
    - img : 해당 회차의 분량 (평가지표)
    - person : 해당 회차의 웹툰 이용자의 투표 참여도 (평가지표)
    - datetime : 해당 회차 업로드 날짜
    - rank : 웹툰 순위
    - cate_year : 웹툰 연재 연도 
```
- 가설
    + *순위가 높은 웹툰은 평점과 분량, 참여도 모두 높을 것이다.*
        > 순위를 수치화한 파생변수 생성 후 평가지표와의 상관관계 파악
    + *평점이 낮은 회차는 분량과 참여도가 낮을 것이다.*
        > 평점과 분량, 참여도와의 상관관계 파악 및 고평점, 저평점회차의 통계량 차이 시각화
    + *가을에 로맨스 장르의 웹툰이 인기가 많을 것이다.*
        > 월별 장르간 웹툰 개수를 통한 계절에 따른 장르의 분포 시각화
        > 
        > 월별 장르간 참여도를 통한 각 월의 1위 장르에 대해 해당 월의 인기장르로 지정 후 각 월의 인기장르 파악

#### 1-5. 팀구성
- 이승주
    - Crawling, 데이터 전처리, EDA, git 코드정리
    - GitHub : [https://github.com/aeea-0605](https://github.com/aeea-0605)
- 고현실
    - EDA, README 작성
    - GitHub : [https://github.com/kohyunsil](https://github.com/kohyunsil)
---
---
## 2. EDA 결과 요약
<br/>

### 2-1. 기간별, 장르별 웹툰 빈도분석 및 추세분석
<br/>

1) **2021년 요일별 웹툰의 수와 회차 총량**

![EDA_weekly_count.png](https://user-images.githubusercontent.com/80459520/124462970-2c86d480-ddcd-11eb-8c62-9494c5cb15bd.png)
- 수요일의 연재 웹툰 수가 가장 많고 금요일이 가장 적다.
- 금, 토 웹툰의 회차 총량 웹툰 수에 비해 많은 것을 보아 연재를 오래한 웹툰이 분포되어 있는 것을 알 수 있다.

<br/>

2) **2021년 요일별 카테고리 분포**

![EDA_weekly_category_count.png](https://user-images.githubusercontent.com/80459520/124463526-fe55c480-ddcd-11eb-93dc-2c15f40a4124.png)
- 카테고리별로 대체로 고르게 분포되어 연재되고 있다.

<br/>

3) **2021년 카테고리별 평가지표**

![EDA_weekly_category_variables.png](https://user-images.githubusercontent.com/80459520/124464193-d7e45900-ddce-11eb-8939-cd8691586e1a.png)
- 스토리의 분량과 참여도가 높은 것에 비해 평점이 가장 낮다는 것을 알 수 있다.
- 에피소드와 옴니버스의 분량이 스토리에 비해 적은 것을 알 수 있다.
    + 옴니버스 : 하나의 장르 속에 서로 다른 독립된 이야기를 묶어 풀어내는 형식
    + 에피소드 : 하나의 큰 주제를 갖고 그 안에서 일어나는 일을 웹툰화, ex) 시트콤
    > 각 카테고리가 가진 특성으로 인해 분량의 차이가 있다는 것을 알 수 있다.

<br/>

4) **2021년 세부장르별 평가지표**

![EDA_weekly_detailgenre_variavble.png](https://user-images.githubusercontent.com/80459520/124465275-2fcf8f80-ddd0-11eb-9794-adffaac0018c.png)
- 평균 평점과 평균 참여도 사이에 반대되는 성향을 보임
> **가설 2 설정에 대한 원인이 된 그래프**

<br/>

5) **연도별 웹툰시장의 추이**

![EDA_yearly_count.png](https://user-images.githubusercontent.com/80459520/124465975-06fbca00-ddd1-11eb-9d2e-1879b7dbeb0e.png)
- 해마다 웹툰시장이 커지는 것을 확인할 수 있다.
- 2021.04 데이터밖에 없기에 2021년의 빈도 수가 전년도에 비해 적다.

<br/>

6) **연재웹툰 및 전체연도에 대한 카테고리 빈도**

![EDA_weekly_vs_yearly_category_count.png](https://user-images.githubusercontent.com/80459520/124466409-9b662c80-ddd1-11eb-8d5f-00ee5d7239e1.png)
- 카테고리 중 스토리가 가장 많이 연재되었다는 것을 알 수 있다.

<br/>

7) **연도별 카테고리 추이**

![EDA_yearly_category_count.png](https://user-images.githubusercontent.com/80459520/124466736-e2542200-ddd1-11eb-92d8-9eaa76dc6951.png)
- 스토리와 에피소드는 증가추세지만 옴니버스는 변화가 미비하다는 것을 알 수 있다.

<br/>

8) **연재웹툰 및 전체연도에 대한 세부장르 빈도**

![EDA_weekly_yearly_genre_count.png](https://user-images.githubusercontent.com/80459520/124466967-2ba47180-ddd2-11eb-91d1-2ebbf23371ee.png)
- 2021 : 로맨스 > 드라마 > 판타지 순으로 장르 분포
- 전체 : 드라마 > 판타지 > 로맨스 순으로 장르 분포
> 2021년엔 로맨스 장르의 웹툰이 다른 연도들에 비해 많이 다뤄졌다는 것을 알 수 있다.

<br/>

9) **세부장르별 추이**

![EDA_yearly_genre_count.png](https://user-images.githubusercontent.com/80459520/124467585-fea48e80-ddd2-11eb-9407-8734521d8894.png)
- 로맨스, 드라마, 스릴러, 판타지, 액션 장르는 높은 증가추세를 보이고 있지만 개그, 시대극 장르는 다른 장르에 비래 인기가 없다고 할 수 있다.

<br/>

### 2-2 가설에 대한 검증

가설 1) _순위가 높은 웹툰은 평점과 분량, 참여도 모두 높을 것이다._

![EDA_Hypothesis_1-1.png](https://user-images.githubusercontent.com/80459520/124545330-d44ee180-de63-11eb-8295-3565f9ae0f5a.png)
> score : 순위를 점수로 수치화한 지표
- score와 참여도간의 상관계수가 0.81로 강한 양의 상관관계를 보이는 것을 알 수 있다.
- score와 평점, 분량은 각각 0.051, 0.085의 상관계수를 가지므로 상관관계가 없다고 볼 수 있다.
- **결론 : 순위가 높을수록 참여도가 높다.**

<카테고리별 세분화한 score와의 상관관계도>
![EDA_Hypothesis_1-2.png](https://user-images.githubusercontent.com/80459520/124546511-b3878b80-de65-11eb-9517-5bba2599860e.png)
- 에피소드 : 평점, 분량 모두 약한 음의 상관관계를 가지고 있다.
- 스토리 : 평점, 분량 모두 score와 상관관계가 없다고 할 수 있다.
- 옴니버스 : 참여도는 약한 양의 상관관계, 평점은 약한 음의 상관관계, 분량은 상관관계가 없다고 할 수 있다.
- **결론 : 세분화했을 때 옴니버스는 참여도에 대해 약한 양의 상관관계를 보였고, 에피소드와 옴니버스에서는 평점과 분량에도 관계가 보였지만 스토리의 수가 압도적으로 많기때문에(6번 참고) 전체적으로 봤을 때 관계가 없다고 결론이 도출되었다.**

<br/>

가설 2) _평점이 낮은 회차는 분량과 참여도가 낮을 것이다._

![EDA_Hypothesis_2.png](https://user-images.githubusercontent.com/80459520/124547113-9901e200-de66-11eb-8f48-2fc20413e02f.png)
```
star_person : 평점과 참여도간 상관계수
star_img : 평점과 분량간 상관계수
img_person : 분량과 참여도간 상관계수
```
- 각 웹툰의 평점과 참여도간의 상관계수를 구해 평균낸 값이 -0.4013이므로 평점과 참여도간 약한 음의 상관관계를 가진다고 할 수 있다.
- 카테고리별로 세분화했을 때에도 평점과 참여도간 약한 음의 상관관계를 가진다.

<평점의 1분위수를 기준으로 기준을 나눠 평가지표의 분포 및 통계량 확인>
![EDA_project%208f7720df02474eeeb191461ae73f2b44/Untitled%203.png](EDA_project%208f7720df02474eeeb191461ae73f2b44/Untitled%203.png)

- **결론 : 평점이 낮은 회차일수록 참여도가 높다는 것을 알 수 있다. 원인파악을 위해 추후에 추가적인 분석이 필요해보인다. ex)평점이 낮은 회차가 업로드된 시기의 뉴스를 통한 이슈파악**

<br/>

가설 3) _가을에 로맨스 장르의 웹툰이 인기가 많을 것이다._

#### <방법 1. 월별 장르간 웹툰 수를 통한 계절별 장르의 분포 시각화>
![EDA_Hypothesis_3-1.png](https://user-images.githubusercontent.com/80459520/124547912-e2066600-de67-11eb-9d17-84178c49fce0.png)
- 첫번째 그래프를 통해 로맨스와 그와 비슷한 장르인 감성이 1~4월, 봄에 인기가 더 많다고 할 수 있다.

#### <방법 2. 월별 장르간 참여도 수를 통한 각 월의 인기장르를 선정, 각 월의 인기장르 분포 시각화>
![EDA_Hypothesis_3-2.png](https://user-images.githubusercontent.com/80459520/124548520-cbacda00-de68-11eb-82b3-aaad83a7d361.png)
- 가을에는 개그가 인기가 많고, 로맨스는 4, 6, 7, 8월에 가장 높아 대체적으로 여름에 인기가 높다고 할 수 있다.

- **결론 : 웹툰 수와 참여도 수로 인기장르를 선정했을 때의 결과가 다르다는 것을 알 수 있다. 데이터를 바라보는 관점에 따라 결과가 달라질 수 있다는 것을 알 수 있다.**

<br/>

# 💡 Project Preparation

### 🎨 Requirements

- python

### 🎨 Installation

```markdown
import pickle
import platform
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
from sklearn.preprocessing import StandardScaler, MinMaxScaler
```

# 💡 Project Review

### Review

- 반복되는 코드에 대해 변수와 함수로 저장할 필요성을 느꼈습니다.
- EDA과정에서 결과를 도출할 때 분석가의 주관적 판단이 개입될 수 있기에 해당 분야의 도메인지식에 대한 필요성, 그리고 이를 통해 신뢰할 수 있는 결과를 내기위한 깊은 분석이 필요하다는 것을 느꼈습니다.
- 각 회차마다 댓글 수와 댓글 내용을 수집하여 다른 인사이트를 도출해보면 좋을 것 같습니다.

> 자세한 EDA과정 : [webtoon_EDA.ipynb](https://github.com/aeea-0605/eda-repo-3/blob/main/webtoon_EDA.ipynb)
