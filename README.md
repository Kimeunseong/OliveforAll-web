# Olive For All 
### "카메라로 찰칵!📷 AI가 찾아주고 요약해주는 It's Olive for All🍏"
![image](https://user-images.githubusercontent.com/111672496/221744937-178dc155-ebcc-4a13-bfa0-715b47ac9743.png)
<br>
## 개요
올리브영 매장에 있는 화장품을 카메라로 찍으면 그 제품의 간단한 정보와 주요 리뷰만 요약한 상세페이지를 보여줌으로서 사용자의 합리적인 선택을 도와주는 어플이케이션
## 팀원
* 최다솔 - 기획, 데이터 수집, 라벨링, 데이터 전처리, 모델 설계
* 김은성 - 기획, 데이터 수집, 라벨링, 웹개발, 크롤링, 배포
## 프로젝트 기간
* 2023.1.10 - 2023.2.28
## 기술 스택
- 백엔드 :  Flask
- DB : MongoDB
- Cloud : AWS
- DE / ML : tensorflow, kears, pandas, numpy,
- Crawling : selenium, beautifulsoup, request
- Design / Mock-up Tool : KakaoOven, Figma
## 기능 구현
* 메인 화면 : MainPage
    * 본 프로젝트에 대한 설명 및 서비스 이용법 소개
    * ‘검색하러 가기’
* 카메라 촬영 및 이미지 업로드 페이지 : UploadPage
   * 이미지를 업로드(PC) 또는 카메라로 촬영(모바일)하면 이미지가 서버에 저장됨.
   * 학습된 이미지 분류 모델이 이미지 속 모델을 예측.
* 상품 페이지
   * 상품 상세 정보 : 제품명, 제품 공식 이미지, 올리브영 온라인몰 판매가, 별점
   * ‘구매하러 가기’ : 해당 제품의 올리브영 온라인몰의 구매 가능 링크로 연결해줌
   * ‘찐 리뷰’ : 핵심 문장만으로 이루어진 리뷰들을 긍정/부정적 의견으로 나누어 보여줌
## 딥러닝 모델 설계
* 이미지 분류 모델 (https://github.com/Dasol-Choi/OliveYoung_cosmetics_img_classifier)
* 텍스트 분류 모델 ([https://github.com/Dasol-Choi/OliveYoung_cosmetics_img_classifier](https://github.com/Dasol-Choi/OliveYoung_review_classifier))
<br><br>
<hr>

[Olive for All 웹페이지 바로가기](http://3.36.96.232:5000/)
