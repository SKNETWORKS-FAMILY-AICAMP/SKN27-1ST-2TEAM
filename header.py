import streamlit as st

def render_header(current_page=""):
    st.markdown("""
    <style>
    @import url('https://cdn.jsdelivr.net/gh/webfontworld/paperlogy/Paperlogy.css');
* { font-family: 'Paperlogy', sans-serif; }
                
    div[data-testid="stMainBlockContainer"] {
        max-width: 100% !important;
        padding-left: 0 !important;
        padding-right: 0 !important;
    }
    
    
                
    .header-wrap {
        background: white;
        border-bottom: 1px solid #e2e8f0;
        display: flex;
        align-items: center;
        justify-content: space-between;
        height: 64px;
        margin-bottom: 32px;
        margin-top: -60px;
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