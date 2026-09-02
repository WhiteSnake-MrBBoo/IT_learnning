# JupyterLab Git / GitHub 반복 실습 강사용 가이드

이 문서는 학생이 JupyterLab의 `jupyterlab-git` UI를 직접 클릭하며 Git과 GitHub의 기본 흐름을 반복 학습하도록 돕는 강사용 진행 가이드입니다. Git 내부 이론이나 Terminal 명령 암기보다 **현재 Branch 확인 → 화면 조작 → 결과 확인**에 집중합니다.

실습의 핵심은 다음 두 흐름입니다.

```text
실습 1: main에서 Pull → Edit → Stage → Commit → Push

실습 2: branch1 작업 → Push → PR → Merge
        → main Pull → branch1에서 main Merge → Push → 다음 작업
```

> **수업 운영 전제:** 이 문서는 Git 동작을 반복 관찰하기 위해 `branch1`을 계속 사용하는 방식입니다. 실제 협업에서는 작업마다 `feature/...`, `fix/...`, `docs/...`처럼 새 Branch를 만들고 PR 병합 후 삭제하는 방식도 많이 사용합니다.

## 1. 학습 목표와 범위

수업을 마친 학생은 다음 작업을 JupyterLab UI에서 수행할 수 있어야 합니다.

- 현재 Branch가 `main`인지 `branch1`인지 확인합니다.
- GitHub 변경을 Fetch한 뒤 현재 Local Branch에 Pull합니다.
- Notebook을 수정하고 필요한 파일만 Stage합니다.
- Commit과 Push의 차이를 설명하고 실행합니다.
- 최신 `main`에서 `branch1`을 만들고 Remote Repository에 Push합니다.
- GitHub에서 `base: main`, `compare: branch1` 방향으로 Pull Request를 만듭니다.
- PR을 Merge한 뒤 Local `main`과 기존 Local `branch1`을 차례로 최신화합니다.
- GitHub에 표시되는 ahead / behind 상태를 읽습니다.

이 문서의 본 실습에서는 다음 고급 기능을 다루지 않습니다.

- Rebase와 Interactive Rebase
- Cherry-pick
- Force Push
- `reset --hard` 실습
- Stash 심화
- Merge Conflict 해결 심화
- Git Flow
- GitHub Actions

## 2. 네 가지 역할만 먼저 구분하기

| 항목 | 쉬운 역할 | 이 수업에서 하는 일 |
|---|---|---|
| **JupyterLab** | Notebook과 파일을 편집하는 작업 환경 | `01_git_test.ipynb`를 열고 수정·저장합니다. |
| **jupyterlab-git** | JupyterLab에서 Git을 GUI로 조작하는 확장 기능 | Stage, Commit, Push, Pull, Branch 전환과 Merge를 수행합니다. |
| **Git** | Local 버전 관리 시스템 | 내 PC의 Commit과 Branch 이력을 관리합니다. |
| **GitHub** | 인터넷의 Remote Repository와 협업 서비스 | Remote Branch, Pull Request, 리뷰와 Merge를 관리합니다. |

파일을 GitHub로 보내는 방향:

```text
파일 수정
   ↓
CHANGES
   ↓ Stage
Staged
   ↓ Commit
Local Repository
   ↓ Push
GitHub Remote Repository
```

GitHub 변경을 내 PC에 반영하는 방향:

```text
GitHub Remote Repository
   ↓ Fetch
Remote 변경 이력 확인
   ↓ Pull
현재 Local Branch에 반영
```

### Fetch와 Pull 차이

| 기능 | 초보자 설명 | 현재 파일에 미치는 영향 |
|---|---|---|
| **Fetch** | GitHub의 새 Commit을 내려받고 원격 Branch 정보를 갱신합니다. | 현재 Local Branch와 작업 파일에는 아직 합치지 않습니다. |
| **Pull** | Fetch한 원격 변경을 현재 Local Branch에 통합합니다. | 현재 Branch와 작업 파일이 바뀔 수 있습니다. |

강사 멘트:

> “Fetch는 원격 소식을 가져와 확인하는 단계이고, Pull은 그 소식을 현재 내가 서 있는 Local Branch에 실제 반영하는 단계입니다.”

## 3. 실습 전 준비

### 3-1. 프로그램과 계정

- JupyterLab 4.x 환경
- `jupyterlab-git` 확장 기능
- Git 2.x 이상
- 이메일 인증과 2FA를 마친 GitHub 계정
- GitHub Remote Repository에 Push할 수 있는 인증 환경

