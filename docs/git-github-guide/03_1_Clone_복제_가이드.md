# 03-1. Clone(복제) 완전 가이드

`git clone`은 GitHub 같은 원격 저장소를 내 컴퓨터에 **처음 한 번 복제**하는 명령입니다. 단순히 파일만 내려받는 것이 아니라 커밋 이력, 브랜치 정보, 원격 저장소 연결까지 함께 준비합니다.

## 1. clone 한 문장 정의

```text
GitHub 원격 저장소
  └─ git clone
       ├─ 프로젝트 파일
       ├─ 커밋 이력
       ├─ 로컬 기본 브랜치
       └─ origin 원격 연결
```

clone이 끝난 폴더는 즉시 Git 저장소입니다. 다시 `git init`하거나 `git remote add origin`을 할 필요가 없습니다.

## 2. clone, ZIP, fork, pull의 차이

| 기능 | 어디로 가져오는가 | 이력 포함 | 원격 연결 | 언제 쓰는가 |
|---|---|---:|---:|---|
| `git clone` | GitHub → 내 컴퓨터 | O | O | 저장소를 내 PC에 처음 받을 때 |
| Download ZIP | GitHub → 내 컴퓨터 | X | X | 소스의 현재 모습만 잠깐 볼 때 |
| Fork | 다른 사람의 GitHub → 내 GitHub 계정 | O | GitHub 사이 관계 | 원본 권한 없이 독립 작업·기여할 때 |
| `git pull` | 원격 변경 → 이미 존재하는 로컬 저장소 | 새 이력만 | 기존 연결 사용 | clone 이후 최신 상태로 갱신할 때 |

가장 흔한 오해는 “변경될 때마다 다시 clone한다”입니다. **처음에는 clone, 그다음부터는 pull**이라고 기억하세요.

## 3. 기본 clone 실습

### 3-1. GitHub에서 주소 복사

1. 복제할 GitHub 저장소를 엽니다.
2. 초록색 **Code** 버튼을 누릅니다.
3. **Local → HTTPS**를 선택합니다.
4. 복사 버튼으로 URL을 복사합니다.

주소는 보통 다음 형태입니다.

```text
https://github.com/사용자명/저장소명.git
```

### 3-2. 저장할 상위 폴더로 이동

저장소 폴더가 생성될 **상위 위치**로 이동합니다. 이미 Git으로 관리되는 프로젝트 안에 무심코 clone하지 않도록 현재 위치를 확인합니다.

```powershell
$cloneRoot = Join-Path ([Environment]::GetFolderPath('MyDocuments')) 'github-projects'
New-Item -ItemType Directory -Path $cloneRoot -Force
Set-Location $cloneRoot
Get-Location
```

현재 위치가 다른 Git 저장소 안인지 확인합니다.

```powershell
git rev-parse --show-toplevel
```

`not a git repository`가 나오면 지금 폴더 자체는 Git 저장소가 아니라는 뜻이며, 여러 저장소를 나란히 보관하는 상위 작업 공간으로 사용하기 좋습니다.

### 3-3. 복제 실행

아래 URL을 실제 저장소의 HTTPS 주소로 바꿉니다.

```powershell
$repositoryUrl = 'https://github.com/사용자명/hello-git.git'
git clone $repositoryUrl
```

Git은 보통 URL의 저장소 이름과 같은 새 폴더를 만듭니다.

```powershell
Set-Location 'hello-git'
git status
git remote -v
git branch -vv
git log --oneline --decorate -5
```

성공 기준:

- `git status`가 현재 브랜치를 표시합니다.
- `git remote -v`에 `origin`과 복사한 URL이 보입니다.
- `git branch -vv`에 로컬 브랜치와 `origin/...` 추적 관계가 보입니다.
- `git log`에 GitHub의 커밋 이력이 보입니다.

## 4. 원하는 로컬 폴더명으로 clone

URL 뒤에 폴더명을 지정할 수 있습니다.

