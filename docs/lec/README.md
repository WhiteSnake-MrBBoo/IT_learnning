# 처음 배우는 사람을 위한 Python 데이터 수업

![표에서 Python, 머신러닝, 시각화까지 이어지는 초보자의 학습 여정](./assets/beginner-learning-journey.png)

처음에는 코드가 외국어처럼 보이는 것이 정상입니다. 이 자료는 코드를 외우는 책이 아니라, **한 줄씩 읽고 직접 실행하면서 뜻을 알아가는 안내서**입니다.

## 처음이라면 여기서 시작하세요

아래 세 문서만 순서대로 엽니다.

1. [왕초보 시작하기](./START_HERE.md) — Notebook을 여는 법, 셀 실행, 변수와 함수
2. [쉬운 용어사전](./용어사전.md) — 모르는 단어가 나올 때 찾아보기
3. [lec01 - DataFrame 기초](./lec01_DataFrame_기초.md) — 첫 데이터 표 만들기

설치가 아직 안 되었다면 [설치 가이드](./INSTALL.md)의 “가장 쉬운 설치” 부분만 따라 합니다.

## 이 수업에서 만드는 큰 그림

```text
표를 읽는다
  ↓
필요한 행과 열을 고른다
  ↓
비어 있는 값을 정리한다
  ↓
컴퓨터가 숫자나 종류를 예측하도록 학습시킨다
  ↓
그래프와 지도로 결과를 확인한다
```

처음부터 머신러닝 전체를 이해하려고 하지 않아도 됩니다. 매 강의의 **“오늘 이것만 기억하기”** 상자 한 개씩만 익히면 다음 강의로 넘어갈 수 있습니다.

## 강의 순서

| 순서 | 문서 | 원본 실습 파일 | 오늘의 질문 | 예상 시간 |
|---:|---|---|---|---:|
| 준비 | [왕초보 시작하기](./START_HERE.md) | - | Notebook은 어떻게 실행할까? | 20분 |
| 준비 | [공통 핵심 개념](./00_공통_핵심개념.md) | - | 데이터 공부의 전체 순서는? | 15분 |
| 1 | [lec01 - DataFrame 기초](./lec01_DataFrame_기초.md) | [Notebook](../../sam/lec01_DataFrame__.ipynb) | 표에서 원하는 값을 어떻게 고를까? | 60분 |
| 2 | [lec02 - DataFrame 활용](./lec02_DataFrame_활용.md) | [Notebook](../../sam/lec02_DataFrame활용__.ipynb) | 조건에 맞는 사원만 어떻게 찾을까? | 50분 |
| 3 | [lec03 - 컴프리헨션과 람다](./lec03_컴프리헨션과_람다.md) | [Notebook](../../sam/lec03_람다__.ipynb) | 반복 작업을 짧게 쓰려면? | 40분 |
| 4 | [lec04 - 머신러닝 기초](./lec04_머신러닝_기초.md) | [Notebook](../../sam/lec04_머신러닝기초__.ipynb) | 컴퓨터는 어떻게 가격을 예측할까? | 50분 |
| 5 | [lec05 - 전처리·가공](./lec05_머신러닝_전처리_가공.md) | [Notebook](../../sam/lec05_머신러닝_전처리가공__.ipynb) | EDA·이상치·스케일링·PCA를 어떻게 안전하게 적용할까? | 2회 × 60분 |
| 6 | [lec06 - Matplotlib](./lec06_Matplotlib.md) | [기본편](../../sam/lec06_강_시각화_matplotlib__.ipynb) · [확장편](../../sam/lec06_시각화_matplotlib__.ipynb) | 가장 기본적인 그래프는 어떻게 그릴까? | 60분 |
| 7 | [lec07 - Seaborn](./lec07_Seaborn.md) | [Notebook](../../sam/lec07_시각화_seaborn__.ipynb) | 그룹별 차이를 쉽게 그리려면? | 45분 |
| 8 | [lec08 - Plotly](./lec08_Plotly.md) | [Notebook](../../sam/lec08_시각화_plotly__.ipynb) | 움직이는 그래프는 어떻게 만들까? | 35분 |
| 9 | [lec09 - Folium](./lec09_Folium.md) | [Notebook](../../sam/lec09_시각화_folium__.ipynb) | 지도에 장소를 어떻게 표시할까? | 40분 |
| 10 | [lec10 - Pandas Plot](./lec10_Pandas_Plot.md) | [Notebook](../../sam/lec10_시각화_pandas__.ipynb) | 표에서 바로 그래프를 그리려면? | 30분 |
| 11 | [lec11 - 자전거 대여량 회귀 실습](./lec11_자전거_대여량_회귀.md) | [Notebook](../../sam/lec11_실습_회귀_bike__공모전.ipynb) | 시간과 날씨에 따른 대여량 패턴을 어떻게 찾을까? | 70분 |
| 12 | [lec12 - Titanic 생존 분류 실습](./lec12_Titanic_생존_분류.md) | [Notebook](../../sam/lec12_실습_분류_titanic__.ipynb) | 누가 생존했는지 분류하고 오답의 종류까지 어떻게 평가할까? | 2회 × 60분 |

