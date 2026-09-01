# 5차시. Submodule 단계별 실습

## 수업 개요

- 권장 시간: 90~120분
- 선수 학습: 저장소, clone, commit, push, pull, branch 개념
- 준비물: 서로 다른 GitHub 저장소 2개와 접근 권한
- 완료 결과: 자식 저장소를 부모 저장소에 submodule로 추가하고, 재귀 clone과 자식 업데이트·부모 포인터 업데이트 순서를 실습합니다.

## 학습 목표

- 일반 폴더와 submodule의 차이를 설명합니다.
- `.gitmodules`와 `160000` gitlink의 역할을 확인합니다.
- 부모가 자식 파일 전체가 아니라 **자식의 특정 커밋 ID**를 기록한다는 사실을 설명합니다.
- 자식 `commit → push` 후 부모 포인터 `commit → push` 순서를 지킵니다.
- `clone --recurse-submodules`와 `submodule update --init --recursive`를 사용합니다.

## 0. GitHub 저장소 두 개 준비

GitHub에서 다음 두 저장소를 만듭니다.

| 저장소 | 역할 | 생성 옵션 |
|---|---|---|
| `git-class-parent` | 부모 프로젝트 | **Add README: On** |
| `git-class-module` | 독립 자식 프로젝트 | **Add README: On** |

두 저장소 모두 최소 한 개의 커밋이 필요합니다. 완전히 빈 자식 저장소는 checkout할 기본 커밋이 없어 `git submodule add` 실습이 실패할 수 있습니다.

공개 범위는 둘 다 Private 또는 둘 다 Public으로 맞추면 권한 설명이 단순합니다. Private 저장소라면 학생 계정이 부모와 자식 각각에 접근할 수 있어야 합니다.

학생별 URL 예시:

```text
https://github.com/내-사용자명/git-class-parent.git
https://github.com/내-사용자명/git-class-module.git
```

## 1. Submodule을 쓰는 이유부터 설명

```text
git-class-parent 저장소
└─ modules/class-note  ─────> git-class-module 저장소의 특정 커밋
```

부모와 자식은 다음 항목을 각각 따로 가집니다.

- Git 커밋 이력
- 브랜치와 태그
- GitHub Issue와 Pull Request
- 접근 권한
- Release와 Actions

Submodule은 여러 프로젝트 파일을 그냥 한 폴더에 모으는 기능이 아닙니다. **독립 저장소의 정확한 버전을 부모 프로젝트가 고정**해야 할 때 사용합니다.

강사 질문:

> “자식 저장소의 main이 새 커밋으로 이동하면 부모도 자동으로 그 최신 버전을 사용하게 될까요?”

기대 답변: 아니요. 부모가 기록한 자식 커밋 포인터를 새로 커밋해야 합니다.

## 2. 부모 저장소 Clone

```powershell
# 수업 전용 루트 준비
$classRoot = Join-Path ([Environment]::GetFolderPath('MyDocuments')) 'git-class-practice'
New-Item -ItemType Directory -Path $classRoot -Force
Set-Location $classRoot

# 반드시 자신의 GitHub 주소로 변경
$parentUrl = 'https://github.com/내-사용자명/git-class-parent.git'
$moduleUrl = 'https://github.com/내-사용자명/git-class-module.git'

# 부모 저장소를 로컬에 복제
git clone $parentUrl 'git-class-parent'
Set-Location 'git-class-parent'

# 부모 저장소 상태 확인
git status
git remote -v
git log --oneline --decorate -3
```

기존에 같은 폴더가 있으면 다른 이름을 사용합니다. 기존 폴더를 무작정 삭제하지 않습니다.

## 3. 자식 저장소를 Submodule로 추가

```powershell
# 부모 저장소의 상태가 깨끗한지 먼저 확인
git status

# 자식 저장소를 modules/class-note 경로에 submodule로 등록
git submodule add $moduleUrl 'modules/class-note'
```

등록 후 바로 확인합니다.

```powershell
# 부모에 생긴 stage 변경 확인
git status

# submodule URL과 경로 설정 확인
Get-Content .gitmodules

# 자식이 어떤 커밋을 가리키는지 확인
git submodule status

# 부모의 stage에서 submodule 경로가 gitlink인지 확인
git ls-files --stage 'modules/class-note'

# submodule 차이를 읽기 좋은 형식으로 확인
git diff --cached --submodule
```

`git ls-files --stage` 결과의 모드가 `160000`이면 일반 파일·폴더 내용이 아니라 자식 커밋을 가리키는 **gitlink**가 기록된 것입니다.

`.gitmodules`의 대표 내용:

```ini
[submodule "modules/class-note"]
	path = modules/class-note
	url = https://github.com/내-사용자명/git-class-module.git
```

## 4. 부모 저장소에 Submodule 등록 기록