```powershell
Set-Location $cloneRoot
git clone $repositoryUrl 'hello-git-practice'
Set-Location 'hello-git-practice'
```

이 명령은 GitHub 저장소 이름을 바꾸지 않습니다. 내 컴퓨터의 폴더명만 `hello-git-practice`로 만듭니다.

대상 폴더가 이미 존재하고 비어 있지 않으면 clone은 보통 중단됩니다. 오류를 피하려고 기존 폴더를 강제로 지우지 말고, 다른 이름을 지정하거나 폴더 내용을 먼저 확인하세요.

## 5. 특정 브랜치로 clone

기본 브랜치가 아닌 `develop`부터 열고 싶다면 다음처럼 실행합니다.

```powershell
Set-Location $cloneRoot
git clone --branch develop $repositoryUrl 'hello-git-develop'
Set-Location 'hello-git-develop'
git branch -vv
```

이 명령도 기본적으로 저장소의 이력과 원격 브랜치 정보를 가져옵니다. 특정 브랜치 하나만 최소한으로 받으려는 고급 목적이 아니라면 `--single-branch`는 붙이지 않아도 됩니다.

## 6. Private 저장소 clone

Private 저장소는 다음 두 조건이 모두 필요합니다.

1. 로그인한 GitHub 계정에 저장소 읽기 권한이 있어야 합니다.
2. 내 PC의 Git이 그 계정으로 인증되어야 합니다.

HTTPS URL로 처음 clone할 때 브라우저 인증 창이 열리면 로그인하고 접근을 승인합니다. GitHub 계정 비밀번호를 PowerShell의 password 입력란에 직접 넣는 방식은 사용하지 않습니다.

저장소가 보이지 않거나 `Repository not found`가 나오면 다음을 확인합니다.

- URL의 사용자명·조직명·저장소명이 정확한가?
- 브라우저가 다른 GitHub 계정으로 로그인되어 있지 않은가?
- 조직의 SSO 승인이나 저장소 권한이 필요한가?
- submodule이 있다면 **모든 자식 저장소**에도 접근 권한이 있는가?

## 7. submodule이 포함된 저장소 clone

일반 `git clone`은 부모 저장소를 복제하지만, submodule 작업 폴더가 아직 비어 있거나 지정 커밋이 준비되지 않을 수 있습니다. 처음부터 모두 준비하려면 다음 명령을 사용합니다.

```powershell
$parentUrl = 'https://github.com/사용자명/부모-저장소.git'
git clone --recurse-submodules $parentUrl
```

이미 일반 clone을 했다면 저장소 폴더 안에서 초기화합니다.

```powershell
git submodule update --init --recursive
git submodule status --recursive
```

`--recursive`는 submodule 안에 또 다른 submodule이 있는 경우까지 처리합니다. 자세한 내용은 [저장소 구조와 Submodule 심화 가이드](./08_저장소_구조와_Submodule_심화.md)를 참고하세요.

## 8. clone 이후 일상 작업

복제 직후 바로 파일을 수정하기 전에 현재 브랜치와 상태를 확인합니다.

```powershell
git status
git branch -vv
git pull --ff-only
```

팀 작업이라면 최신 기본 브랜치에서 작업 브랜치를 만듭니다.

```powershell
git switch main
git pull --ff-only
git switch -c feature/my-work
```

수정 후의 흐름은 기존과 같습니다.

```powershell
git status
git diff
git add README.md
git diff --staged
git commit -m "Update project README"
git push -u origin feature/my-work
```

## 9. Fork한 저장소 clone과 upstream 연결

다른 사람의 저장소를 fork했다면 일반적으로 두 원격을 구분합니다.

```text
origin   = 내 GitHub 계정의 fork
upstream = 원본 작성자의 GitHub 저장소
```

내 fork를 clone한 뒤 원본을 `upstream`으로 추가합니다.

```powershell
$forkUrl = 'https://github.com/내-사용자명/project.git'
$upstreamUrl = 'https://github.com/원본-사용자명/project.git'

git clone $forkUrl
Set-Location 'project'
git remote add upstream $upstreamUrl
git remote -v
```

