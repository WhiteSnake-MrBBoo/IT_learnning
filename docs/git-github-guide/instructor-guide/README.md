# 강사용 Git & GitHub 단계별 실습 가이드

이 문서는 Windows PowerShell과 GitHub 웹 화면을 함께 사용해 초보자 수업을 진행하는 강사를 위한 운영 안내서입니다. 학생용 개념 설명은 상위 폴더의 [Git & GitHub 초보자 가이드북](../README.md)을 사용하고, 이 폴더의 문서는 **강의 순서·시연 포인트·질문·오류 대응**에 집중합니다.

## 1. 전체 수업 구성

| 차시 | 권장 시간 | 핵심 결과 |
|---:|---:|---|
| [1차시: Commit·Push·Pull·Clone](./01_Commit_Push_Pull_Clone_실습.md) | 70~90분 | 로컬 변경이 어떤 단계를 거쳐 GitHub로 이동하고 다시 내려오는지 설명한다. |
| [2차시: Branch 생성과 전환](./02_Branch_생성과_전환_실습.md) | 60~75분 | 브랜치마다 파일 상태가 달라지고 브랜치는 폴더 복사가 아님을 확인한다. |
| [3차시: Merge와 Pull Request](./03_Merge와_Pull_Request_실습.md) | 80~100분 | 로컬 merge와 GitHub PR의 차이, 병합 후 pull의 필요성을 익힌다. |
| [4차시: 브랜치 분기 심화](./04_브랜치_분기_심화_실습.md) | 80~100분 | 형제·연쇄·역할 기반 브랜치 구조와 로컬/원격 브랜치를 구분한다. |
| [5차시: Submodule](./05_Submodule_실습.md) | 90~120분 | 부모 저장소가 자식 저장소의 특정 커밋을 가리킨다는 원리를 실습한다. |

한 번에 모두 진행하기보다 1~3차시로 기본 흐름을 완성한 뒤 4~5차시를 심화 수업으로 분리하는 것을 권장합니다.

## 2. 강의 전 준비

### 강사 PC

- Windows PowerShell 5.1 또는 PowerShell 7
- Git for Windows
- VS Code
- 이메일 인증과 2FA를 마친 GitHub 계정
- 브라우저 로그인 상태
- 화면 한쪽에는 VS Code, 다른 쪽에는 GitHub 웹 페이지

설치 확인:

```powershell
# Git이 설치되어 있고 PowerShell에서 인식되는지 확인
git --version

# 강사 계정의 커밋 작성자 정보 확인
git config --global --get user.name
git config --global --get user.email
```

### 학생 준비

학생마다 **자신의 GitHub 계정과 자신의 연습 저장소**를 사용하게 합니다. 강사의 비밀번호, 토큰 또는 저장소 쓰기 권한을 공유하지 않습니다. 계정 생성과 2FA는 [설치와 GitHub 가입](../02_설치와_GitHub_가입.md)을 수업 전에 완료하는 것이 좋습니다.

### 공통 연습 위치

기존 프로젝트나 수업 자료 저장소 안에서 `git init`을 실행하지 않도록 별도 실습 폴더를 사용합니다.

```powershell
# 사용자의 문서 폴더 아래에 Git 수업 전용 공간 생성
$classRoot = Join-Path ([Environment]::GetFolderPath('MyDocuments')) 'git-class-practice'
New-Item -ItemType Directory -Path $classRoot -Force
Set-Location $classRoot
Get-Location
```

OneDrive가 문서 폴더를 관리하는 PC에서는 실제 경로에 `OneDrive`가 포함될 수 있습니다. `Get-Location` 결과가 의도한 실습 폴더이면 정상입니다.

## 3. 수업 운영 공식

각 명령을 빠르게 복사하게 하기보다 다음 다섯 단계를 반복합니다.

```text
설명 → 결과 예측 → 한 줄 실행 → 화면 확인 → 학생이 자기 말로 설명
```

예:

1. “지금 변경은 Working Tree에만 있습니다.”
2. “`git add` 후 `git status`에서 어느 영역으로 이동할까요?”
3. 학생이 직접 `git add README.md`를 실행합니다.
4. `Changes to be committed`를 확인합니다.
5. 학생이 “다음 커밋 후보로 선택됐다”고 설명합니다.

## 4. 모든 차시에서 반복할 안전 습관

