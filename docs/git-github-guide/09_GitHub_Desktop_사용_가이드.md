# 09. GitHub Desktop 사용 가이드

GitHub Desktop은 Git의 clone, commit, branch, pull, push, Pull Request 작업을 화면에서 확인하며 수행하는 공식 데스크톱 프로그램입니다. 명령어를 완전히 대체하기보다 **변경 파일과 브랜치 흐름을 눈으로 확인하는 도구**라고 이해하면 좋습니다.

## 1. Git 명령과 GitHub Desktop 버튼 연결

| Git 개념·명령 | GitHub Desktop에서 보이는 기능 |
|---|---|
| `git clone` | File → Clone repository |
| 기존 로컬 저장소 열기 | File → Add local repository |
| `git status`, `git diff` | Changes 탭과 파일별 변경 미리보기 |
| stage 대상 선택 | Changes 목록의 파일·변경 줄 체크 |
| `git commit` | Summary 작성 → Commit to 현재 브랜치 |
| `git fetch` | Fetch origin |
| `git pull` | Pull origin |
| `git push` | Push origin / Publish branch |
| `git switch` | Current Branch에서 브랜치 선택 |
| `git switch -c` | Current Branch → New branch |
| Pull Request | Preview Pull Request / Create Pull Request |
| `git log` | History 탭 |

버튼 문구는 저장소 상태에 따라 `Fetch origin`, `Pull origin`, `Push origin`, `Publish branch`처럼 바뀝니다. 현재 해야 할 동기화 작업을 나타냅니다.

## 2. 설치와 로그인