`jupyterlab-git` 공식 프로젝트는 JupyterLab 왼쪽의 Git 탭에서 확장을 열고, Git Sidebar 상단의 Pull·Push 버튼으로 Remote Repository와 통신하는 사용 흐름을 안내합니다. 설치 버전과 화면 폭에 따라 아이콘·메뉴 위치나 문구가 조금 달라질 수 있으므로 **기능 이름과 현재 Branch**를 함께 확인합니다.

공식 참고: [jupyterlab-git 프로젝트와 사용 안내](https://github.com/jupyterlab/jupyterlab-git)

### 3-2. 실습 Repository 조건

수업 전에 다음 상태를 준비합니다.

- Local Repository가 JupyterLab 파일 브라우저에서 열려 있습니다.
- Remote Repository `origin`이 GitHub 저장소를 가리킵니다.
- Local `main`이 GitHub의 `main`을 추적합니다.
- 첫 Commit이 존재합니다.
- `01_git_test.ipynb`를 만들 수 있는 쓰기 권한이 있습니다.
- Git Sidebar에 오류나 진행 중인 Merge가 없습니다.

> Git Sidebar가 Repository를 찾지 못하면 JupyterLab 파일 브라우저에서 Git Repository의 최상위 폴더를 먼저 엽니다. 그래도 보이지 않으면 강사가 `Open Git Repository in Terminal`을 사용해 위치와 Git 상태를 진단하되, 학생 실습 자체는 GUI로 계속 진행합니다.

### 3-3. `.gitignore` 사전 확인

JupyterLab은 Notebook 자동 복구 과정에서 `.ipynb_checkpoints/` 폴더를 만들 수 있습니다. Git 메뉴의 **Open .gitignore**로 현재 정책을 확인합니다.

권장 패턴:

```gitignore
.ipynb_checkpoints/
**/.ipynb_checkpoints/
```

확인 기준:

- 같은 목적의 규칙이 이미 있으면 중복 추가하지 않습니다.
- Repository의 기존 `.gitignore` 정책을 우선합니다.
- `.ipynb_checkpoints/`가 CHANGES에 보이면 Stage하지 않습니다.
- 이미 추적 중인 파일은 `.gitignore`에 적는 것만으로 자동 제외되지 않으므로 강사에게 알립니다.

이 가이드 작성 작업에서는 Repository의 `.gitignore` 파일을 변경하지 않습니다.

### 3-4. `Simple staging` 확인

이번 수업은 CHANGES와 Staged의 차이를 직접 관찰해야 하므로 Git 메뉴의 **Simple staging**을 끈 상태를 권장합니다.

| 설정 | 동작 | 수업 적합성 |
|---|---|---|
| `Simple staging` Off | 학생이 파일을 직접 Stage하고 Staged 상태를 확인 | 이번 입문 실습에 권장 |
| `Simple staging` On | 변경 파일이 자동으로 Staged될 수 있음 | CHANGES → Stage 개념을 구분하기 어려움 |

## 4. JupyterLab Git UI 지도

### 4-1. Git Sidebar

| UI | 역할 | 학생이 확인할 내용 |
|---|---|---|
| **현재 Branch 이름** | 현재 작업 위치 | 작업 전과 Push 전에 항상 `main` 또는 `branch1`인지 확인 |
| **CHANGES** | 저장 후 아직 Commit하지 않은 변경 | 수정·추가·삭제된 파일과 Stage 여부 확인 |
| **Staged** | 다음 Commit에 들어갈 파일 | 필요한 파일만 들어 있는지 확인 |
| **Commit Message 입력 영역** | Commit 설명 작성 | `Practice 1`처럼 무엇을 한 Commit인지 작성 |
| **HISTORY** | Local Commit 이력 | 방금 만든 Commit과 순서 확인 |
| **BRANCHES AND TAGS** | Local·Remote Branch와 Tag 확인 | `main`, `branch1`, 원격 Branch 상태 확인 |
| **New Branch** | 새 Local Branch 생성 | 최신 `main`에서 `branch1` 생성 |

CHANGES의 파일 행에 표시되는 `+`, Stage 버튼 또는 메뉴 이름은 버전에 따라 다를 수 있습니다. 아이콘 모양보다 “이 파일을 Staged 영역으로 이동하는 동작인가?”를 확인합니다.

### 4-2. Git Menu

| 메뉴 | 용도 | 이번 실습에서의 사용 |
|---|---|---|
| **Merge Branch...** | 선택한 Branch를 현재 Branch에 Merge | `branch1`에서 최신 `main`을 반영할 때 사용 |
| **Push to Remote** | 현재 Local Branch의 Commit을 연결된 Remote Branch로 Push | 정상 Push에 사용 |
| **Push to Remote (Advanced)** | Remote와 대상 Branch를 더 자세히 지정 | 첫 Push에서 선택이 필요할 때만 사용 |
| **Pull from Remote** | 현재 Branch의 Remote 변경을 가져와 반영 | `main`과 필요한 Branch 최신화에 사용 |
| **Pull from Remote (Force)** | Local 상태를 강제로 바꿀 위험이 있는 Pull 방식 | **이번 실습에서 사용 금지** |
| **Reset to Remote** | Local 상태를 Remote 기준으로 되돌림 | **이번 실습에서 사용 금지** |
| **Manage Remote Repositories** | `origin` 등 Remote URL 확인·관리 | 연결 진단이 필요할 때 강사가 사용 |
| **Open Git Repository in Terminal** | 현재 Repository 위치에서 Terminal 열기 | UI 오류 진단용 보조 기능 |
| **Simple staging** | Staging 표시 방식을 단순화 | 이번 수업에서는 Off 권장 |
| **Open .gitignore** | Git 제외 규칙 파일 열기 | `.ipynb_checkpoints/` 규칙 확인 |

> **중요:** `Pull from Remote (Force)`와 `Reset to Remote`는 Local의 미커밋 작업을 잃게 할 수 있습니다. 버튼이 보인다고 시험 삼아 누르지 않습니다.

## 5. Local과 Remote 관계 시각화

```text
┌──────────────────── JupyterLab / Local Repository ────────────────────┐
│                                                                      │
│  Local main       ←─ Pull ──  origin/main                            │
│       │                         ↑                                    │
│       └────────── Push ─────────┘                                    │
│                                                                      │
│  Local branch1    ←─ Pull ──  origin/branch1                         │
│       │                         ↑                                    │
│       └────────── Push ─────────┘                                    │
└──────────────────────────────────────────────────────────────────────┘
                                      │
                                      │ 마지막 Fetch 시점의 원격 정보
                                      ▼
┌────────────────────── GitHub Remote Repository ──────────────────────┐
│                                                                      │
│  GitHub branch1  ── Pull Request ──>  GitHub main                    │
│                   base: main / compare: branch1                      │
│                                                                      │
└──────────────────────────────────────────────────────────────────────┘
```

정확한 Git 용어로 `origin/main`과 `origin/branch1`은 Local Repository가 마지막 Fetch 시점에 기억하는 **remote-tracking Branch**입니다. 학생에게는 다음 두 문장을 먼저 기억하게 합니다.

```text
Push: Local Branch → 같은 이름의 GitHub Branch
PR: GitHub branch1 → GitHub main으로 병합 요청
```

## 6. 실습 1. main Branch 기본 반복

### 실습 목표

`main` 하나만 사용해 다음 흐름을 최소 3회 반복합니다.

```text
Pull → Edit → Stage → Commit → Push → GitHub 확인
```

### STEP 1. Current Branch가 `main`인지 확인

1. 왼쪽 **Git Sidebar**를 엽니다.
2. Sidebar 위쪽 또는 상태 표시줄의 현재 Branch 이름을 확인합니다.
3. 현재 Branch가 `main`이 아니면 Branch 선택 UI에서 `main`으로 전환합니다.

확인 화면:

```text
현재 Branch
main
```

> **강사 확인:** 학생이 파일을 수정하기 전에 현재 Branch를 말하게 합니다.

### STEP 2. Fetch

Git Sidebar 상단의 **Fetch** 동작을 실행합니다. 설치 버전에 따라 Fetch 아이콘, Remote 새로고침 아이콘 또는 Git 메뉴 항목으로 표시될 수 있습니다.

확인할 내용:

- 오류 알림이 없는가?
- `BRANCHES AND TAGS`의 Remote Branch 정보가 갱신되었는가?
- Fetch만으로 현재 Notebook 내용이 자동 변경되지는 않았는가?

### STEP 3. Pull

현재 Branch가 여전히 `main`인지 다시 확인하고 **Pull from Remote**를 실행합니다.

```text
GitHub main
   ↓ Pull from Remote
Local main
```

Pull 결과가 `Already up to date`와 비슷한 의미라면 실패가 아니라 이미 최신이라는 뜻입니다.

### STEP 4. Notebook 열기 또는 만들기

JupyterLab 파일 브라우저에서 `01_git_test.ipynb`를 엽니다. 파일이 없다면 새 Python Notebook을 만들고 해당 이름으로 저장합니다.

첫 Python 셀:

```python
print("Git Practice 1")
```

셀을 실행한 뒤 `Ctrl+S` 또는 **File → Save Notebook**으로 저장합니다.

> **강사 확인:** 셀 실행만 하고 저장하지 않으면 Git이 변경을 감지하지 못할 수 있습니다. Notebook 탭의 미저장 표시가 사라졌는지 확인합니다.

### STEP 5. CHANGES 확인

Git Sidebar의 **CHANGES**에서 `01_git_test.ipynb`를 찾습니다.

학생이 확인할 것:

- 파일 이름이 맞는가?
- `.ipynb_checkpoints/`가 함께 선택되지 않았는가?
- 의도하지 않은 다른 Notebook이나 데이터 파일이 보이지 않는가?

Notebook 파일을 클릭하거나 Diff 기능을 열 수 있다면 변경 내용을 확인합니다. `.ipynb`는 JSON 구조로 저장되므로 코드뿐 아니라 실행 횟수, 출력과 metadata 변경도 보일 수 있습니다.

### STEP 6. Stage

`01_git_test.ipynb` 행의 Stage 동작을 실행합니다.

```text
CHANGES
  01_git_test.ipynb
        ↓ Stage
Staged
  01_git_test.ipynb
```

여러 파일이 보여도 이번 실습에 필요한 파일만 Stage합니다.

### STEP 7. Staged 상태 확인

다음 Commit에 들어갈 파일이 `01_git_test.ipynb` 하나인지 확인합니다.

강사 질문:

> “CHANGES에 보인다는 것과 Staged에 있다는 것은 어떤 차이인가요?”

기대 답변: CHANGES는 Commit하지 않은 변경 전체이고, Staged는 그중 다음 Commit에 넣기로 선택한 변경입니다.

### STEP 8. Commit Message 입력

Commit Message 입력 영역에 다음 메시지를 적습니다.

```text
Practice 1
```

Commit Message는 작업 내용을 찾을 수 있도록 짧고 구체적으로 작성합니다. `수정`, `test`, `aaa`처럼 의미를 알기 어려운 메시지는 피합니다.

### STEP 9. Commit

**Commit** 버튼을 누릅니다.

확인할 내용:

- Staged 영역에서 파일이 사라졌는가?
- 오류 알림이 없는가?
- Push 전이므로 이 Commit은 우선 Local Repository에만 존재한다는 것을 이해하는가?

### STEP 10. HISTORY 확인

Git Sidebar의 **HISTORY**에서 가장 위에 `Practice 1`이 보이는지 확인합니다.

```text
● Practice 1
│
● Initial commit
```

### STEP 11. Push to Remote

Push 전에 현재 Branch가 `main`인지 다시 확인합니다.

1. Git Sidebar 상단 Push 버튼 또는 Git 메뉴의 **Push to Remote**를 실행합니다.
2. 첫 Push에서 Remote 또는 Branch 선택 창이 나오면 `origin`과 `main`을 확인합니다.
3. 로그인이나 인증 창이 나오면 자신의 GitHub 계정으로 승인합니다.

```text
Local main
   ↓ Push to Remote
GitHub main
```

### STEP 12. GitHub main 확인

브라우저에서 GitHub Repository를 새로 고칩니다.

- 선택된 Branch가 `main`인가?
- `01_git_test.ipynb`가 보이는가?
- 최신 Commit Message가 `Practice 1`인가?

### STEP 13. Practice 2와 Practice 3 반복

같은 Notebook에 셀을 하나씩 추가하거나 기존 셀 내용을 변경합니다.

| 반복 | Notebook 예제 | Commit Message |
|---:|---|---|
| 1 | `print("Git Practice 1")` | `Practice 1` |
| 2 | `print("Git Practice 2")` | `Practice 2` |
| 3 | `print("Git Practice 3")` | `Practice 3` |

각 반복 전에 **Fetch → Pull**을 수행하고, 같은 순서로 Edit → Save → CHANGES → Stage → Commit → Push를 진행합니다.

HISTORY 예상 모습:

```text
● Practice 3
│
● Practice 2
│
● Practice 1
│
● Initial commit
```

### 실습 1 암기 공식

```text
Pull
  → Edit
  → Stage
  → Commit
  → Push
  → 반복
```

## 7. 실습 2. `branch1` + Pull Request

이 실습은 `main`을 안정된 기준으로 두고 `branch1`에서 변경을 만든 뒤 GitHub PR로 `main`에 병합합니다.

### STEP 1. Local `main` 선택

Git Sidebar에서 현재 Branch를 확인하고 `main`으로 전환합니다.

```text
현재 Branch
main
```

CHANGES 또는 Staged에 파일이 남아 있으면 Branch 전환부터 하지 말고 저장·Stage·Commit 여부를 먼저 결정합니다.

### STEP 2. Fetch / Pull

1. **Fetch**를 실행합니다.
2. 현재 Branch가 `main`인지 확인합니다.
3. **Pull from Remote**를 실행합니다.

새 Branch는 가능한 한 최신 `main`에서 시작해야 다른 학생이나 GitHub에서 이미 반영된 변경을 포함할 수 있습니다.

```text
GitHub main
   ↓ Fetch / Pull
Local main 최신화
```

### STEP 3. `branch1` 생성

`branch1`이 아직 없다면 다음 UI를 사용합니다.

```text
BRANCHES AND TAGS
  → New Branch
  → Branch name: branch1
  → 시작점: 현재 main
  → Create
```

버전에 따라 새 Branch 생성 후 자동으로 전환되거나 별도로 선택해야 할 수 있습니다.

이미 `branch1`이 있다면 새로 만들지 말고 기존 `branch1`으로 전환합니다. 반복 수업에서 같은 이름을 다시 만들면 “이미 존재한다”는 오류가 발생합니다.

### STEP 4. 현재 Branch가 `branch1`인지 확인

파일을 수정하기 전에 반드시 확인합니다.

```text
현재 Branch
branch1
```

> **강사 확인:** 학생에게 “지금 Commit은 어느 Branch에 생기나요?”라고 질문합니다. 정답은 `branch1`입니다.

### STEP 5. Notebook 수정과 저장

`01_git_test.ipynb`에 새 셀을 추가합니다.

```python
print("Branch Practice 1")
```

셀을 실행한 뒤 Notebook을 저장합니다.

### STEP 6. CHANGES → Stage

1. Git Sidebar의 **CHANGES**에서 `01_git_test.ipynb`를 확인합니다.
2. 의도하지 않은 파일이 없는지 확인합니다.
3. `01_git_test.ipynb`만 Stage합니다.
4. 파일이 **Staged** 영역으로 이동했는지 확인합니다.

### STEP 7. Commit

Commit Message 예:

```text
Branch Practice 1
```

Commit 버튼을 누르고 HISTORY에서 Commit을 확인합니다.

```text
Local branch1
● Branch Practice 1
│
● Practice 3
```

### STEP 8. Push to Remote

Push 직전에 현재 Branch가 `branch1`인지 다시 확인합니다.

1. **Push to Remote**를 실행합니다.
2. 처음 Push하는 `branch1`이면 Remote Branch 생성이나 upstream 연결을 묻는 창이 나올 수 있습니다.
3. Remote는 `origin`, Branch는 `branch1`인지 확인합니다.

```text
Local branch1
   ↓ Push to Remote
GitHub branch1
```

일반 Push에서 대상 선택이 불가능한 경우에만 **Push to Remote (Advanced)**를 열어 `origin`과 `branch1`을 정확히 지정합니다.

### STEP 9. GitHub에서 `branch1` 확인

GitHub Repository의 Branch 선택 메뉴에서 `branch1`을 선택합니다.

- `01_git_test.ipynb`의 변경이 보이는가?
- 최신 Commit이 `Branch Practice 1`인가?
- `main`을 선택했을 때는 아직 이 변경이 없는가?

### STEP 10. Pull Request 생성

Push 직후 GitHub 상단에 노란색 **Compare & pull request** 안내가 보일 수 있습니다. 이 배너는 편의 기능이며 항상 표시되는 것은 아닙니다. 배너가 없다고 Push가 실패한 것은 아닙니다.

PR 생성 경로 A:

```text
Compare & pull request
  → Create pull request
```

PR 생성 경로 B:

```text
GitHub에서 branch1 선택
  → Contribute
  → Open pull request
```

PR 생성 경로 C:

```text
Pull requests
  → New pull request
```

PR 작성 화면에서 반드시 확인합니다.

```text
base: main
compare: branch1
```

방향:

```text
GitHub branch1
   ↓ Pull Request
GitHub main
```

PR 제목 예:

```text
Add branch practice notebook update
```

PR 본문 예:

```markdown
## 변경 내용

- `01_git_test.ipynb`에 Branch Practice 셀을 추가했습니다.

## 확인 방법

- JupyterLab에서 셀 실행 결과를 확인했습니다.
- Git Sidebar에서 변경 파일과 Commit을 확인했습니다.
```

### STEP 11. GitHub에서 Merge

1. **Files changed**에서 의도한 Notebook만 변경됐는지 확인합니다.
2. `base: main`, `compare: branch1`을 다시 확인합니다.
3. 가능하면 이번 반복 실습에서는 **Create a merge commit**을 선택합니다.
4. **Merge pull request → Confirm merge**를 실행합니다.
5. 반복 수업에 같은 `branch1`을 사용할 것이므로 **Delete branch**는 누르지 않습니다.

> **병합 방식 주의:** `Squash and merge` 또는 `Rebase and merge`는 Commit ID와 이력 모양이 달라져 반복 사용하는 `branch1`의 ahead / behind 표시가 예상과 다를 수 있습니다. 이 수업에서는 Branch 관계를 관찰하기 쉬운 `Create a merge commit`을 기준으로 설명합니다.

## 8. 가장 중요한 단계: PR Merge 이후 Local 동기화

GitHub에서 PR을 Merge하면 GitHub의 `main`만 먼저 최신이 됩니다. Local `main`과 Local `branch1`은 자동으로 갱신되지 않습니다.

따라서 PR Merge 직후 첫 동기화 방향은 **GitHub main → Local main**입니다.

병합 직후 상태:

```text
GitHub main       최신 Merge 포함
Local main        아직 Merge 전 상태
Local branch1     작업 Commit은 있지만 GitHub main의 Merge 결과는 아직 미반영
```

다음 순서를 생략하지 않습니다.

### STEP 1. JupyterLab에서 `main` 전환

Git Sidebar의 Branch 선택 UI에서 `main`을 선택합니다.

```text
현재 Branch
main
```

### STEP 2. Local `main`에 Pull

1. Fetch를 실행합니다.
2. **Pull from Remote**를 실행합니다.
3. HISTORY에서 GitHub PR Merge Commit이 내려왔는지 확인합니다.

```text
GitHub main
   ↓ Pull from Remote
Local main
```

### STEP 3. 다시 `branch1` 전환

Branch 선택 UI에서 `branch1`으로 이동합니다.

```text
현재 Branch
branch1
```

### STEP 4. `branch1`에서 `main` Merge

현재 Branch가 `branch1`인 상태에서 실행합니다.

```text
Git
  → Merge Branch...
  → Select the branch to merge in branch1
  → main 선택
  → Merge
```

방향을 그림으로 읽습니다.

```text
최신 Local main
   ↓ Merge Branch...
현재 Local branch1
```

이 UI 동작에 대응하는 Git CLI 개념은 다음과 같습니다. 학생은 명령을 실행하지 않고 의미만 참고합니다.

```powershell
# CLI 개념 참고: 현재 Branch를 branch1으로 선택
git switch branch1

# CLI 개념 참고: main의 Commit을 현재 branch1에 반영
git merge main
```

> **방향 주의:** `Merge Branch...`는 선택한 Branch를 **현재 Branch 안으로** 합칩니다. 현재 Branch가 `branch1`인지 확인한 뒤 목록에서 `main`을 선택해야 `main → branch1` 방향이 됩니다.

`Create a merge commit` 방식으로 PR을 Merge한 정상 흐름에서는 `branch1`이 Local `main`으로 Fast-forward될 수 있습니다. Fast-forward도 성공적인 Merge입니다.

### STEP 5. 최신화한 `branch1` Push

현재 Branch가 `branch1`인지 확인한 뒤 **Push to Remote**를 실행합니다.

```text
Local branch1
   ↓ Push to Remote
GitHub branch1
```

최종적으로 다음 실습 시작점에 가까워집니다.

```text
Local main
≈ Local branch1
≈ GitHub main
≈ GitHub branch1
```

`≈`는 현재 반복 실습에 필요한 Commit 기준이 거의 같다는 뜻입니다. 실제 화면의 ahead / behind 수치는 병합 방식과 새 Commit 유무에 따라 달라질 수 있습니다.

## 9. ahead / behind 읽기

GitHub의 Branch 화면에 다음과 같은 문구가 보일 수 있습니다.

```text
This branch is 1 commit ahead of and 3 commits behind main.
```

| 표시 | 의미 |
|---|---|
| **1 commit ahead of main** | `branch1`에만 있고 `main`에는 아직 없는 Commit이 1개 있습니다. |
| **3 commits behind main** | `main`에는 있지만 `branch1`에는 아직 반영되지 않은 Commit이 3개 있습니다. |

### behind가 계속 증가하는 이유

PR을 계속 `main`에 Merge한 뒤 Local `main`만 Pull하고, 기존 `branch1`에 최신 `main`을 Merge하지 않으면 `branch1`은 새 `main` Commit을 모릅니다.

```text
1 ahead / 1 behind
        ↓ 다음 PR Merge 후 branch1 동기화 생략
1 ahead / 2 behind
        ↓ 다시 생략
1 ahead / 3 behind
```

이것은 Git 오류가 아니라 Branch의 Commit 포함 관계가 달라졌다는 상태 설명입니다.

해결 순서:

1. JupyterLab에서 `main`으로 전환합니다.
2. Fetch 후 **Pull from Remote**를 실행합니다.
3. `branch1`으로 전환합니다.
4. **Git → Merge Branch...**를 엽니다.
5. `main`을 선택합니다.
6. Merge 결과를 확인합니다.
7. 현재 `branch1`을 **Push to Remote**합니다.

> `branch1`에 아직 PR로 보내지 않은 Commit이 있다면 ahead가 0이 되지 않을 수 있습니다. 숫자를 억지로 0으로 만드는 것이 목표가 아니라, 어떤 Commit이 어느 Branch에만 있는지 이해하는 것이 목표입니다.

## 10. 최종 반복 Workflow

### Branch 작업

```text
branch1
   ↓
Edit
   ↓
CHANGES
   ↓
Stage
   ↓
Commit
   ↓
Push to Remote
   ↓
GitHub branch1
   ↓
Pull Request
   ↓
Merge → GitHub main
```

### PR Merge 후 정리

```text
JupyterLab
   ↓
main 전환
   ↓
Fetch / Pull from Remote
   ↓
branch1 전환
   ↓
Git → Merge Branch...
   ↓
main 선택
   ↓
Merge
   ↓
Push to Remote
```

### 다음 실습

```text
branch1
   ↓ Edit
Stage
   ↓ Commit
Push
   ↓ PR
Merge
   ↓ main Pull
branch1에 main Merge
   ↓ Push
다음 작업 반복
```

### 한 줄 암기 공식

```text
branch1 작업 → Push → PR → Merge → main Pull → branch1에서 main Merge → Push → 다음 작업
```

## 11. 실수 방지 경고

> **경고 1 — 현재 Branch부터 확인:** 파일 수정, Commit, Push, Merge 전에 현재 Branch가 `main`인지 `branch1`인지 확인합니다.

> **경고 2 — PR Merge가 Local 동기화는 아님:** GitHub에서 Merge한 뒤 Local `main`으로 전환해 Pull해야 합니다.

> **경고 3 — 기존 branch1도 최신화:** `main` Pull 후 `branch1`으로 돌아와 `Merge Branch... → main`까지 수행합니다.

> **경고 4 — 노란색 배너는 선택 안내:** **Compare & pull request**가 없어도 Push 성공 여부는 GitHub의 `branch1`과 Commit을 직접 확인하면 됩니다.

> **경고 5 — PR 방향 확인:** 항상 `base: main`, `compare: branch1`인지 확인합니다.

> **경고 6 — Push 대상 확인:** Push 전에 현재 Branch가 `branch1`인지 확인합니다. `main`에서 Push하면 branch1 작업을 보내는 것이 아닙니다.

> **경고 7 — 강제 기능 사용 금지:** `Pull from Remote (Force)`, `Reset to Remote`, Force Push는 이번 실습에서 사용하지 않습니다.

## 12. 강사용 진행 포인트

### 실습 시작 전

- 학생이 JupyterLab에서 올바른 Repository를 열었는지 확인합니다.
- Git Sidebar가 정상 표시되는지 확인합니다.
- `origin`이 학생 자신의 GitHub Repository인지 확인합니다.
- CHANGES와 Staged가 비어 있는지 확인합니다.
- `Simple staging`이 Off인지 확인합니다.
- `.gitignore`에서 `.ipynb_checkpoints/` 규칙을 확인합니다.

### 실습 중 반복 질문

| 시점 | 강사 질문 | 기대 답변 |
|---|---|---|
| Edit 전 | 현재 Branch는 무엇인가요? | `main` 또는 `branch1`을 화면에서 확인해 답함 |
| Stage 전 | 어떤 파일만 Commit할 것인가요? | `01_git_test.ipynb` 등 의도한 파일을 지정 |
| Commit 후 | GitHub에도 바로 보이나요? | 아직 Local Commit이므로 Push해야 함 |
| Push 후 | 어느 Remote Branch로 갔나요? | `main` 또는 `branch1` |
| PR 전 | base와 compare는 무엇인가요? | `base: main`, `compare: branch1` |
| PR Merge 후 | 어느 Local Branch를 먼저 최신화하나요? | Local `main` |
| main Pull 후 | 기존 `branch1`은 자동 최신인가요? | 아니므로 `branch1`에서 `main` Merge 필요 |
| ahead/behind 확인 | behind는 오류인가요? | main의 Commit이 아직 branch1에 없다는 상태 |

### 학생 화면에서 반드시 확인할 것

- 현재 Branch 표시
- CHANGES와 Staged의 파일 목록 차이
- HISTORY의 Commit 순서
- Push 후 GitHub에서 선택된 Branch
- PR의 base / compare 방향
- PR Merge 후 Local `main` HISTORY
- `branch1`에서 **Merge Branch... → main** 방향
- Push 후 GitHub `branch1`의 ahead / behind 상태

## 13. 학생용 체크리스트

### 작업 전

- [ ] JupyterLab에서 올바른 Repository를 열었는가?
- [ ] 현재 Branch를 확인했는가?
- [ ] `main`에서 Fetch와 Pull을 했는가?
- [ ] Branch 실습이라면 현재 Branch가 `branch1`인가?
- [ ] CHANGES와 Staged에 이전 작업이 남아 있지 않은가?

### Commit 전

- [ ] Notebook을 저장했는가?
- [ ] CHANGES의 파일을 확인했는가?
- [ ] `.ipynb_checkpoints/`를 Stage하지 않았는가?
- [ ] 필요한 파일만 Stage했는가?
- [ ] Staged 영역을 다시 확인했는가?
- [ ] 작업 내용을 설명하는 Commit Message를 작성했는가?

### Push 전과 Push 후

- [ ] Push 전 현재 Branch가 `branch1`인지 확인했는가?
- [ ] **Push to Remote**가 성공했는가?
- [ ] GitHub에서 `branch1`을 선택했는가?
- [ ] GitHub `branch1`에 최신 Commit이 보이는가?

### Pull Request

- [ ] `base: main`인가?
- [ ] `compare: branch1`인가?
- [ ] Files changed에 의도한 파일만 있는가?
- [ ] PR 제목과 설명을 작성했는가?
- [ ] Merge 결과가 GitHub `main`에 보이는가?

### PR Merge 후

- [ ] JupyterLab에서 `main`으로 전환했는가?
- [ ] Local `main`에서 Fetch와 Pull을 했는가?
- [ ] HISTORY에서 Merge 결과를 확인했는가?
- [ ] `branch1`으로 다시 전환했는가?
- [ ] **Merge Branch...**에서 `main`을 선택했는가?
- [ ] Merge 방향이 `main → branch1`인가?
- [ ] Local `branch1`을 Push했는가?
- [ ] 다음 작업 전 현재 Branch와 CHANGES 상태를 확인했는가?

## 14. 문제 발생 시 안전한 확인 순서

### Push가 안 될 때

1. Notebook을 저장했는지 확인합니다.
2. Staged 파일이 있는지 확인합니다.
3. Commit이 HISTORY에 있는지 확인합니다.
4. 현재 Branch 이름을 확인합니다.
5. **Manage Remote Repositories**에서 `origin`을 확인합니다.
6. GitHub 로그인·접근 권한을 확인합니다.
7. Force Push 대신 오류 메시지를 강사에게 보여 줍니다.

### Pull이 안 될 때

1. 현재 Branch가 `main`인지 `branch1`인지 확인합니다.
2. CHANGES와 Staged에 미커밋 변경이 있는지 확인합니다.
3. 진행 중인 Merge 표시가 있는지 확인합니다.
4. **Pull from Remote (Force)**를 누르지 않습니다.
5. 오류 전체를 보존해 강사에게 보여 줍니다.

### Branch 전환이 안 될 때

미커밋 변경이 다른 Branch 전환과 충돌할 수 있습니다. 먼저 Notebook 저장 여부와 CHANGES·Staged 상태를 확인합니다. 변경을 버리기 위해 `Reset to Remote`를 누르지 않습니다.

### UI가 갱신되지 않을 때

Git Sidebar의 Refresh 동작을 사용하고 잠시 기다립니다. `jupyterlab-git`은 파일 상태를 일정 간격으로 갱신하므로 저장 직후 표시가 약간 늦을 수 있습니다. 계속 문제가 있으면 강사가 **Open Git Repository in Terminal**로 Repository 위치와 상태를 진단합니다.

## 15. 수업 종료 확인

학생이 다음 세 문장을 자기 말로 설명하면 핵심 목표를 달성한 것입니다.

1. “Commit은 Local Repository의 기록이고 GitHub에 보내려면 Push가 필요합니다.”
2. “PR은 GitHub `branch1`의 변경을 GitHub `main`에 Merge하기 위한 검토 요청입니다.”
3. “PR Merge 후에는 Local `main`을 Pull하고, 기존 `branch1`에서 최신 `main`을 Merge한 뒤 Push합니다.”

최종 루틴:

```text
branch1 작업
→ Push
→ PR
→ Merge
→ main Pull
→ branch1에서 main Merge
→ Push
→ 다음 작업
```

## 16. 다음 학습 단계

이 반복 흐름에 익숙해진 뒤 다음 주제를 별도 실습으로 진행합니다.

- 작업마다 새 Branch를 만드는 GitHub Flow
- Merge Conflict 해결
- 여러 학생이 하나의 Repository에서 협업하는 방법
- Rebase와 Cherry-pick의 목적
- GitHub Actions를 이용한 Notebook 검사

기존 강사용 과정과 함께 사용할 때는 [Merge와 Pull Request 실습](./03_Merge와_Pull_Request_실습.md), [브랜치 분기 심화 실습](./04_브랜치_분기_심화_실습.md)을 이어서 참고합니다.
