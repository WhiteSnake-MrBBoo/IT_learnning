# lec06 - Matplotlib

[이전 강의](./lec05_머신러닝_전처리_가공.md) · [전체 목차](./README.md) · [용어사전](./용어사전.md) · 원본: [기본편](../../sam/lec06_강_시각화_matplotlib__.ipynb) · [확장편](../../sam/lec06_시각화_matplotlib__.ipynb) · [다음 강의](./lec07_Seaborn.md)

## 오늘 이것만 기억하기

> `plt.plot(x, y)`로 데이터를 그리고, 제목·축 이름을 붙인 뒤 `plt.show()`로 보여 줍니다.

어떤 그래프를 골라야 할지 모르겠다면 [그림으로 보는 그래프 선택](./00_공통_핵심개념.md#4-그래프-선택-기준)을 먼저 봅니다.

두 `lec06` Notebook은 기본 차트 부분이 거의 같습니다. 확장편에만 있는 `subplots`/`subplot` 예제를 이 문서에 합쳐 중복 없이 정리했습니다. 각 차트를 언제 쓰는지는 [공통 그래프 선택 기준](./00_공통_핵심개념.md#4-그래프-선택-기준)을 참고합니다.

## 1. Matplotlib의 구조

- **Figure**: 그래프를 그리는 전체 종이입니다.
- **Axes**: 종이 안에서 실제 그래프 하나를 그리는 칸입니다. x/y축과 제목을 가집니다.
- `plt`: 현재 Figure/Axes를 대상으로 빠르게 그리는 상태 기반 인터페이스입니다.

처음에는 Figure와 Axes를 직접 만들지 않고 아래 네 줄만 실행합니다.

```python
import matplotlib.pyplot as plt

plt.plot([1, 2, 3], [10, 20, 15])
plt.title("첫 그래프")
plt.show()
```

첫 번째 리스트 `[1, 2, 3]`은 x축 위치, 두 번째 리스트 `[10, 20, 15]`는 각 위치의 y값입니다.

```python
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme()
plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False
```

`Malgun Gothic`은 Windows 글꼴입니다. 다른 운영체제에서는 설치된 한글 글꼴로 바꿉니다.

## 2. 기본 그래프 구성

```python
x = [1, 2, 3, 4]

plt.figure(figsize=(10, 3))
plt.plot(x, [1, 4, 9, 16], "b--", label="제곱")
plt.plot(x, [2, 5, 10, 14], "r--", label="비교")

plt.fill_between([2, 3], [4, 9], alpha=0.5)
plt.axvline(1.5, color="gray", linestyle="-")
plt.hlines(10, 1, 4, color="green")

plt.title("차트 제목")
plt.xlabel("X축")
plt.ylabel("Y축")
plt.xlim(0, 6)
plt.ylim(0, 20)
plt.grid(True)
plt.legend()
plt.show()
```

| 함수 | 역할 |
|---|---|
| `figure(figsize=(w, h))` | 전체 그림 크기(인치) |
| `title`, `xlabel`, `ylabel` | 제목과 축 이름 |
| `xlim`, `ylim` | 표시 범위 |
| `grid` | 격자 |
| `legend` | `label`을 모은 범례 |
| `show` | 완성된 그림 표시 |
| `fill_between` | 두 경계 사이 영역 채우기 |
| `axvline`/`vlines`/`hlines` | 기준 수직선/수평선 |

## 3. 대표 차트 API

```python
import numpy as np

plt.plot(x, y)                         # 선
plt.bar(categories, values)            # 막대
plt.scatter(x, y)                      # 산점도
plt.hist(values, bins=10)              # 히스토그램
plt.pie(ratio, labels=labels, autopct="%.1f%%")
plt.boxplot(values)                    # 박스플롯
plt.violinplot(values)                 # 바이올린플롯
```

`bins`는 히스토그램 구간 수입니다. 너무 적으면 구조가 사라지고 너무 많으면 잡음이 강조되므로 표본 수와 분포를 보며 조정합니다.

첫 학습에서는 선, 막대, 산점도, 히스토그램 네 가지만 먼저 실행합니다. 파이·박스·바이올린 플롯은 다음 복습 때 추가해도 됩니다.

### 박스플롯 읽기

```python
q1 = np.percentile(values, 25)
median = np.percentile(values, 50)
q3 = np.percentile(values, 75)
iqr = q3 - q1
```

- 상자 아래/가운데/위: Q1, 중앙값, Q3
- IQR: `Q3 - Q1`, 데이터의 가운데 50% 범위
- 일반적인 이상치 후보 경계: `Q1 - 1.5×IQR`, `Q3 + 1.5×IQR`
- 수염 끝이 반드시 실제 최솟값·최댓값인 것은 아닙니다. 경계 밖 값은 별도 점으로 표시됩니다.

바이올린플롯은 박스플롯의 요약에 분포 밀도 형태를 더해 여러 봉우리나 비대칭을 보기 좋습니다.

## 4. 이중축

```python
fig, ax1 = plt.subplots(figsize=(10, 3))
ax1.plot(x, [1, 4, 9, 16], color="green")
ax1.set_ylabel("첫 번째 단위", color="green")

ax2 = ax1.twinx()
ax2.plot(x, [200, 210, 240, 250], color="deeppink")
ax2.set_ylabel("두 번째 단위", color="deeppink")

plt.show()
```

`twinx()`는 x축을 공유하고 y축을 하나 더 만듭니다. 두 선의 높이가 비슷해 보여도 축 범위가 다를 수 있으므로 색, 단위, 눈금을 분명히 표시합니다. 단순 비교라면 분리된 서브플롯이 더 정직할 수 있습니다.

## 5. 여러 그래프 배치

### `plt.subplots`: Axes를 받아 제어

```python
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(14, 3))

ax1.bar(x, [2, 5, 10, 14])
ax1.set_title("막대")

ax2.plot(x, [1, 4, 9, 16], color="red")
ax2.set_title("선")

ax3.scatter(x, [3, 2, 8, 6])
ax3.set_title("산점도")

fig.suptitle("전체 차트 제목")
fig.tight_layout()
plt.show()
```

복잡한 그림은 Figure와 Axes를 명시적으로 다루는 이 객체 지향 방식이 권장됩니다.

### `plt.subplot`: 현재 영역을 순서대로 선택

```python
plt.figure(figsize=(10, 3))

plt.subplot(1, 3, 1)
plt.bar(x, [2, 5, 10, 14])

plt.subplot(1, 3, 2)
plt.plot(x, [1, 4, 9, 16])

plt.subplot(1, 3, 3)
plt.scatter(x, [3, 2, 8, 6])

plt.tight_layout()
plt.show()
```

`subplot(행 수, 열 수, 위치)`에서 위치는 1부터 시작합니다. 빠른 예제에는 편하지만 개별 그래프 설정이 많아지면 `subplots`가 더 읽기 쉽습니다.

## 핵심 체크리스트

- `plt.plot(x, y)`가 선 그래프를 그린다는 것을 아나요?
- 제목, x축 이름, y축 이름을 붙일 수 있나요?
- 변화는 선, 종류별 비교는 막대, 두 숫자의 관계는 산점도라고 고를 수 있나요?
- `plt.show()`가 그래프를 화면에 보여 주는 코드임을 아나요?
