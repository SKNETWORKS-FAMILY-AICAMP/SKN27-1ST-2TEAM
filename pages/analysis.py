import streamlit as st
import pandas as pd
import plotly.express as px

#헤더 페이지 추가 
from header import render_header

st.set_page_config(
    page_title="리콜 분석 - 리콜체커",
    page_icon="📊",
    layout="wide"
)

render_header(current_page="analysis")

col_left, col_main, col_right = st.columns([1, 8, 1])
with col_main:

    st.markdown("""
    <style>
    @import url('https://cdn.jsdelivr.net/gh/webfontworld/paperlogy/Paperlogy.css');
    * { font-family: 'Paperlogy', sans-serif; }
                


    .stApp { background-color: #f8fafc; }
                
    section[data-testid="stSidebar"] { background-color: #ffffff; border-right: 1px solid #e2e8f0; }
    .card { background: white; border-radius: 16px; padding: 28px; box-shadow: 0 4px 24px rgba(0,0,0,0.07); margin-bottom: 24px; }
    .card-header { font-size: 17px; font-weight: 700; color: #1e293b; padding-bottom: 16px; }
    .stat-card { background: white; border-radius: 16px; padding: 24px; box-shadow: 0 4px 24px rgba(0,0,0,0.07); display: flex; align-items: center; gap: 16px; }
    .stat-icon-red    { background:#fef2f2; width:56px; height:56px; border-radius:14px; display:flex; align-items:center; justify-content:center; font-size:26px; }
    .stat-icon-orange { background:#fff7ed; width:56px; height:56px; border-radius:14px; display:flex; align-items:center; justify-content:center; font-size:26px; }
    .stat-icon-blue   { background:#eff6ff; width:56px; height:56px; border-radius:14px; display:flex; align-items:center; justify-content:center; font-size:26px; }
    .stat-label { font-size:13px; color:#64748b; margin-bottom:4px; }
    .stat-value { font-size:24px; font-weight:800; color:#0f172a; }
    .page-header h1 { font-size: 30px; font-weight: 800; color: #0f172a; margin-bottom: 6px; }
    .page-header p  { color: #64748b; font-size: 15px; }
    .rank-item {
        display: flex; align-items: center; gap: 12px;
        padding: 10px 0; border-bottom: 1px solid #f1f5f9;
    }
    .rank-num { font-size: 18px; font-weight: 900; color: #dc2626; width: 28px; }
    .rank-name { flex: 1; font-size: 15px; font-weight: 600; color: #1e293b; }
    .rank-count { font-size: 14px; color: #64748b; }
    </style>
    """, unsafe_allow_html=True)

    # ── 데이터 로드 ──
    @st.cache_data
    def load_recall_data():
        import glob
        files = sorted(glob.glob("data/*.csv"))
        dfs = []
        for f in files:
            for enc in ["cp949", "utf-8", "euc-kr"]:
                try:
                    tmp = pd.read_csv(f, encoding=enc)
                    dfs.append(tmp)
                    break
                except:
                    continue
        if dfs:
            df = pd.concat(dfs, ignore_index=True)
            df.columns = df.columns.str.strip()
            df = df.drop_duplicates()
        else:
            df = pd.DataFrame({
                "제작자": ["현대","기아","BMW","현대","기아","벤츠","도요타","현대","기아","BMW"],
                "차명":   ["쏘나타","K5","520i","그랜저","쏘렌토","E클래스","캠리","아반떼","K3","320i"],
                "생산기간(부터)": ["20180101"]*10,
                "생산기간(까지)": ["20231231"]*10,
                "리콜개시일": ["20220315","20230101","20230601","20210901","20231101","20220401","20220701","20230201","20221001","20230301"],
                "리콜사유": ["엔진 결함"]*10
            })
        return df
    df = load_recall_data()

    # ── 헤더 ──
    st.markdown("""
    <div class="page-header">
        <h1>📊 리콜 데이터 분석</h1>
        <p>브랜드별, 차종별 리콜 현황을 분석한 결과입니다.</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    # ── 통계 카드 ──
    total = len(df)
    brand_count = df["제작자"].nunique()
    car_count   = df["차명"].nunique()

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-icon-red">🚨</div>
            <div><div class="stat-label">전체 리콜 건수</div><div class="stat-value">{total:,}건</div></div>
        </div>""", unsafe_allow_html=True)
    with c2:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-icon-orange">🏭</div>
            <div><div class="stat-label">리콜 발생 브랜드 수</div><div class="stat-value">{brand_count}개</div></div>
        </div>""", unsafe_allow_html=True)
    with c3:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-icon-blue">🚗</div>
            <div><div class="stat-label">리콜 발생 차종 수</div><div class="stat-value">{car_count}개</div></div>
        </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ── 브랜드별 & 차종별 ──
    col_left, col_right = st.columns(2)

    with col_left:
        st.markdown('<div class="card"><div class="card-header">🏭 브랜드별 리콜 건수 TOP 10</div>', unsafe_allow_html=True)
        brand_df = df["제작자"].value_counts().head(10).reset_index()
        brand_df.columns = ["브랜드", "리콜 건수"]
        
        # Plotly Bar Chart로 교체
        fig_brand = px.bar(brand_df, x="브랜드", y="리콜 건수", 
                        text="리콜 건수", # 막대 위에 숫자 표시
                        color_discrete_sequence=["#dc2626"])
        fig_brand.update_traces(textposition='outside', texttemplate='%{text}건')
        fig_brand.update_layout(
            height=400, margin=dict(l=10, r=10, t=10, b=10),
            xaxis_title="", yaxis_title="",
            plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)'
        )
        st.plotly_chart(fig_brand, use_container_width=True, config={'displayModeBar': False})

        # 순위 리스트 (기본 코드 유지)
        for i, row in brand_df.iterrows():
            st.markdown(f"""
            <div class="rank-item">
                <div class="rank-num">{i+1}</div>
                <div class="rank-name">{row['브랜드']}</div>
                <div class="rank-count">{row['리콜 건수']}건</div>
            </div>""", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col_right:
        st.markdown('<div class="card"><div class="card-header">🚗 차종별 리콜 건수 TOP 10</div>', unsafe_allow_html=True)
        car_df = df["차명"].value_counts().head(10).reset_index()
        car_df.columns = ["차종", "리콜 건수"]
        
        # Plotly Bar Chart로 교체
        fig_car = px.bar(car_df, x="차종", y="리콜 건수", 
                        text="리콜 건수", 
                        color_discrete_sequence=["#f97316"])
        fig_car.update_traces(textposition='outside', texttemplate='%{text}건')
        fig_car.update_layout(
            height=400, margin=dict(l=10, r=10, t=10, b=10),
            xaxis_title="", yaxis_title="",
            plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)'
        )
        st.plotly_chart(fig_car, use_container_width=True, config={'displayModeBar': False})

        # 순위 리스트 (기본 코드 유지)
        for i, row in car_df.iterrows():
            st.markdown(f"""
            <div class="rank-item">
                <div class="rank-num">{i+1}</div>
                <div class="rank-name">{row['차종']}</div>
                <div class="rank-count">{row['리콜 건수']}건</div>
            </div>""", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # ── 연도별 리콜 추이 ──
    st.markdown('<div class="card"><div class="card-header">📅 연도별 리콜 건수 추이</div>', unsafe_allow_html=True)
    try:
        df["리콜연도"] = pd.to_numeric(df["리콜개시일"].astype(str).str[:4], errors="coerce")
        year_df = df["리콜연도"].value_counts().sort_index().reset_index()
        year_df.columns = ["연도", "리콜 건수"]
        year_df = year_df[year_df["연도"] >= 2010]
        year_df["연도"] = year_df["연도"].astype(int)

        # Plotly Line Chart로 교체
        fig_year = px.line(year_df, x="연도", y="리콜 건수", markers=True, text="리콜 건수")
        fig_year.update_traces(
            line_color="#dc2626", 
            textposition="top center", 
            texttemplate='%{text}건'
        )
        fig_year.update_layout(
            height=400, margin=dict(l=20, r=20, t=30, b=20),
            xaxis=dict(tickmode='linear', dtick=1), # 연도별로 축 눈금 표시
            xaxis_title="", yaxis_title="",
            plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)'
        )
        st.plotly_chart(fig_year, use_container_width=True, config={'displayModeBar': False})
    except:
        st.info("연도별 데이터를 불러올 수 없습니다.")
    st.markdown('</div>', unsafe_allow_html=True)