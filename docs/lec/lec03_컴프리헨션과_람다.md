# lec03 - 컴프리헨션과 람다

[이전 강의](./lec02_DataFrame_활용.md) · [전체 목차](./README.md) · [용어사전](./용어사전.md) · [원본 Notebook](../../sam/lec03_람다__.ipynb) · [다음 강의](./lec04_머신러닝_기초.md)

## 오늘 이것만 기억하기

> 컴프리헨션은 반복해서 새 목록을 만들 때, `lambda`는 아주 짧은 함수를 잠깐 전달할 때 사용합니다.

처음부터 한 줄 코드를 외우지 않습니다. 먼저 평범한 `for`문을 이해한 뒤, 같은 일을 짧게 쓴 모습이라고 비교합니다.

## 학습 목표

- 반복문을 리스트 컴프리헨션으로 간결하게 표현한다.
- 짧은 함수를 `lambda`로 작성한다.
- Series의 각 값에 함수를 적용하는 `apply`를 이해한다.
- 간결함과 가독성·성능 사이의 균형을 판단한다.

## 1. 리스트 컴프리헨션

리스트 컴프리헨션은 반복 결과를 새 리스트로 수집합니다.

### 조건에 맞는 값만 필터링

```python
evens = [v for v in range(1, 11) if v % 2 == 0]
# [2, 4, 6, 8, 10]
```

한 줄을 다음 순서로 읽습니다.

```text
range(1, 11)          → 1부터 10까지 준비
for v in ...          → 숫자를 하나씩 v에 넣기
if v % 2 == 0         → 짝수만 통과
맨 앞의 v             → 통과한 값을 결과 목록에 담기
```

구조는 `[결과식 for 변수 in 반복대상 if 필터조건]`입니다. 뒤쪽 `if`는 조건을 만족하지 않는 값을 결과에서 제외합니다.

### 모든 값을 조건에 따라 변환

```python
converted = [v * 2 if v > 3 else v for v in range(1, 6)]
# [1, 2, 3, 8, 10]
```

구조는 `[참일_때_값 if 조건 else 거짓일_때_값 for 변수 in 반복대상]`입니다. 삼항 표현식은 결과식 위치에 오며 모든 입력이 결과에 포함됩니다.

| 목적 | 형태 |
|---|---|
| 일부만 남기기 | `[x for x in items if condition]` |
| 모두 남기되 값 바꾸기 | `[a if condition else b for x in items]` |

## 2. `lambda`: 이름 없는 짧은 함수

일반 함수와 람다는 다음처럼 대응합니다.

```python
def add(n1, n2):
    return n1 + n2

add_lambda = lambda n1, n2: n1 + n2
```

람다의 기본형은 `lambda 매개변수: 반환식`이며 표현식 하나만 작성합니다.

처음 배우는 단계에서는 아래 두 코드가 같은 일을 한다는 것만 확인합니다.

```python
def double(n):
    return n * 2

double_short = lambda n: n * 2
```

읽기 쉬운 `def`를 먼저 쓸 수 있다면 충분합니다. `lambda`는 Pandas의 `apply`처럼 함수를 바로 전달해야 할 때 다시 사용합니다.

```python
double = lambda n: n * 2
positive_or_zero = lambda n: n if n > 10 else 0
```

다음 경우에는 `def`가 더 적합합니다.

- 여러 단계의 처리나 여러 조건문이 필요할 때
- 같은 함수를 여러 곳에서 재사용할 때
- 함수 이름과 문서 문자열이 이해에 도움을 줄 때
- 예외 처리나 디버깅이 필요할 때

람다는 “무조건 1회용”이라기보다 **짧은 함수를 다른 함수에 인자로 전달할 때** 특히 유용합니다.

## 3. DataFrame과 `apply`

```python
import pandas as pd

df = pd.DataFrame({
    "name": ["kim", "hong", "park"],
    "age": [20, 25, 30],
})

df["age_plus_10"] = df["age"].apply(lambda age: age + 10)
df["status"] = df["age_plus_10"].apply(
    lambda age: "성인" if age >= 20 else "미성년"
)
```

`Series.apply(func)`는 각 원소를 함수에 넣고 반환값으로 새 Series를 만듭니다.

### 가능한 경우 벡터 연산 우선

단순 산술은 `apply`보다 Pandas/NumPy의 벡터 연산이 더 간단하고 빠릅니다.

```python
df["age_plus_10"] = df["age"] + 10
```

조건 분기도 대규모 데이터에서는 다음처럼 표현할 수 있습니다.

```python
import numpy as np

df["status"] = np.where(df["age_plus_10"] >= 20, "성인", "미성년")
```

`apply`는 Python 함수로 복잡한 규칙을 표현해야 할 때 사용합니다.

## 4. 원본 Notebook 실행 시 주의점

원본은 같은 `age` 열에 `+10`을 직접 적용한 뒤 다시 `apply(lambda a: a+10)`을 적용합니다. 전체 셀을 순서대로 실행하면 나이는 원래보다 총 20 증가합니다. 변화 전후를 비교하려면 새 열을 만드는 편이 안전합니다.

```python
df["age_plus_10"] = df["age"] + 10
```

## 핵심 체크리스트

- 컴프리헨션이 반복 결과를 새 리스트에 모은다는 것을 아나요?
- `lambda n: n * 2`가 입력값을 두 배로 돌려주는 함수라고 읽을 수 있나요?
- 단순히 10을 더할 때는 `df["age"] + 10`이 가장 쉽다는 것을 아나요?
