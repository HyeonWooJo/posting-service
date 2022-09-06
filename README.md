# 📎 목차

1. [Posting Service]
2. [요구사항 및 분석]
4. [기술 스택]
5. [API Endpoints]
6. [ERD]
7. [참조 문서]

<br>

---

# 1. Posting Service
- 비밀번호를 입력하여 포스팅 작성 및 수정을 할 수 있는 사이트
- 개발 기간: 2022.09.06 ~ 2022.09.07

<br>

---


# 2. 요구사항 및 분석

## 1) 게시글 포스팅

- 게시글 올리기
    - 제목과 본문으로 구성
    - 제목은 최대 20자, 본문은 200자로 제한
    - 제목과 본문 모두 이모지 포함
- 게시물 올릴 때 비밀번호 설정
    - 추후 본인이 작성한 게시물에 비밀번호 입력 후 수정, 삭제 가능
    - 회원가입, 로그인 없이 비밀번호만 일치하면 수정, 삭제 가능
    - 비밀번호는 데이터베이스에 저장
- 모든 사용자는 한 페이지 내에서 모든 게시물을 최신 글 순서로 확인 할 수 있어야 함

<br>

## 2) 게시글 리스트 조회

- 게시글의 개수가 많을 때, 사용자가 스크롤을 내릴 때마다 오랜된 글이 로드되는 API
    - 추가 로드는 20개 단위


<br>

---



# 3. 기술 스택
Language | Framwork | Database | HTTP | Tools
| :----------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------: | 
| <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> | <img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white"> | <img src="https://img.shields.io/badge/mysql-4479A1?style=for-the-badge&logo=mysql&logoColor=white"> | <img src="https://img.shields.io/badge/postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white"> | <img src="https://img.shields.io/badge/git-F05032?style=for-the-badge&logo=git&logoColor=white"> 


<br>

---

# 4. API Endpoints
| endpoint | HTTP Method | 기능   | require parameter                                                                                                   | response data |
|----------|-------------|------|---------------------------------------------------------------------------------------------------------------------|---------------|
| postings  | GET   | 게시글 리스트 조회 |  없음  | 게시글 리스트 |
| postings/detail  | POST     | 게시글 포스팅  | title: string <br/>context: string <br/> psword: string <br/> posting_id: string   | 게시글 포스팅 혹은 수정 성공 여부   |
| postings/detail  | DELETE   | 게시글 포스팅 삭제|  psword: string <br/> posting_id: string  | 게시글 삭제 성공 여부 |


<br>

---

# 5. ERD
![](https://user-images.githubusercontent.com/65996045/188566128-49665194-0e28-4d1c-891f-e2a7ad382aec.png)

<br>

---

# 6. 참조 문서
- [Postman API Docs](https://documenter.getpostman.com/view/21254145/VV4xww9H)


