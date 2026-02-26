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

# ── 국내/해외 브랜드 분류 ──
DOMESTIC_BRANDS = {
    "현대자동차(주)", "기아자동차(주)", "기아 주식회사", "기아주식회사",
    "쌍용자동차(주)", "르노삼성자동차(주)", "르노코리아(주)", "르노코리아자동차 주식회사",
    "한국지엠(주)", "한국지엠주식회사", "지엠코리아(주)",
    "케이지모빌리티 주식회사(KG Mobility Corp.)",
    "(주)다산중공업", "(주)대창모터스", "대전기계공업(주)",
    "자일대우버스 주식회사", "자일대우상용차 주식회사",
    "한국쓰리축공업(주)", "한신특장", "진일엔지니어링 주식회사",
    "범한자동차 주식회사", "마스타전기차(주)", "비바모빌리티 주식회사",
    "주식회사 마이브", "주식회사 이비온", "주식회사 젠트로피",
    "주식회사 케이에스티일렉트릭", "큐로모터스(주)", "제이스모빌리티 주식회사",
    "아이씨피(주)", "명원아이앤씨(주)", "주식회사 더좋은사람",
    "주식회사 오토스원", "케이알모터스 주식회사", "한솜바이크(주)",
    "(주)에이치알이앤아이", "바이크원", "화창상사(주)",
    "지엠아시아퍼시픽지역본부 주식회사",
}

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
    .info-banner {
        background: #eff6ff; border-left: 4px solid #2563eb;
        border-radius: 0 12px 12px 0; padding: 14px 20px;
        color: #1e40af; font-size: 13px; line-height: 1.7; margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

    # ── 데이터 로드 ──
    @st.cache_data
    def load_recall_data():
        import glob
        files = sorted(glob.glob("data/*.csv"))
        files = [f for f in files if "faq" not in f]
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
                "제작자": ["현대자동차(주)","기아자동차(주)","비엠더블유코리아(주)","현대자동차(주)","메르세데스벤츠코리아(주)"],
                "차명":   ["쏘나타","K5","520i","그랜저","E클래스"],
                "생산기간(부터)": ["2018-01-01"]*5,
                "생산기간(까지)": ["2023-12-31"]*5,
                "리콜개시일": ["2022-03-15","2023-01-01","2023-06-01","2021-09-01","2023-11-01"],
                "리콜사유": ["엔진 결함"]*5
            })
        # 국내/해외 구분 컬럼 추가
        df["구분"] = df["제작자"].apply(lambda x: "국내" if x in DOMESTIC_BRANDS else "해외")
        return df

    df = load_recall_data()

    # ── 위험도 지수 계산 ──
    @st.cache_data
    def calc_risk(df):
        tmp = df.copy()
        col_from = [c for c in tmp.columns if "부터" in c or ("from" in c.lower() and "생산" in c)][0]
        col_to   = [c for c in tmp.columns if "까지" in c or ("to" in c.lower() and "생산" in c)][0]
        tmp["_from"] = pd.to_datetime(tmp[col_from], errors="coerce")
        tmp["_to"]   = pd.to_datetime(tmp[col_to],   errors="coerce")
        tmp["생산기간(일수)"] = (tmp["_to"] - tmp["_from"]).dt.days.clip(lower=1)

        risk_df = tmp.groupby(["제작자", "차명", "구분"]).agg(
            리콜건수=("차명", "count"),
            평균생산기간=("생산기간(일수)", "mean")
        ).reset_index()

        risk_df["평균생산기간(년)"] = (risk_df["평균생산기간"] / 365).round(1)
        raw = risk_df["리콜건수"] / (risk_df["평균생산기간"] / 365)
        risk_df["위험도지수(%)"] = ((raw - raw.min()) / (raw.max() - raw.min()) * 100).round(2)

        q66 = risk_df["위험도지수(%)"].quantile(0.66)
        q33 = risk_df["위험도지수(%)"].quantile(0.33)
        risk_df["위험등급"] = risk_df["위험도지수(%)"].apply(
            lambda v: "높음" if v >= q66 else ("보통" if v >= q33 else "낮음")
        )
        return risk_df.sort_values("위험도지수(%)", ascending=False)

    risk_df = calc_risk(df)

    # ── 페이지 헤더 ──
    st.markdown("""
    <div class="page-header">
        <h1>📊 리콜 데이터 분석</h1>
        <p>국내/해외 브랜드별 리콜 현황 및 위험도 분석 결과입니다.</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    # ── 전체 통계 카드 ──
    total        = len(df)
    domestic_cnt = len(df[df["구분"] == "국내"])
    foreign_cnt  = len(df[df["구분"] == "해외"])

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
            <div class="stat-icon-orange">🇰🇷</div>
            <div><div class="stat-label">국내 브랜드 리콜</div><div class="stat-value">{domestic_cnt:,}건</div></div>
        </div>""", unsafe_allow_html=True)
    with c3:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-icon-blue">🌍</div>
            <div><div class="stat-label">해외 브랜드 리콜</div><div class="stat-value">{foreign_cnt:,}건</div></div>
        </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ── 분석 렌더링 함수 ──
    def render_analysis(filtered_df, filtered_risk, color_brand, color_car):

        # 브랜드별 & 차종별
        col_l, col_r = st.columns(2)

        with col_l:
            st.markdown('<div class="card"><div class="card-header">🏭 브랜드별 리콜 건수 TOP 10</div>', unsafe_allow_html=True)
            brand_df = filtered_df["제작자"].value_counts().head(10).reset_index()
            brand_df.columns = ["브랜드", "리콜 건수"]
            fig_brand = px.bar(brand_df, x="브랜드", y="리콜 건수",
                               text="리콜 건수", color_discrete_sequence=[color_brand])
            fig_brand.update_traces(textposition='outside', texttemplate='%{text}건')
            fig_brand.update_layout(
                height=400, margin=dict(l=10, r=10, t=10, b=10),
                xaxis_title="", yaxis_title="",
                plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)'
            )
            st.plotly_chart(fig_brand, use_container_width=True, config={'displayModeBar': False})
            for i, row in brand_df.iterrows():
                with st.expander(f"{i+1}.  {row['브랜드']}  ({row['리콜 건수']}건)"):
                    reasons = (filtered_df[filtered_df["제작자"] == row['브랜드']]
                               ["리콜사유"].dropna().value_counts().head(3))
                    for reason, cnt in reasons.items():
                        st.markdown(f"- {reason} ({cnt}건)")
            st.markdown('</div>', unsafe_allow_html=True)

        with col_r:
            st.markdown('<div class="card"><div class="card-header">🚗 차종별 리콜 건수 TOP 10</div>', unsafe_allow_html=True)
            car_df = filtered_df["차명"].value_counts().head(10).reset_index()
            car_df.columns = ["차종", "리콜 건수"]
            fig_car = px.bar(car_df, x="차종", y="리콜 건수",
                             text="리콜 건수", color_discrete_sequence=[color_car])
            fig_car.update_traces(textposition='outside', texttemplate='%{text}건')
            fig_car.update_layout(
                height=400, margin=dict(l=10, r=10, t=10, b=10),
                xaxis_title="", yaxis_title="",
                plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)'
            )


            st.plotly_chart(fig_car, use_container_width=True, config={'displayModeBar': False})
            for i, row in car_df.iterrows():
                with st.expander(f"{i+1}.  {row['차종']}  ({row['리콜 건수']}건)"):
                    reasons = (filtered_df[filtered_df["차명"] == row['차종']]
                               ["리콜사유"].dropna().value_counts().head(3))
                    for reason, cnt in reasons.items():
                        st.markdown(f"- {reason} ({cnt}건)")
            st.markdown('</div>', unsafe_allow_html=True)

       
        # 리콜 사유 키워드 분석
        st.markdown('<div class="card"><div class="card-header">🔍 주요 리콜 사유 키워드 TOP 10</div>', unsafe_allow_html=True)
        keywords = [
            "엔진", "에어백", "브레이크", "연료", "조향", "변속기", "배터리",
            "전기", "화재", "누유", "누수", "소프트웨어", "ECU", "서스펜션",
            "타이어", "시동", "가속", "냉각", "배기", "클러치", "안전벨트",
            "램프", "센서", "모터", "충전", "파손", "부식", "결함"
        ]
        text_all = " ".join(filtered_df["리콜사유"].dropna().astype(str).tolist())
        kw_counts = {kw: text_all.count(kw) for kw in keywords}
        kw_df = pd.DataFrame(list(kw_counts.items()), columns=["키워드", "빈도"])
        kw_df = kw_df[kw_df["빈도"] > 0].sort_values("빈도", ascending=False).head(10).reset_index(drop=True)

        if not kw_df.empty:
            fig_kw = px.bar(kw_df, x="키워드", y="빈도",
                            text="빈도", color_discrete_sequence=[color_brand])
            fig_kw.update_traces(textposition='outside', texttemplate='%{text}회')
            fig_kw.update_layout(
                height=350, margin=dict(l=10, r=10, t=10, b=10),
                xaxis_title="", yaxis_title="언급 횟수",
                plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)'
            )
            st.plotly_chart(fig_kw, use_container_width=True, config={'displayModeBar': False})
        else:
            st.info("키워드 데이터를 불러올 수 없습니다.")
        st.markdown('</div>', unsafe_allow_html=True)

        # 연도별 추이
        st.markdown('<div class="card"><div class="card-header">📅 연도별 리콜 건수 추이</div>', unsafe_allow_html=True)
        try:
            tmp = filtered_df.copy()
            tmp["리콜연도"] = pd.to_numeric(tmp["리콜개시일"].astype(str).str[:4], errors="coerce")
            year_df = tmp["리콜연도"].value_counts().sort_index().reset_index()
            year_df.columns = ["연도", "리콜 건수"]
            year_df = year_df[year_df["연도"] >= 2010]
            year_df["연도"] = year_df["연도"].astype(int)
            fig_year = px.line(year_df, x="연도", y="리콜 건수", markers=True, text="리콜 건수")
            fig_year.update_traces(line_color=color_brand, textposition="top center", texttemplate='%{text}건')
            fig_year.update_layout(
                height=400, margin=dict(l=20, r=20, t=30, b=20),
                xaxis=dict(tickmode='linear', dtick=1),
                xaxis_title="", yaxis_title="",
                plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)'
            )
            st.plotly_chart(fig_year, use_container_width=True, config={'displayModeBar': False})
        except:
            st.info("연도별 데이터를 불러올 수 없습니다.")
        st.markdown('</div>', unsafe_allow_html=True)

    # ── 국내 / 해외 탭 ──
    tab_domestic, tab_foreign = st.tabs(["🇰🇷  국내 브랜드", "🌍  해외 브랜드"])

    with tab_domestic:
        df_dom   = df[df["구분"] == "국내"]
        risk_dom = risk_df[risk_df["구분"] == "국내"]
        render_analysis(df_dom, risk_dom, "#dc2626", "#f97316")

    with tab_foreign:
        df_for   = df[df["구분"] == "해외"]
        risk_for = risk_df[risk_df["구분"] == "해외"]
        render_analysis(df_for, risk_for, "#2563eb", "#7c3aed")