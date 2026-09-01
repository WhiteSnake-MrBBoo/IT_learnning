# 01. Git 핵심 개념과 GitHub 용어사전

## 1. Git과 GitHub는 다릅니다

| 구분 | Git | GitHub |
|---|---|---|
| 정체 | 파일 변경 이력을 관리하는 **버전 관리 프로그램** | Git 저장소를 인터넷에서 보관하고 협업하는 **웹 서비스** |
| 주로 동작하는 곳 | 내 컴퓨터 | 인터넷의 GitHub 서버 |
| 인터넷 필요 여부 | 커밋, 브랜치, 로컬 병합은 불필요 | push, pull, Pull Request 등은 필요 |
| 대표 기능 | add, commit, branch, merge, log | 원격 저장소, Pull Request, Issue, Actions, 리뷰 |

비유하면 Git은 내 컴퓨터의 “시간 기록 장치”이고, GitHub는 그 기록을 공유하고 검토하는 “온라인 협업 공간”입니다. Git은 GitHub 없이도 사용할 수 있고, GitHub는 Git 저장소를 중심으로 여러 협업 기능을 제공합니다.

## 2. 변경이 이동하는 네 공간

Git을 이해하려면 파일이 어느 공간에 있는지를 먼저 봐야 합니다.

| 공간 | 쉬운 뜻 | 확인·이동 명령 |
|---|---|---|
| Working Tree | 지금 직접 편집하는 실제 파일 | `git status`, `git diff` |
| Staging Area | 다음 커밋에 넣기로 선택한 변경 | `git add`, `git diff --staged` |
| Local Repository | 내 컴퓨터에 저장된 커밋 기록 | `git commit`, `git log` |
| Remote Repository | GitHub 등에 있는 공유 커밋 기록 | `git push`, `git fetch`, `git pull` |

```text
파일 편집 ──add──> 스테이징 ──commit──> 로컬 기록 ──push──> GitHub
GitHub ──fetch/pull──> 로컬 기록과 작업 브랜치
```

### Git 기본 개념 한눈에 보기

![Git의 init, commit, branch, merge, push, fetch, pull 흐름을 한눈에 정리한 그림](./assets/git-core-concepts-overview.png)

그림을 볼 때는 다음 순서로 읽습니다.

1. `init`으로 일반 폴더를 Git 저장소로 시작합니다.
2. `add → commit`으로 선택한 변경을 로컬 저장소에 기록합니다.
3. `branch`로 기존 커밋에서 별도의 작업 흐름을 만듭니다.
4. `merge`로 다른 브랜치의 커밋 이력을 현재 브랜치에 합칩니다.
5. `push`로 로컬 커밋을 원격 저장소에 보내고, `fetch` 또는 `pull`로 원격 변경을 가져옵니다.

> 이 그림은 전체 관계를 빠르게 기억하기 위한 학습용 요약입니다. 실제 파일이 어느 단계에 있는지는 `git status`, 브랜치 흐름은 `git log --oneline --graph --decorate --all`, 로컬·원격 차이는 `git fetch` 후 로그로 확인하세요.

## 3. 꼭 알아야 할 Git 용어

### Commit(커밋): 맡기다·확정하다 : 설명이 붙은 로컬 스냅샷

- Git 의미: 스테이징한 변경을 하나의 이력으로 로컬 저장소에 기록합니다.
- 쉬운 비유: 게임의 세이브 포인트
- 핵심 명령: `git commit -m "Add login validation"`

커밋은 “팀이 승인했다”는 뜻이 아닙니다. 내 컴퓨터에서 기록을 확정한 것이며, 팀 승인은 보통 Pull Request 리뷰와 병합 규칙으로 관리합니다. 커밋하기 전에는 `git diff --staged`로 저장될 내용을 확인하세요.

### Push(푸시): 밀다 : 로컬 커밋을 원격으로 보내기

- Git 의미: 내 로컬 저장소에만 있던 커밋을 GitHub 같은 원격 저장소에 전송합니다.
- 핵심 명령: `git push origin main`

저장하지 않은 파일이나 아직 커밋하지 않은 변경은 push되지 않습니다. **파일 저장 → add → commit → push** 순서입니다.

### Pull(풀): 당기다 : 원격 변경을 가져와 현재 브랜치에 반영하기

- Git 의미: 보통 `fetch`로 원격 커밋을 받은 뒤 현재 브랜치에 `merge` 또는 `rebase`합니다.
- 핵심 명령: `git pull --ff-only`

`git pull`과 GitHub의 **Pull Request**는 전혀 다릅니다. `pull`은 동기화 명령이고, Pull Request는 변경 검토와 병합을 요청하는 GitHub 기능입니다.

### Branch(브랜치): 가지 : 독립적인 작업 흐름을 가리키는 가지

