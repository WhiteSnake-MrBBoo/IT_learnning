# 3차시. Merge와 Pull Request 실습

## 수업 개요

- 권장 시간: 80~100분
- 선수 학습: `practice/branch-switch` 브랜치 commit·push 완료
- 완료 결과: GitHub PR로 작업 브랜치를 `main`에 병합하고 로컬 `main`을 pull합니다. 이어서 로컬 merge와 선택형 충돌 해결을 비교합니다.

## 학습 목표

- `git pull`과 GitHub Pull Request가 전혀 다른 개념임을 설명합니다.
- merge 전에 **변경을 받을 도착 브랜치**를 먼저 확인합니다.
- PR의 base와 compare 방향을 정확히 읽습니다.
- GitHub에서 병합한 뒤 로컬 `main`에 pull이 필요한 이유를 설명합니다.
- 로컬 merge 뒤에는 원격 반영을 위해 push가 필요함을 설명합니다.

## 0. 시작 상태 확인

```powershell
# 원본 실습 저장소로 이동
$classRoot = Join-Path ([Environment]::GetFolderPath('MyDocuments')) 'git-class-practice'
Set-Location (Join-Path $classRoot 'git-class-demo')

# 작업 브랜치와 원격 추적 상태 확인
git status
git switch practice/branch-switch
git pull --ff-only
git branch -vv
git log --oneline --graph --decorate --all -10
```

반드시 `working tree clean`이고 `origin/practice/branch-switch`와 동기화된 상태에서 시작합니다.

## 1. Pull과 Pull Request 구분

수업 시작 질문:

> “Pull Request를 만들면 내 PC에서 `git pull` 명령이 실행되는 것일까요?”

정답은 **아닙니다.**

| 구분 | `git pull` | Pull Request(PR) |
|---|---|---|
| 정체 | Git 명령 | GitHub 협업 기능 |
| 목적 | 원격 커밋을 현재 로컬 브랜치에 반영 | 한 브랜치의 변경을 다른 브랜치에 합치기 전에 검토 요청 |
| 주로 실행하는 곳 | PowerShell | GitHub 웹 또는 `gh` CLI |
| 리뷰 | 없음 | 댓글, 승인, 수정 요청, Checks 가능 |

## 2. GitHub에서 Pull Request 생성

브라우저에서 `git-class-demo` 저장소를 엽니다.

1. **Pull requests → New pull request**를 선택합니다.
2. 방향을 다음처럼 지정합니다.
   - **base: `main`** — 변경을 받을 도착 브랜치
   - **compare: `practice/branch-switch`** — 변경을 제안하는 작업 브랜치
3. **Files changed**에서 다음 변경을 확인합니다.
   - `branch-only.txt` 추가
   - `shared-note.txt` 삭제
4. 제목을 `Practice branch file changes`로 작성합니다.
5. 본문에 변경 내용, 이유, 확인 방법을 적습니다.
6. **Create pull request**를 누릅니다.

PR 본문 예시:

```markdown
## 변경 내용

- 브랜치 전용 파일을 추가했습니다.
- 브랜치 전환 관찰용 기준 파일을 삭제했습니다.

## 변경 이유

- main과 작업 브랜치의 파일 상태 차이를 학습하기 위해서입니다.

## 확인 방법

- 두 브랜치를 전환하며 파일 존재 여부를 확인했습니다.
```

### 강사가 반드시 확인시킬 화면

- Conversation: PR 설명과 대화
- Commits: 포함된 커밋
- Files changed: 실제 추가·수정·삭제
- Checks: 자동 검사 결과가 있는 경우
- base/compare 방향

base와 compare를 반대로 선택하면 `main`을 작업 브랜치에 합치는 반대 요청이 될 수 있습니다. 제목보다 먼저 방향을 확인합니다.

## 3. 리뷰 수정 흐름—선택

강사가 “설명을 한 줄 더 추가해 주세요”라고 리뷰했다고 가정합니다. PR을 닫거나 새 PR을 만들 필요 없이 같은 작업 브랜치를 수정합니다.

```powershell
# 같은 작업 브랜치에서 리뷰 요청 반영
Add-Content -Encoding utf8 branch-only.txt 'PR 리뷰를 반영한 문장입니다.'
git diff
git add branch-only.txt
git diff --staged
git commit -m "Clarify branch practice note"
git push
```

GitHub PR을 새로 고치면 새 커밋과 변경이 기존 PR에 자동으로 추가됩니다.

## 4. GitHub에서 PR 병합

이 실습은 브랜치 이력을 눈으로 확인하기 위해 **Create a merge commit** 방식을 선택합니다.

1. Files changed와 Checks를 다시 확인합니다.
2. **Merge pull request**를 누릅니다.
3. **Confirm merge**를 누릅니다.
4. 병합 완료 화면과 merge commit을 확인합니다.
5. 원격 작업 브랜치를 정리하려면 **Delete branch**를 누릅니다.

강사 질문:

> “GitHub의 main은 최신이 됐습니다. 지금 내 PC의 main 파일도 자동으로 바뀌었을까요?”

기대 답변: 아니요. 로컬 저장소는 아직 pull하지 않았습니다.

## 5. 로컬 main 동기화와 브랜치 정리

```powershell
# 변경을 받을 로컬 main으로 이동
git switch main

# GitHub에서 병합된 origin/main을 로컬 main에 반영
git pull --ff-only origin main

# 브랜치 작업 결과가 main에 나타났는지 확인
Test-Path branch-only.txt
Test-Path shared-note.txt
git log --oneline --graph --decorate --all -12
```