1. [GitHub Desktop 공식 다운로드](https://desktop.github.com/download/)에서 Windows 설치 파일을 받습니다.
2. 설치 후 GitHub Desktop을 실행합니다.
3. **Sign in to GitHub.com**을 선택합니다.
4. 브라우저가 열리면 사용할 GitHub 계정으로 로그인하고 승인을 완료합니다.
5. GitHub Desktop으로 돌아와 커밋에 표시할 이름과 이메일을 확인합니다.

Private 저장소를 사용한다면 반드시 해당 저장소에 권한이 있는 계정으로 로그인해야 합니다.

## 3. 저장소를 여는 세 가지 방법

### 방법 A: GitHub 저장소를 처음 clone

1. **File → Clone repository**를 선택합니다.
2. **GitHub.com** 탭에서 저장소를 찾습니다. 목록에 없다면 **URL** 탭에 HTTPS URL을 넣습니다.
3. **Local path**에서 저장할 상위 폴더를 선택합니다.
4. **Clone**을 누릅니다.

이 작업은 PowerShell의 다음 명령과 같은 목적입니다.

```powershell
git clone 'https://github.com/사용자명/저장소명.git'
```

기존 폴더 안에 다시 중복 clone하지 않도록 Local path를 확인하세요.

### 방법 B: 이미 내 PC에 있는 Git 저장소 추가

PowerShell이나 VS Code에서 이미 clone한 저장소라면 다시 clone하지 않습니다.

1. **File → Add local repository**를 선택합니다.
2. **Choose**를 눌러 `.git`이 있는 저장소 루트 폴더를 선택합니다.
3. **Add repository**를 누릅니다.

폴더를 GitHub Desktop 창으로 끌어 놓아 추가할 수도 있습니다. 저장소를 목록에 등록하는 작업일 뿐 파일이나 커밋을 복사하지 않습니다.

### 방법 C: 새 로컬 저장소 생성

1. **File → New repository**를 선택합니다.
2. Name, Description, Local path를 입력합니다.
3. 필요하면 README, `.gitignore`, License를 선택합니다.
4. **Create repository**를 누릅니다.
5. 로컬 작업만 할 수 있으며, GitHub에 올리려면 **Publish repository**를 누릅니다.

Publish 화면의 **Keep this code private** 선택 여부를 반드시 확인하세요.

## 4. 화면 읽는 법

### Current Repository

현재 조작할 저장소입니다. 여러 저장소가 등록되어 있으면 여기서 바꿉니다. 버튼을 누르기 전에 부모 저장소인지 submodule 저장소인지 확인하세요.

### Current Branch

현재 커밋이 들어갈 브랜치입니다. `main`에서 직접 작업하지 않기로 한 팀이라면 파일 편집 전에 작업 브랜치를 만듭니다.

### Changes

아직 커밋하지 않은 변경 목록입니다.

- 초록색: 추가된 파일·줄
- 노란색: 수정된 파일
- 빨간색: 삭제된 파일·줄
- 체크됨: 이번 커밋에 포함할 변경
- 체크 해제: 작업 폴더에는 남지만 이번 커밋에는 제외

파일을 선택하면 오른쪽에서 diff를 확인할 수 있습니다. 전체 선택 상태에서 바로 커밋하기보다 의도한 파일만 체크되어 있는지 읽으세요.

### Summary와 Description

- Summary: 필수 커밋 제목, 짧고 명확하게 작성
- Description: 선택 사항, 이유나 추가 설명 작성
- Commit to `브랜치명`: 선택한 변경을 현재 로컬 브랜치에 커밋

Commit은 아직 GitHub에 올리는 동작이 아닙니다. 그다음 **Push origin** 또는 **Publish branch**가 필요합니다.

### History

현재 브랜치의 커밋 이력을 보여 줍니다. 커밋을 선택하면 어떤 파일과 줄이 바뀌었는지 확인할 수 있습니다.

## 5. 가장 안전한 하루 작업 순서

### 5-1. 시작할 때 동기화

1. Current Repository가 맞는지 확인합니다.
2. Current Branch에서 `main`을 선택합니다.
3. **Fetch origin**을 누릅니다.
4. 원격 변경이 있으면 **Pull origin**을 누릅니다.

### 5-2. 작업 브랜치 생성

1. **Current Branch**를 누릅니다.
2. **New branch**를 선택합니다.
3. `docs/update-guide`, `feature/login`처럼 목적이 드러나는 이름을 입력합니다.
4. 기준 브랜치가 최신 `main`인지 확인하고 생성합니다.

### 5-3. 파일 수정과 커밋

1. **Repository → Open in Visual Studio Code**처럼 연결된 편집기를 엽니다.
2. 파일을 수정하고 저장합니다.
3. GitHub Desktop의 Changes 탭으로 돌아옵니다.
4. 파일별 diff와 체크 상태를 확인합니다.
5. Summary를 작성합니다.
6. **Commit to 작업-브랜치**를 누릅니다.

### 5-4. GitHub에 브랜치 올리기

처음 올리는 로컬 브랜치라면 **Publish branch**, 이후 커밋은 **Push origin**을 누릅니다.

```text
Commit to branch = 로컬 기록
Publish branch / Push origin = GitHub 전송
```

## 6. Pull Request 만들기

작업 브랜치를 push한 뒤 진행합니다.

1. **Preview Pull Request**를 누릅니다.
2. base가 `main`, compare가 현재 작업 브랜치인지 확인합니다.
3. 변경 파일과 커밋을 검토합니다.
4. **Create Pull Request**를 누릅니다.
5. 브라우저의 GitHub 화면에서 제목·본문·리뷰어를 확인하고 PR을 생성합니다.

GitHub Desktop 버튼이 보이지 않으면 **Branch → Create Pull Request** 또는 저장소의 GitHub 웹 Pull requests 탭을 사용합니다. PR 전에 현재 브랜치가 GitHub에 publish되어 있어야 합니다.

## 7. PR 병합 후 로컬 정리

GitHub 웹에서 PR을 병합했다면 GitHub Desktop으로 돌아옵니다.

1. Current Branch에서 `main`을 선택합니다.
2. **Fetch origin**을 누릅니다.
3. **Pull origin**을 눌러 병합 결과를 받습니다.
4. 작업 브랜치가 더 필요 없는지 확인한 뒤 삭제합니다.

원격 브랜치를 삭제했어도 로컬 브랜치는 자동으로 사라지지 않을 수 있습니다. 중요한 미병합 작업이 없는지 History를 확인한 뒤 정리하세요.

## 8. 변경 버리기와 커밋 취소 주의

GitHub Desktop의 **Discard changes**는 파일의 커밋되지 않은 내용을 되돌립니다. 일반 파일은 휴지통에서 복구 가능한 경우가 있지만, 작업 종류와 환경에 따라 복구가 어려울 수 있습니다.

실행 전 확인:

- 선택한 저장소가 맞는가?
- 선택한 파일과 줄이 맞는가?
- 아직 커밋하지 않은 중요한 작업은 없는가?
- 대상이 일반 파일이 아니라 submodule 포인터는 아닌가?

push하지 않은 마지막 커밋은 Undo 또는 Amend 기능으로 정리할 수 있지만, 이미 push해 다른 사람이 사용한 이력은 함부로 다시 작성하지 않습니다. 공유한 변경을 취소할 때는 새 revert 커밋을 만드는 방식이 안전합니다.

## 9. 충돌이 발생했을 때

GitHub Desktop이 merge conflict를 표시하면 다음 순서로 진행합니다.

1. 충돌 파일 목록을 확인합니다.
2. Visual Studio Code에서 파일을 열어 양쪽 내용을 비교합니다.
3. 최종 내용을 선택·수정하고 충돌 표시를 제거합니다.
4. GitHub Desktop으로 돌아와 해결 상태를 확인합니다.
5. merge 커밋을 완료하고 push합니다.

상태가 불분명하면 저장소 폴더에서 PowerShell을 열고 읽기 전용 명령으로 확인합니다.

```powershell
git status
git diff
git log --oneline --graph --decorate --all -10
```

## 10. 여러 독립 저장소 관리

`project-a`, `project-b`처럼 독립 저장소가 여러 개라면 각각 GitHub Desktop에 추가합니다.

```text
GitHub Desktop 저장소 목록
├─ project-a
├─ project-b
└─ shared-library
```

각 저장소는 Current Repository에서 선택하며 commit, pull, push도 각각 수행합니다. 상위 작업 폴더를 하나의 저장소처럼 publish하지 않습니다.

## 11. submodule을 GitHub Desktop과 함께 관리

submodule은 부모와 자식이 독립 저장소이므로 GitHub Desktop에서도 각각 추가해 두는 편이 상태를 구분하기 쉽습니다.

1. **File → Add local repository**로 부모 저장소를 추가합니다.
2. 같은 메뉴로 `부모\sub_repository01` 폴더도 별도 저장소로 추가합니다.
3. 자식 저장소를 선택해 수정 내용을 commit하고 **먼저 push**합니다.
4. 부모 저장소를 선택합니다.
5. 변경된 submodule 커밋 포인터를 부모에서 commit하고 push합니다.

```text
자식 저장소: 파일 변경 → commit → push
부모 저장소: 자식 커밋 ID 변경 → commit → push
```

submodule 추가·초기화·재귀 업데이트는 전용 GUI 버튼보다 PowerShell 명령이 상태를 더 분명하게 보여 줍니다.

```powershell
git submodule status --recursive
git submodule update --init --recursive
git diff --submodule
```

GitHub Desktop에서 부모의 submodule 변경을 **Discard changes**로 처리하기 전에 특히 주의하세요. 자식 작업 폴더에 커밋하지 않은 내용이 있는지 먼저 확인합니다.

## 12. VS Code 화면과 GitHub Desktop의 차이

첨부된 화면은 GitHub Desktop이 아니라 **VS Code의 소스 제어 패널**입니다. VS Code가 부모와 `sub_repository01`을 동시에 두 개의 저장소로 표시한 것은 정상입니다.

| VS Code | GitHub Desktop |
|---|---|
| 한 창의 소스 제어 패널에 여러 저장소가 함께 보일 수 있음 | Current Repository에서 한 저장소씩 전환 |
| 편집기와 Git 상태가 한 화면에 있음 | 변경 검토·커밋·동기화에 집중 |
| 확장 기능에 따라 동작이 달라질 수 있음 | GitHub 공식 GUI 흐름 제공 |

두 프로그램을 함께 사용해도 됩니다. VS Code에서 편집하고 GitHub Desktop에서 diff·commit·push를 검토하는 방식이 초보자에게 편리할 수 있습니다.

## 13. GitHub Desktop이 특히 편한 작업

- 파일별 diff를 색상으로 확인
- 커밋에 넣을 파일과 변경 줄 선택
- 브랜치 생성과 이동
- 원격과의 fetch/pull/push 상태 확인
- 커밋 History 탐색
- PR 생성 화면으로 이동
- 여러 로컬 저장소 목록 관리

## 14. PowerShell이 더 명확한 작업

- submodule 추가·초기화·정확한 커밋 상태 확인
- 복잡한 커밋 그래프와 원격 추적 관계 진단
- 자동화 스크립트와 반복 작업
- GitHub Desktop이 표시하지 않는 상세 오류 확인
- 고급 rebase, bisect, reflog 등의 복구·분석

GUI와 명령줄 중 하나만 고집할 필요는 없습니다. 어떤 도구를 쓰더라도 Working Tree, Commit, Branch, Remote 개념은 같습니다.

## 15. 완료 점검

- [ ] clone, add local repository, new repository의 차이를 안다.
- [ ] Changes와 History의 역할을 구분한다.
- [ ] Commit과 Push origin이 다른 동작임을 안다.
- [ ] 최신 main에서 작업 브랜치를 만들 수 있다.
- [ ] Publish branch 후 Pull Request를 만들 수 있다.
- [ ] 부모 저장소와 submodule을 별도 저장소로 선택할 수 있다.
- [ ] submodule은 자식 push 후 부모 포인터를 commit해야 함을 안다.
- [ ] Discard changes 전에 저장소와 대상 파일을 확인한다.

공식 참고: [GitHub Desktop 문서](https://docs.github.com/en/desktop) · [저장소 clone과 fork](https://docs.github.com/en/desktop/adding-and-cloning-repositories/cloning-and-forking-repositories-from-github-desktop) · [변경 검토와 커밋](https://docs.github.com/en/desktop/making-changes-in-a-branch/committing-and-reviewing-changes-to-your-project-in-github-desktop) · [브랜치 동기화](https://docs.github.com/en/desktop/working-with-your-remote-repository-on-github-or-github-enterprise/syncing-your-branch-in-github-desktop)

이전: [저장소 구조와 Submodule 심화](./08_저장소_구조와_Submodule_심화.md) · 다음: [GitHub 심화 운영 가이드](./10_GitHub_심화_운영_가이드.md)