원본의 최신 정보를 확인할 때는 다음처럼 fetch합니다.

```powershell
git fetch upstream
git log --oneline --graph --decorate --all -10
```

원본 변경을 내 `main`에 어떤 방식으로 반영할지는 프로젝트의 merge/rebase 정책을 따릅니다.

## 10. 대용량 저장소의 선택 사항

최근 한 커밋의 파일만 필요한 일회성 검사라면 shallow clone을 사용할 수 있습니다.

```powershell
git clone --depth 1 $repositoryUrl 'hello-git-shallow'
```

하지만 과거 이력이 제한되어 `log`, 과거 버전 비교, 일부 merge 작업에 제약이 생깁니다. 학습용이나 정상 개발 환경에서는 일반 clone을 먼저 권장합니다.

## 11. clone 뒤 확인해야 하는 파일

```powershell
Get-ChildItem -Force
```

| 항목 | 뜻 |
|---|---|
| `.git` | 이 복제본의 Git 이력·설정 데이터 |
| `.gitignore` | 추적하지 않을 파일 패턴 |
| `.gitmodules` | submodule이 있을 때 경로와 URL 기록 |
| `README.md` | 저장소 목적과 실행 방법 |
| `LICENSE` | 사용·배포 조건 |
| `CONTRIBUTING.md` | 기여 절차와 팀 규칙 |

`.git`은 숨김 항목이며 직접 편집하거나 다른 저장소의 `.git`으로 덮어쓰지 않습니다.

## 12. 자주 만나는 clone 오류

### 대상 폴더가 이미 존재함

```text
fatal: destination path '...' already exists and is not an empty directory.
```

다른 폴더명을 지정하거나 기존 폴더가 정말 불필요한지 먼저 확인합니다. 삭제 명령으로 성급하게 해결하지 않습니다.

### 저장소를 찾을 수 없음

```text
remote: Repository not found.
```

URL 오타, 저장소 삭제·이름 변경, Private 저장소 권한, 로그인 계정을 확인합니다.

### submodule clone 실패

부모 저장소에는 접근할 수 있어도 Private submodule 권한이 없으면 전체 재귀 clone이 실패할 수 있습니다. `.gitmodules`의 각 URL과 계정 권한을 확인한 뒤 실행합니다.

```powershell
Get-Content .gitmodules
git submodule status --recursive
git submodule update --init --recursive
```

### clone은 됐는데 최신 내용이 아닌 것 같음

현재 브랜치와 원격 브랜치를 확인합니다.

```powershell
git status
git branch --all
git remote -v
git fetch --all --prune
```

원하는 브랜치가 원격에만 있다면 이름을 확인하고 전환합니다.

```powershell
git switch develop
```

## 13. 완료 점검

- [ ] clone과 ZIP 다운로드의 차이를 설명할 수 있다.
- [ ] 처음에는 clone, 이후에는 pull을 사용한다는 것을 안다.
- [ ] clone 뒤 `origin`이 자동 등록되는 것을 확인했다.
- [ ] Private 저장소는 계정 권한과 인증이 모두 필요함을 안다.
- [ ] submodule 저장소는 `--recurse-submodules`로 복제할 수 있다.
- [ ] fork의 `origin`과 원본의 `upstream`을 구분할 수 있다.
- [ ] 기존 Git 저장소 안에 다른 저장소를 무심코 clone하지 않는다.

공식 참고: [Git clone 명령](https://git-scm.com/docs/git-clone.html) · [GitHub Desktop으로 clone과 fork](https://docs.github.com/en/desktop/adding-and-cloning-repositories/cloning-and-forking-repositories-from-github-desktop)

이전: [로컬에서 GitHub까지 첫 실습](./03_로컬에서_GitHub까지_첫_실습.md) · 다음: [브랜치와 병합 실습](./04_브랜치와_병합_실습.md)
