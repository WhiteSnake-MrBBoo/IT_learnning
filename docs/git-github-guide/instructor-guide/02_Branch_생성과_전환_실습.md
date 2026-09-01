# 2차시. Branch 생성과 전환 실습

## 수업 개요

- 권장 시간: 60~75분
- 선수 학습: 1차시의 commit과 push 완료
- 시작 위치: `git-class-demo` 원본 폴더의 깨끗한 `main`
- 완료 결과: 작업 브랜치에서 파일을 추가·삭제하고, `main`과 오갈 때 작업 폴더가 커밋 상태에 따라 바뀌는 것을 관찰합니다.

## 학습 목표

- 브랜치는 프로젝트 폴더 전체 복사본이 아니라 커밋을 가리키는 이름임을 설명합니다.
- `git switch -c`와 `git switch`의 차이를 사용합니다.
- 로컬 브랜치와 원격 브랜치가 별도로 존재함을 확인합니다.
- 브랜치 전환 전에 작업 상태를 확인하는 습관을 익힙니다.

## 0. 화면과 시작 상태 준비

VS Code 탐색기와 PowerShell을 같은 화면에 보이게 합니다. 브라우저에는 `git-class-demo` 저장소를 열어 둡니다.

```powershell
# 공통 실습 루트와 원본 저장소로 이동
$classRoot = Join-Path ([Environment]::GetFolderPath('MyDocuments')) 'git-class-practice'
Set-Location (Join-Path $classRoot 'git-class-demo')

# 최신의 깨끗한 main에서 시작
git status
git switch main
git pull --ff-only
git branch --show-current
```

`working tree clean`이 아니면 학생의 변경을 확인합니다. 강사가 임의로 삭제하거나 `reset --hard`를 실행하지 않습니다.

## 1. main에 관찰용 기준 파일 만들기

브랜치에서 삭제했다가 `main`에서 다시 보이는 것을 안전하게 관찰할 전용 파일을 만듭니다.

```powershell
# 삭제 연습 전용 파일 생성
@'
이 파일은 main의 기준 파일입니다.
브랜치 전환에 따른 파일 변화를 관찰합니다.
'@ | Set-Content -Encoding utf8 shared-note.txt

# 변경 확인 후 main에 기록하고 원격 반영
git status
git add shared-note.txt
git diff --staged
git commit -m "Add branch practice base file"
git push
```

## 2. 작업 브랜치 생성과 이동

```powershell
# 현재 main 커밋을 시작점으로 새 브랜치를 만들고 즉시 이동
git switch -c practice/branch-switch

# 현재 브랜치와 전체 로컬 브랜치 확인
git branch --show-current
git branch
```

예상 관찰:

- `git branch`에 `main`과 `practice/branch-switch`가 보입니다.
- 현재 브랜치 앞에는 `*` 표시가 있습니다.
- 브랜치를 만든 직후 파일 내용은 `main`과 같습니다. 두 브랜치가 같은 커밋을 가리키기 때문입니다.

강사 질문:

> “새 브랜치를 만들었는데 탐색기 파일이 그대로인 이유는 무엇인가요?”

기대 답변: 처음에는 두 브랜치가 같은 시작 커밋을 가리키기 때문입니다.

## 3. 브랜치에서 파일 추가와 삭제

```powershell
# 현재 브랜치에만 존재할 새 파일 생성
@'
이 파일은 practice/branch-switch 브랜치에서 만들었습니다.
'@ | Set-Content -Encoding utf8 branch-only.txt

# 삭제 연습용 파일만 명시적으로 삭제
Remove-Item -LiteralPath 'shared-note.txt'

# 추가와 삭제 상태 확인
git status
git diff
```

여기서 학생에게 두 변경을 말하게 합니다.

```text
branch-only.txt  → Untracked, 새 파일
shared-note.txt  → deleted, 추적 파일 삭제
```

커밋합니다.

```powershell
# 추가 파일과 삭제 파일만 stage
git add -- branch-only.txt shared-note.txt
git diff --staged

# 현재 브랜치 이력에 기록
git commit -m "Practice file changes on branch"
git status
```

> 파일을 삭제했는데 다시 살릴 수 있는 이유는 삭제도 해당 브랜치의 커밋에 기록된 변경이기 때문입니다. `main`이 가리키는 이전 커밋에는 원래 파일이 남아 있습니다.

## 4. 로컬 브랜치를 GitHub에 Push

```powershell
# 같은 이름의 원격 브랜치를 만들고 upstream 연결
git push -u origin practice/branch-switch

# 로컬과 원격 추적 관계 확인
git branch -vv
git branch --all
```

GitHub 웹의 브랜치 선택 메뉴에서 다음을 비교합니다.

