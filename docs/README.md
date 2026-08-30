# 문서 안내

이 폴더는 프로젝트에 추가되는 여러 종류의 문서를 분류해서 관리하는 공간입니다.

## 문서 분류

| 분류 | 내용 | 바로가기 |
|---|---|---|
| `lec` | `sam` 폴더의 lec01~lec11 Notebook을 풀어서 설명한 초보자용 수업 자료 | [강의 학습 목차](./lec/README.md) |
| `git-github-guide` | Windows PowerShell로 배우는 Git·GitHub 개념, 실습, 브랜치와 협업 가이드 | [Git & GitHub 초보자 가이드북](./git-github-guide/README.md) |

나중에 프로젝트, 데이터베이스, 웹 개발 같은 자료가 생기면 `docs/project`, `docs/database`, `docs/web`처럼 별도 하위 폴더를 추가하면 됩니다.

## 처음 학습하는 분께

다음 순서로 시작하세요.

1. [왕초보 시작하기](./lec/START_HERE.md)
2. [쉬운 용어사전](./lec/용어사전.md)
3. [강의 전체 목차](./lec/README.md)
4. [lec01 - DataFrame 기초](./lec/lec01_DataFrame_기초.md)

환경 설치가 필요하면 [설치 가이드](./lec/INSTALL.md)를 먼저 확인합니다.

Git과 GitHub를 처음 배운다면 [Git & GitHub 초보자 가이드북](./git-github-guide/README.md)을 개념부터 순서대로 진행하세요.

## 관리 원칙

- 강의 문서, 강의용 그림, 설치 파일은 `docs/lec` 안에서 함께 관리합니다.
- 각 분류에는 진입점 역할을 하는 `README.md`를 둡니다.
- Notebook 원본은 `sam`에 두고, 문서에서는 상대 경로 링크로 연결합니다.
- Jupyter 자동 체크포인트는 학습 자료나 Git 관리 대상에 포함하지 않습니다.
