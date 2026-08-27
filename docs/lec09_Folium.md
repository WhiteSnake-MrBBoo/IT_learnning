# lec09 - Folium

[이전 강의](./lec08_Plotly.md) · [전체 목차](./README.md) · [용어사전](./용어사전.md) · [원본 Notebook](../sam/lec09_시각화_folium__.ipynb) · [다음 강의](./lec10_Pandas_Plot.md)

## 오늘 이것만 기억하기

> Folium 좌표는 항상 `[위도, 경도]` 순서이고, 만든 마커는 `.add_to(지도)`로 지도에 붙입니다.

> 원본 Notebook의 첫 제목은 “plotly”로 적혀 있지만 실제 강의 내용과 코드는 **Folium 지도 시각화**입니다.

Folium은 Python에서 Leaflet 기반 HTML 지도를 만들고, 위도·경도 위치에 마커와 팝업을 추가합니다.

처음에는 “빈 지도 만들기 → 마커 하나 만들기 → 지도에 붙이기” 세 단계만 실행합니다.

```python
import folium

m = folium.Map(location=[37.4848, 126.7831], zoom_start=15)
folium.Marker([37.4848, 126.7831], popup="부천").add_to(m)
m
```

## 1. 좌표와 기본 지도

- 위도(latitude, `lat`): 남북 위치. 대한민국은 대략 33~38도입니다.
- 경도(longitude, `lng`/`lon`): 동서 위치. 대한민국은 대략 126~129도입니다.
- Folium의 위치 순서는 `[위도, 경도]`입니다.

```python
import folium

center = [37.4848, 126.7831]
map_view = folium.Map(location=center, zoom_start=15)
map_view
```

순서를 바꾸면 전혀 다른 지역이 표시됩니다. 열 이름과 범위를 먼저 확인합니다.

## 2. 마커와 팝업

```python
folium.Marker(
    location=[37.4848, 126.7831],
    tooltip="마우스를 올렸을 때 표시",
    popup="클릭했을 때 표시",
    icon=folium.Icon(color="green"),
).add_to(map_view)
```

- `tooltip`: 커서를 올렸을 때 간단히 표시합니다.
- `popup`: 클릭했을 때 텍스트나 HTML을 표시합니다.
- `add_to(map_view)`: 만든 객체를 지도에 연결합니다.

HTML 팝업은 이미지와 줄바꿈 등을 표현할 수 있지만 외부 입력을 그대로 넣으면 HTML 삽입 문제가 생길 수 있습니다. 신뢰할 수 없는 텍스트는 escape 처리합니다.

### 원형 마커

```python
folium.CircleMarker(
    location=[37.484056, 126.782528],
    radius=10,
    color="#3186cc",
    fill=True,
    fill_color="#3186cc",
    popup="부천역",
).add_to(map_view)
```

`CircleMarker`의 `radius`는 화면 픽셀 기준이라 확대/축소해도 화면상 크기가 유지됩니다. 실제 거리 반경을 미터로 표시하려면 `folium.Circle(radius=...)`을 사용합니다.

## 3. 마커 클러스터

많은 마커를 한 번에 그리면 겹치고 브라우저가 느려집니다. `MarkerCluster`는 가까운 마커를 숫자가 표시된 묶음으로 보여주고 확대하면 분리합니다.

```python
import numpy as np
from folium import plugins

rng = np.random.default_rng(0)
n = 100
locations = np.column_stack([
    rng.uniform(36, 38, n),
    rng.uniform(127, 128, n),
])
popups = [str(i) for i in range(n)]

map_view = folium.Map([37.566345, 126.977893], zoom_start=8)
plugins.MarkerCluster(locations, popups=popups).add_to(map_view)
map_view
```

고정된 난수 생성기를 사용하면 같은 위치를 재현할 수 있습니다.

## 4. 제주 데이터 실습

[jeju.csv](../datas/jeju.csv)는 `name`, `tel`, `lat`, `lng`, `addr`, `img`를 포함합니다.

```python
import html
import pandas as pd
from folium import plugins

df = pd.read_csv("../datas/jeju.csv")

locations = df[["lat", "lng"]].to_numpy()
popups = [
    (
        f"<b>{html.escape(str(row['name']))}</b><br>"
        f"{html.escape(str(row['tel']))}<br>"
        f"{html.escape(str(row['addr']))}<br>"
        f"<img src=\"{html.escape(str(row['img']), quote=True)}\" width=\"100\">"
    )
    for _, row in df.iterrows()
]

jeju_map = folium.Map([33.511, 126.493], zoom_start=9)
plugins.MarkerCluster(locations, popups=popups).add_to(jeju_map)
jeju_map
```

실제 분석에서는 다음도 검사합니다.

```python
df[["lat", "lng"]].isna().sum()
df["lat"].between(-90, 90).all()
df["lng"].between(-180, 180).all()
```

## 5. HTML 저장

```python
jeju_map.save("jeju_map.html")
```

파일을 브라우저로 열면 Notebook 없이도 공유할 수 있습니다. 다만 기본 지도 타일과 외부 팝업 이미지를 불러오려면 인터넷 연결이 필요합니다.

## 핵심 체크리스트

- 좌표 순서가 `[위도, 경도]`라는 것을 기억하나요?
- `folium.Map`으로 지도를 만들고 `Marker`를 붙일 수 있나요?
- 마커가 많으면 `MarkerCluster`로 묶는 이유를 아나요?
- 지도 타일과 외부 이미지는 인터넷이 필요할 수 있다는 것을 아나요?
