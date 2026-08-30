# 05. GitHub 협업과 Pull Request

이 장에서는 GitHub에서 가장 많이 쓰는 작업 흐름인 **GitHub Flow**를 연습합니다.

```text
Issue/할 일 확인
  → 최신 main 받기
  → 작업 브랜치 만들기
  → 수정·커밋
  → 브랜치 push
  → Pull Request 작성
  → 리뷰·검사
  → main에 merge
  → 로컬 main 동기화와 브랜치 정리
```

Pull Request(PR)는 “내 변경을 대상 브랜치에 합치기 전에 함께 검토해 주세요”라는 요청입니다. `git pull` 명령과는 관계가 없습니다.

## 1. 시작 전 main 최신화

[첫 실습](./03_로컬에서_GitHub까지_첫_실습.md)의 `hello-git` 저장소에서 시작합니다.

```powershell
$practiceRoot = Join-Path ([Environment]::GetFolderPath('MyDocuments')) 'git-practice'
Set-Location (Join-Path $practiceRoot 'hello-git')
git status
git switch main
git pull --ff-only
```

`working tree clean`을 확인합니다. 새 브랜치는 가능하면 최신 `main`에서 만듭니다.

## 2. 작업 브랜치 만들기

```powershell
git switch -c docs/add-contributing
git branch --show-current
```

브랜치 이름을 `docs/add-contributing`으로 지어 문서 작업임을 드러냈습니다.

## 3. 파일 작성하고 커밋하기

```powershell
@'
# 기여 방법

1. 최신 main에서 작업 브랜치를 만듭니다.
2. 변경을 작은 단위로 커밋합니다.
3. 브랜치를 push하고 Pull Request를 만듭니다.
'@ | Set-Content -Encoding utf8 CONTRIBUTING.md
```

커밋 전 세 단계로 검토합니다.

```powershell
git status
git diff
git add CONTRIBUTING.md
git diff --staged
```

의도한 파일과 내용만 보이면 커밋합니다.

```powershell
git commit -m "Add contribution guide"
git status
```

## 4. 작업 브랜치를 GitHub에 push하기

```powershell
git push -u origin docs/add-contributing
```

`-u`는 로컬 브랜치와 같은 이름의 원격 브랜치를 추적 관계로 연결합니다. 이후 이 브랜치에서는 `git push`와 `git pull`만 입력할 수 있습니다.

확인합니다.

```powershell
git branch -vv
git remote -v
```

## 5. GitHub에서 Pull Request 만들기

1. 브라우저에서 `hello-git` 저장소를 엽니다.
2. 새로 push한 브랜치 안내의 **Compare & pull request**를 누릅니다. 안내가 없다면 **Pull requests → New pull request**로 이동합니다.
3. 다음 방향이 맞는지 확인합니다.
   - base: `main` — 변경을 받을 브랜치
   - compare: `docs/add-contributing` — 변경을 제안하는 브랜치
4. **Files changed**에서 `CONTRIBUTING.md`만 추가되었는지 확인합니다.
5. 제목을 `Add contribution guide`로 작성합니다.
6. 본문에는 아래 세 가지를 간단히 씁니다.
   - 무엇을 바꿨는가
   - 왜 바꿨는가
   - 어떻게 확인했는가
7. **Create pull request**를 누릅니다.

PR 본문 예시:

```markdown
## 변경 내용

- 초보자를 위한 `CONTRIBUTING.md`를 추가했습니다.

## 이유

- 브랜치와 Pull Request 작업 순서를 쉽게 확인할 수 있도록 했습니다.

## 확인

- Markdown 미리보기에서 목록이 정상 표시되는지 확인했습니다.
```

## 6. 리뷰와 자동 검사 이해하기

팀 저장소에서는 바로 병합하기 전에 다음을 확인합니다.

- **Conversation**: 설명과 댓글, 리뷰 대화
- **Commits**: PR에 포함된 커밋
- **Files changed**: 실제 변경 내용
- **Checks**: 테스트, 빌드, 형식 검사 같은 자동 실행 결과
- **Reviewers**: 검토를 요청한 사람과 승인 상태

리뷰에서 수정 요청을 받았다면 같은 로컬 브랜치에서 수정하고 다시 push합니다. 기존 PR에 자동으로 추가됩니다.

