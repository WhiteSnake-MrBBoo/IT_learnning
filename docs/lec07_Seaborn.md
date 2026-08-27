# lec07 - Seaborn

[이전 강의](./lec06_Matplotlib.md) · [전체 목차](./README.md) · [용어사전](./용어사전.md) · [원본 Notebook](../sam/lec07_시각화_seaborn__.ipynb) · [다음 강의](./lec08_Plotly.md)

## 오늘 이것만 기억하기

> Seaborn은 `data=표`, `x=열 이름`, `y=열 이름`, `hue=Groupby로 나눌열` 순서로 읽습니다.

Seaborn은 Matplotlib 위에서 동작하며, DataFrame 열 이름과 범주 그룹을 직접 지정해 통계 그래프를 쉽게 만듭니다. 차트의 일반적 의미는 [공통 그래프 선택 기준](./00_공통_핵심개념.md#4-그래프-선택-기준)을 참고합니다.

Matplotlib이 좌표값을 직접 넣는 도화지라면, Seaborn은 표의 열 이름을 말하면 알아서 그려 주는 도구라고 생각합니다.

## 1. 기본 사용법

```python
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme()
df = sns.load_dataset("penguins")
df.head()
```

`sns.load_dataset`은 온라인 저장소에서 예제 데이터를 내려받으므로 최초 실행에 인터넷 연결이 필요합니다.

Seaborn 함수의 공통 구조는 다음과 같습니다.

```python
sns.scatterplot(data=df, x="carat", y="price", hue="clarity")
```

이 코드는 다음처럼 읽습니다.

```text
diamonds 표를 사용한다
x축에는 carat 열을 놓는다
y축에는 price 열을 놓는다
clarity 값이 다르면 색도 다르게 그린다
```

- `data`: 사용할 DataFrame
- `x`, `y`: 축에 연결할 열 이름
- `hue`: 범주에 따라 색을 나눌 열
- 필요에 따라 `style`, `size`, `row`, `col` 같은 시각적 채널을 사용합니다.

## 2. 강의의 차트

### 선과 막대

```python
fmri = sns.load_dataset("fmri")

sns.lineplot(
    data=fmri, x="timepoint", y="signal",
    hue="region", errorbar=None,
)

sns.barplot(
    data=fmri, x="timepoint", y="signal",
    hue="region", errorbar=None,
)
```

Seaborn은 같은 x/hue 조합의 여러 관측치를 기본적으로 평균 등 추정값으로 요약할 수 있습니다. `errorbar=None`은 불확실성 구간을 숨깁니다. 원자료의 모든 점을 그리는 것과 집계된 선/막대를 그리는 것은 해석이 다릅니다.

### 산점도와 히스토그램

```python
diamonds = sns.load_dataset("diamonds")
sns.scatterplot(data=diamonds, x="carat", y="price", hue="clarity")
sns.histplot(data=diamonds, x="price")
```

`hue` 범주가 너무 많으면 색 구분이 어려워집니다. 산점도가 과도하게 겹치면 투명도, 표본 추출, 더 작은 점을 고려합니다.

### 조건별 분포

```python
penguins = sns.load_dataset("penguins")
sns.displot(
    data=penguins,
    x="flipper_length_mm",
    col="species",
    row="sex",
    height=2,
    aspect=1.5,
)
```

`displot`은 자체 Figure를 관리하는 figure-level 함수입니다. 바깥에서 만든 `plt.figure(...)`의 크기를 사용하지 않으며 `height`, `aspect`, `row`, `col`로 배치를 제어합니다.

### 박스플롯과 바이올린플롯

```python
tips = sns.load_dataset("tips")

sns.boxplot(
    data=tips, x="day", y="total_bill", hue="smoker"
)

sns.violinplot(
    data=tips, x="day", y="total_bill",
    hue="smoker", split=True, inner="quart",
)
```

`split=True`는 hue가 두 그룹일 때 한 바이올린의 좌우를 나누어 비교합니다. `inner="quart"`는 사분위 정보를 내부에 표시합니다.

## 3. 피벗과 히트맵

원본 flights 데이터는 한 행에 연도, 월, 승객 수가 있는 긴 형태입니다. 히트맵을 위해 행=월, 열=연도인 행렬로 바꿉니다.

```python
flights = sns.load_dataset("flights")
matrix = flights.pivot(
    index="month",
    columns="year",
    values="passengers",
)

plt.figure(figsize=(12, 4))
sns.heatmap(matrix, annot=True, fmt="d")
plt.show()
```

- `annot=True`: 셀 안에 실제 값 표시
- `fmt="d"`: 정수 형식
- 색상 범례의 단위를 확인해야 합니다.

## 4. 페어플롯

```python
penguins = sns.load_dataset("penguins")
sns.pairplot(penguins, hue="species")
plt.show()
```

대각선은 각 변수의 분포, 나머지 칸은 두 변수의 관계를 보여줍니다. 그룹이 특정 변수 조합에서 분리되는지 빠르게 탐색할 수 있지만, 열이 많으면 그래프 수와 계산량이 제곱으로 늘어납니다. 필요한 수치 열만 먼저 선택하는 것이 좋습니다.

## 5. Axes-level과 Figure-level

| 종류 | 예 | 크기/배치 제어 |
|---|---|---|
| Axes-level | `lineplot`, `barplot`, `scatterplot`, `histplot`, `boxplot`, `violinplot`, `heatmap` | `ax=...` 또는 `plt.figure` |
| Figure-level | `displot`, `pairplot` | 함수의 `height`, `aspect`, `row`, `col` |

이 차이를 알면 `plt.figure(figsize=...)`가 왜 일부 Seaborn 함수에 반영되지 않는지 이해할 수 있습니다.

## 핵심 체크리스트

- `data`, `x`, `y`에 각각 무엇을 넣는지 아나요?
- `hue`가 그룹마다 색을 나누는 설정이라고 설명할 수 있나요?
- 분포는 `histplot`, 관계는 `scatterplot`을 고를 수 있나요?
- `load_dataset`은 인터넷이 필요할 수 있다는 것을 아나요?
