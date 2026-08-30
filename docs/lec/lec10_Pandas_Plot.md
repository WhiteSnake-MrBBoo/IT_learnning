# lec10 - Pandas Plot

[이전 강의](./lec09_Folium.md) · [전체 목차](./README.md) · [용어사전](./용어사전.md) · [원본 Notebook](../../sam/lec10_시각화_pandas__.ipynb) · [다음 강의](./lec11_자전거_대여량_회귀.md)

## 오늘 이것만 기억하기

> 이미 DataFrame이 있다면 `df.plot(...)`으로 가장 빠르게 그래프를 확인할 수 있습니다.

Pandas는 Series/DataFrame에서 바로 `.plot()`을 호출해 빠르게 데이터를 탐색할 수 있습니다. 기본 백엔드는 Matplotlib이고 설정으로 Plotly를 사용할 수도 있습니다. 차트 선택 기준은 [공통 핵심 개념](./00_공통_핵심개념.md#4-그래프-선택-기준)에 정리되어 있습니다.

처음에는 다음 두 줄만 실행해 봅니다.

```python
df["sex"].value_counts().plot(kind="bar")
plt.show()
```

“성별 값이 각각 몇 번 나오는지 센 뒤, 막대그래프로 그려라”라고 읽습니다.

## 1. 기본 `.plot()`

```python
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = sns.load_dataset("penguins")

df[["bill_length_mm", "bill_depth_mm"]].plot(
    kind="line",
    figsize=(8, 2),
)
plt.show()
```

`df.plot()`의 기본 `kind`는 `line`입니다. 인덱스가 x축이 되므로 현재 행 순서가 실제 시간이나 의미 있는 순서를 나타내는지 확인합니다. penguins의 단순 행 순서를 선으로 연결한 그래프는 시간 추세가 아니며, API 연습 이상의 해석을 해서는 안 됩니다.

## 2. 강의의 차트 호출법

```python
# 범주 빈도 → 막대
df["sex"].value_counts().plot(kind="bar", figsize=(4, 2))

# 수치 열 하나의 분포 → 히스토그램
df["bill_length_mm"].plot(kind="hist", bins=20, figsize=(8, 2))

# 모든 수치 열의 히스토그램
df.hist(figsize=(8, 5))
plt.tight_layout()

# 수치 열 분포 요약 → 박스플롯
df[["bill_length_mm"]].plot(kind="box", figsize=(8, 2))

# 두 수치 열 관계 → 산점도
df.plot(
    kind="scatter",
    x="bill_length_mm",
    y="bill_depth_mm",
    figsize=(8, 2),
)

plt.show()
```

`.plot()`은 선택된 열과 인덱스를 바탕으로 빠르게 그리므로, 복잡한 통계 집계는 먼저 Pandas에서 명시적으로 계산하는 편이 좋습니다.

```python
counts = df["sex"].value_counts(dropna=False)
counts.plot(kind="bar")
```

## 3. 반환 객체로 세부 설정

Matplotlib 백엔드에서 `.plot()`은 보통 Axes를 반환합니다.

```python
ax = df["bill_length_mm"].plot(kind="hist", bins=20, figsize=(8, 3))
ax.set_title("부리 길이 분포")
ax.set_xlabel("부리 길이(mm)")
ax.set_ylabel("빈도")
plt.show()
```

빠르게 그린 뒤 제목, 축 이름, 단위를 Matplotlib API로 보완할 수 있습니다.

## 4. Plotly 백엔드로 전환

```python
pd.options.plotting.backend = "plotly"

fig = df[["bill_length_mm", "bill_depth_mm"]].plot(kind="line")
fig.show()
```

백엔드를 바꾸면 같은 Pandas `.plot()` 호출이 Plotly Figure를 만들기 때문에 대화형 기능을 사용할 수 있습니다. 이 설정은 현재 Python 세션의 이후 그래프에도 영향을 줍니다.

Matplotlib로 되돌리려면 다음처럼 설정합니다.

```python
pd.options.plotting.backend = "matplotlib"
```

백엔드에 따라 지원 옵션과 반환 객체가 다르므로 Matplotlib 전용 `figsize`나 Axes 메서드가 그대로 동작한다고 가정하지 않습니다.

## 5. 어떤 인터페이스를 선택할까?

| 목적 | 추천 |
|---|---|
| DataFrame을 즉시 탐색 | Pandas `.plot()` |
| 범주와 통계 요약을 간단히 표현 | Seaborn |
| 축, 주석, 레이아웃을 세밀하게 제어 | Matplotlib |
| 확대·툴팁·웹 공유 | Plotly |
| 위치 정보 | Folium |

Pandas Plot은 다른 시각화 도구를 대체한다기보다, 데이터 가공 직후 빠르게 확인하는 입구에 가깝습니다.

## 핵심 체크리스트

- `df.plot()`이 표에서 바로 그래프를 그리는 기능이라는 것을 아나요?
- 범주 개수는 `value_counts().plot(kind="bar")`로 볼 수 있나요?
- 기본 백엔드는 Matplotlib라는 것을 아나요?
- 움직이는 그래프가 필요하면 Plotly 백엔드를 선택할 수 있다는 것을 아나요?