```powershell
Add-Content -Encoding utf8 CONTRIBUTING.md "`n변경 전후에는 ``git status``를 확인합니다."
git diff
git add CONTRIBUTING.md
git commit -m "Clarify status check"
git push
```

새 PR을 다시 만들 필요가 없습니다.

## 7. Pull Request 병합하기

이 개인 실습에서는 변경과 Checks를 확인한 뒤 GitHub에서 병합합니다.

1. PR 페이지에서 **Merge pull request**를 선택합니다.
2. **Confirm merge**를 누릅니다.
3. 병합 후 **Delete branch**가 보이면 원격 작업 브랜치를 삭제합니다.

저장소 설정에 따라 다음 병합 방식 중 일부만 보일 수 있습니다.

| 방식 | 결과 | 초보자가 이해할 핵심 |
|---|---|---|
| Create a merge commit | 작업 브랜치 커밋과 병합 커밋을 유지 | 브랜치 흐름이 기록에 선명하게 남음 |
| Squash and merge | PR의 여러 커밋을 하나로 합침 | `main` 이력이 단순해짐 |
| Rebase and merge | 커밋을 `main` 끝에 차례로 다시 배치 | 선형 이력이 되지만 커밋 ID가 바뀜 |

팀의 규칙이 있다면 그 규칙을 따릅니다. 어떤 방식이 항상 정답인 것은 아닙니다.

## 8. 로컬 main 동기화와 정리

GitHub에서 병합했으므로 로컬 `main`은 아직 뒤처져 있습니다.

```powershell
git switch main
git pull --ff-only
Test-Path CONTRIBUTING.md
git log --oneline --graph --decorate --all -10
```

로컬 작업 브랜치를 안전하게 삭제하고, 사라진 원격 브랜치 참조도 정리합니다.

```powershell
git branch -d docs/add-contributing
git fetch --prune
git branch --all
```

이제 다음 작업도 **main 최신화 → 새 브랜치** 순서로 시작합니다.

## 9. Issue와 연결하기

Issue는 버그, 기능, 질문, 할 일을 기록하는 GitHub 항목입니다. 팀에서는 보통 다음처럼 연결합니다.

1. Issue에 배경과 완료 조건을 기록합니다.
2. Issue 번호를 포함하거나 목적이 드러나는 브랜치를 만듭니다.
3. PR 본문에 `Closes #12`처럼 씁니다.
4. PR이 기본 브랜치에 병합되면 연결된 Issue가 자동으로 닫힐 수 있습니다.

예시:

```text
Issue #12: 설치 문서에 Windows 안내 추가
Branch: docs/12-windows-setup
Commit: Add Windows setup steps
PR: Add Windows setup guide / 본문에 Closes #12
```

## 10. 다른 사람의 저장소에 기여할 때: fork

직접 push 권한이 없는 공개 저장소에서는 흔히 다음 순서로 작업합니다.

```text
원본 저장소
  → GitHub에서 Fork
  → 내 계정의 fork를 Clone
  → 브랜치 작업과 Push
  → 내 fork에서 원본 저장소로 Pull Request
```

- **Fork**: GitHub 저장소를 내 GitHub 계정 아래로 복사합니다.
- **Clone**: GitHub 저장소를 내 컴퓨터로 복제합니다.

처음에는 자신의 `hello-git` 저장소에서 PR 흐름을 충분히 익힌 뒤 공개 프로젝트의 기여 안내(`CONTRIBUTING.md`)를 읽고 참여하세요.

## 11. 팀 작업용 반복 레시피

```powershell
# 1. 시작
git switch main
git pull --ff-only
git switch -c feature/short-description

# 2. 작업 후 검토와 기록
git status
git diff
git add <파일명>
git diff --staged
git commit -m "Describe the change"

# 3. 공유와 PR
git push -u origin feature/short-description

# 4. GitHub에서 PR 리뷰·병합 후 정리
git switch main
git pull --ff-only
git branch -d feature/short-description
git fetch --prune
```

`<파일명>`은 실제 파일명으로 바꿉니다. 팀에서 테스트 명령이 정해져 있다면 push 전에 반드시 실행합니다.

## 12. 완료 점검

- [ ] 최신 `main`에서 새 작업 브랜치를 만들었다.
- [ ] 커밋 전 `status`, `diff`, `diff --staged`를 확인했다.
- [ ] 작업 브랜치를 `git push -u`로 올렸다.
- [ ] base와 compare 방향을 확인하고 PR을 만들었다.
- [ ] Files changed에서 의도한 변경만 있는지 확인했다.
- [ ] GitHub에서 병합한 뒤 로컬 `main`을 pull했다.
- [ ] 병합된 로컬·원격 브랜치를 정리했다.

공식 참고: [GitHub Flow](https://docs.github.com/en/get-started/using-github/github-flow)

이전: [브랜치와 병합 실습](./04_브랜치와_병합_실습.md) · 다음: [명령어 치트시트](./06_명령어_치트시트.md)
