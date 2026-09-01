# 1차시. Commit·Push·Pull·Clone 실습

## 수업 개요

- 권장 시간: 70~90분
- 선수 학습: Git 설치, GitHub 가입·이메일 인증·2FA
- 준비물: GitHub의 빈 `git-class-demo` 저장소, PowerShell, VS Code, 브라우저
- 완료 결과: 로컬에서 만든 커밋을 GitHub에 push하고, GitHub 변경을 pull하며, 새 폴더에 clone합니다.

## 학습 목표

학생이 다음 차이를 설명하도록 합니다.

| 용어 | 수업 종료 시 설명 |
|---|---|
| Save | 편집기에서 실제 파일 내용을 저장 |
| Add | 다음 커밋에 포함할 변경을 선택 |
| Commit | 선택한 변경을 로컬 Git 이력에 기록 |
| Push | 로컬 커밋을 GitHub에 전송 |
| Pull | 원격 변경을 가져와 현재 브랜치에 반영 |
| Clone | 원격 저장소의 파일·이력·원격 연결을 새 로컬 폴더에 복제 |

## 0. 강의 전 GitHub 준비

GitHub에서 다음 조건으로 저장소를 만듭니다.

```text
Repository name: git-class-demo
Visibility: Private 또는 Public
Template: No template
Add README: Off
Add .gitignore: No .gitignore
Add license: No license
```

이번 수업은 로컬에서 첫 커밋을 만들기 때문에 GitHub 저장소는 **비어 있어야** 흐름이 단순합니다. 각 학생은 자기 저장소의 **Code → HTTPS** 주소를 복사합니다.

강사 질문:

> “GitHub에서 README를 켜면 무엇이 생길까요?”

기대 답변: GitHub 쪽에 첫 커밋이 생기며, 로컬의 별도 첫 커밋과 이력이 갈라질 수 있습니다.

## 1. 실습 폴더 만들기

```powershell
# 문서 폴더 아래에 수업 전용 루트 준비
$classRoot = Join-Path ([Environment]::GetFolderPath('MyDocuments')) 'git-class-practice'
New-Item -ItemType Directory -Path $classRoot -Force
Set-Location $classRoot

# 이 차시의 프로젝트 폴더 생성 및 이동
New-Item -ItemType Directory -Path 'git-class-demo'
Set-Location 'git-class-demo'
Get-Location
```

기존 폴더가 있다는 오류가 나면 다른 이름을 사용하거나 이전 실습 폴더의 내용을 먼저 확인합니다. 수업 자료가 있는 폴더를 무작정 삭제하지 않습니다.

## 2. 일반 폴더를 Git 저장소로 만들기

```powershell
# 현재 폴더에 Git 저장소를 만들고 기본 브랜치를 main으로 지정
git init -b main

# 현재 브랜치와 파일 상태 확인
git status
git branch --show-current
```

예상 관찰:

- 현재 브랜치는 `main`입니다.
- 아직 커밋이 없습니다.
- 숨김 영역에 `.git`이 생겼지만 직접 수정하지 않습니다.

강사 멘트:

> “`git init`은 GitHub 저장소를 만든 것이 아닙니다. 내 컴퓨터의 이 폴더에 로컬 Git 기록 장치를 설치한 것입니다.”

## 3. 첫 파일 작성과 상태 변화 관찰

```powershell
# PowerShell에서 UTF-8 Markdown 파일 생성
@'
# Git Class Demo

Git의 add, commit, push, pull, clone을 연습합니다.
'@ | Set-Content -Encoding utf8 README.md

# 파일 내용과 Git 상태 확인
Get-Content README.md
git status
git diff
```

첫 파일은 아직 **Untracked**이므로 `git diff`에 내용이 보이지 않을 수 있습니다. `git status`의 `Untracked files`가 핵심 확인 지점입니다.

## 4. Add와 Commit

```powershell
# README.md만 다음 커밋 대상으로 선택
git add README.md

# Changes to be committed 영역 확인
git status

# 실제로 커밋될 내용 확인
git diff --staged

# 로컬 저장소에 첫 스냅샷 기록
git commit -m "Add class README"

# 작업 폴더와 커밋 이력 확인
git status
git log --oneline --decorate -3
```

예상 결과:

- `git status`에 `working tree clean`이 표시됩니다.
- `git log`에 `Add class README`가 표시됩니다.
- 아직 GitHub 웹에는 파일이 없습니다.

강사 질문:

> “커밋했는데 GitHub에 파일이 없는 이유는 무엇인가요?”

기대 답변: commit은 로컬 기록이고 아직 push하지 않았기 때문입니다.

## 5. GitHub 원격 저장소 연결

학생이 복사한 주소로 자리표시자를 바꿉니다.

```powershell
# 반드시 자신의 GitHub 사용자명과 저장소 주소로 변경
$repoUrl = 'https://github.com/내-사용자명/git-class-demo.git'

# origin이라는 별칭으로 원격 주소 등록
git remote add origin $repoUrl

# fetch/push 주소 확인
git remote -v
```