- Git 의미: 특정 커밋을 가리키는 이동 가능한 이름표입니다.
- 쉬운 비유: 원본을 망가뜨리지 않고 시험하는 별도 작업선
- 생성과 이동: `git switch -c feature/login`

브랜치는 프로젝트 전체를 무겁게 복사하는 폴더가 아닙니다. 커밋을 가리키는 가벼운 포인터에 가깝습니다.

### Merge(머지): 병합 : 두 작업 이력을 합치기

- Git 의미: 다른 브랜치의 커밋 이력을 현재 브랜치에 통합합니다.
- 핵심 명령: `git merge feature/login`

“merge에는 insert와 update 두 종류가 있다”는 설명은 데이터베이스 작업과 혼동하기 쉽습니다. Git merge 결과에는 파일 **추가(insert처럼 보임), 수정(update처럼 보임), 삭제**가 모두 포함될 수 있지만, 이것들이 merge의 종류는 아닙니다.

Git에서 초보자가 구분할 병합 방식은 다음과 같습니다.

| 관점 | 방식 | 의미 |
|---|---|---|
| Git 내부 병합 | Fast-forward | 현재 브랜치에 새 커밋이 없어 포인터만 앞으로 이동 |
| Git 내부 병합 | 3-way merge | 두 브랜치가 각각 진행되어 공통 조상을 기준으로 합치며 보통 merge commit 생성 |
| GitHub Pull Request | Merge commit | 브랜치의 커밋들을 유지하고 병합 커밋 생성 |
| GitHub Pull Request | Squash and merge | 여러 커밋을 하나로 압축해 대상 브랜치에 추가 |
| GitHub Pull Request | Rebase and merge | 커밋을 대상 브랜치 끝에 차례로 다시 놓음 |

같은 줄을 양쪽 브랜치에서 다르게 고치면 Git이 자동 판단하지 못해 **merge conflict(병합 충돌)**가 발생합니다. 충돌은 고장이 아니라 사람이 최종 내용을 선택해야 한다는 신호입니다.

## 4. Git 용어사전

| 용어 | 뜻 | 기억할 점 |
|---|---|---|
| Repository(repo) | 프로젝트 파일과 Git 이력이 있는 저장소 | 일반 폴더에 `git init`을 하면 Git 저장소가 됨 |
| `.git` | 커밋, 브랜치, 설정 등 Git 내부 데이터 폴더 | 직접 수정하거나 삭제하지 않기 |
| Working Tree | 실제로 편집 중인 파일 영역 | 저장했지만 add하지 않은 변경도 여기에 있음 |
| Staging Area(Index) | 다음 커밋에 포함할 변경 목록 | `git add`로 올리고 `git restore --staged`로 내림 |
| Tracked | Git이 이미 추적하는 파일 | 수정·삭제 상태를 Git이 감지함 |
| Untracked | Git이 아직 추적하지 않는 파일 | add 전에는 커밋되지 않음 |
| Modified | 추적 파일의 내용이 바뀐 상태 | `git diff`로 확인 |
| Staged | 다음 커밋 대상으로 선택된 상태 | `git diff --staged`로 확인 |
| Commit | 한 시점의 스냅샷과 작성자·시각·메시지 기록 | 먼저 add해야 변경이 포함됨 |
| Commit hash | 커밋을 식별하는 문자열 | 보통 앞 7자 정도만 써도 식별 가능 |
| `HEAD` | 현재 체크아웃한 커밋/브랜치를 가리키는 기준 | “내가 지금 어디에 있는가”를 나타냄 |
| Branch | 작업 흐름을 가리키는 이름 | 브랜치를 만든 뒤 `switch`로 이동 |
| `main` | 흔히 쓰는 기본 브랜치 이름 | 저장소마다 이름이 다를 수 있음 |
| Merge | 다른 브랜치의 이력을 현재 브랜치로 합침 | 먼저 결과를 받을 브랜치로 이동 |
| Conflict | Git이 자동으로 합칠 수 없는 겹친 변경 | 파일을 수정하고 add한 뒤 commit |
| Tag | 특정 커밋에 붙이는 고정 이름 | 보통 `v1.0.0` 같은 배포 지점 표시 |
| Remote | 인터넷이나 다른 위치의 Git 저장소 별칭 | `git remote -v`로 확인 |
| `origin` | 첫 원격 저장소에 관례적으로 붙이는 이름 | 특별한 예약어는 아니며 바꿀 수 있음 |
| Clone | 원격 저장소와 이력을 로컬에 복제 | 보통 remote `origin`도 자동 등록 |
| Fetch | 원격 변경을 가져오되 내 현재 브랜치에는 합치지 않음 | 안전하게 원격 상태부터 확인 가능 |
| Pull | fetch 후 현재 브랜치에 반영 | 작업 중인 변경이 있으면 먼저 정리 |
| Push | 로컬 커밋을 원격에 전송 | 커밋되지 않은 변경은 전송되지 않음 |
| Upstream branch | 로컬 브랜치가 기본으로 추적하는 원격 브랜치 | 첫 push의 `-u`로 연결 가능 |
| Diff | 두 상태 사이의 내용 차이 | 커밋 전에 반드시 확인하는 습관 권장 |
| Log | 커밋 이력 | `git log --oneline --graph --all`이 보기 편함 |
| Stash | 커밋 전 변경을 임시 보관 | 짧게 피신할 때 사용하고 잊지 않기 |
| Revert | 기존 커밋을 되돌리는 새 커밋 생성 | 이미 공유한 커밋을 안전하게 취소할 때 유용 |
| Reset | 브랜치·스테이징 기준을 과거로 이동 | 옵션에 따라 변경을 잃을 수 있어 주의 |
| Rebase | 커밋의 기반을 바꾸며 이력을 다시 작성 | 공유한 커밋에는 함부로 사용하지 않기 |
| `.gitignore` | Git이 추적하지 않을 파일 패턴 목록 | 이미 추적 중인 파일에는 자동 적용되지 않음 |

