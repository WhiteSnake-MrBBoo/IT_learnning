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

### 방법 A: winget(Windows Package Manager)  사용 - 윈도우패키지관리프로그램

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
6. 2FA 설정 중 발급되는 복구 코드는 다른 사람이 볼 수 없는 안전한 장소에 보관합니다.

GitHub 공식 문서도 개인 계정 생성 후 이메일 인증과 **2FA(2단계 인증)** 설정을 권장합니다.

GitHub의 메뉴와 버튼은 영어로 표시되는 경우가 많습니다. 영어 단어를 전부 외우려고 하기보다 **메뉴 이름 → 역할 → 언제 사용하는지**를 연결해서 익히세요.

- [GitHub 계정 만들기](https://docs.github.com/en/account-and-profile/how-tos/account-management/creating-an-account-on-github)

## 5. GitHub 개인 Settings 메뉴 이해하기

오른쪽 위 프로필 사진을 누르고 **Settings(설정)**를 선택합니다. 화면 폭이 좁으면 먼저 **Menu(메뉴)** 버튼을 눌러야 왼쪽 설정 목록이 보일 수 있습니다.

![GitHub 개인 설정 메뉴에서 Password and authentication을 선택한 화면](./assets/github-account-settings-menu.png)

> 위 이미지는 예시 계정 화면입니다. 계정 종류, 요금제, 조직 가입 여부와 GitHub 화면 업데이트에 따라 항목 이름이나 순서가 조금 달라질 수 있습니다.

| 영문 메뉴 | 쉬운 한국어 뜻 | 초보자가 알아야 할 역할 |
|---|---|---|
| **Public profile** | 공개 프로필 | 이름, 소개, 프로필 사진, 회사, 위치처럼 다른 사람에게 보이는 정보를 설정합니다. 주소·전화번호 같은 민감한 정보는 적지 않습니다. |
| **Account** | 계정 | 사용자명 변경, 계정 관련 기본 작업을 관리합니다. 사용자명을 바꾸면 저장소 주소와 기존 링크에 영향이 있을 수 있으므로 신중히 변경합니다. |
| **Appearance** | 화면 모양 | 밝은/어두운 테마와 표시 방식을 선택합니다. 코드 내용이나 저장소에는 영향을 주지 않습니다. |
| **Accessibility** | 접근성 | 키보드 사용, 애니메이션, 링크 밑줄 등 화면 사용 편의 기능을 조정합니다. |
| **Notifications** | 알림 | Issue, Pull Request, 리뷰, Actions 등의 웹·이메일 알림 방식을 정합니다. 처음에는 기본값을 사용하고 알림이 너무 많을 때 조정해도 됩니다. |
| **Billing and licensing** | 결제와 라이선스 | 요금제, 사용량, 결제 수단을 확인합니다. 무료 기능만 사용할 때도 유료 전환 여부를 확인할 수 있습니다. |
| **Emails** | 이메일 | 이메일 추가·인증, 기본 이메일, 공개 여부와 GitHub `noreply` 이메일을 관리합니다. 커밋 기여 내역 연결과 관련이 있습니다. |
| **Password and authentication** | 비밀번호와 인증 | 비밀번호, passkey, 2FA, 복구 수단 등 로그인 보안을 설정합니다. 이 장에서 가장 먼저 확인할 보안 메뉴입니다. |
| **Sessions** | 로그인 세션 | 현재 로그인된 브라우저와 기기를 확인하고 모르는 세션을 종료합니다. 공용 PC 사용 후 점검합니다. |
| **SSH and GPG keys** | SSH·GPG 키 | SSH로 GitHub에 연결하거나 서명된 커밋을 검증할 때 공개 키를 등록합니다. 첫 HTTPS 실습에서는 건드리지 않아도 됩니다. |
| **Credentials** | 자격 증명 | 계정에 연결된 인증 정보와 자격 증명을 확인합니다. 정확히 모르는 항목은 삭제하지 않습니다. |
| **Organizations** | 조직 | 소속된 GitHub Organization과 관련 설정을 확인합니다. 회사·팀·수업 단위 협업에서 사용합니다. |
| **Enterprises** | 엔터프라이즈 | 기업 전체 GitHub 환경과 관련된 항목입니다. 개인 학습자는 보통 사용할 일이 없습니다. |
| **Moderation** | 사용자 관리 | 차단한 사용자와 상호 작용 제한 같은 커뮤니티 관리 기능을 다룹니다. |

초보자가 먼저 확인할 순서는 다음과 같습니다.

```text
Emails에서 이메일 인증 확인
  → Password and authentication에서 2FA 설정
  → Sessions에서 모르는 로그인 확인
  → Notifications에서 필요한 알림 조정
```

## 6. 2차 인증(2FA)과 모바일 연동

### 6-1. 2FA는 무엇인가요?

**Two-factor authentication(2FA)**은 비밀번호 외에 내가 가진 인증 앱, 휴대폰, passkey 또는 보안 키 같은 두 번째 증거를 한 번 더 확인하는 로그인 보안 방식입니다.

```text
1차 인증: 내가 아는 것       → 비밀번호
2차 인증: 내가 가진 것 등   → 일회용 코드, GitHub Mobile 승인, passkey, 보안 키
```

비밀번호가 유출되더라도 두 번째 인증 수단이 없으면 다른 사람이 바로 로그인하기 어렵게 만듭니다.

GitHub는 2023년 3월부터 GitHub.com에서 코드를 기여하는 사용자를 대상으로 하나 이상의 2FA 방식 설정을 의무화해 왔습니다. 실제 계정이 의무 설정 대상이 되면 이메일과 GitHub 화면의 안내 배너로 등록 기간을 알려 줍니다. 아직 안내를 받지 않았더라도 학습·개발 계정은 2FA를 설정하는 것을 권장합니다.

- [2FA 기본 개념과 의무화 안내](https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa/about-two-factor-authentication)
- [의무 2FA 상세 안내](https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa/about-mandatory-two-factor-authentication)

### 6-2. 휴대폰 앱 연동이 반드시 필요한가요?

정확히 구분하면 다음과 같습니다.

- **2FA 설정**: 코드를 기여하는 계정에는 의무화될 수 있으며, 모든 개발 계정에 강력히 권장됩니다.
- **특정 모바일 앱 설치**: 필수는 아닙니다. GitHub가 지정한 앱 하나만 사용해야 하는 것도 아닙니다.
- **권장 기본 방식**: GitHub는 시간 기반 일회용 비밀번호를 만드는 **TOTP 인증 앱**을 기본 2FA 방식으로 권장합니다.
- **GitHub Mobile**: 기본 2FA를 설정한 뒤 로그인 승인 알림을 받는 추가 방식으로 사용할 수 있습니다.
- **추가 백업 방식**: passkey, 물리 보안 키 등을 함께 등록하면 휴대폰 분실로 계정이 잠길 위험을 줄일 수 있습니다.

스마트폰을 사용할 수 없다면 RFC 6238 방식과 호환되는 데스크톱 TOTP 앱도 사용할 수 있습니다. SMS가 제공되는 지역도 있지만 보안성과 복구 가능성을 고려하면 TOTP 앱과 별도 백업 수단의 조합을 우선 검토하세요.

### 6-3. 설정 화면으로 이동하기

아래 화면은 **Settings → Password and authentication → Sign in methods(로그인 수단)** 영역의 위쪽입니다.

![GitHub Password and authentication의 Sign in methods 화면](./assets/github-account-sign-in-methods.png)

화면에 보이는 항목의 뜻은 다음과 같습니다.

| 화면 항목 | 뜻 |
|---|---|
| **Email** | 로그인·알림·계정 복구에 사용하는 인증된 이메일을 관리합니다. |
| **Password** | 계정 비밀번호를 변경합니다. 다른 사이트와 같은 비밀번호를 재사용하지 않습니다. |
| **Passkeys** | 기기의 생체 인식, 화면 잠금 또는 보안 키를 이용하는 로그인 수단입니다. |
| **Google / Apple** | 해당 계정과 연결해 로그인할 수 있는 선택 기능입니다. 2FA 복구 코드를 대신하지는 않습니다. |

이 화면에서 **조금 더 아래로 스크롤**하면 **Two-factor authentication(2FA)** 섹션이 나옵니다.

```text
프로필 사진
  → Settings
  → Password and authentication
  → 아래로 스크롤
  → Two-factor authentication
  → Enable two-factor authentication
```

### 6-4. TOTP 인증 앱으로 설정하기—권장

TOTP는 **Time-based One-Time Password(시간 기반 일회용 비밀번호)**의 줄임말입니다. 인증 앱이 일정 시간마다 새로운 6자리 코드를 만듭니다.

1. 스마트폰에 TOTP 호환 인증 앱을 설치합니다. 예: Google Authenticator, Microsoft Authenticator, Authy 또는 비밀번호 관리자의 TOTP 기능.
2. GitHub의 **Enable two-factor authentication**을 누릅니다.
3. GitHub가 보여 주는 QR 코드를 인증 앱으로 스캔합니다.
4. 인증 앱에 표시된 6자리 코드를 GitHub 입력란에 넣어 확인합니다.
5. GitHub가 제공하는 **Recovery codes(복구 코드)**를 다운로드합니다.
6. 복구 코드를 안전하게 보관한 뒤 저장 완료 버튼을 눌러 설정을 마칩니다.
7. 로그아웃하기 전에 추가 인증 수단을 하나 더 등록하는 것을 권장합니다.

> **보안 주의:** QR 코드, 수동 설정 키, 6자리 인증 코드, 복구 코드는 비밀번호와 같은 비밀 정보입니다. 스크린샷을 찍어 공유하거나 Git 저장소·README·클라우드 공개 폴더에 올리지 마세요.

QR 코드를 스캔할 수 없다면 화면의 **setup key(설정 키)**를 인증 앱에 직접 입력할 수 있습니다. 설정 키도 다른 사람에게 보여 주면 안 됩니다.

공식 절차: [TOTP 앱으로 2FA 설정하기](https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa/configuring-two-factor-authentication#configuring-two-factor-authentication-using-a-totp-app)

### 6-5. GitHub Mobile을 추가 인증 수단으로 사용하기

GitHub Mobile은 PC에서 로그인할 때 스마트폰으로 온 알림을 열어 **Approve(승인)** 또는 **Reject(거부)**를 선택하는 방식입니다.

1. 먼저 TOTP 앱 또는 GitHub가 안내하는 기본 방식으로 2FA를 활성화합니다.
2. 스마트폰의 공식 앱 스토어에서 **GitHub Mobile**을 설치합니다.
3. 같은 GitHub 계정으로 로그인합니다.
4. GitHub의 **Password and authentication**에서 GitHub Mobile을 추가 2FA 방식으로 구성합니다.
5. 시험 로그인을 하여 내 기기의 요청만 승인되는지 확인합니다.

내가 시도하지 않은 로그인 알림은 승인하지 말고 **Reject**를 선택한 뒤 비밀번호와 활성 세션을 점검합니다.

공식 절차: [GitHub Mobile로 2FA 구성하기](https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa/configuring-two-factor-authentication#configuring-two-factor-authentication-using-github-mobile)

### 6-6. 복구 코드가 중요한 이유

휴대폰을 잃어버리거나 인증 앱을 삭제하면 복구 코드가 계정 접근을 되찾는 핵심 수단이 됩니다. GitHub Support가 본인 확인만으로 2FA 보호를 임의로 해제해 줄 것이라고 기대하면 안 됩니다.

권장 보관 방법:

- 비밀번호 관리자처럼 암호화된 안전한 저장소에 보관합니다.
- 휴대폰과 분리된 안전한 위치에 두 번째 사본을 보관합니다.
- 메신저, 이메일 본문, Git 저장소, 코드 파일에는 붙여 넣지 않습니다.
- 사용하거나 노출된 복구 코드는 GitHub에서 새로 발급해 교체합니다.

공식 참고: [2FA 복구 방법 구성](https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa/configuring-two-factor-authentication-recovery-methods)

### 6-7. 2FA 완료 점검

- [ ] TOTP 등 기본 2FA 방식이 활성화되어 있다.
- [ ] 로그아웃 후 다시 로그인해 6자리 코드 또는 승인 요청을 시험했다.
- [ ] 복구 코드를 다운로드해 안전한 별도 장소에 보관했다.
- [ ] 가능하면 GitHub Mobile, passkey 또는 보안 키 같은 백업 수단을 추가했다.
- [ ] QR 코드·설정 키·복구 코드가 저장소나 캡처 이미지에 노출되지 않았다.

## 7. Git과 GitHub 인증 방식 이해하기

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

## 8. 선택 사항: GitHub CLI 설치

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

## 9. 준비 완료 점검

아래 항목이 모두 맞으면 다음 실습으로 이동합니다.

- [ ] PowerShell에서 `git --version`이 성공한다.
- [ ] `user.name`이 내 이름으로 나온다.
- [ ] `user.email`이 GitHub에 등록한 이메일 또는 `noreply` 이메일이다.
- [ ] 기본 브랜치 이름이 `main`이다.
- [ ] GitHub 가입과 이메일 인증을 완료했다.
- [ ] 2FA를 활성화하고 실제 로그인을 시험했다.
- [ ] 2FA 복구 코드와 추가 인증 수단을 안전하게 준비했다.

이전: [핵심 개념과 용어사전](./01_핵심개념과_용어사전.md) · 다음: [로컬에서 GitHub까지 첫 실습](./03_로컬에서_GitHub까지_첫_실습.md)