```powershell
# 현재 PowerShell 위치 확인
Get-Location

# 현재 저장소의 최상위 폴더 확인
git rev-parse --show-toplevel

# 현재 브랜치와 파일 상태 확인
git status
git branch --show-current

# 커밋 전 실제 변경 확인
git diff
git diff --staged

# 브랜치와 커밋 관계를 그림처럼 확인
git log --oneline --graph --decorate --all -15
```

강사는 학생이 오류를 말하면 해결 명령부터 주지 말고 먼저 `Get-Location → git status → git branch --show-current → git remote -v` 결과를 읽게 합니다.

## 5. 초보 수업에서 기본적으로 금지할 명령

다음 명령은 의미와 복구 방법을 배우기 전에는 실행하지 않습니다.

```text
git push --force       # 공유된 원격 이력을 덮어쓸 수 있음
git reset --hard       # 커밋하지 않은 로컬 변경을 잃을 수 있음
git clean -fd          # 추적되지 않은 파일·폴더를 삭제할 수 있음
git branch -D          # 병합되지 않은 브랜치를 강제로 삭제
```

로컬과 GitHub에 서로 다른 첫 커밋이 생겼다고 해서 `git push --force`로 덮어쓰지 않습니다. 초보 실습은 GitHub에 **빈 저장소**를 만들거나, 보존해야 할 원격 저장소를 먼저 clone한 뒤 로컬 파일을 옮기는 방식으로 시작합니다.

또한 기본 수업에서는 `git add .`보다 다음처럼 의도한 파일을 명시합니다.

```powershell
# README.md 하나만 다음 커밋 대상으로 선택
git add README.md
```

`git add .`은 비밀 파일, 대용량 데이터, 가상환경과 임시 파일까지 함께 stage할 수 있으므로 `.gitignore`와 상태 확인을 익힌 뒤 사용합니다.

## 6. 강의 중 자주 나오는 질문

| 학생 질문 | 강사용 핵심 답변 |
|---|---|
| 저장했는데 왜 GitHub에 없나요? | 편집기 저장은 Working Tree만 바꿉니다. `add → commit → push`가 추가로 필요합니다. |
| commit이 승인인가요? | commit은 로컬 스냅샷입니다. 팀의 승인은 보통 PR 리뷰와 병합 규칙에서 이뤄집니다. |
| branch는 복사 폴더인가요? | 커밋을 가리키는 가벼운 이름표입니다. `switch`하면 같은 작업 폴더가 해당 커밋 상태로 바뀝니다. |
| pull과 Pull Request가 같은가요? | `git pull`은 원격 변경 동기화 명령이고 PR은 GitHub의 검토·병합 요청입니다. |
| merge하면 원격도 자동 변경되나요? | 로컬 merge는 로컬 기록만 바꿉니다. 원격 반영에는 push가 필요합니다. GitHub에서 PR을 merge했다면 로컬에는 pull이 필요합니다. |
| submodule은 일반 폴더인가요? | 폴더처럼 보이지만 독립 Git 저장소이며, 부모는 자식 파일 전체가 아니라 특정 자식 커밋 ID를 기록합니다. |

## 7. 평가 방법

### 과정 평가

- 명령 전에 현재 위치와 브랜치를 확인하는가?
- `git status`의 Untracked, Modified, Staged를 말로 설명하는가?
- 커밋 전에 `git diff --staged`를 확인하는가?
- base/compare 브랜치를 확인하고 PR을 만드는가?
- 오류가 나면 강제 명령 대신 상태를 먼저 읽는가?

### 종료 질문

학생이 다음 흐름을 그림 없이 설명하면 기본 목표를 달성한 것입니다.

```text
파일 수정
  → add
  → commit
  → 작업 브랜치 push
  → Pull Request
  → main merge
  → 로컬 main pull
```

## 8. 공식 참고 자료

- [Git 명령어 공식 문서](https://git-scm.com/docs)
- [Pro Git 무료 전자책](https://git-scm.com/book/ko/v2)
- [Git 브랜치 전환](https://git-scm.com/docs/git-switch)
- [Git submodule 명령](https://git-scm.com/docs/git-submodule)
- [GitHub의 Git 기본 안내](https://docs.github.com/en/get-started/git-basics)
- [GitHub Pull Request 안내](https://docs.github.com/en/pull-requests)

학생용 처음으로: [Git & GitHub 초보자 가이드북](../README.md)
