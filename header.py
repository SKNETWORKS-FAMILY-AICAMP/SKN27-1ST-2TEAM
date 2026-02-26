import streamlit as st

def render_header(current_page=""):
    st.markdown("""
    <style>
    @font-face {
        font-family: 'Paperlogy';
        src: url('/app/static/Paperlogy-1Thin.ttf') format('truetype');
        font-weight: 100; /* Thin */
    }

    @font-face {
        font-family: 'Paperlogy';
        src: url('/app/static/Paperlogy-3Light.ttf') format('truetype');
        font-weight: 300; /* Light */
    }

    @font-face {
        font-family: 'Paperlogy';
        src: url('/app/static/Paperlogy-5Medium.ttf') format('truetype');
        font-weight: 500; /* Medium */
    }

    @font-face {
        font-family: 'Paperlogy';
        src: url('/app/static/Paperlogy-7Bold.ttf') format('truetype');
        font-weight: 700; /* Bold */
    }

    @font-face {
        font-family: 'Paperlogy';
        src: url('/app/static/Paperlogy-8ExtraBold.ttf') format('truetype');
        font-weight: 800; /* ExtraBold */
    }
   *, *::before, *::after,
    html, body, .stApp, .stMarkdown,
    h1, h2, h3, h4, h5, h6,
    p, span, div, a, button, input, label, textarea {
        font-family: 'Paperlogy', sans-serif !important;
    }             
                

    .stMarkdown p {
    margin: 0px !important;
    padding: 0px !important;
    }

    div[data-testid="stMainBlockContainer"] {
        max-width: 100% !important;
        padding-left: 0 !important;
        padding-right: 0 !important;
    }
                
    /* Deploy 버튼 숨기기 */
    .stDeployButton { display: none !important; }

    /* 사이드바 화살표 숨기기 */
    button[data-testid="collapsedControl"] { display: none !important; }

    # /* 상단 Streamlit 메뉴 숨기기 */
    MainMenu { display: none !important; }
    header[data-testid="stHeader"] { display: none !important; }
        
    /* 1. 화살표 역할을 하는 텍스트(keyboard_arrow_down)를 투명하게 제거 */
    span[data-testid="stIconMaterial"] {
        font-size: 0px !important;
        display: none !important;
        visibility: hidden !important;
    }

    /* 2. 아이콘이 담긴 span 컨테이너의 너비까지 제거하여 글씨 쏠림 방지 */
    .st-emotion-cache-1c9yjad.exvv1vr0 {
        display: none !important;
    }     
                    
    .header-wrap {
        background: white;
        border-bottom: 1px solid #e2e8f0;
        display: flex;
        align-items: center;
        justify-content: space-between;
        height: 64px;
        margin-bottom: 32px;
        margin-top: -120px;
        padding-right: 50px;
        padding-left: 50px;

        position: sticky;
        top: 0;
        z-index: 999;
        box-shadow: 0 1px 8px rgba(0,0,0,0.06);
        
        
    }
    .header-logo {
        display: flex;
        align-items: center;
        gap: 10px;
        text-decoration: none;
        text-decoration: none !important;
    }

    .header-logo-title {
        font-size: 18px; font-weight: 900; color: #0f172a;
    }
    .header-nav {
        display: flex;
        align-items: center;
        gap: 4px;
    }
    .nav-item {
        padding: 7px 16px;
        border-radius: 8px;
        font-size: 14px;
        font-weight: 600;
        color: #64748b;
        text-decoration: none;
        transition: all 0.15s;
        text-decoration: none !important;
    }
    .nav-item:hover { background: #f1f5f9; color: #0f172a; }
    .nav-item.active {
        background: #fef2f2;
        color: #dc2626;
        text-decoration: none !important;
    }
    .nav-item-report {
        background: #dc2626;
        color: white !important;
        padding: 7px 16px;
        border-radius: 8px;
        font-size: 14px;
        font-weight: 700;
        margin-left: 8px;
        text-decoration: none !important;
    }
    .nav-item-report:hover { background: #b91c1c; }
    </style>
    """, unsafe_allow_html=True)

    pages = {
        "홈":        ("main"),
        "리콜 조회": ("check"),
        "리콜 분석": ("analysis"),
        "FAQ":       ("faq"),
    }

    nav_html = ""
    for label, (page_id) in pages.items():
        active = "active" if current_page == page_id else ""
        if page_id == "main":
            href = "/"
        else:
            href = f"/{page_id}"
        nav_html += f'<a class="nav-item {active}" href="{href}" target="_self">{label}</a>'

    # 결함신고 버튼 별도
    nav_html += '<a class="nav-item-report" href="/report" target="_self">🚨 결함신고</a>'

    st.markdown(f"""
    <div class="header-wrap">
        <a class="header-logo" href="/" target="_self">
            <span class="header-logo-title">RecallChecker</span>
        </a>
        <nav class="header-nav">
            {nav_html}
        </nav>
    </div>
    """, unsafe_allow_html=True)