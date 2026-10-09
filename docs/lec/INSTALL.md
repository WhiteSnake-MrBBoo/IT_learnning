# 처음 배우는 사람을 위한 설치 및 실행

[전체 목차](./README.md) · [왕초보 시작하기](./START_HERE.md) · [의존성 파일](./requirements.txt)

## 터미널이 무엇인가요?

터미널은 마우스 대신 글자로 컴퓨터에 명령하는 창입니다. Windows에서는 시작 메뉴에서 `PowerShell`을 검색해 엽니다.

## 0. Python 설치 확인

PowerShell에 다음 한 줄을 입력합니다.

```powershell
python --version
```

`Python 3.x.x`처럼 나오면 다음 단계로 갑니다. “명령을 찾을 수 없다”는 메시지가 나오면 Python을 먼저 설치하고 PowerShell을 다시 엽니다.

## 가장 쉬운 설치

프로젝트 폴더를 연 PowerShell에서 아래 명령을 **한 줄씩** 실행합니다. 한 줄이 끝난 뒤 다음 줄을 실행합니다.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r .\docs\lec\requirements.txt
python -m jupyter lab
```

각 줄의 뜻은 다음과 같습니다.

| 명령 | 하는 일 |
|---|---|
| `python -m venv .venv` | 이 수업만 사용하는 독립된 Python 방 만들기 |
| `Activate.ps1` | 방 안으로 들어가기 |
| `pip install --upgrade pip` | 설치 도구를 최신 상태로 준비 |
| `pip install -r ...` | 수업 도구를 목록대로 한 번에 설치 |
| `jupyter lab` | Notebook 프로그램 열기 |

명령줄 앞에 `(.venv)`가 보이면 가상환경이 잘 활성화된 것입니다.

## 운영체제별 자세한 명령

프로젝트 루트 `C:\001_Code_Programing\040_Woori\IT_learrning`에서 실행합니다. 위의 가장 쉬운 설치를 완료했다면 이 절은 건너뜁니다.

### Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r .\docs\lec\requirements.txt
python -m jupyter lab
```

PowerShell이 활성화 스크립트를 차단할 때는 현재 창에만 다음 설정을 적용한 뒤 다시 활성화합니다.

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

### Windows 명령 프롬프트

```bat
python -m venv .venv
.venv\Scripts\activate.bat
python -m pip install --upgrade pip
python -m pip install -r docs\lec\requirements.txt
python -m jupyter lab
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r docs/lec/requirements.txt
python -m jupyter lab
```

JupyterLab이 열리면 `sam` 폴더로 이동해 `lec01`부터 실행합니다. 커널 선택 화면이 나오면 방금 만든 `.venv`의 Python을 선택합니다.

## 설치 확인

```powershell
python -c "import numpy, pandas, sklearn, xgboost, lightgbm, matplotlib, seaborn, plotly, folium; print('모든 수업 라이브러리 import 성공')"
```

`모든 수업 라이브러리 import 성공`이 나오면 설치가 끝난 것입니다.

Jupyter 커널이 가상환경을 찾지 못할 때는 다음을 한 번 실행합니다.

```powershell
python -m ipykernel install --user --name woori-learning --display-name "Python (woori-learning)"
```

## Notebook 실행 시 알아둘 점

1. `lec01`의 원본 코드는 현재 없는 `Boston-house-price-data.csv`를 참조합니다. 다음처럼 실제 파일명을 사용합니다.

   ```python
   df = pd.read_csv("../datas/BostonHousing.csv")
   df.columns = df.columns.str.upper()
   ```

2. Seaborn의 `load_dataset`, Plotly의 원격 Apple CSV, Folium 지도 타일은 인터넷 연결이 필요합니다.
3. 한글이 네모로 표시되면 Matplotlib 폰트를 운영체제에 설치된 한글 폰트로 변경합니다.
4. Plotly 그래프가 Notebook에 표시되지 않으면 JupyterLab을 재시작하고 `nbformat` 설치 여부를 확인합니다.
5. `lec11`의 Bike CSV는 `datas/bike`, `lec12`의 Titanic CSV는 `datas/titanic`에 포함되어 있습니다. 각 Notebook을 `sam` 폴더에서 열면 `../datas/...` 상대 경로가 연결됩니다.
6. lec12에서 `xgboost`와 `lightgbm`을 처음 설치하면 시간이 조금 걸릴 수 있습니다. 설치가 끝났는데도 Notebook이 모듈을 찾지 못하면 Jupyter 커널을 다시 시작합니다.

## 자주 만나는 설치 오류

| 오류 마지막 줄 | 뜻 | 먼저 할 일 |
|---|---|---|
| `python is not recognized` | Python 명령을 찾지 못함 | Python 설치 후 PowerShell 다시 열기 |
| `running scripts is disabled` | PowerShell이 활성화 파일을 막음 | 아래의 `Set-ExecutionPolicy` 명령 실행 |
| `No module named ...` | 해당 라이브러리가 현재 환경에 없음 | `.venv` 활성화 후 requirements 다시 설치 |
| `FileNotFoundError` | 파일 이름이나 현재 폴더가 다름 | 프로젝트 루트에서 실행했는지 확인 |

## 패키지별 용도

| 패키지 | 필요한 이유 |
|---|---|
| `numpy` | 배열, 난수, 사분위수, RMSE 계산 |
| `pandas` | CSV와 DataFrame 처리 |
| `scikit-learn` | 데이터 분할, 선형회귀, 평가, 전처리 |
| `xgboost` | lec12의 XGBoost 부스팅 분류 모델 |
| `lightgbm` | lec12의 LightGBM 부스팅 분류 모델 |
| `matplotlib` | 정적 그래프 |
| `seaborn` | 통계 시각화와 예제 데이터 |
| `plotly` | 대화형 그래프 |
| `folium` | 지도 시각화 |
| `jupyterlab`, `ipykernel`, `nbformat` | `.ipynb` 실행과 그래프 출력 |

## 가상환경 종료

```powershell
deactivate
```
