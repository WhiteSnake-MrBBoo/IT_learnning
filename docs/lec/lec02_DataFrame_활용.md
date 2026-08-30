# lec02 - DataFrame 활용

[이전 강의](./lec01_DataFrame_기초.md) · [전체 목차](./README.md) · [용어사전](./용어사전.md) · [원본 Notebook](../../sam/lec02_DataFrame활용__.ipynb) · [다음 강의](./lec03_컴프리헨션과_람다.md)

## 오늘 이것만 기억하기

> 긴 문제를 보면 **① 어떤 행을 찾는가 ② 어떤 열을 보여 주는가**로 나눕니다.

이 강의는 [lec01](./lec01_DataFrame_기초.md)의 선택, 결측, 집계, 결합을 `emp.csv`와 `dept.csv`에 적용합니다. 중복 문법 설명 대신 실제 문제를 어떤 순서로 푸는지에 집중합니다.

사원 표를 엑셀에서 필터한다고 생각하면 쉽습니다. “10번 부서”를 먼저 고른 뒤 “이름과 급여 열만 보기”를 하는 과정입니다.

## 1. 데이터 관계 이해

```python
import numpy as np
import pandas as pd

emp = pd.read_csv("../datas/emp.csv")
dept = pd.read_csv("../datas/dept.csv")
```

### 사원 `emp`

| 열 | 의미 |
|---|---|
| `EMPNO` | 사원 번호 |
| `ENAME` | 사원 이름 |
| `JOB` | 직무 |
| `MGR` | 관리자 사원 번호 |
| `HIREDATE` | 입사일 |
| `SAL` | 급여 |
| `COMM` | 커미션; 일부 결측 |
| `DEPTNO` | 부서 번호; 부서 테이블과 연결하는 키 |

### 부서 `dept`

| 열 | 의미 |
|---|---|
| `DEPTNO` | 부서 번호 |
| `DNAME` | 부서명 |
| `LOC` | 부서 위치 |

처음에는 `info()`, `shape`, `head()`, `isna().sum()`으로 크기·자료형·결측을 확인합니다.

## 2. 선택 문제를 읽는 법

문장을 **행 조건**과 **출력 열**로 분해합니다.

> “부서 번호가 10이고 급여가 2000 이상인 사원의 번호, 이름, 급여, 부서 번호”

```python
mask = (emp["DEPTNO"] == 10) & (emp["SAL"] >= 2000)
columns = ["EMPNO", "ENAME", "SAL", "DEPTNO"]

result = emp.loc[mask, columns]
```

코드를 한 조각씩 실행해 봅니다.

```python
emp["DEPTNO"] == 10
```

각 사원의 부서 번호가 10인지 확인하므로 `True`, `False`가 여러 개 나옵니다. 이 참/거짓 목록을 **마스크**라고 합니다.

```python
emp.loc[mask]
```

`True`인 사원 행만 남습니다. 마지막으로 `columns`를 넣으면 필요한 열만 보입니다.

이 형태는 `emp[columns][mask]`보다 행과 열의 의도가 명확하고, 값을 수정할 때 발생할 수 있는 연쇄 인덱싱 문제도 피합니다.

### 조건 연산 규칙

```python
emp.loc[emp["DEPTNO"].isin([20, 30])]
emp.loc[~emp["DEPTNO"].isin([20, 30])]
```

- `&`: 그리고(AND)
- `|`: 또는(OR)
- `~`: 부정(NOT)
- 여러 값 중 하나인지 확인할 때는 연속된 `|`보다 `isin([...])`이 읽기 쉽습니다.
- 각 비교식은 반드시 괄호로 감쌉니다. Python의 `and`, `or`가 아니라 `&`, `|`를 사용합니다.

## 3. 결측 처리와 파생 열

`COMM`이 없는 사원을 “커미션 0”으로 해석한다는 규칙을 적용합니다.

