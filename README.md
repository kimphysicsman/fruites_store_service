# [🍊 fruites_store_service]((https://www.notion.so/kimphysicsman/694ed2006cc44f2f8532339d04d315b3?showMoveTo=true&saveParent=true))
과일 쇼핑몰 서비스

<br />

## 🔑 MVP

> `사용자`가 구매하고자 하는 `상품(과일)`을 선택하여 `주문`, `결제`할 수 있다.

<br />

## ✏ 주요 기능

### 회원관리

`사용자`는 이용자, 관리자로 나눠진다.

- 사용자 정보
    - 기본정보
        - 이름
        - 패스워드
    - 사용자 유형
        - 이용자
            - 권한
                
                `상품` : 조회
                
                `주문` : 조회/입력/수정
                
                `결제` : 조회/입력/수정
                
        - 관리자
            - 권한
                
                `상품` : 조회/입력/수정/삭제
                
                `주문` : 조회/입력/수정/삭제
                
                `결제` : 조회/입력/수정/삭제
                
- 공통기능
    - 회원가입/탈퇴, 회원정보 조회/수정
    - 로그인, 로그아웃

### 상품관리

`상품(과일)`은 관리자에 의해 등록/수정/삭제 될 수 있으며 이용자는 조회만 가능하다.

- 상품 정보
    - 기본정보
        - 이름
        - 설명
        - 판매지
        - 기본 배송비
    - 가격
        - 판매 단위별 가격
        - 재고 개수
    - 판매 상태
        - 판매 준비중
        - 판매 중
        - 판매 완료

### 주문관리

`주문`은 관리자에 의해 등록/수정/삭제될 수 있다. 

이용자는 판매 중인 상품을 판매 단위별로 `주문`할 수 있다. (등록)

이용자는 본인의 `주문`을 조회/수정 가능하다.

주문 대기중일 때만 기본 정보를 수정할 수 있다.

- 주문 정보
    - 기본정보
        - 주문자 (`사용자`)
        - `상품(과일)`
        - 배송지
        - 배송비
        - 총 가격
    - 주문 상태
        
        주문 대기중, 주문 취소, 주문 완료 & 결재 대기중,  결재 완료 & 배송 중, 배송 완료
        

### 결제관리

`결제`는 관리자에 의해 등록/수정/삭제될 수 있다. 

이용자는 주문 대기중인 본인의 `주문`에 대하여 `결제`할 수 있다. (등록)

이용자는 본인의 `결제`을 조회/수정할 수 있다.

결제 대기중일 때만 기본 정보를 수정할 수 있다.

- 결제 정보
    - 기본 정
        - `주문`
        - 결제 가격
        - 결제 방법
    - 결제 상태
        
        결제 대기중, 결제 취소, 결제 완료

<br />

## 💻 기술 스택

`Python` `Django` `DRF`

<br />

## 👉 ERD
![image](https://user-images.githubusercontent.com/68724828/190190699-68ae4fe3-29ca-4890-864d-dc80febe06d5.png)

<br />

## 🙏 API 명세서
https://www.notion.so/kimphysicsman/f326da05d7764060babdafebd0c9d287?v=39854678bcb647e38bcd21a44270ad32

<br />

## 📈 진행상황

- ~~유저, 상품, 주문, 결제 모델링~~
- ~~유저 CRUD 기능 구현~~
- ~~상품 CRUD 기능 구현~~
- ~~주문 CRUD 기능 구현~~
- ~~결제 CRUD 기능 구현~~
- ~~유저 기능 error 핸들링~~

- **상품 기능 error 핸들링(진행중)**
- 주문 기능 error 핸들링
- 결제 기능 error 핸들링

- 상품 CRUD 권한 핸들링
- 주문 CRUD 권한 핸들링
- 결제 CRUD 권한 핸들링

- Test 코드 작성

<br />

## 📌 컨벤션

### ❓ Commit Message

- feat/ : 새로운 기능 추가/수정/삭제
- enhan/ : 기존 코드에 기능을 추가하거나 기능을 강화할 때
- refac/ : 코드 리팩토링,버그 수정
- test/ : 테스트 코드/기능 추가
- edit/ : 파일을 수정한 경우(파일위치변경, 파일이름 변경, 삭제)

### ❓ Naming

- Class : Pascal
- Variable : Snake
- Function : Snake
- Constant : Pascal + Snake

### ❓ 주석

- Docstring을 활용하여 클래스와 함수단위에 설명을 적어주도록 하자.
- input/output을 명시하여 문서 없이 코드만으로 어떠한 결과가 나오는지 알 수 있도록 하자.

### 🚷 벼락치기의 규칙

- 컨벤션 지키기
- Commit 단위 지키기
- 말 이쁘게하기
- 문제를 마주하여 트러블을 겪었다면, 어떻게 해결을 했는지 공유를 해주기
- 각자의 작업을 미리 작성을 하여서 각자의 작업을 공유하기

<br />

