# Git & GitHub 초보자 가이드북

Windows의 **PowerShell**을 중심으로 Git의 기본 개념을 익히고, 내 컴퓨터의 프로젝트를 GitHub에 올린 뒤 clone, 브랜치, Pull Request, submodule과 GitHub Desktop까지 연습하는 가이드입니다.

이 문서는 명령어를 외우는 책이 아닙니다. 각 명령이 **어디의 무엇을 바꾸는지** 이해하고, 실행 전후에 `git status`로 확인하는 습관을 만드는 것이 목표입니다.

## 이 가이드로 할 수 있는 것

- Git과 GitHub의 차이를 설명할 수 있습니다.
- GitHub 개인 설정 메뉴를 구분하고 TOTP 앱·GitHub Mobile·복구 코드를 이용해 2FA를 안전하게 설정할 수 있습니다.
- 새 저장소 생성 화면과 저장소 Settings의 주요 영문 항목을 한국어 개념으로 설명할 수 있습니다.
- GitHub 저장소를 clone하고 기존 복제본을 최신 상태로 관리할 수 있습니다.
- 작업 파일을 `add → commit → push` 순서로 GitHub에 올릴 수 있습니다.
- GitHub의 변경을 `pull`로 내 컴퓨터에 받을 수 있습니다.
- 브랜치를 만들고 이동하고 병합할 수 있습니다.
- Pull Request를 만들고 병합한 뒤 로컬 브랜치를 정리할 수 있습니다.
- 일반 폴더, 독립 저장소, submodule 중 적절한 프로젝트 구조를 선택할 수 있습니다.
- GitHub Desktop에서 clone, commit, branch, push와 PR 흐름을 수행할 수 있습니다.
- 자주 만나는 오류와 충돌을 안전하게 해결할 수 있습니다.

## 전체 그림

```text
내가 편집 중인 파일       커밋 후보 보관함        내 컴퓨터의 Git 기록       GitHub 저장소
(Working Tree)          (Staging Area)         (Local Repository)       (Remote Repository)
       │                       │                       │                       │
       └── git add ───────────>│                       │                       │
                               └── git commit ───────>│                       │
                                                       └── git push ─────────>│
                                                       <── git fetch/pull ────┘
```

가장 중요한 구분은 다음과 같습니다.

- `git add`: 다음 커밋에 넣을 변경을 고릅니다.
- `git commit`: 선택한 변경을 **로컬 저장소의 스냅샷**으로 기록합니다.
- `git push`: 로컬 커밋을 GitHub 같은 원격 저장소로 전송합니다.
- `git pull`: 원격 변경을 가져와 현재 브랜치에 반영합니다.

> 커밋은 “승인”이라기보다 **설명표가 붙은 로컬 세이브 포인트**에 가깝습니다. 팀의 승인 과정은 보통 GitHub의 Pull Request와 코드 리뷰에서 일어납니다.

## 권장 학습 순서

| 순서 | 문서 | 완료 기준 |
|---:|---|---|
| 1 | [핵심 개념과 용어사전](./01_핵심개념과_용어사전.md) | Git과 GitHub, commit과 push, pull과 Pull Request의 차이를 말할 수 있다. |
| 2 | [설치와 GitHub 가입](./02_설치와_GitHub_가입.md) | `git --version`, 사용자 설정, 이메일 인증과 2FA 설정을 확인한다. |
| 3 | [로컬에서 GitHub까지 첫 실습](./03_로컬에서_GitHub까지_첫_실습.md) | 저장소 생성 항목을 이해하고 로컬 커밋을 GitHub에 push한 뒤 양방향 동기화를 확인한다. |
| 3-1 | [Clone(복제) 완전 가이드](./03_1_Clone_복제_가이드.md) | 저장소를 clone하고 `origin`, 브랜치, submodule 초기화 상태를 확인한다. |
| 4 | [브랜치와 병합 실습](./04_브랜치와_병합_실습.md) | 브랜치 생성·이동·병합과 충돌 해결을 직접 해 본다. |
| 5 | [GitHub 협업과 Pull Request](./05_GitHub_협업과_Pull_Request.md) | 작업 브랜치를 push하고 Pull Request로 병합한다. |
| 6 | [명령어 치트시트](./06_명령어_치트시트.md) | 일상 작업 순서를 보지 않고 수행할 수 있다. |
| 7 | [문제 해결과 안전 수칙](./07_문제해결과_안전수칙.md) | 오류가 나도 강제 명령부터 쓰지 않고 상태를 진단한다. |

