---
marp: true
title: 차량 리콜 대상 확인 서비스 (RecallChecker)
theme: recall-template
paginate: true
size: 16:9
header: RecallChecker
style: |
  /* @theme recall-template */
  @import url('https://cdn.jsdelivr.net/gh/webfontworld/paperlogy/Paperlogy.css');

  :root{
    /* 🔴 Red theme */
    --brand-rgb: 185, 28, 28;         /* base red */
    --navy:#B91C1C;                   /* primary */
    --navy2:#7F1D1D;                  /* deep */
    --sky:#FFF1F2;                    /* rose-50 */
    --sky2:#FFE4E6;                   /* rose-100 */
    --text:#0F172A;
    --muted:#64748B;
    --card:#FFFFFF;
    --line:rgba(15,23,42,.12);
  }

  section{
    font-family: Paperlogy, Pretendard, "Noto Sans KR", "Apple SD Gothic Neo", "Malgun Gothic", sans-serif;
    background: var(--sky);
    color: var(--text);
    padding: 86px 72px 78px 72px;
  }

  /* top bar */
  section::before{
    content:"";
    position:absolute;
    top:0; left:0; right:0;
    height:18px;
    background: var(--navy);
  }

  /* header / footer placement (RecallChecker: 오른쪽 상단 고정) */
  header{
    position:absolute;
    top:42px;
    right:72px;
    left:auto !important;
    font-weight:1000;
    letter-spacing:.04em;
    color: var(--navy);
    font-size: 16px;
    z-index: 10;
  }
  footer{
    position:absolute;
    left:72px;
    bottom:42px;
    font-size: 14px;
    color: var(--muted);
  }

  /* pagination badge */
  section::after{
    right:56px;
    bottom:38px;
    color:#fff;
    background: var(--navy);
    padding: 6px 12px;
    border-radius: 999px;
    font-weight:800;
    font-size: 14px;
  }

  /* default typography */
  h1{ font-size: 48px; margin: 0 0 18px 0; }
  h2{ font-size: 28px; margin: 0 0 12px 0; color: var(--navy); }
  p, li{ font-size: 22px; line-height: 1.45; }
  ul{ margin: 10px 0 0 0; }
  li{ margin: 8px 0; }
  small{ color: var(--muted); }

  /* banded slides */
  section.banded{
    background: linear-gradient(to bottom, var(--sky2) 0 150px, var(--sky) 150px 100%);
    padding-top: 190px;
  }
  section.banded > h1{
    position:absolute;
    top:64px;
    left:72px;
    margin:0;
    color: var(--navy);
    font-size: 52px;
    font-weight: 900;
  }

  /* layout helpers */
  .grid{ display:grid; gap:18px; }
  .grid-2{ display:grid; grid-template-columns: 1fr 1fr; gap: 18px; }
  .grid-3{ display:grid; grid-template-columns: 1fr 1fr 1fr; gap: 18px; }

  /* cards */
  .card{
    background: var(--card);
    border: 1px solid var(--line);
    border-radius: 14px;
    overflow:hidden;
    box-shadow: 0 10px 24px rgba(15,23,42,.06);
  }
  .card .bar{
    background: var(--navy);
    color:#fff;
    padding: 12px 16px;
    font-weight: 900;
    font-size: 18px;
    letter-spacing:.02em;
  }
  .card .body{
    padding: 16px 18px 18px 18px;
    font-size: 20px;
    color: var(--text);
  }

  .badge{
    display:inline-block;
    padding: 4px 10px;
    border-radius: 999px;
    background: rgba(var(--brand-rgb), .12);
    color: var(--navy);
    font-weight: 900;
    font-size: 14px;
    letter-spacing:.06em;
  }

  /* charts / ranking */
  .chart-img{
    width:100%;
    height:150px;
    object-fit:contain;
    border-radius:14px;
    border:1px solid rgba(15,23,42,.12);
    margin-top:10px;
    margin-bottom:12px;
  }
  .chart-img.year{ height:140px; margin-top:0; }

  .rank{
    list-style:none;
    padding:0;
    margin:0;
  }
  .rank li{
    display:flex;
    justify-content:space-between;
    align-items:center;
    gap:12px;
    padding:6px 0;
    border-bottom: 1px dashed rgba(15,23,42,.10);
    font-size:16px;
  }
  .rank li:last-child{ border-bottom:none; }
  .rank .name{
    flex:1;
    min-width:0;
    white-space:nowrap;
    overflow:hidden;
    text-overflow:ellipsis;
    color: rgba(15,23,42,.85);
    font-weight:800;
  }
  .rank .cnt{
    font-weight:1000;
    color: var(--navy);
  }

  /* screenshots */
  .imgbox{
    height: 250px;
    border-radius: 18px;
    border: 1px solid rgba(15,23,42,.12);
    background: rgba(255,255,255,.7);
    overflow: hidden;
    margin-bottom: 14px;
  }
  img.main-shot{
    width: 100%;
    height: 100% !important;
    object-fit: cover;
    object-position: center 2%;
    display: block;
  }
  img.contain-shot{
    width: 100%;
    height: 100% !important;
    object-fit: contain;     /* ✅ 전체 보이게(안 잘림) */
    display: block;
    background: rgba(255,255,255,.7);
  }

  /* TOC layout */
  section.toc{
    padding: 0;
    background: var(--sky);
  }
  section.toc::after{ display:none; }
  section.toc footer{ display:none; }

  .toc-wrap{
    position:absolute;
    top:18px; left:0; right:0; bottom:0;
    display:flex;
  }
  .toc-left{
    width: 36%;
    background: linear-gradient(180deg, var(--sky2), rgba(var(--brand-rgb), .12));
    padding: 72px 42px 56px 54px;
  }
  .toc-right{
    flex:1;
    padding: 78px 64px 44px 44px;
  }
  .toc-title{
    font-size: 56px;
    font-weight: 1000;
    color: var(--navy);
    margin-bottom: 18px;
  }
  .toc-project{ margin-top: 22px; }
  .toc-project-name{
    margin-top:10px;
    font-size:20px;
    color: var(--navy);
    font-weight:1000;
  }
  .toc-project-desc{
    margin-top:6px;
    font-size:14px;
    color: rgba(15,23,42,.65);
    line-height: 1.35;
    word-break: keep-all;
  }
  .toc-list{
    list-style:none;
    padding:0;
    margin:0;
    display:grid;
    grid-template-columns: 1fr;
    gap: 12px;
  }
  .toc-item{
    display:flex;
    align-items:center;
    gap: 12px;
    padding: 10px 12px;
    border-radius: 14px;
    background: rgba(255,255,255,.78);
    border: 1px solid var(--line);
  }
  .toc-num{
    width: 48px;
    height: 48px;
    border-radius: 12px;
    background: var(--navy);
    color:#fff;
    display:flex;
    align-items:center;
    justify-content:center;
    font-weight: 1000;
    letter-spacing:.05em;
    font-size: 16px;
    flex: 0 0 auto;
  }
  .toc-main{ font-weight: 1000; font-size: 20px; color: var(--navy); }

  /* cover */
  section.cover{
    background:
      linear-gradient(135deg, #FFFFFF 0%, #FFF7F8 40%, var(--sky) 100%),
      linear-gradient(
        135deg,
        transparent 0 62%,
        rgba(255,228,230,.95) 62% 80%,
        rgba(var(--brand-rgb), .95) 80% 100%
      );
    background-size: cover, 520px 420px;
    background-position: center, right -80px bottom -120px;
    background-repeat:no-repeat;
    padding-top: 120px;
  }
  section.cover footer{ display:none; }
  section.cover::after{ display:none; }

  .cover-date{
    position:absolute;
    top:66px;
    right:72px;
    font-size: 16px;
    font-weight: 900;
    color: var(--navy);
    letter-spacing:.08em;
  }
  .cover-title{
    font-size: 56px;
    font-weight: 1000;
    color: var(--navy);
    line-height: 1.05;
  }
  .cover-sub{
    margin-top: 18px;
    font-size: 22px;
    color: rgba(15,23,42,.75);
  }
  .cover-meta{
    position:absolute;
    right:72px;
    bottom:54px;
    font-size: 14px;
    color: rgba(255,255,255,.92);
    text-align:right;
  }

  /* placeholder */
  .shot{
    height: 330px;
    border-radius: 18px;
    border: 2px dashed rgba(var(--brand-rgb), .35);
    background: rgba(255,255,255,.6);
    display:flex;
    align-items:center;
    justify-content:center;
    font-size: 18px;
    font-weight: 900;
    color: rgba(var(--brand-rgb), .7);
  }

  .mini{
    font-size: 18px;
    color: rgba(15,23,42,.78);
  }

  /* ✅ 높이 키우기(필요 시) */
  .grid-2.stretch{ align-items: stretch; }
  .tall-360{ height:360px !important; }
  .tall-400{ height:400px !important; }
  .tall-420{ height:420px !important; }

  /* ✅ Q&A 전용(가운데 크게 + 헤더/페이지번호/상단바 제거) */
  section.qa{
    background: var(--sky) !important;
    padding: 0 !important;
    display:flex;
    align-items:center;
    justify-content:center;
    text-align:center;
  }
  section.qa::before{ display:none !important; } /* 상단 bar 제거 */
  section.qa::after{ display:none !important; }  /* 페이지번호 제거 */
  section.qa header,
  section.qa footer{ display:none !important; }  /* RecallChecker/푸터 제거 */
  section.qa h1{
    font-size: 110px !important;
    font-weight: 1000 !important;
    color: var(--navy) !important;
    margin: 0 !important;
  }

  /* thanks */
  section.thanks{
    background: linear-gradient(to right, var(--sky) 0 55%, var(--navy) 55% 100%);
    padding-top: 210px;
  }
  section.thanks footer{ display:none; }
  section.thanks::after{ display:none; }
  section.thanks header{ color:#fff; }

  .thanks-wrap{
    display:grid;
    grid-template-columns: 55% 45%;
    height: 100%;
    align-items:center;
  }
  .thanks-left{ padding-right: 40px; }
  .thanks-right{
    color:#fff;
    text-align:right;
    padding-left: 40px;
  }
  .thanks-right .big{
    font-size: 52px;
    font-weight: 1000;
    line-height:1.05;
  }
  .thanks-right .small{
    margin-top: 10px;
    font-size: 18px;
    opacity:.9;
  }
---

<!-- class: cover -->
<div class="cover-date">2026.02.26</div>

<div class="cover-title">차량 리콜 대상 확인 서비스<br/>RecallChecker</div>
<div class="cover-sub">
클릭 한 번으로 내 차량 리콜 대상 여부 확인 + 분석 + FAQ + 결함신고
</div>

<div class="cover-meta">
팀/발표자: (팀명/이름 입력)<br/>
데이터: 한국교통안전공단·자동차리콜센터 (2019–2023)
</div>

---

<!-- class: toc -->
<div class="toc-wrap">
  <div class="toc-left">
    <div class="toc-title">목차</div>
    <div class="toc-project">
      <div class="toc-project-name">RecallChecker</div>
      <div class="toc-project-desc">내 차 리콜 조회 & 데이터 분석 서비스</div>
    </div>
  </div>

  <div class="toc-right">
    <ul class="toc-list">
      <li class="toc-item"><div class="toc-num">01</div><div><div class="toc-main">프로젝트 배경</div></div></li>
      <li class="toc-item"><div class="toc-num">02</div><div><div class="toc-main">요구사항(기능)</div></div></li>
      <li class="toc-item"><div class="toc-num">03</div><div><div class="toc-main">데이터 수집 & QC</div></div></li>
      <li class="toc-item"><div class="toc-num">04</div><div><div class="toc-main">DB 설계(ERD)</div></div></li>
      <li class="toc-item"><div class="toc-num">05</div><div><div class="toc-main">화면 설계</div></div></li>
      <li class="toc-item"><div class="toc-num">06</div><div><div class="toc-main">분석 결과 & 결론</div></div></li>
    </ul>
  </div>
</div>

---

<!-- class: banded -->
# 01. 프로젝트 배경 (Background)

<div class="grid-2">
  <div class="card">
    <div class="bar">정보의 파편화 & 접근성 한계</div>
    <div class="body">
      <ul>
        <li>공공기관 리콜 데이터가 <b>텍스트 위주로 산재</b></li>
        <li>일반 사용자가 본인 차량 정보를 <b>신속·정확하게</b> 파악하기 어려움</li>
        <li>확인 과정이 번거로워 리콜 공지를 <b>놓치기 쉬움</b></li>
      </ul>
    </div>
  </div>

  <div class="card">
    <div class="bar">데이터 시각화/인사이트 부재</div>
    <div class="body">
      <ul>
        <li>브랜드별 결함 추이, 차종별 비교 분석 등 <b>통계 인사이트</b> 채널 부족</li>
        <li>소비자의 합리적 판단을 돕는 <b>비교 기준</b>이 부족</li>
      </ul>
    </div>
  </div>
</div>

<br/>
<div class="card" style="margin-top:18px;" >
  <div class="bar">소비자 안전권 확보(사회적 필요성)</div>
  <div class="body">
    결함 사례가 복잡화됨에 따라 리콜 이력을 <b>투명하게 공개</b>하고  
    사용자 <b>접근성</b>을 높여야 할 사회적 필요성이 증가
  </div>
</div>

---

<!-- class: banded -->
# 01_1. wbs


  <div class="imgbox tall-360" style="margin-bottom:0;">
    <img class="contain-shot" src="./img/wbs.png" />
  </div>


---



<!-- class: banded -->
# 02. 요구사항(기능) 요약

<div class="grid-2">
  <div class="card">
    <div class="bar">01 · 리콜 대상 차량 조회</div>
    <div class="body">제작사/차명/생산연도 선택 → 리콜 대상 여부 확인</div>
  </div>

  <div class="card">
    <div class="bar">02 · 결함신고</div>
    <div class="body">리콜 대상이면 즉시 신고(자동 입력 연동)</div>
  </div>

  <div class="card">
    <div class="bar">03 · 리콜 데이터 분석</div>
    <div class="body">국내/해외, 브랜드·차종·연도별 리콜 건수 시각화</div>
  </div>

  <div class="card">
    <div class="bar">04 · FAQ</div>
    <div class="body">자주 묻는 질문 검색/열람 + 상담 경로 안내</div>
  </div>
</div>

---

<!-- class: banded -->
# 02_1. 리콜 대상 차량 조회

<div class="imgbox" style="height:180px;">
  <img class="contain-shot" src="./img/SELECT2_page.png" />
</div>

<div class="card">
  <div class="bar">설계 포인트</div>
  <div class="body">
    <ul>
      <li>가장 중요한 요구사항: <b>내 차가 리콜 대상인지 바로 확인</b></li>
      <li>데이터 신뢰성 확보: <b>한국교통안전공단 CSV</b> 기반</li>
      <li>입력 부담 최소화: <b>선택 박스</b>로 제작사/차명 선택</li>
      <li>리콜 대상일 경우 <b>리콜 사유</b>를 함께 제공</li>
    </ul>
  </div>
</div>

---

<!-- class: banded -->
# 02_2. 결함신고

<div class="grid-2 stretch">

  <div class="card tall-360">
    <div class="bar">핵심 UX</div>
    <div class="body">
      <ul>
        <li>리콜 조회 결과가 “대상”이면 <b>신고 버튼 활성화</b></li>
        <li>조회에서 입력한 차량 정보가 <b>신고 폼에 자동 저장</b></li>
        <li>차주는 <b>본인 정보 + 결함 내용</b>만 입력하면 신고 완료</li>
      </ul>
    </div>
  </div>

  <div class="imgbox tall-360" style="margin-bottom:0;">
    <img class="contain-shot" src="./img/defects_page.png" />
  </div>

</div>

---


<!-- class: banded -->
# 02_3. 리콜 데이터 분석

<div class="grid-2 stretch">

  <div class="card tall-360">
    <div class="bar">분석 목적</div>
    <div class="body">
      <ul>
        <li>국내/해외 탭으로 <b>리콜 규모</b>를 비교</li>
        <li>브랜드/차종/연도별 리콜 건수 시각화</li>
        <li>TOP10 항목은 <b>주요 리콜사유(상위 3개)</b>까지 함께 확인</li>
      </ul>
      <div class="mini" style="margin-top:10px;">
        구매 전 “리콜이 잦은 브랜드/차종”을 미리 파악하여 합리적 판단 유도
      </div>
    </div>
  </div>

  <div class="imgbox tall-360" style="margin-bottom:0;">
    <img class="contain-shot" src="./img/analysis_page.png" />
  </div>

---

<!-- class: banded -->
# 02_4. FAQ

<div class="imgbox" style="height:240px;">
  <img class="contain-shot" src="./img/FAQ_page.png" />
</div>

<div class="card">
  <div class="bar">FAQ 구성</div>
  <div class="body">
    <ul>
      <li>“신고 후 처리 과정”, “리콜 관련 고지 방식” 등 <b>자주 묻는 질문</b> 제공</li>
      <li>검색 기반으로 원하는 답변을 빠르게 탐색</li>
      <li>해결이 어려운 경우를 대비해 <b>상담 경로</b>까지 연결</li>
    </ul>
  </div>
</div>

---

<!-- class: banded -->
# 03. 데이터 수집 & QC

<div class="grid-2">
  <div class="card">
    <div class="bar">데이터 수집</div>
    <div class="body">
      <ul>
        <li><b>리콜 현황</b>: 한국교통안전공단(TS) 연도별 CSV(2019–2023)</li>
        <li><b>FAQ</b>: 자동차리콜센터 공개 웹 페이지 <b>크롤링</b>(질문/답변 수집)</li>
        <li><b>국내/해외 구분</b>: 제작사 리스트 기준으로 “구분” 컬럼 생성</li>
      </ul>
      <div class="mini" style="margin-top:10px;">
        ※ 리콜 현황은 공공 데이터, FAQ는 공개 페이지 기반 크롤링 데이터
      </div>
    </div>
  </div>

  <div class="card">
    <div class="bar">전처리(QC)</div>
    <div class="body">
      <ul>
        <li>5개년 결합 → 컬럼 정규화</li>
        <li>날짜 파싱/논리 오류(생산 from &gt; to) 점검</li>
        <li>중복 제거(동일 결함 레코드) + 결측/이상치 플래그</li>
      </ul>
      <div class="mini" style="margin-top:10px;">
        데이터 특성상 VIN/대상대수 부재 → <b>건수 중심</b> 분석
      </div>
    </div>
  </div>
</div>

---

<!-- class: banded -->
# 04. DB 설계(ERD) 설명

<div class="imgbox" style="height:310px;">
  <img class="contain-shot" src="./img/ERD.png" />
</div>

<div class="grid-2">
  <div class="card">
    <div class="bar">정규화 테이블</div>
    <div class="body" style="font-size:16px;">
      <ul>
        <li>manufacturers: 제작사</li>
        <li>vehicles: 차명(차종)</li>
        <li>recall_campaigns: 리콜 공고(캠페인)</li>
        <li>campaign_vehicles: 캠페인-차종 매핑 + 생산기간</li>
      </ul>
    </div>
  </div>

  <div class="card">
    <div class="bar">조회 로직 요약</div>
    <div class="body" style="font-size:16px;">
      <ul>
        <li>사용자 입력(제작사/차명/연도) → DB 조회</li>
        <li>해당 연도가 생산기간과 <b>겹치면 리콜 대상</b></li>
        <li>대상일 경우: 리콜사유/개시일/대상기간 제공</li>
      </ul>
    </div>
  </div>
</div>

---

<!-- class: banded -->
# 05. 화면 설계

<div class="card">
  <div class="bar">사용자 동선</div>
  <div class="body">
    <ol>
      <li><b>메인</b> → 서비스 소개 + CTA</li>
      <li><b>리콜 조회</b> → 제작사/차명/연도 선택 후 결과 확인</li>
      <li><b>결함신고</b> → 대상이면 자동 입력 연동 후 신고</li>
      <li><b>분석/FAQ</b> → 통계 인사이트 확인 + 궁금증 해결</li>
    </ol>
  </div>
</div>

---

<!-- class: banded -->
# 05_1. 메인 페이지

<div class="grid-2">

<div class="card">
  <div class="bar">디자인 의도</div>
  <div class="body">
    <ul>
      <li>상단 레드 그라데이션: 결함의 <b>위험</b>·리콜의 <b>중요성</b> 시각화</li>
      <li>가독성 높은 <b>Paperlogy 폰트</b> 적용(서비스 UI 기준)</li>
      <li>4가지 서비스 키워드/아이콘 배치 → 한눈에 이해</li>
      <li>CTA 버튼으로 조회 페이지 즉시 이동</li>
    </ul>
  </div>
</div>

  <div class="imgbox tall-360" style="margin-bottom:0;">
    <img class="contain-shot" src="./img/main_page.png" />
  </div>

---

<!-- class: banded -->
# 05_2. 리콜 조회 시스템 페이지


<div class="grid-2">

<div class="card">
  <div class="bar">화면 구성</div>
  <div class="body">
    <ul>
      <li>입력: <b>제작사 → 차명 → 생산연도</b></li>
      <li>리콜대상: <b>빨간색</b>으로 강조 + 결함 사유 노출</li>
      <li>리콜비대상: <b>초록색</b> 안내로 안전 상태 확인</li>
      <li>대상일 때만 “결함 신고하기” 버튼 활성화</li>
    </ul>
  </div>
</div>

<div class="imgbox" style="height:240px;">
  <img class="contain-shot" src="./img/SELECT_page.png" />
</div>

---


<!-- class: banded -->
# 05_3. 리콜 데이터 분석 페이지

<div class="grid-2">
  <div class="card">
    <div class="bar">구성</div>
    <div class="body">
      <ul>
        <li><b>상단</b>: KPI 카드(전체/국내/해외 리콜 건수)</li>
        <li><b>탭</b>: 국내/해외 브랜드 분리 비교</li>
        <li><b>중단</b>: 브랜드 TOP10 / 차종 TOP10 그래프</li>
        <li><b>상세</b>: TOP 항목은 Expander로 <b>주요 리콜사유 TOP3</b> 확인</li>
        <li><b>하단</b>: 연도별 리콜 추이(연도 tick 고정)</li>
      </ul>
    </div>
  </div>

  <div class="imgbox tall-360" style="margin-bottom:0;">
    <img class="contain-shot" src="./img/analysis_page.png" />
  </div>

  
</div>

---

<!-- class: banded -->
# 05_4. FAQ 화면

<div class="imgbox" style="height:220px;">
  <img class="contain-shot" src="./img/FAQ_page.png" />
</div>

<div class="card">
  <div class="bar">화면 구성</div>
  <div class="body">
    <ul>
      <li>검색바(‘리콜/보상/신고’ 키워드로 빠른 탐색)</li>
      <li>질문 목록형(원하는 질문만 선택해 집중 읽기)</li>
      <li>전화번호/온라인 상담 링크(해결 창구 연결)</li>
    </ul>
  </div>
</div>

---

<!-- class: banded -->
# 05_5. 결함신고 페이지

<div class="card">
  <div class="bar">신고 플로우(3-Step)</div>
  <div class="body">
    <ol>
      <li><b>신고 안내</b>: 결함 정의/제외 항목/상담번호 안내</li>
      <li><b>약관 동의</b>: 처리 과정 신뢰 확보 + 책임감 있는 입력 유도</li>
      <li><b>결함신고 등록</b>: 차량/신고자/결함내용 입력(조회 시 차량정보 자동 저장)</li>
    </ol>
    <div class="mini" style="margin-top:10px;">
      목표: 안내→동의→작성으로 사용자가 “다음 행동”을 고민하지 않도록 구성
    </div>
  </div>
</div>

---

<!-- class: banded -->
# 06_1. 사용자 시나리오

<div class="card">
  <div class="body">
    <ol>
      <li><b>리콜 조회</b>: 제작사/차명/연도 선택 → 대상 여부 + 결함 사유 확인</li>
      <li><b>결함신고</b>: 대상이면 신고 버튼 → 자동 입력 확인 후 제출</li>
      <li><b>데이터 분석</b>: 국내/해외 탭 + 브랜드/차종 TOP + 연도별 추이 확인</li>
      <li><b>FAQ</b>: 키워드 검색으로 빠르게 답변 확인</li>
    </ol>
  </div>
</div>

---

<!-- class: banded -->
# 06_2. 결론

<div class="card">
  <div class="bar">RecallChecker 요약</div>
  <div class="body">
    <ul>
      <li>텍스트로 흩어진 리콜 정보를 <b>클릭 한 번</b>으로 확인</li>
      <li>국내/해외 분리 + 시각화 인사이트로 소비자의 <b>합리적 판단</b> 지원</li>
      <li>조회부터 신고까지 <b>한 곳에서 해결</b>하는 서비스로 접근성 향상</li>
    </ul>
  </div>
</div>

---

<!-- class: qa -->
# Q&A

---
<!-- class: qa -->
# 감사합니다.