`git submodule add`는 보통 `.gitmodules`와 gitlink를 stage합니다. 커밋 전 정확한 두 항목만 포함됐는지 확인합니다.

```powershell
# stage된 변경 다시 확인
git status
git diff --cached --submodule

# 부모 저장소에 submodule 등록 기록
git commit -m "Add class-note submodule"

# 부모 GitHub 저장소에 push
git push origin main
```

GitHub 부모 저장소에서 확인할 내용:

- `.gitmodules` 파일이 보입니다.
- `modules/class-note`가 일반 폴더와 다른 화살표 형태로 보일 수 있습니다.
- 경로 옆에 자식 커밋 ID가 표시될 수 있습니다.
- 클릭하면 별도의 `git-class-module` 저장소로 이동합니다.

강사 멘트:

> “부모 커밋에는 자식 README 내용 자체가 복사된 것이 아니라, 자식의 이 커밋을 사용하라는 주소표가 들어갔습니다.”

## 5. 재귀 Clone 실습

부모 저장소 밖으로 이동해 새 복제본을 만듭니다.

```powershell
# 수업 루트로 이동
Set-Location $classRoot

# 부모와 등록된 모든 자식 저장소를 함께 clone
git clone --recurse-submodules $parentUrl 'git-class-parent-copy'

# 새 복제본으로 이동해 상태 확인
Set-Location 'git-class-parent-copy'
git status
git submodule status --recursive
Get-Content 'modules/class-note/README.md'
```

### 부모만 Clone한 경우

`--recurse-submodules`를 빼고 clone하면 submodule 폴더가 비어 있거나 초기화되지 않은 것처럼 보일 수 있습니다. 이때 다음 명령을 사용합니다.

```powershell
# 이미 clone한 부모에서 submodule 초기화와 지정 커밋 checkout
git submodule update --init --recursive

# 부모가 기록한 자식 커밋과 일치하는지 확인
git submodule status --recursive
```

`update --init --recursive`는 자식의 무조건 최신 `main`을 받는 명령이 아니라 **부모가 기록한 커밋**으로 맞추는 명령입니다.

## 6. 자식 저장소 수정

처음 clone한 부모 작업 폴더로 돌아갑니다.

```powershell
# 원래 부모 작업 폴더로 이동
Set-Location (Join-Path $classRoot 'git-class-parent')

# 부모와 자식 상태를 각각 확인
git status
git -C 'modules/class-note' status
git -C 'modules/class-note' branch --show-current
```

Submodule은 update 후 detached HEAD일 수 있습니다. 자식 저장소에 새 커밋을 만들기 전에는 실제 작업 브랜치로 이동합니다.

```powershell
# 자식 저장소에서 main 브랜치로 이동하고 최신화
git -C 'modules/class-note' switch main
git -C 'modules/class-note' pull --ff-only origin main
```

자식 README를 수정합니다.

```powershell
# 자식 저장소 파일에 학습 문장 추가
Add-Content -Encoding utf8 'modules/class-note/README.md' "`nSubmodule 수업에서 추가한 문장입니다."

# 자식 저장소 기준으로 변경 확인
git -C 'modules/class-note' status
git -C 'modules/class-note' diff
```

## 7. 자식 Commit과 Push를 먼저 수행

```powershell
# 자식 저장소에서 README만 stage
git -C 'modules/class-note' add README.md
git -C 'modules/class-note' diff --staged

# 자식 저장소의 독립 이력에 commit
git -C 'modules/class-note' commit -m "Update module class note"

# 새 자식 커밋을 자식 GitHub 저장소에 먼저 push
git -C 'modules/class-note' push origin main
```

자식 push를 먼저 하는 이유:

```text
부모가 새 자식 커밋 ID를 기록했는데
그 자식 커밋이 GitHub에 push되지 않았다면
다른 학생은 부모가 요구하는 자식 커밋을 내려받을 수 없음
```

## 8. 부모가 새 자식 커밋 포인터를 기록

현재 PowerShell 위치는 부모 저장소입니다. 부모 기준 상태를 확인합니다.

```powershell
# 부모는 submodule 경로가 새 커밋을 가리킨다고 표시
git status
git diff --submodule
git submodule status
```

부모에 포인터 변경을 기록하고 push합니다.

```powershell
# submodule 경로의 새 커밋 포인터만 stage
git add 'modules/class-note'
git diff --staged --submodule

# 부모 저장소 이력에 자식 버전 변경 기록
git commit -m "Update class-note submodule revision"

# 부모 GitHub 저장소에 push
git push origin main
```

전체 순서를 학생이 소리 내어 읽게 합니다.

```text
자식 수정
  → 자식 add
  → 자식 commit
  → 자식 push
  → 부모에서 포인터 변경 확인
  → 부모 add
  → 부모 commit
  → 부모 push