```python
emp["COMM"] = emp["COMM"].fillna(0)
emp["YSAL"] = emp["SAL"] * 12 + emp["COMM"]
```

연봉 파생식의 의미는 “월 급여 12개월 + 커미션”입니다. 원본의 `COMM`이 월 커미션인지 연간 커미션인지는 실제 업무 정의를 확인해야 합니다.

삭제 연습은 원본 보존을 위해 새로 읽거나 복사한 데이터에서 수행합니다.

```python
emp_drop = pd.read_csv("../datas/emp.csv")
emp_drop = emp_drop.dropna(subset=["COMM"])
emp_drop = emp_drop.drop(columns=["JOB", "MGR"])
```

## 4. 그룹 집계 문제

`groupby`는 반 학생을 반별로 모은 뒤 반마다 평균 점수를 계산하는 것과 같습니다. **누구끼리 묶을지**를 먼저 정하고 **무엇을 계산할지**를 뒤에 적습니다.

### 직무별 사원 수

```python
emp["JOB"].value_counts()
```

### 부서와 직무별 급여 합계

```python
salary_by_group = (
    emp.groupby(["DEPTNO", "JOB"])["SAL"]
       .sum()
       .reset_index()
)
```

### 부서별 급여 최솟값과 최댓값

```python
emp.groupby("DEPTNO")["SAL"].agg(["min", "max"])
```

### 열마다 다른 집계

```python
emp.groupby("DEPTNO").agg({"SAL": "min", "HIREDATE": "max"})
```

`HIREDATE`를 문자열 상태로 `max` 하면 날짜 순서가 아니라 문자열 비교가 될 수 있습니다. 날짜 분석 전에는 날짜형으로 변환합니다.

```python
emp["HIREDATE"] = pd.to_datetime(emp["HIREDATE"], dayfirst=True)
emp.groupby("DEPTNO").agg({"SAL": "min", "HIREDATE": "max"})
```

## 5. 사원과 부서 결합

`DEPTNO`가 관계를 연결하는 키입니다.

```text
사원 표: SMITH ─ DEPTNO 20 ┐
사원 표: JONES ─ DEPTNO 20 ├─ 부서 표: 20 ─ RESEARCH ─ DALLAS
사원 표: ALLEN ─ DEPTNO 30 ── 부서 표: 30 ─ SALES ─ CHICAGO
```

같은 `DEPTNO`를 찾아 사원 정보 옆에 부서 이름과 위치를 붙이는 작업이 `merge`입니다.

```python
employee_department = pd.merge(
    emp,
    dept,
    on="DEPTNO",
    how="inner",
    validate="many_to_one",
)
```

`validate="many_to_one"`은 여러 사원이 한 부서에 속한다는 기대를 검사합니다. 부서 번호가 `dept`에 중복되어 있으면 오류가 나므로 조용히 잘못된 행 수가 늘어나는 일을 막을 수 있습니다.

## 6. 실전 풀이 템플릿

```python
# 1) 읽기
emp = pd.read_csv("../datas/emp.csv")

# 2) 품질 확인
print(emp.shape)
print(emp.isna().sum())

# 3) 업무 규칙에 따른 정제
emp["COMM"] = emp["COMM"].fillna(0)

# 4) 파생 열
emp["YSAL"] = emp["SAL"] * 12 + emp["COMM"]

# 5) 조건 및 출력 열
mask = (emp["DEPTNO"] == 10) & (emp["SAL"] >= 2000)
answer = emp.loc[mask, ["EMPNO", "ENAME", "SAL", "YSAL", "DEPTNO"]]
```

## 핵심 체크리스트

- 문제에서 “찾을 행”과 “보여 줄 열”을 나눌 수 있나요?
- 조건 결과가 `True`와 `False`로 나온다는 것을 이해했나요?
- `groupby`는 같은 값끼리 묶어 합계·평균 등을 계산한다고 말할 수 있나요?
- `merge`는 공통 열을 이용해 두 표를 연결한다고 설명할 수 있나요?
