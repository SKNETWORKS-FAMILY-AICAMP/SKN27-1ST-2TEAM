import streamlit as st

#헤더 페이지 추가
from header import render_header



st.set_page_config(
    page_title="리콜체커 - 내 차 리콜 확인",
    page_icon="🚗",
    layout="wide"
)

render_header(current_page="main")

col_left, col_main, col_right = st.columns([1, 8, 1])
with col_main:

    st.markdown("""
    <style>
    @import url('https://cdn.jsdelivr.net/gh/webfontworld/paperlogy/Paperlogy.css');
    * { font-family: 'Paperlogy', sans-serif; }
    .stApp { background-color: #f8fafc; }
    section[data-testid="stSidebar"] {
        background-color: #ffffff;
        border-right: 1px solid #e2e8f0;
    }
    .hero {
        background: linear-gradient(135deg, #dc2626 0%, #b91c1c 50%, #7f1d1d 100%);
        border-radius: 20px;
        padding: 60px 40px;
        text-align: center;
        margin-bottom: 40px;
    }
    .hero-badge {
        display: inline-block;
        background: rgba(255,255,255,0.15);
        color: #fecaca;
        padding: 8px 20px;
        border-radius: 50px;
        font-size: 14px;
        margin-bottom: 24px;
    }
    .hero h1 { color: white; font-size: 48px; font-weight: 900; line-height: 1.2; margin-bottom: 16px; }
    .hero h1 span { color: #fca5a5; }
    .hero p { color: #fecaca; font-size: 17px; line-height: 1.8; margin-bottom: 36px; }
    .feature-card {
        background: white;
        border-radius: 16px;
        padding: 28px;
        border: 1px solid #e2e8f0;
        height: 100%;
    }
    .feature-icon {
        font-size: 28px;
        background: #fef2f2;
        width: 56px; height: 56px;
        border-radius: 14px;
        display: flex; align-items: center; justify-content: center;
        margin-bottom: 16px;
    }
    .feature-card h3 { font-size: 16px; font-weight: 700; color: #1e293b; margin-bottom: 8px; }
    .feature-card p  { font-size: 14px; color: #64748b; line-height: 1.7; }
    .cta {
        background: #0f172a;
        border-radius: 20px;
        padding: 50px 40px;
        text-align: center;
        margin-bottom: 40px;
    }
    .cta h2 { color: white; font-size: 32px; font-weight: 800; margin-bottom: 12px; }
    .cta p  { color: #94a3b8; font-size: 16px; margin-bottom: 32px; }
    </style>
    """, unsafe_allow_html=True)

    # ── Hero ──
    st.markdown("""
    <div class="hero">
        <div class="hero-badge">🚨 한국교통안전공단 리콜 데이터 기반</div>
        <h1>내 차, 리콜 대상인가요?<br><span>지금 바로 확인하세요</span></h1>
        <p>제작사와 차명, 생산연도만 입력하면<br>리콜 대상 여부를 즉시 알려드립니다.</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("🔍 리콜 대상 조회하기 →", use_container_width=False, key="hero_btn"):
        st.switch_page("pages/check.py")

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Features ──
    features = [
        ("🔍", "간편한 조회", "제작사, 차명, 생산연도만 입력하면 리콜 해당 여부를 바로 확인할 수 있어요."),
        ("📋", "리콜 사유 안내", "어떤 결함으로 리콜이 실시됐는지 상세 사유를 제공합니다."),
        ("📊", "브랜드별 분석", "어떤 브랜드와 차종에 리콜이 많은지 데이터로 분석해 드립니다."),
        ("🛡️", "공식 데이터", "한국교통안전공단의 공식 리콜 현황 데이터를 기반으로 합니다."),
    ]

    cols = st.columns(4)
    for col, (icon, title, desc) in zip(cols, features):
        with col:
            st.markdown(f"""
            <div class="feature-card">
                <div class="feature-icon">{icon}</div>
                <h3>{title}</h3>
                <p>{desc}</p>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # ── CTA ──
    st.markdown("""
    <div class="cta">
        <h2>내 차의 안전을 지금 확인하세요</h2>
        <p>리콜을 모르고 지나치면 안전에 위협이 될 수 있습니다.</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("🚗 리콜 조회 시작하기 →", use_container_width=False, key="cta_btn"):
        st.switch_page("pages/check.py")