```

## 9. 다른 복제본에서 새 자식 버전 받기

앞에서 만든 `git-class-parent-copy`는 아직 이전 부모 커밋과 이전 자식 커밋을 가리킵니다.

```powershell
# 두 번째 부모 복제본으로 이동
Set-Location (Join-Path $classRoot 'git-class-parent-copy')

# 부모의 최신 커밋을 받음
git pull --ff-only origin main

# 부모가 새로 지정한 자식 커밋으로 맞춤
git submodule update --init --recursive

# 상태와 실제 내용 확인
git submodule status --recursive
Get-Content 'modules/class-note/README.md'
```

이제 `Submodule 수업에서 추가한 문장입니다.`가 보이면 전체 흐름이 성공했습니다.

## 10. Submodule 상태 읽기

```powershell
git submodule status --recursive
```

커밋 ID 앞 문자의 대표 의미:

| 표시 | 의미 | 강사용 확인 방향 |
|---|---|---|
| 공백 | 부모가 기록한 커밋과 일치 | 정상 |
| `-` | 아직 초기화되지 않음 | `git submodule update --init --recursive` |
| `+` | 자식 현재 커밋이 부모 기록과 다름 | 자식 변경·checkout·부모 포인터 상태 확인 |
| `U` | submodule 커밋 충돌 | 부모 브랜치 병합 상태와 선택할 자식 커밋 확인 |

추가 진단:

```powershell
# 부모 상태
git status
git diff --submodule

# 자식 상태와 최근 이력
git -C 'modules/class-note' status
git -C 'modules/class-note' log --oneline --decorate -5
```

## 11. 일반 폴더와 Submodule 비교

| 항목 | 일반 폴더 | Submodule |
|---|---|---|
| Git 이력 | 부모 저장소 이력에 포함 | 자식 저장소가 독립 이력 보유 |
| GitHub 저장소 | 부모 하나 | 부모·자식 각각 존재 |
| 부모가 기록하는 것 | 파일 내용 | 자식 저장소의 특정 커밋 ID |
| clone | 일반 clone으로 파일 포함 | 재귀 clone 또는 별도 update 필요 |
| commit·push | 부모에서 한 번 | 자식 먼저, 부모 포인터 다음 |
| 적합한 경우 | 항상 함께 수정·배포 | 독립 버전·권한·배포가 필요한 재사용 구성 요소 |

프로젝트 폴더를 보기 좋게 나누는 목적만으로 submodule을 사용하지 않습니다. 함께 수정·배포하는 수업 파일이라면 일반 폴더가 더 단순합니다.

## 12. 자주 발생하는 오류

### 자식 폴더가 비어 있음

```powershell
git submodule update --init --recursive
git submodule status --recursive
```

### Private 자식 저장소 접근 실패

- 브라우저에 로그인한 GitHub 계정이 맞는지 확인합니다.
- 그 계정이 부모뿐 아니라 자식 저장소에도 접근 가능한지 확인합니다.
- 원격 URL을 확인합니다.

```powershell
git -C 'modules/class-note' remote -v
```

### 자식에서 커밋했는데 부모 `status`에도 변경이 보임

정상입니다. 부모가 기록한 자식 커밋 ID와 현재 자식 커밋 ID가 달라졌다는 뜻입니다. 자식을 먼저 push한 뒤 부모 포인터를 커밋합니다.

### 자식이 detached HEAD임

구경하거나 부모 지정 버전을 사용할 때는 정상일 수 있습니다. 새 커밋을 만들려면 먼저 팀의 작업 브랜치로 이동합니다.

```powershell
git -C 'modules/class-note' switch main
git -C 'modules/class-note' pull --ff-only origin main
```

### 같은 경로에 `git submodule add`를 다시 실행함

이미 `.gitmodules`와 gitlink에 등록된 경로에는 다시 `add`하지 않습니다. `git status`, `Get-Content .gitmodules`, `git submodule status`로 현재 등록부터 확인합니다. 오류를 피하려고 `--force`를 사용하지 않습니다.

## 13. 종료 질문

1. 부모 저장소는 자식의 무엇을 기록하는가?
2. `.gitmodules`에는 어떤 정보가 들어 있는가?
3. `160000` 모드는 무엇을 뜻하는가?
4. 자식과 부모 중 어느 저장소를 먼저 push해야 하는가?
5. `submodule update --init --recursive`는 자식의 무조건 최신 main을 받는가?
6. 일반 폴더가 submodule보다 나은 상황은 무엇인가?

## 14. 공식 참고 자료

- [Git submodule 공식 문서](https://git-scm.com/docs/git-submodule)
- [Git submodule 내부 개념](https://git-scm.com/docs/gitsubmodules)
- [`.gitmodules` 공식 문서](https://git-scm.com/docs/gitmodules)
- [Pro Git: Submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules)

이전: [브랜치 분기 심화 실습](./04_브랜치_분기_심화_실습.md) · 학생용 참고: [저장소 구조와 Submodule 심화](../08_저장소_구조와_Submodule_심화.md)
