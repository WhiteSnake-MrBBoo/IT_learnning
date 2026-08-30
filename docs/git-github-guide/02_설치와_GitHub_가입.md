# 02. Windows 설치와 GitHub 가입

이 장에서는 Windows에 Git을 설치하고, PowerShell에서 사용자 정보를 설정한 뒤 GitHub 계정을 준비합니다.

## 1. PowerShell 열기

시작 메뉴에서 **PowerShell** 또는 **Windows Terminal**을 검색해 실행합니다. 관리자 권한은 일반적으로 필요하지 않습니다.

현재 PowerShell 버전을 확인합니다.

```powershell
$PSVersionTable.PSVersion
```

이 가이드의 명령은 Windows PowerShell 5.1과 PowerShell 7에서 사용할 수 있도록 작성했습니다.

## 2. Git 설치

### 방법 A: winget 사용

`winget`을 사용할 수 있다면 PowerShell에서 실행합니다.

```powershell
winget install --id Git.Git -e --source winget
```

설치가 끝나면 열려 있던 PowerShell을 모두 닫고 새로 엽니다.

### 방법 B: 공식 설치 파일 사용

1. [Git for Windows 공식 다운로드](https://git-scm.com/install/windows)에 접속합니다.
2. 자신의 Windows에 맞는 설치 파일을 내려받아 실행합니다.
3. 특별한 팀 규칙이 없다면 기본 선택값으로 설치합니다.
4. 설치 후 PowerShell을 새로 엽니다.

설치를 확인합니다.

```powershell
git --version
```

`git version 2.x.x`처럼 나오면 성공입니다. “`git` 용어를 인식하지 못했습니다”가 나오면 [문제 해결 문서](./07_문제해결과_안전수칙.md)를 확인하세요.

## 3. Git 사용자 정보 설정

아래 이름과 이메일을 자신의 정보로 바꿔 실행합니다. 이 정보는 커밋 작성자 표시에 사용되며 GitHub 로그인 자체를 대신하지 않습니다.

```powershell
git config --global user.name "Hong Gildong"
git config --global user.email "gildong@example.com"
git config --global init.defaultBranch main
```

설정을 확인합니다.

```powershell
git config --global --get user.name
git config --global --get user.email
git config --global --get init.defaultBranch
```

### 어떤 이메일을 써야 하나요?

- GitHub 기여 내역에 커밋을 연결하려면 GitHub 계정에 등록·인증된 이메일을 사용합니다.
- 실제 이메일을 커밋에 공개하고 싶지 않다면 GitHub의 **Settings → Emails**에서 제공하는 `noreply` 이메일을 사용할 수 있습니다.
- 회사나 수업 저장소에서는 조직의 이메일 정책을 먼저 확인합니다.

설정이 잘못되었다면 같은 명령을 올바른 값으로 다시 실행하면 덮어씁니다.

```powershell
git config --global user.name "올바른 이름"
git config --global user.email "올바른 이메일"
```

## 4. GitHub 가입

1. [GitHub 가입 페이지](https://github.com/signup)를 엽니다.
2. 이메일, 비밀번호, 사용자명 등을 화면 안내에 따라 입력합니다. Google 또는 Apple 로그인이 제공될 수도 있습니다.
3. 받은 이메일의 링크나 인증 코드를 사용해 **이메일 인증**을 완료합니다.
4. 처음에는 무료 개인 계정으로 충분합니다. 필요할 때 나중에 요금제를 바꿀 수 있습니다.
5. 프로필의 **Settings → Password and authentication**에서 2단계 인증(2FA)을 설정합니다.
6. 2FA 복구 코드는 다른 사람이 볼 수 없는 안전한 장소에 보관합니다.

GitHub 공식 문서도 개인 계정 생성 후 이메일 인증과 2FA 설정을 권장합니다.

- [GitHub 계정 만들기](https://docs.github.com/en/account-and-profile/how-tos/account-management/creating-an-account-on-github)
- [2단계 인증 설정](https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa/configuring-two-factor-authentication)

## 5. Git과 GitHub 인증 방식 이해하기

`user.name`과 `user.email`은 커밋의 작성자 정보이고, **GitHub에 접속할 권한을 증명하는 로그인 정보가 아닙니다.** 다음 실습은 초보자에게 비교적 간단한 HTTPS 방식을 사용합니다.

```text
커밋 작성자 표시: git config의 user.name / user.email
GitHub 접속 인증: 브라우저 로그인, Git Credential Manager, 토큰 또는 SSH 키
```

Git for Windows의 일반적인 설치 구성에서는 자격 증명 관리 도구가 HTTPS 로그인을 도와줍니다. 첫 `git push` 때 브라우저 로그인 창이 열리면 GitHub에 로그인하고 접근을 승인합니다.

주의할 점:

- GitHub 계정 비밀번호를 Git 명령줄의 password 칸에 직접 넣는 방식은 사용하지 않습니다.
- 브라우저 로그인이 제공되지 않는 환경에서는 Personal Access Token 또는 SSH를 사용할 수 있지만, 첫 실습에서는 필요하지 않습니다.
- 토큰, 비밀번호, SSH 개인 키는 파일에 적어 커밋하면 안 됩니다.

공식 참고: [GitHub 인증 안내](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/about-authentication-to-github)

## 6. 선택 사항: GitHub CLI 설치

GitHub CLI의 `gh` 명령을 쓰고 싶은 경우에만 설치합니다. 이 가이드의 필수 조건은 아닙니다.

```powershell
winget install --id GitHub.cli
```

PowerShell을 새로 연 뒤 로그인합니다.

```powershell
gh --version
gh auth login
```

화면에서 일반적으로 `GitHub.com → HTTPS → Login with a web browser` 순서로 선택할 수 있습니다. 선택 문구는 버전에 따라 달라질 수 있습니다.

## 7. 준비 완료 점검

아래 항목이 모두 맞으면 다음 실습으로 이동합니다.

- [ ] PowerShell에서 `git --version`이 성공한다.
- [ ] `user.name`이 내 이름으로 나온다.
- [ ] `user.email`이 GitHub에 등록한 이메일 또는 `noreply` 이메일이다.
- [ ] 기본 브랜치 이름이 `main`이다.
- [ ] GitHub 가입과 이메일 인증을 완료했다.
- [ ] 가능하면 2FA와 복구 코드 보관까지 완료했다.

이전: [핵심 개념과 용어사전](./01_핵심개념과_용어사전.md) · 다음: [로컬에서 GitHub까지 첫 실습](./03_로컬에서_GitHub까지_첫_실습.md)
