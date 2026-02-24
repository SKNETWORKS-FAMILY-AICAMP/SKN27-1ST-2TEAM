import streamlit as st
import pandas as pd

#헤더 페이지 추가 
from header import render_header

render_header(current_page="check")

col_left, col_main, col_right = st.columns([1, 8, 1])
with col_main:
    st.set_page_config(
        page_title="리콜 조회 - 리콜체커",
        page_icon="🔍",
        layout="wide"
    )

    st.markdown("""
    <style>
    @import url('https://cdn.jsdelivr.net/gh/webfontworld/paperlogy/Paperlogy.css');
    * { font-family: 'Paperlogy', sans-serif; }
                

    .stApp { background-color: #f8fafc; }
    section[data-testid="stSidebar"] { background-color: #ffffff; border-right: 1px solid #e2e8f0; }
    .card { background: white; border-radius: 16px; padding: 28px; box-shadow: 0 4px 24px rgba(0,0,0,0.07); margin-bottom: 24px; }
    .card-header { font-size: 17px; font-weight: 700; color: #1e293b; padding-bottom: 16px; border-bottom: 1px solid #f1f5f9; margin-bottom: 20px; }
    .page-header h1 { font-size: 30px; font-weight: 800; color: #0f172a; margin-bottom: 6px; }
    .page-header p  { color: #64748b; font-size: 15px; }
    .recall-card {
        background: #fef2f2; border: 1.5px solid #fca5a5;
        border-radius: 14px; padding: 20px; margin-bottom: 16px;
    }
    .recall-card h4 { color: #991b1b; font-size: 16px; font-weight: 700; margin-bottom: 8px; }
    .recall-card p  { color: #7f1d1d; font-size: 13px; line-height: 1.7; }
    .recall-meta    { color: #b91c1c; font-size: 12px; margin-top: 10px; }
    .safe-card {
        background: #f0fdf4; border: 1.5px solid #86efac;
        border-radius: 14px; padding: 28px; text-align: center;
    }
    .safe-card h3 { color: #166534; font-size: 22px; font-weight: 800; margin-bottom: 8px; }
    .safe-card p  { color: #15803d; font-size: 15px; }
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
                "제작자": ["현대", "기아", "BMW"],
                "차명":   ["쏘나타", "K5", "520i"],
                "생산기간(부터)": ["20180101","20190101","20200101"],
                "생산기간(까지)": ["20211231","20221231","20231231"],
                "리콜개시일": ["20220315","20230101","20230601"],
                "리콜사유": ["엔진 결함","브레이크 불량","냉각수 누수"]
            })
        return df

    df = load_recall_data()

    # ── 헤더 ──
    st.markdown("""
    <div class="page-header">
        <h1>🔍 리콜 대상 조회</h1>
        <p>제작사, 차명, 생산연도를 입력하면 리콜 해당 여부를 알려드립니다.</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    # ── 입력 폼 ──
    st.markdown('<div class="card"><div class="card-header">🚗 차량 정보 입력</div>', unsafe_allow_html=True)

    manufacturers = sorted(df["제작자"].dropna().unique().tolist())
    col1, col2 = st.columns(2)
    with col1:
        manufacturer = st.selectbox("제작사", ["선택하세요"] + manufacturers)
    with col2:
        if manufacturer != "선택하세요":
            car_names = sorted(df[df["제작자"] == manufacturer]["차명"].dropna().unique().tolist())
        else:
            car_names = []
        car_name = st.selectbox("차명", ["선택하세요"] + car_names, disabled=(manufacturer == "선택하세요"))

    prod_year = st.number_input("생산연도", min_value=1990, max_value=2024, value=2020, step=1)

    st.markdown('</div>', unsafe_allow_html=True)

    is_valid = manufacturer != "선택하세요" and car_name != "선택하세요"

    if st.button("🔍 리콜 조회하기", use_container_width=True, disabled=not is_valid):
        st.session_state["check_input"] = {
            "manufacturer": manufacturer,
            "car_name": car_name,
            "prod_year": prod_year
        }
        st.rerun()

    # ── 결과 표시 ──
    if "check_input" in st.session_state:
        inp = st.session_state["check_input"]
        prod_date = int(f"{inp['prod_year']}0101")

        # 리콜 대상 필터링
        filtered = df[
            (df["제작자"] == inp["manufacturer"]) &
            (df["차명"] == inp["car_name"])
        ].copy()

        try:
            # 날짜 형식: 2021-01-01 → datetime 변환 후 비교
            filtered["생산기간(부터)"] = pd.to_datetime(filtered["생산기간(부터)"], errors="coerce")
            filtered["생산기간(까지)"] = pd.to_datetime(filtered["생산기간(까지)"], errors="coerce")
            prod_dt = pd.Timestamp(f"{inp['prod_year']}-01-01")
            prod_dt_end = pd.Timestamp(f"{inp['prod_year']}-12-31")
            recalls = filtered[
                (filtered["생산기간(부터)"] <= prod_dt_end) &
                (filtered["생산기간(까지)"] >= prod_dt)
            ]
        except Exception as e:
            st.error(f"필터링 오류: {e}")
            recalls = pd.DataFrame()

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(f"### 📋 {inp['manufacturer']} {inp['car_name']} {inp['prod_year']}년식 조회 결과")

        # 디버깅: 원본 데이터 확인
        with st.expander("🔧 해당 차량의 리콜 현황 "):
            # st.markdown(f"제작사: {inp['manufacturer']}  \n차명: {inp['car_name']}  \n생산연도: {inp['prod_year']}")
            # st.write(f"prod_date: {prod_date}")
            raw = df[(df["제작자"] == inp["manufacturer"]) & (df["차명"] == inp["car_name"])]
            st.write(f"동일 차 명 데이터 {len(raw)}건")
            if len(raw) > 0:
                st.dataframe(raw[["제작자","차명","생산기간(부터)","생산기간(까지)","리콜개시일"]].head(5))

        if len(recalls) > 0:
            st.error(f"⚠️ **리콜 대상 차량입니다!** 총 {len(recalls)}건의 리콜이 확인되었습니다.")
            for _, row in recalls.iterrows():
                recall_date = str(row.get("리콜개시일", ""))
                if len(recall_date) == 8:
                    recall_date = f"{recall_date[:4]}.{recall_date[4:6]}.{recall_date[6:]}"
                st.markdown(f"""
                <div class="recall-card">
                    <h4>🚨 리콜 사유</h4>
                    <p>{row.get('리콜사유', '정보 없음')}</p>
                    <div class="recall-meta">📅 리콜 개시일: {recall_date}</div>
                </div>
                """, unsafe_allow_html=True)
            st.warning("👉 가까운 서비스센터 또는 제작사에 연락하여 리콜 시정을 받으세요.")
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("🚨 결함신고 하기", type="primary", use_container_width=True):
                st.switch_page("pages/report.py")
        else:
            st.markdown("""
            <div class="safe-card">
                <h3>✅ 리콜 대상이 아닙니다</h3>
                <p>해당 차량은 현재 등록된 리콜 대상에 해당하지 않습니다.<br>
                데이터는 2023년 12월 기준입니다.</p>
            </div>
            """, unsafe_allow_html=True)

    if not is_valid:
        st.caption("⚠️ 제작사와 차명을 모두 선택해야 조회할 수 있습니다.")