## 5. GitHub 용어사전

| 용어 | 뜻 | Git 용어와의 관계 |
|---|---|---|
| GitHub repository | GitHub 서버에 있는 저장소 | 로컬 저장소와 push/pull로 동기화 |
| Public / Private | 공개 / 접근이 제한된 저장소 | 비밀 파일을 Public에만 안 올리면 된다는 뜻은 아님 |
| Pull Request(PR) | 한 브랜치의 변경을 다른 브랜치에 합쳐 달라는 검토 요청 | `git pull` 명령과 무관 |
| Base branch | PR 변경을 받을 대상 브랜치 | 보통 `main` |
| Compare branch | PR에서 제안하는 변경 브랜치 | 보통 `feature/...` |
| Review | PR의 코드·문서 변경 검토 | 승인, 의견, 수정 요청 가능 |
| Issue | 버그, 할 일, 질문 등을 기록·논의하는 항목 | 코드 변경 전 목적을 기록할 때 유용 |
| Fork | 다른 사람의 GitHub 저장소를 내 GitHub 계정으로 복사 | `clone`은 컴퓨터로 복사한다는 차이 |
| Collaborator | 저장소에 직접 협업 권한을 받은 사용자 | 권한 수준에 따라 push 가능 여부가 다름 |
| Organization | 여러 사용자와 저장소를 팀 단위로 관리하는 공간 | 회사·스터디·오픈소스 팀에서 사용 |
| Actions | 빌드, 테스트, 배포 등을 자동 실행하는 기능 | `.github/workflows`의 설정으로 동작 |
| Workflow | Actions에서 실행할 자동화 절차 | push나 PR을 실행 조건으로 지정 가능 |
| Check | 테스트·검사 등의 자동 실행 결과 | 브랜치 규칙에서 통과를 요구할 수 있음 |
| Ruleset / branch protection | 중요 브랜치의 직접 push나 병합 조건을 제한하는 규칙 | 리뷰나 테스트 통과를 강제할 수 있음 |
| Release | 사용자에게 배포할 버전과 파일을 묶어 공개 | Git tag와 함께 사용하는 경우가 많음 |
| README | 저장소의 목적과 사용법을 설명하는 대표 문서 | 보통 Markdown 파일 `README.md` |
| License | 코드를 사용할 수 있는 법적 조건 | 공개 저장소라고 자동으로 자유 이용 가능한 것은 아님 |
| Star | 관심 있는 저장소를 표시 | 북마크·추천과 비슷하며 복사 기능은 아님 |
| Watch | 저장소 활동 알림을 구독 | 알림 범위를 설정할 수 있음 |

## 6. 자주 혼동하는 짝

| A | B | 차이 |
|---|---|---|
| Git | GitHub | 로컬 버전 관리 도구 / 온라인 협업 서비스 |
| Save | Commit | 편집기의 파일 저장 / Git 이력 스냅샷 기록 |
| Commit | Push | 로컬 기록 생성 / 그 기록을 원격에 전송 |
| Fetch | Pull | 원격 이력만 가져옴 / 가져온 뒤 현재 브랜치에 반영 |
| Pull | Pull Request | 동기화 명령 / 병합 검토 요청 |
| Clone | Fork | 원격에서 내 컴퓨터로 복제 / GitHub에서 내 계정으로 복제 |
| Branch | Folder | 커밋 흐름의 포인터 / 파일 시스템 디렉터리 |
| Merge | Rebase | 이력을 합침 / 이력의 기반을 다시 작성 |
| Revert | Reset | 취소 커밋을 새로 만듦 / 기준점을 옮김 |

다음: [설치와 GitHub 가입](./02_설치와_GitHub_가입.md)
