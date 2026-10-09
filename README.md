# IT Learning

Python 기초, 데이터 분석, 머신러닝, 시각화, 웹 수업 자료를 정리한 학습 저장소입니다.

## 학습 문서

처음 학습한다면 다음 순서로 시작합니다.

1. [전체 문서 안내](./docs/README.md)
2. [강의 학습 목차](./docs/lec/README.md)
3. [왕초보 시작하기](./docs/lec/START_HERE.md)
4. [쉬운 용어사전](./docs/lec/용어사전.md)
5. [환경 설치 및 실행](./docs/lec/INSTALL.md)

## 폴더 구성

| 폴더 | 내용 |
|---|---|
| `docs` | 전체 문서 분류를 안내하는 문서 허브 |
| `docs/lec` | `sam` Notebook을 분석해 만든 초보자용 강의 문서와 그림 |
| `sam` | lec01~lec12 데이터 분석·머신러닝 Notebook |
| `datas` | 강의에서 사용하는 CSV 데이터 |
| `lec_python` | Python 수업 자료 |
| `lec_ml` | 머신러닝 수업 자료 |
| `lec_web` | 웹 수업 자료 |

## 전체 라이브러리 설치

프로젝트 폴더에서 다음 명령을 실행합니다.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r .\docs\lec\requirements.txt
python -m jupyter lab
```

## 브랜치 구성

- `main`: 검증된 학습 자료를 보관하는 기준 브랜치
- `develop`: 새로운 수업 자료와 문서 변경을 진행하는 작업 브랜치

Jupyter가 자동 생성하는 `.ipynb_checkpoints`와 로컬 가상환경은 Git에 포함하지 않습니다.