| GitHub에서 선택한 브랜치 | `shared-note.txt` | `branch-only.txt` |
|---|---:|---:|
| `main` | 있음 | 없음 |
| `practice/branch-switch` | 없음 | 있음 |

강사 포인트: push하기 전에는 GitHub 브랜치 목록에 이 브랜치가 없었고, push 후 `origin/practice/branch-switch`가 생겼습니다.

## 5. main으로 이동하며 파일 변화 관찰

학생에게 VS Code 파일 탐색기에서 눈을 떼지 말라고 안내한 뒤 실행합니다.

```powershell
# 변경을 커밋했으므로 안전하게 main으로 이동
git switch main

# 현재 브랜치와 파일 존재 여부 확인
git branch --show-current
Test-Path branch-only.txt
Test-Path shared-note.txt
```

예상 결과:

```text
branch-only.txt  → False
shared-note.txt  → True
```

강사 멘트:

> “파일이 삭제되거나 복구되는 마술이 아니라, 하나의 작업 폴더가 현재 브랜치가 가리키는 커밋 모습으로 바뀐 것입니다. `main`은 브랜치 작업을 아직 합치지 않았기 때문에 안전합니다.”

## 6. 다시 작업 브랜치로 이동

```powershell
# 직전에 작업했던 브랜치로 이동
git switch practice/branch-switch

# 반대 상태가 나타나는지 확인
Test-Path branch-only.txt
Test-Path shared-note.txt
Get-Content branch-only.txt
```

예상 결과:

```text
branch-only.txt  → True
shared-note.txt  → False
```

직전 브랜치로 빠르게 오가는 명령도 보여 줄 수 있습니다.

```powershell
# 직전에 있던 main으로 전환
git switch -

# 다시 직전 브랜치로 전환
git switch -
```

## 7. 커밋 그래프로 브랜치 이해하기

```powershell
# 로컬·원격 브랜치와 커밋 관계 시각화
git log --oneline --graph --decorate --all -10
```

개념 그림:

```text
A---B  main, origin/main
     \
      C  practice/branch-switch, origin/practice/branch-switch
```

`main`과 작업 브랜치가 서로 다른 폴더가 아니라, 서로 다른 커밋을 가리키는 이름임을 다시 강조합니다.

## 8. 일부러 커밋하지 않고 전환 시도하기—선택 실습

시간이 있으면 작업 브랜치에서 `branch-only.txt`를 수정하되 커밋하지 않고 `main`으로 전환을 시도합니다.

```powershell
# 커밋하지 않은 변경 생성
Add-Content -Encoding utf8 branch-only.txt '아직 커밋하지 않은 문장'
git status

# 다른 브랜치와 겹치는 변경이면 Git이 전환을 거부할 수 있음
git switch main
```

Git이 전환을 허용할 수도 있고 변경 손실 가능성이 있으면 거부할 수도 있습니다. 핵심은 “항상 거부한다”가 아니라 **전환 전 `git status`로 작업을 정리해야 한다**는 점입니다.

다음 차시를 위해 변경을 현재 작업 브랜치에 커밋합니다.

```powershell
# main으로 전환되었다면 작업 브랜치로 돌아옴
git switch practice/branch-switch

# 선택 실습 변경이 있다면 확인 후 커밋·push
git diff
git add branch-only.txt
git commit -m "Add branch switch observation"
git push
```

선택 실습을 생략했거나 변경이 없다면 commit 명령은 실행하지 않습니다.

## 9. 자주 발생하는 오류

| 현상 | 확인 | 강사용 안내 |
|---|---|---|
| `branch already exists` | `git branch` | 기존 브랜치로 `git switch practice/branch-switch`하거나 학생별 새 이름 사용 |
| 브랜치 전환 거부 | `git status` | 변경을 커밋하거나 명확한 이름으로 stash한 뒤 전환 |
| GitHub에 브랜치가 없음 | `git branch -vv` | 로컬 commit 여부 확인 후 `git push -u origin <브랜치>` |
| 파일이 예상과 다름 | `git branch --show-current` | 현재 브랜치가 맞는지 먼저 확인 |

## 10. 종료 질문

1. 브랜치를 만들자마자 파일이 같은 이유는 무엇인가?
2. 브랜치에서 삭제한 파일이 main에서 다시 보이는 이유는 무엇인가?
3. 로컬 브랜치가 생기면 원격 브랜치도 자동으로 생기는가?
4. `git switch -c`에서 `-c`는 무엇을 뜻하는가?
5. 현재 브랜치를 확인하는 명령은 무엇인가?

다음 차시를 위해 `practice/branch-switch` 브랜치와 원격 브랜치를 삭제하지 않고 유지합니다.

이전: [Commit·Push·Pull·Clone 실습](./01_Commit_Push_Pull_Clone_실습.md) · 다음: [Merge와 Pull Request 실습](./03_Merge와_Pull_Request_실습.md)
