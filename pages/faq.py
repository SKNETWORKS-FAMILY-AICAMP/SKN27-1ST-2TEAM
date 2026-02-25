import streamlit as st
from database.connection import get_faq_data

st.set_page_config(
    page_title="FAQ - 리콜체커",
    page_icon="❓",
    layout="wide"
)

from header import render_header

render_header(current_page="faq")

col_left, col_main, col_right = st.columns([1, 8, 1])
with col_main:

    st.markdown("""
    <style>
    @import url('https://cdn.jsdelivr.net/gh/webfontworld/paperlogy/Paperlogy.css');
    * { font-family: 'Paperlogy', sans-serif; }
    .stApp { background-color: #ffffff; }
    section[data-testid="stSidebar"] { background-color: #ffffff; border-right: 1px solid #e2e8f0; }


    .page-header h1 { font-size: 30px; font-weight: 800; color: #0f172a; margin-bottom: 6px; }
    .page-header p  { color: #64748b; font-size: 15px; }

    
    .faq-count {
        font-size: 13px; color: #64748b; margin-bottom: 16px;
    }
    .faq-item {
        background: white; border-radius: 12px;
        border: 1px solid #e2e8f0;
        margin-bottom: 10px; overflow: hidden;
    }
    .faq-q {
        display: flex; align-items: flex-start; gap: 14px;
        padding: 18px 20px; cursor: pointer;
    }
    .faq-q-badge {
        background: #dc2626; color: white;
        font-size: 14px; font-weight: 900;
        width: 28px; height: 28px; border-radius: 50%;
        display: flex; align-items: center; justify-content: center;
        flex-shrink: 0; margin-top: 1px;
    }
    .faq-q-text {
        font-size: 15px; font-weight: 600; color: #1e293b; flex: 1; line-height: 1.6;
    }
    .faq-a {
        background: #ffffff; 
        margin-top:-10px;
        margin-bottom:10px;
    }
    .faq-a-badge {
        color: #2563eb; font-size: 14px; font-weight: 900; margin-right: 8px;
    }
    .faq-a-text {
        font-size: 14px; color: #475569; line-height: 1.9; white-space: pre-line;
    }
    .contact-box {
        background: #eff6ff; border-radius: 14px;
        padding: 20px 24px; margin-top: 24px; text-align: center;
    }
    .contact-box p { color: #1e40af; font-size: 14px; margin: 0; line-height: 2; }
    </style>
    """, unsafe_allow_html=True)

    # 이제 위에서 만든 함수로 데이터를 가져옵니다
    df = get_faq_data()

    # ── 헤더 ──
    st.markdown("""
    <div class="page-header">
        <h1>❓ 자주 묻는 질문 (FAQ)</h1>
        <p>자동차 제작결함 및 리콜과 관련하여 자주 묻는 질문을 안내드립니다.</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    # ── 검색 ──
    search = st.text_input("🔍 질문 검색", placeholder="궁금한 내용을 검색해보세요  예: 리콜, 결함신고, 보상")
    st.markdown('</div>', unsafe_allow_html=True)

    # ── 필터링 ──
    if search.strip():
        filtered = df[
            df["질문"].str.contains(search, na=False) |
            df["답변"].str.contains(search, na=False)
        ]
    else:
        filtered = df

    st.markdown(f'<div class="faq-count">전체 <strong>{len(filtered)}건</strong></div>', unsafe_allow_html=True)

    # ── 화면 출력 부분 ──
    if len(filtered) == 0:
        st.info("검색 결과가 없습니다. 다른 키워드로 검색해보세요.")
    else:
        # row.iterrows()를 쓰면 인덱스와 행을 함께 가져옵니다.
        for i, row in filtered.iterrows():
            # DB 컬럼명인 'question'과 'answer'를 사용하세요!
            answer= str(row.get("answer", "")).strip()
            question  = str(row.get("question", "")).strip()
            
            # 줄바꿈 및 이스케이프 문자 처리
            answer = answer.replace("\\n", "\n").replace(" \n ", "\n")

            # 환상님이 만드신 예쁜 expander UI에 데이터 담기
            with st.expander(f"Q.  {answer}"):
                st.markdown(f"""
                <div class="faq-a">
                    <span class="faq-a-badge">A.</span>
                    <span class="faq-a-text">{question}</span>
                </div>
                """, unsafe_allow_html=True)

    # ── 하단 연락처 ──
    st.markdown("""
    <div class="contact-box">
        <p>원하시는 답변을 찾지 못하셨나요?<br>
        <strong>☏ 080-357-2500</strong> (무료통화) · 평일 09:00 ~ 18:00<br>
        또는 <a href="https://www.car.go.kr/ds/online/list.do" target="_blank" style="color:#2563eb">온라인 상담</a>을 이용해 주세요.</p>
    </div>
    """, unsafe_allow_html=True)