## 문서를 읽는 방법

각 강의는 같은 순서로 읽습니다.

1. **오늘 이것만 기억하기**를 먼저 읽습니다.
2. 그림으로 전체 모양을 확인합니다.
3. 짧은 코드만 직접 입력합니다. 복사·붙여넣기보다 한 번 타이핑하는 편이 좋습니다.
4. 코드 아래의 “이 줄을 읽는 법”을 소리 내어 읽습니다.
5. 예상 결과와 내 결과를 비교합니다.
6. 마지막 체크 문제 3개 중 2개 이상 답하면 다음 강의로 갑니다.

## 코드가 길어 보일 때 읽는 순서

예를 들어 다음 코드를 처음부터 한 덩어리로 보지 않습니다.

```python
emp.loc[emp["DEPTNO"] == 10, ["ENAME", "SAL"]]
```

오른쪽 안쪽부터 작은 조각으로 읽습니다.

```text
emp["DEPTNO"]             → 부서 번호 열을 꺼낸다
emp["DEPTNO"] == 10       → 부서 번호가 10인지 확인한다
["ENAME", "SAL"]         → 이름과 급여 열을 고른다
emp.loc[조건, 열 목록]     → 조건에 맞는 행과 열을 보여준다
```

코드는 긴 문장이 아니라 작은 레고 블록 여러 개가 연결된 것입니다.

## 실습 데이터

| 파일 | 쉽게 말하면 | 사용 강의 |
|---|---|---|
| [BostonHousing.csv](../../datas/BostonHousing.csv) | 지역별 특징과 주택 가격 표 | lec01, 04, 05 |
| [emp.csv](../../datas/emp.csv) | 사원 명단과 급여 표 | lec02 |
| [dept.csv](../../datas/dept.csv) | 부서 이름과 위치 표 | lec02 |
| [jeju.csv](../../datas/jeju.csv) | 제주 장소와 위도·경도 표 | lec09 |
| [Bike Sharing Demand](../../datas/bike/train.csv) | 시간·날씨별 자전거 대여량 표 | lec11 |
| [Titanic](../../datas/titanic/train.csv) | 승객 정보와 생존 여부 표 | lec12 |

> `lec01` 원본에는 현재 없는 `Boston-house-price-data.csv`가 적혀 있습니다. 실습할 때는 실제 파일인 `../../datas/BostonHousing.csv`를 사용합니다.
>
> lec11의 Bike CSV와 lec12의 Titanic CSV는 각각 `datas/bike`, `datas/titanic`에 포함되어 있습니다. Kaggle 원본과 라이선스·최신 버전을 확인하려면 [Bike Sharing Demand](https://www.kaggle.com/competitions/bike-sharing-demand/data)와 [Titanic](https://www.kaggle.com/competitions/titanic/data) 페이지를 참고합니다.

## 전체 라이브러리 설치

모든 강의에 필요한 패키지는 [requirements.txt](./requirements.txt)에 모아 두었습니다.

```powershell
python -m pip install -r .\docs\lec\requirements.txt
```

설치 오류가 나면 오류 문장의 마지막 5줄을 먼저 읽고 [설치 가이드](./INSTALL.md)를 확인합니다.