`origin`은 GitHub 자체를 뜻하는 예약어가 아니라 첫 원격 저장소에 흔히 사용하는 별칭입니다.

이미 `origin`이 있다는 오류가 나면 먼저 주소를 확인합니다.

```powershell
# 기존 origin 확인
git remote -v

# 주소가 잘못된 경우에만 올바른 주소로 교체
git remote set-url origin $repoUrl
```

## 6. 첫 Push

```powershell
# 로컬 main 커밋을 origin/main으로 보내고 추적 관계 설정
git push -u origin main

# 로컬 main이 origin/main을 추적하는지 확인
git branch -vv
git status
```

브라우저 로그인 창이 열리면 GitHub 계정으로 승인합니다. GitHub 계정 비밀번호를 PowerShell의 password 입력란에 직접 넣는 방식은 사용하지 않습니다.

GitHub 웹 확인:

- `README.md`가 보이는가?
- `Add class README` 커밋이 보이는가?
- 선택된 브랜치가 `main`인가?

> **안전 경고:** push가 거절되어도 `git push --force`를 사용하지 않습니다. 원격에 로컬에 없는 커밋이 있다는 뜻일 수 있으므로 `git fetch origin`과 `git log --oneline --graph --decorate --all`로 상태부터 확인합니다.

## 7. 두 번째 로컬 변경과 Push

```powershell
# 기존 README 끝에 학습 기록 추가
Add-Content -Encoding utf8 README.md "`n## 학습 기록`n`n첫 push를 완료했습니다."

# Working Tree 변경 확인
git status
git diff

# 의도한 파일만 stage하고 커밋
git add README.md
git diff --staged
git commit -m "Record first push"

# upstream이 이미 있으므로 짧은 push 가능
git push
```

학생에게 “파일 저장만 한 상태”, “commit까지 한 상태”, “push까지 한 상태”를 각각 말로 구분하게 합니다.

## 8. GitHub 변경을 Pull

브라우저에서 다음을 진행합니다.

1. GitHub 저장소의 `README.md`를 엽니다.
2. 편집 버튼을 누릅니다.
3. `GitHub 웹에서 추가한 문장입니다.`를 마지막에 적습니다.
4. 커밋 메시지를 `Edit README on GitHub`로 입력하고 `main`에 커밋합니다.

로컬 PowerShell에서 확인합니다.

```powershell
# pull 전에 로컬 작업 폴더가 깨끗한지 확인
git status

# 단순 fast-forward가 가능할 때만 원격 변경 반영
git pull --ff-only

# GitHub에서 작성한 문장이 내려왔는지 확인
Get-Content README.md
git log --oneline --decorate -5
```

강사 멘트:

> “웹에서 merge 또는 commit했다고 내 PC 파일이 자동으로 바뀌지는 않습니다. 로컬은 pull해야 최신 원격 상태를 반영합니다.”

## 9. Clone으로 새 복제본 만들기

현재 저장소 밖으로 이동해 별도 이름으로 clone합니다.

```powershell
# 실습 루트로 이동
Set-Location $classRoot

# 원격 저장소를 새로운 로컬 폴더에 복제
git clone $repoUrl 'git-class-demo-copy'
Set-Location 'git-class-demo-copy'

# 파일뿐 아니라 커밋 이력과 origin 연결까지 확인
git status
git remote -v
git log --oneline --decorate -5
Get-Content README.md
```

### Init과 Clone 비교

| 명령 | 시작 상황 | 결과 |
|---|---|---|
| `git init` | 내 PC의 일반 폴더에서 새 프로젝트 시작 | 로컬 `.git` 생성, 원격은 별도 연결 필요 |
| `git clone` | 이미 존재하는 원격 저장소로 작업 시작 | 파일·이력 복제, `origin`과 기본 추적 브랜치 생성 |

## 10. 학생 확인 과제

학생이 명령어를 보지 않고 다음 질문에 답하게 합니다.

1. 수정한 파일이 push되지 않는 가장 흔한 이유는 무엇인가?
2. commit 전 내용을 확인하는 명령은 무엇인가?
3. 처음 push할 때 `-u`는 무엇을 연결하는가?
4. clone과 ZIP 다운로드의 차이는 무엇인가?
5. GitHub 웹에서 수정한 뒤 로컬에서 무엇을 해야 하는가?

## 11. 수업 종료 상태

다음 차시는 원본 폴더에서 진행합니다.

```powershell
# 원본 프로젝트로 복귀
Set-Location (Join-Path $classRoot 'git-class-demo')

# 깨끗한 main인지 확인
git switch main
git status
git branch -vv
```

이전: [강사용 안내서](./README.md) · 다음: [Branch 생성과 전환 실습](./02_Branch_생성과_전환_실습.md)