처음이라면 1번부터 차례대로 읽으세요. 이미 설치가 끝났다면 3번부터 실습해도 됩니다.

## 심화·확장 학습 순서

기본 편을 마친 뒤 실제 프로젝트 구조와 GitHub 운영 방법을 익힙니다.

| 순서 | 문서 | 핵심 내용 |
|---:|---|---|
| 8 | [저장소 구조와 Submodule 심화](./08_저장소_구조와_Submodule_심화.md) | 일반 폴더·독립 저장소·submodule 비교, 추가·clone·수정·push 순서 |
| 9 | [GitHub Desktop 사용 가이드](./09_GitHub_Desktop_사용_가이드.md) | GUI로 clone, 변경 검토, commit, branch, push, PR, 여러 저장소 관리 |
| 10 | [GitHub 심화 운영 가이드](./10_GitHub_심화_운영_가이드.md) | Repository Settings, Danger Zone, Ruleset, CODEOWNERS, Issues, Actions, Release, Secrets, LFS |

## 강사용 단계별 실습 가이드

학생들과 같은 화면을 보며 수업을 진행하는 강사는 [강사용 Git & GitHub 단계별 실습 가이드](./instructor-guide/README.md)를 사용하세요. 차시별 수업 목표, 권장 시간, 강사 멘트, PowerShell 명령, 예상 결과, 확인 질문, 오류 대응과 Submodule 실습을 별도로 정리했습니다.

## 명령어 읽는 법

모든 터미널 명령은 PowerShell 기준입니다.

```powershell
git status
```

- 코드 블록 안의 명령만 입력합니다. 앞에 `PS C:\...>` 같은 프롬프트는 입력하지 않습니다.
- `<사용자명>`, `<파일명>`은 설명용 자리 표시자입니다. 꺾쇠까지 입력하지 말고 자신의 값으로 바꿉니다.
- 명령은 한 줄씩 실행하고 결과를 확인합니다.
- 위치가 헷갈리면 `Get-Location`, 파일이 궁금하면 `Get-ChildItem -Force`를 실행합니다.
- Git 명령 전후에는 `git status`를 자주 실행합니다. 가장 안전하고 유용한 습관입니다.

## 초보자가 먼저 기억할 원칙

1. 새 작업 전에는 현재 위치와 브랜치를 확인합니다.
2. 한 커밋에는 하나의 목적만 담습니다.
3. 커밋 메시지에는 “무엇을 했는지” 분명하게 씁니다.
4. 비밀번호, API 키, 인증서, `.env` 파일은 절대 커밋하지 않습니다.
5. `reset --hard`, `clean -fd`, 강제 push는 뜻을 완전히 알기 전에는 사용하지 않습니다.
6. 팀 저장소에서는 `main`에 바로 작업하지 않고 작업 브랜치와 Pull Request를 사용합니다.

## 공식 참고 자료

- [Git 공식 문서](https://git-scm.com/docs)
- [Pro Git 무료 전자책](https://git-scm.com/book/ko/v2)
- [Git 공식 치트시트](https://git-scm.com/cheat-sheet.pdf)
- [GitHub의 Git 기본 안내](https://docs.github.com/en/get-started/git-basics)
- [GitHub 시작 안내](https://docs.github.com/en/get-started/onboarding/getting-started-with-your-github-account)
- [GitHub Desktop 공식 문서](https://docs.github.com/en/desktop)

GitHub 화면의 버튼 이름이나 위치는 서비스 업데이트로 달라질 수 있습니다. 화면이 문서와 다르면 위 GitHub 공식 문서에서 최신 화면을 확인하세요.
