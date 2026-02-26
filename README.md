# SKN27-1ST-2TEAM

## 🔎 프로젝트명 

### 자동차 리콜 통합 조회  시스템


## 📆 프로젝트 기간 

###  2026/02/23 ~ 2026/02/26 (총 4일)


# 프로젝트 구성원 및 역할

**팀명: 리콜체크해조**
| 임예은 | 이재건 | 오주희 | 권환성 | 이성진 | 주연중|
| --- | --- | --- | --- | --- | --- |
| ![title](https://image.zeta-ai.io/profile-image/6c77c471-95aa-4a6a-8757-fbac21d7c266/80a1c813-5798-4d7e-a64b-d81e9d31240f.png) | ![title](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRf37jD-_tgMHRVsj_vjPq6UXJOIevp7bsfIw&s) | ![title](https://lh3.googleusercontent.com/GLoH7rT6jRD-e6-vGIzbt41dsebD8UXnCJyokXpSHbk2YEMsYN_mA6krr_7IusjiLxhSXA6NoVGL1awXzVmX1eJ8uBHE0JlJDnxM=e365-w262) | ![title](https://i.pinimg.com/236x/8b/d0/c1/8bd0c190d5648e6c3969a1e54d8965a4.jpg) | ![title](https://daewonshop.cdn-nhncommerce.com/20240319/160312.983926000/glowpikmin_600.jpg) | ![title](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRncmxILJd7_JvY8MitNz_qu1Uhg66bkvSQ7Q&s) | 
| [@ye-eun-min201](https://github.com/ye-eun-min201) | [@skn27jg](https://github.com/skn27jg) |  [@ohjuheecode](https://github.com/ohjuheecode) | [@nanseong](https://github.com/nanseong) | [@soiez2958](https://github.com/soiez2958) | [@samjucubix-stack](https://github.com/samjucubix-stack) |

- 임예은: 팀장 , 프론트엔드 개발, 발표
- 이재건 : ERD 설계, 백엔드 개발 
- 오주희 : 데이터 분석, 데이터 전처리
- 권환성 : ERD 설계, 백엔드 개발
- 이성진 : 자료조사, 발표준비
- 주연중 : 자료조사, 깃허브

## 프로젝트 주제 
1. 브랜드별 차종별 리콜 현황 조회 및 신고
2. 브랜드별 차종별 리콜 데이터 분석 대시보드 
3. 일단 여기까지 추후 추가요망

## 프로젝트 개요 
본 프로젝트는 한국교통안전공단의 공공데이터를 기반으로 브랜드 및 차종별 리콜 현황과 분석 자료를 통합 제공하는 것을 목적으로 합니다. 사용자는 포털을 통해 리콜 현황을 조회 및 신고 할 수 있으며, 전용 대시보드에서 브랜드별 비교 데이터를 시각적으로 확인하고 FAQ를 통해 상세 정보를 간편하게 열람할 수 있습니다.
 
* 프로젝트명:  자동차 리콜 통합 조회 시스템
* 핵심 개요: 자동차 리콜현황 조회, 신고, 분석데이터 대시보드 제공 및 FAQ 정보열람 을 제공하는 streamlit 기반 웹
* 프로젝트 배경 (Background)
  - 정보의 파편화 및 접근성 한계: 공공기관의 리콜 데이터가 텍스트 위주로 산재되어 있어 일반 사용자가 본인 차량의 정보를 신속하고 정확하게 파악하기 어려움.

  - 데이터 시각화의 부재: 브랜드별 결함 추이나 차종별 비교 분석 등 소비자의 합리적 판단을 돕는 통계적 인사이트 제공 채널이 부족함.

  - 소비자 안전권 확보: 자동차 결함 사례가 복잡화됨에 따라 리콜 이력을 투명하게 공개하고 사용자 접근성을 높여야 할 사회적 필요성 증대.
* 주요 기능 (Key Features)
  - 통합 리콜 조회: 브랜드 및 차종 검색을 통한 실시간 리콜 대상 여부 및 상세 이력 확인.

  - 비교 분석 대시보드: 브랜드별 리콜 빈도, 연도별 추이 브랜드 및 차종별 리콜건수 순위의 시각화 데이터 제공.

  -  FAQ: 자동차 리콜에 관해 자주 묻는 정보 열람.

* 기대 효과 (Expected Effects)
  - 정보 접근성 혁신: 사용자 중심의 UI/UX를 통해 복잡한 공공데이터를 누구나 쉽게 이해할 수 있는 정보로 재구성.

  - 안전 대응력 강화: 정확한 리콜 정보를 적시에 제공하여 운전자의 즉각적인 조치를 유도하고 결함 사고 예방에 기여.

  - 시장 투명성 제고: 객관적인 리콜 분석 데이터를 제공함으로써 자동차 제조사의 품질 관리 및 소비자의 합리적인 차량 구매 보조.

# 🚗 RecallChecker - 자동차 리콜 조회 시스템

## 📁 프로젝트 구조

```
SKN27-1ST-2TEAM/
├── main.py                        # 홈 페이지
├── header.py                      # 공통 헤더 컴포넌트
├── crawling.py                    # FAQ 크롤링 스크립트
├── requirements.txt               # 패키지 목록
├── ppt.md                         # 발표 자료
├── README.md
│
├── pages/
│   ├── analysis.py                # 리콜 데이터 분석
│   ├── check.py                   # 리콜 대상 차량 조회
│   ├── faq.py                     # 자주 묻는 질문
│   └── report.py                  # 결함 신고
│
├── data/
│   ├── 자동차리콜현황(2019)_v2.0.csv
│   ├── 자동차리콜현황(2020) v3.0.csv
│   ├── 자동차리콜현황(2021).csv
│   ├── 자동차리콜현황(2022).csv
│   ├── 자동차리콜현황(2023).csv
│   └── faq.csv
│
├── database/                      # DB 관련 파일
├── img/                           # 이미지 파일
├── static/                        # 폰트 등 정적 파일
│
└── .streamlit/
    └── config.toml                # Streamlit 설정
```
🚗 RecallChecker - 자동차 리콜 조회 시스템
한국교통안전공단의 공공데이터를 기반으로 내 차량의 리콜 여부를 간편하게 조회하고, 결함 신고까지 한 번에 처리할 수 있는 서비스입니다.
브랜드별·차종별 리콜 현황을 시각화하여 소비자가 더 안전하고 합리적인 차량 선택을 할 수 있도록 돕습니다.

## 💻기술스택 
<img src="https://img.shields.io/badge/python-%233776AB.svg?&style=for-the-badge&logo=python&logoColor=white" /> <img src="https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white"> 
<img src="https://img.shields.io/badge/markdown-%23000000.svg?style=for-the-badge&logo=markdown&logoColor=white">
</div>

## 📚 사용 라이브러리
<img src="https://img.shields.io/badge/Streamlit-%23FE4B4B.svg?style=for-the-badge&logo=streamlit&logoColor=white"> <img src="https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white"> <img src="https://img.shields.io/badge/jupyter-%23F37626.svg?&style=for-the-badge&logo=jupyter&logoColor=white" /> <img src="https://blog.nashtechglobal.com/wp-content/uploads/2024/12/Playwright-2-1024x206.png" width = 120 height = 30>

## Project History


| 날짜 | 주요작업 | 비고 |
| --- | --- | --- |
| 26/02/23 | 주제기획, 개발환경 세팅, 개발 방향 확정 | 기획 |
| 26/02/24 | 화면설계, ERD 설계 | 개발 |
| 26/02/25 | 테스트 시나리오 진행 및 버그수정, 개발확정 | 개발 |
| 26/02/26 | 발표자료 및 문서 작업 진행 | 마감 |

## 요구사항 명세서
* 리콜 대상 조회 
  - 브랜드, 차종 및 생산년도 선택
  -  결과출력
* 리콜 대상 신고
  - 약관 동의
  - 결함 신고 
  -  결과 페이지 출력
* 리콜 데이터 분석 대시보드
  - 브랜드 및 차종별 리콜수 막대그래프 제공
  - 총 리콜 수, 리콜 발생 브랜드 총 수, 리콜 발생 차종 수 제공
  -  총 리콜 수 랭킹 제공
  - 연도별 리콜 건수 추이 막대그레프 제공 
* FAQ
  - 자주 묻는 질문 검색 및 조회

### 시스템 아키텍처
![title](https://postfiles.pstatic.net/MjAyNjAyMjZfMjQ3/MDAxNzcyMDY0Nzk0ODI5.YX8WfWni2p_oTz4VknI1LO4VndzQraSh5nJu_nJaVYsg.ZPLMTYUEuAj02QF1tRRjNTSx8r97Gp5tTP0g2hDHbYog.PNG/KakaoTalk_20260225_100325624.png?type=w966)   

## ERD 설계
#### **설명도**
![title](https://postfiles.pstatic.net/MjAyNjAyMjZfNTEg/MDAxNzcyMDY0NzkzMjg5.dObo2RLd5u-MuLAf0e6GdM5RXU1AFCzoyGpM1lybL00g.CKZqIeKsa94LmAS8wRWFOtOysZFNUaNt_WJQk5OuHJ0g.PNG/KakaoTalk_20260225_160813015.png?type=w966)   

* 🛠️ 주요 기능 (Key Features)
  - 실시간 데이터 검증 (Check)

    + 제조사·모델·리콜 정보를 통합하여 차량 정보의 유효성을 실시간 조회 및 검증

  + 유기적 데이터 매핑 (Mapping)

    + 기초 데이터와 리콜 이력을 연동하여 대상 여부를 즉각 판별하는 관계형 구조 구축

  + 결함 신고 및 관리 (Insert)

    + 신고자-차량-결함 정보를 연결하여 체계적인 리포트 생성 및 이력 저장

#### **실제 ERD**
![title](https://postfiles.pstatic.net/MjAyNjAyMjZfMTQ4/MDAxNzcyMDczNjY0MTk1.T-0MG4egCv6idAnJUhzKg1gEU5FEJ3RZ2TyrpBtMPdgg.wm2Jk_haDjUv45E_358xQagu96C68mgWH3MPIxm8hoQg.PNG/KakaoTalk_20260226_113855868.png?type=w966)

    리콜리스트: manufacturers(회사),  
    vehicle_models(차명),recall_history
리콜리스트를 정확하게 표출하기 위함과 유지보수까지 생각해서 
짠 테이블입니다. 회사와 차명이 추가될시 각 테이블에 입력하면 되고 
그 이후 해당 회사의 차에 대한 리콜리스트를 추가하는방법으로 
유지보수관리를 잘 할 수 있습니다.
vehicles(차량정보 입력), reporters(신고자정보 입력),defect_reports(결합내용) 
입력를 하여 데이터를 insert를 할수있습니다.


## 화면구성 
### **1. 메인화면**
![title](https://postfiles.pstatic.net/MjAyNjAyMjZfMTU2/MDAxNzcyMDY0NzUxODU5.hyJt8xUT0TfWqrL2S2VymkyMB4vug-6vzwWpBzm45gsg.u80_4y8IkYyDPiZjQZV9aamkKVDyyN29gpAiOHprK14g.PNG/%EB%A9%94%EC%9D%B8%ED%8E%98%EC%9D%B4%EC%A7%80.png?type=w966)

* 메인화면 입니다 우측 상단에 있는 버튼으로 각 서비스로 이동할수 있습니다.

### **2.리콜조회**

#### **2-1. 조회 페이지 (리콜대상인 경우)**
![title](https://postfiles.pstatic.net/MjAyNjAyMjZfMTg2/MDAxNzcyMDY0NzcwOTcz.F-TEnPsv5NHpcLu8YHavggx3uXwQdv_9Vlo5BuzJ5Uwg.lPLi6hiawXUxU5_i4DAA8ORYJB-phf8MsS15kxiEYdYg.PNG/screencapture-localhost-8501-check-2026-02-26-09_02_19.png?type=w966)   

  * 리콜 조회 화면입니다 리콜대상일 경우 "리콜 대상 차량입니다"  
     메시지와 리콜사유, 개수가 출력됩니다.  
     해당 차량의 리콜 현황에서 데이터를 조회 할 수 있습니다.   
하단의 결함 신고하기 버튼을 클릭시 결함 신고 페이지로 연결됩니다.

#### **2-2. 조회 페이지 (리콜대상 아닌경우)**
![title](https://postfiles.pstatic.net/MjAyNjAyMjZfMjI2/MDAxNzcyMDY0NzY2NzUw.5_evFGAD66HrOFLt5UDg7wlvqJzKE3vXmp0BDt1kyocg.GC8fG982-RbZ6ZH3WJkWi22B9gbX8Q7PM-R0wC3gJeMg.PNG/screencapture-localhost-8501-check-2026-02-26-09_01_56.png?type=w966)   
 
  * 리콜 조회 화면입니다 리콜대상이 아닌경우 "리콜 대상이 아닙니다" 메시지가 출력됩니다. 

### **3. 대시보드**

#### **3-1. 국내 브랜드 리콜 데이터 분석**
![title](https://postfiles.pstatic.net/MjAyNjAyMjZfMjk0/MDAxNzcyMDY0Nzc1MjA5.NUBh3_3eWrQZSBYHHb0cKZd5hFCGtVZIlWeCqPgI_dEg.-8mSznFjDCyaHp1IsOqXQO1tzuc_0cEzXjLNLAsUQCAg.PNG/screencapture-localhost-8501-analysis-2026-02-26-09_03_06.png?type=w966)   


  * 국내 브랜드 리콜 분석 페이지 입니다 여기서 국내 브랜드별 리콜건수 TOP10 및 다양한 분석 데이터를 열람할수 있습니다.

#### **3-2. 해외 브랜드 리콜 데이터 분석**
![title](https://postfiles.pstatic.net/MjAyNjAyMjZfMjEx/MDAxNzcyMDY0Nzc4NTY1.Z-upGuMbH4bdFvj_MfIa2udPlIkLphQVfuu6BWC27sEg.pFMpm-ypxZdeXzcKNJXc8jPKwGkkQvJNlxToI9BCDaUg.PNG/screencapture-localhost-8501-analysis-2026-02-26-09_03_40.png?type=w966)   


  * 해외 브랜드 리콜 분석 페이지 입니다 여기서 해외 브랜드별 리콜건수 TOP10 및 다양한 분석 데이터를 열람할수 있습니다.

### 4. **결함신고**

#### **4-1. 안내 페이지**
![title](https://postfiles.pstatic.net/MjAyNjAyMjZfOTcg/MDAxNzcyMDY0Nzg1MDM4.oHx4OgB9X2Ru0CJ-y0mPdsjsKSX5AoCjyrcNnft8DPIg.cgGAz-rEUb2zeWKI-y8_Xor68h-YL_n5CgCI4NTMQiQg.PNG/screencapture-localhost-8501-report-2026-02-26-09_04_30.png?type=w966)   

  * 결함신고 페이지 입니다 주의사항을 확인하고 신고를 계속 진행할 수 있습니다.

#### **4-2. 동의 페이지**
![title](https://postfiles.pstatic.net/MjAyNjAyMjZfNDAg/MDAxNzcyMDY0Nzg2ODQx.CpCMqJHimGZXCFnPPmnwAR4jITw2vQS1OkTHlr03sgsg.h7pc_Z9KwO5uRT-dMhHoEZlDkBniq9Gx5OeCpQ1bzMgg.PNG/screencapture-localhost-8501-report-2026-02-26-09_04_42.png?type=w966)   

  * 약관동의 페이지 입니다 약관정보를 확인하고 동의하여 진행하거나 신고를 그만둘수있습니다.


#### **4-3. 입력 페이지**
![title](https://postfiles.pstatic.net/MjAyNjAyMjZfMiAg/MDAxNzcyMDY0Nzg4OTMy.s24zeE9ntp8nYg63uf2oakq0ep0mUwhztskRrgYuqVQg.JpzRYVgXvlaGywc7LJB5grPvzO9AKC7Ve8ZflybBAqkg.PNG/screencapture-localhost-8501-report-2026-02-26-09_05_53.png?type=w966)   

  * 결함신고 페이지 입니다 제공된 양식을 활용해 신고를 확정할수 있습니다.

#### **4-4. 접수 페이지**
![title](https://postfiles.pstatic.net/MjAyNjAyMjZfMjMw/MDAxNzcyMDY0NzkxMTk3.7Ki6vnkJFpKuaA4RnfQqqBk0LFtL8sxV7mqr4zppoqUg.0qpV4rFlECeLf01f8Z8RNYDDmeYi9bLdAOFc_9R7A4Ag.PNG/screencapture-localhost-8501-report-2026-02-26-09_06_06.png?type=w966)   

* 결함신고 완료 페이지 입니다 결함신고가 완료된것을 확인할 수 있습니다.

#### **5. FAQ**
![title](https://postfiles.pstatic.net/MjAyNjAyMjZfMjcz/MDAxNzcyMDY0NzgxMTQ5.M3cGjq07ZeAp0rzAVbeH8to3mKwXtDWvML1uh-zyHlEg.gQbXvkKDVUmoG0mKX1yhs-lWISrTjEqLoP3x9tlJ5Ugg.PNG/screencapture-localhost-8501-faq-2026-02-26-09_04_21.png?type=w966)

  * FAQ 페이지 입니다 자주 묻는 질문의 검색 및 열람이 가능합니다

## 인용 자료
 [국토교통부 산하 한국교통안전공단 자동차 리콜 센터](https://www.car.go.kr/rs/faq/list.do)   
[공공데이터 포털](https://www.data.go.kr/)   

## 프로젝트 회고
* **임예은:**  
프로젝트 기간이 짧다보니, 임팩트 있는 주제가 필요했는데, 리콜 차량에 대한 주제가 나와 프로젝트를 잘 완성할 수 있었습니다.
프로젝트를 만드는 것에 있어서 기획은 80% 이상의 중요도를 차지한다고 생각합니다. 이슈를 알고, 트랜드를 잘 읽는 개발자가 되고 싶습니다.
또한 다음 프로젝트에서는 개발 지식을 잘 사용하여 개발에 임하고 싶습니다.

* **이재건:**  
표출하는 데이터를 csv파일에서 db로 전이 하면서 표출했던 컬럼이름이 달라져서 
이야기 하면서 고쳐나아가면서 모두가 원하는 데이터를 표출할수있었습니다.

* **오주희:**  
처음 접해보는 것들이 많아 그만큼 걱정도 많았지만, 수업시간에 다뤘던 많은 내용을 복습하고 실제 구현을 해 볼 수 있어 많은 경험을 얻을 수 있었습니다. 이를 통해 이해가 되지 않았던 부분들도 팀원들과 같이 이해하고 해결 할 수 있는 시간이 되었던 것 같습니다

* **이성진:**  
지식이 부족하고 경험이 없다보니 팀에게 도움을 많이 못 준게 아쉬웠다. 첫 미니프로젝트이고 아직은 부족하지만, 계속 공부하다보면 많은 역할을 할 수 있을 것 같다. 그리고 데이터를 수집하고 처리하는 과정에서 생각보다 많은 데이터가 필요하고 그 데이터를 분류하는 능력이 중요하다는 것을 느꼈다. 무엇보다 주제를 잘 선정하고 이에 필요한 데이터를 얼마나 잘 수집하느냐에 따라 결과가 달라질 수 있다는 것을 느꼈다.

* **권환성:**  
공부의 필요성이 느껴졌다. 전공자들이 진행하는것들을 부수적으로 도우는 일들을 하며 배워보려고 했으나 아직까지 어려운점이 너무 많았던건 같다,
다음에는 더 많은 지식을 갖게되어 프로젝트에서 더 많은 역할을 해보고싶다

* **주연중:**  
  팀에 도움이 되고자 노력하였다고 생각합니다. 이번 프로젝트에서 경험한것을 바탕으로 다음 그다음 마지막으로 최종 프로젝트까지 1인분 할수있는 밑거름으로 삼을수있게 하겠습니다 같이 노력해주신 전공자 비 전공자분들 모두 수고 많으셨습니다 리콜체크해조 화이팅!

