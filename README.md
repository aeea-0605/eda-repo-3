# 네이버 웹툰 크롤링을 통한 탐색적 데이터 분석 (EDA) 🎨
---
## 1. 개요

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

---
## 2. EDA 결과 요약

### 2-1. 기간별, 장르별 웹툰 빈도분석

![EDA_project%208f7720df02474eeeb191461ae73f2b44/Untitled.png](EDA_project%208f7720df02474eeeb191461ae73f2b44/Untitled.png)

![EDA_project%208f7720df02474eeeb191461ae73f2b44/Untitled%201.png](EDA_project%208f7720df02474eeeb191461ae73f2b44/Untitled%201.png)

- 가설 1의 결과 - *순위가 높은 웹툰은 평점, 분량, 참여도가 높을 것이다.*
    - 평점을 매긴 참여도 수와 양의 상관관계를 가진다.
    - 순위가 높을수록 참여도의 상관도가 높다고 볼 수 있다.
    - 순위와 평점, 분량은 큰 상관관계를 발견할 수 없었다.

---

![EDA_project%208f7720df02474eeeb191461ae73f2b44/Untitled%202.png](EDA_project%208f7720df02474eeeb191461ae73f2b44/Untitled%202.png)

- 가설 2의 결과 - *평점이 낮은 회차는 분량과 참여도가 낮을 것이다.*
    - 각 웹툰간 상관관계의 평균을 통해 star_person값 -0.4013으로 평균과 참여도 간 약한 음의 상관관계를 가진다는 것을 알 수 있다.
    - 카테고리별, 세부장르별 상관관계에서도 평점과 참여도 간 약한 음의 상관관계를 보인다.

---

<각 웹툰별 평점, 분량, 참여도 컬럼을 MinMaxScaling 한 결과>

![EDA_project%208f7720df02474eeeb191461ae73f2b44/Untitled%203.png](EDA_project%208f7720df02474eeeb191461ae73f2b44/Untitled%203.png)

---

![EDA_project%208f7720df02474eeeb191461ae73f2b44/Untitled%204.png](EDA_project%208f7720df02474eeeb191461ae73f2b44/Untitled%204.png)

![EDA_project%208f7720df02474eeeb191461ae73f2b44/Untitled%205.png](EDA_project%208f7720df02474eeeb191461ae73f2b44/Untitled%205.png)

- 가설 3의 결과 - *가을에는 로맨스 장르의 웹툰이 인기가 많을 것이다.*
    - 장르별 추이 그래프로 확인한 결과 : 로맨스와 로맨스와 비슷한 장르의 감성의 웹툰이 가을에 인기있을 줄 알았지만 1 ~ 4월, 봄에 더 인기가 많았다고 할 수 있다. 나머지 장르에서는 대체로 고루 퍼져있는 것을 알 수 있다.
    - 장르의 월별 분포 확인한 결과 :  가을에는 개그장르가 가장 인기가 많았고, 로맨스 장르는 4~6월에 가장 높아 상반기에 인기가 많다는 것을 알 수 있다. 개그장르가 가장 인기있는 장르이며, 다음으로 로맨스 장르가 인기있는 달이 많다. 1월에는 감성 장르, 5월에는 액션 장르, 12월에는 드라마 장르가 인기 장르로 보인다.

# 💡 Project Preparation

### 🎨 Requirements

- python

### 🎨 Installation

```markdown
import pickle
import platform
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
from sklearn.preprocessing import StandardScaler, MinMaxScaler
```

### 🎨 Dataset

- Naver Webtton Crawling ([link in bio](https://comic.naver.com/index.nhn))

# 💡 Project Review

### Review

- 반복되는 코드에 대해 변수와 함수로 저장할 필요성을 느꼈습니다.
- EDA과정에서 결과를 도출할 때 분석가의 주관적 판단이 개입될 수 있기에 해당 분야의 도메인지식에 대한 필요성, 그리고 이를 통해 신뢰할 수 있는 결과를 내기위한 깊은 분석이 필요하다는 것을 느꼈습니다.
- 각 회차마다 댓글 수와 댓글 내용을 수집하여 다른 인사이트를 도출해보면 좋을 것 같습니다.

# 💡 Built with

- 이승주
    - Crawling, 데이터 전처리, EDA, git 코드정리
    - GitHub : [https://github.com/aeea-0605](https://github.com/aeea-0605)
- 고현실
    - EDA, README 작성
    - GitHub : [https://github.com/kohyunsil](https://github.com/kohyunsil)