원격 브랜치를 GitHub에서 삭제했다면 원격 추적 참조를 정리하고, 병합된 로컬 브랜치도 안전하게 삭제합니다.

```powershell
# 삭제된 원격 브랜치 참조 정리
git fetch --prune

# main에 병합된 로컬 브랜치만 안전하게 삭제
git branch -d practice/branch-switch
git branch --all
```

`-d`가 거부하면 강제로 `-D`를 사용하지 말고 병합 방식과 아직 필요한 커밋이 있는지 확인합니다.

## 6. 로컬 Merge 실습

이번에는 GitHub PR을 사용하지 않고 로컬에서 직접 병합합니다.

```powershell
# 최신 main에서 새 로컬 작업 브랜치 생성
git status
git switch main
git pull --ff-only
git switch -c practice/local-merge

# 작업 브랜치 전용 파일 생성
@'
이 파일은 로컬 merge 실습에서 만들었습니다.
'@ | Set-Content -Encoding utf8 local-merge.txt

# 작업 브랜치에 커밋
git add local-merge.txt
git diff --staged
git commit -m "Add local merge practice file"
```

병합 결과를 받을 `main`으로 먼저 이동합니다.

```powershell
# 도착 브랜치로 이동
git switch main

# 현재 main에 작업 브랜치 이력을 합침
git merge practice/local-merge

# 로컬 그래프와 파일 확인
git log --oneline --graph --decorate --all -12
Test-Path local-merge.txt
```

`main`이 작업 분기 후 따로 진행되지 않았다면 `Fast-forward`가 표시될 수 있습니다. 이는 병합이 실패한 것이 아니라 `main` 포인터만 작업 브랜치 끝으로 이동해도 이력이 보존되기 때문입니다.

로컬 merge는 GitHub를 자동으로 바꾸지 않습니다.

```powershell
# 병합된 로컬 main을 GitHub에 전송
git push origin main

# 병합된 로컬 작업 브랜치 정리
git branch -d practice/local-merge
```

## 7. PR 방식과 로컬 Merge 방식 비교

| 항목 | GitHub Pull Request | 로컬 `git merge` |
|---|---|---|
| 적합한 상황 | 팀 협업, 리뷰, 보호된 main | 개인 실험, 단순 로컬 통합, 팀 규칙이 허용한 경우 |
| 변경 검토 | 웹에서 Files changed·리뷰·Checks | 로컬 diff·log를 직접 확인 |
| 원격 main 반영 | GitHub에서 병합 시 바로 반영 | 로컬 병합 후 push 필요 |
| 로컬 main 반영 | GitHub 병합 후 pull 필요 | 병합한 그 로컬 main은 이미 반영됨 |

초보 팀의 기본 공식:

```text
작업 브랜치 commit
  → 작업 브랜치 push
  → GitHub PR·리뷰·merge
  → 로컬 main pull
```

## 8. 병합 충돌 시연—선택 25분

같은 파일의 같은 줄을 두 브랜치에서 다르게 수정해 충돌이 “고장”이 아니라 사람의 판단 요청임을 보여 줍니다.

```powershell
# main에 공통 기준 파일 생성
git switch main
'공통 시작 문장' | Set-Content -Encoding utf8 conflict-note.txt
git add conflict-note.txt
git commit -m "Add conflict practice base"

# 작업 브랜치에서 같은 줄 수정
git switch -c practice/conflict
'작업 브랜치가 선택한 문장' | Set-Content -Encoding utf8 conflict-note.txt
git add conflict-note.txt
git commit -m "Edit conflict note on branch"

# main에서 같은 줄을 다른 내용으로 수정
git switch main
'main이 선택한 문장' | Set-Content -Encoding utf8 conflict-note.txt
git add conflict-note.txt
git commit -m "Edit conflict note on main"

# 의도적으로 충돌 발생
git merge practice/conflict
git status
Get-Content conflict-note.txt
```

파일의 `<<<<<<<`, `=======`, `>>>>>>>` 표시는 최종 내용이 아닙니다. 두 의도를 읽고 최종 문장으로 수정합니다.

```powershell
# 양쪽 의도를 검토해 최종 내용 작성
'main과 작업 브랜치의 의견을 함께 반영한 문장' | Set-Content -Encoding utf8 conflict-note.txt

# 충돌 해결 표시 후 병합 커밋 완료
git add conflict-note.txt
git status
git commit -m "Resolve conflict note merge"
git log --oneline --graph --decorate --all -15

# 원격 반영과 연습 브랜치 정리
git push origin main
git branch -d practice/conflict
```

해결을 중단하고 병합 시작 전으로 돌아가려면 병합 커밋 전에 `git merge --abort`를 사용합니다.

## 9. 종료 질문

1. merge 전에 왜 도착 브랜치로 먼저 이동해야 하는가?
2. PR의 base와 compare는 각각 무엇인가?
3. GitHub에서 merge한 뒤 로컬에서 필요한 명령은 무엇인가?
4. 로컬에서 merge한 뒤 GitHub 반영에 필요한 명령은 무엇인가?
5. 충돌 표시는 어떤 두 내용을 보여 주는가?

이전: [Branch 생성과 전환 실습](./02_Branch_생성과_전환_실습.md) · 다음: [브랜치 분기 심화 실습](./04_브랜치_분기_심화_실습.md)
