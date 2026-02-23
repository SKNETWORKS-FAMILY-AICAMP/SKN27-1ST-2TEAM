import streamlit as st

st.set_page_config(
    page_title="CarPricer - 중고차 가격 예측",
    page_icon="🚗",
    layout="wide"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;600;700;900&display=swap');

* { font-family: 'Noto Sans KR', sans-serif; }

/* 전체 배경 */
.stApp {
    background-color: #f8fafc;
}

/* 사이드바 */
section[data-testid="stSidebar"] {
    background-color: #ffffff;
    border-right: 1px solid #e2e8f0;
}

/* Hero Section */
.hero {
    background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 50%, #3730a3 100%);
    border-radius: 20px;
    padding: 60px 40px;
    text-align: center;
    position: relative;
    overflow: hidden;
    margin-bottom: 40px;
}
.hero::before {
    content: '';
    position: absolute;
    top: -50px; left: -50px;
    width: 200px; height: 200px;
    background: rgba(255,255,255,0.05);
    border-radius: 50%;
}
.hero::after {
    content: '';
    position: absolute;
    bottom: -80px; right: -50px;
    width: 300px; height: 300px;
    background: rgba(147,197,253,0.1);
    border-radius: 50%;
}
.hero-badge {
    display: inline-block;
    background: rgba(255,255,255,0.15);
    backdrop-filter: blur(10px);
    color: #bfdbfe;
    padding: 8px 20px;
    border-radius: 50px;
    font-size: 14px;
    margin-bottom: 24px;
}
.hero h1 {
    color: white;
    font-size: 52px;
    font-weight: 900;
    line-height: 1.2;
    margin-bottom: 20px;
}
.hero h1 span {
    color: #bfdbfe;
}
.hero p {
    color: #bfdbfe;
    font-size: 18px;
    line-height: 1.8;
    margin-bottom: 36px;
}

/* 버튼 */
.hero-btn {
    display: inline-block;
    background: white;
    color: #1d4ed8;
    padding: 16px 36px;
    border-radius: 14px;
    font-size: 18px;
    font-weight: 700;
    text-decoration: none;
    box-shadow: 0 20px 40px rgba(0,0,0,0.2);
    cursor: pointer;
}

/* Feature 카드 */
.feature-section {
    margin-bottom: 40px;
}
.feature-title {
    text-align: center;
    font-size: 32px;
    font-weight: 800;
    color: #0f172a;
    margin-bottom: 8px;
}
.feature-subtitle {
    text-align: center;
    color: #64748b;
    font-size: 16px;
    margin-bottom: 32px;
}
.feature-card {
    background: white;
    border-radius: 16px;
    padding: 28px;
    border: 1px solid #e2e8f0;
    height: 100%;
    transition: all 0.3s;
}
.feature-icon {
    font-size: 32px;
    margin-bottom: 16px;
    background: #eff6ff;
    width: 56px; height: 56px;
    border-radius: 14px;
    display: flex;
    align-items: center;
    justify-content: center;
}
.feature-card h3 {
    font-size: 17px;
    font-weight: 700;
    color: #1e293b;
    margin-bottom: 8px;
}
.feature-card p {
    font-size: 14px;
    color: #64748b;
    line-height: 1.7;
}

/* CTA Section */
.cta {
    background: #0f172a;
    border-radius: 20px;
    padding: 60px 40px;
    text-align: center;
    margin-bottom: 40px;
}
.cta h2 {
    color: white;
    font-size: 36px;
    font-weight: 800;
    margin-bottom: 16px;
}
.cta p {
    color: #94a3b8;
    font-size: 17px;
    margin-bottom: 32px;
}
.cta-btn {
    display: inline-block;
    background: #2563eb;
    color: white;
    padding: 16px 36px;
    border-radius: 14px;
    font-size: 17px;
    font-weight: 700;
    text-decoration: none;
}
</style>
""", unsafe_allow_html=True)

# ── Hero Section ──
st.markdown("""
<div class="hero">
    <div class="hero-badge">🚗 중고차 옵션 기반 가격 예측 시스템</div>
    <h1>내 차의 진짜 가치,<br><span>CarPricer</span>가 알려드립니다</h1>
    <p>제조사, 모델, 옵션까지 꼼꼼히 분석하여<br>정확한 중고차 시세를 예측해 드립니다.</p>
</div>
""", unsafe_allow_html=True)

if st.button("🔍 가격 예측 시작하기 →", use_container_width=False, key="hero_btn"):
    st.switch_page("pages/prediction.py")

st.markdown("<br>", unsafe_allow_html=True)

# ── Features Section ──
st.markdown("""
<div class="feature-title">왜 CarPricer인가요?</div>
<div class="feature-subtitle">데이터 기반의 정확한 분석으로 합리적인 거래를 도와드립니다.</div>
""", unsafe_allow_html=True)

features = [
    ("📈", "정확한 가격 예측", "실제 시장 데이터 기반으로 중고차 적정 가격을 예측합니다."),
    ("✨", "옵션별 가치 분석", "각 옵션이 차량 가격에 미치는 영향을 상세히 분석합니다."),
    ("📊", "시장 데이터 분석", "제조사별, 연식별 가격 트렌드를 한눈에 확인하세요."),
    ("🛡️", "신뢰할 수 있는 정보", "실제 거래 데이터를 기반으로 투명한 정보를 제공합니다."),
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

# ── CTA Section ──
st.markdown("""
<div class="cta">
    <h2>지금 바로 내 차 가격을 확인하세요</h2>
    <p>간단한 정보 입력만으로 정확한 시세를 예측받을 수 있습니다.</p>
</div>
""", unsafe_allow_html=True)

if st.button("무료로 가격 예측하기 →", use_container_width=False, key="cta_btn"):
    st.switch_page("pages/prediction.py")
