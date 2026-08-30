# lec08 - Plotly

[이전 강의](./lec07_Seaborn.md) · [전체 목차](./README.md) · [용어사전](./용어사전.md) · [원본 Notebook](../../sam/lec08_시각화_plotly__.ipynb) · [다음 강의](./lec09_Folium.md)

## 오늘 이것만 기억하기

> Plotly는 마우스를 올려 값을 보고, 확대하거나 범례를 눌러 항목을 숨길 수 있는 그래프를 만듭니다.

Plotly는 확대, 이동, 툴팁, 범례 토글이 가능한 대화형 그래프를 만듭니다. Notebook, HTML, 웹 애플리케이션에서 탐색 가능한 결과를 공유할 때 유용합니다.

처음에는 사용하기 쉬운 `plotly.express`만 익힙니다. `graph_objects`와 서브플롯은 기본 그래프가 익숙해진 다음 봅니다.

## 1. Express와 Graph Objects

| API | 별칭 | 적합한 경우 |
|---|---|---|
| Plotly Express | `px` | DataFrame에서 표준 차트를 빠르게 생성 |
| Graph Objects | `go` | trace, 축, 서브플롯을 세밀하게 구성 |

```python
import plotly.express as px
import plotly.graph_objects as go
```

Plotly에서 **Figure**는 전체 그래프이고 **trace**는 Figure 안의 선, 막대, 캔들 같은 데이터 계열 하나입니다.

## 2. Express로 선과 막대

```python
df = px.data.gapminder().query("country == 'Canada'")

fig = px.line(df, x="year", y="lifeExp", title="캐나다 기대수명")
fig.update_layout(width=800, height=300)
fig.show()

fig = px.bar(df, x="year", y="lifeExp", title="캐나다 기대수명")
fig.update_layout(width=800, height=300)
fig.show()
```

한 줄씩 읽으면 “Canada 행만 고른다 → year를 x축으로 놓는다 → lifeExp를 y축으로 놓는다 → 화면에 보여 준다”는 뜻입니다.

- `px.data.gapminder()`는 Plotly 패키지에 포함된 예제 데이터입니다.
- `update_layout`은 크기, 제목, 축, 범례 등 전체 레이아웃을 수정합니다.
- 브라우저 또는 Notebook에서 마우스를 올리면 각 값이 표시됩니다.

## 3. Graph Objects와 캔들스틱

```python
import pandas as pd

url = "https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv"
stock = pd.read_csv(url)

fig = go.Figure()
fig.add_trace(go.Candlestick(
    x=stock["Date"],
    open=stock["AAPL.Open"],
    high=stock["AAPL.High"],
    low=stock["AAPL.Low"],
    close=stock["AAPL.Close"],
    name="AAPL",
))
fig.show()
```

캔들 하나는 시가(open), 고가(high), 저가(low), 종가(close)를 표현합니다. 원격 CSV를 읽는 이 예제는 인터넷 연결이 필요합니다. 반복 학습하려면 CSV를 로컬 `datas`에 저장하고 출처와 기준일을 함께 기록하는 편이 재현성이 좋습니다.

## 4. 서브플롯과 trace 배치

```python
from plotly.subplots import make_subplots

fig = make_subplots(rows=1, cols=2)

fig.add_trace(
    go.Scatter(x=[1, 2, 3], y=[4, 5, 6], name="왼쪽"),
    row=1, col=1,
)
fig.add_trace(
    go.Scatter(x=[20, 30, 40], y=[50, 60, 70], name="오른쪽"),
    row=1, col=2,
)

fig.update_layout(height=350, width=900)
fig.show()
```

`make_subplots`로 격자를 만든 뒤 각 `add_trace`에 `row`, `col`을 지정합니다. Matplotlib의 Axes에 직접 그리는 방식과 달리 Plotly는 Figure에 trace를 추가하며 위치를 지정합니다.

## 5. 대화형 결과 저장

```python
fig.write_html("plotly_chart.html", include_plotlyjs="cdn")
```

- HTML은 브라우저에서 대화형 기능을 유지합니다.
- `include_plotlyjs="cdn"`은 파일이 작지만 열 때 인터넷이 필요합니다.
- 완전한 오프라인 파일이 필요하면 `include_plotlyjs=True`를 사용하면 파일 크기가 커집니다.

## 핵심 체크리스트

- Plotly가 움직이며 확인하는 대화형 그래프라는 것을 아나요?
- 처음에는 `px.line`, `px.bar`를 사용하면 된다는 것을 아나요?
- `fig.show()`로 그래프를 표시할 수 있나요?
- HTML로 저장하면 그래프의 대화형 기능을 유지할 수 있다는 것을 아나요?
