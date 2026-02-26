import streamlit as st
import pandas as pd
from database.connection import (
    get_recall_select_data,
    get_recall_history_data,
    get_recall_list_data,
)

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

    # DB 연결 회사 - 차량 조회
    df = get_recall_select_data()

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

    manufacturers = sorted(df["manufacturer_name"].dropna().unique().tolist())
    col1, col2 = st.columns(2)
    with col1:
        manufacturer = st.selectbox("제작사", ["선택하세요"] + manufacturers)
    with col2:
        if manufacturer != "선택하세요":
            car_names = sorted(df[df["manufacturer_name"] == manufacturer]["model_name"].dropna().unique().tolist())
        else:
            car_names = []
        car_name = st.selectbox("차명", ["선택하세요"] + car_names, disabled=(manufacturer == "선택하세요"))

    prod_year = st.number_input("생산연도", min_value=1990, max_value=2024, value=2020, step=1)

    st.markdown('</div>', unsafe_allow_html=True)

    is_valid = manufacturer != "선택하세요" and car_name != "선택하세요"

    if st.button("🔍 리콜 조회하기", use_container_width=True, disabled=not is_valid):
        st.session_state["check_params"] = {
            "manufacturer": manufacturer,
            "car_name": car_name,
            "prod_year": prod_year
        }
        st.rerun()

    # ── 결과 표시 ──
    if "check_params" in st.session_state:
        params = st.session_state["check_params"]
        target_mfg = params["manufacturer"]
        target_model = params["car_name"]
        target_year = params["prod_year"]

        # DB에서 리콜 내역 가져오기
        recalls = get_recall_history_data(target_mfg, target_model, target_year)

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(f"### 📋 {target_mfg} {target_model} ({target_year}년식) 조회 결과")

        recalls_list = get_recall_list_data(target_mfg, target_model)
        
        # 해당 모델 전체 리콜 리스트
        with st.expander(f"📚 {target_model} 모델의 전체 리콜 이력 (총 {len(recalls_list)}건)"):
            if not recalls_list.empty:
                st.dataframe(
                    recalls_list[["recall_start_date", "recall_reason"]],
                    column_config={
                        "recall_start_date": "리콜시작연도",
                        "recall_reason": "리콜사유"
                    },
                    use_container_width=True,
                    hide_index=True
                )
            else:
                st.info("등록된 리콜 이력이 없습니다.")

        if not recalls.empty:
            st.error(f"⚠️ **리콜 대상 차량입니다!** 총 {len(recalls)}건의 리콜이 확인되었습니다.")
            for _, row in recalls.iterrows():
                # recall_start_date가 연도만 가져오고 있으므로 그대로 출력하거나 보완
                st.markdown(f"""
                <div class="recall-card">
                    <p><strong>내용:</strong> {row.get('recall_reason', '정보 없음')}</p>
                    <div class="recall-meta">🔢 리콜 번호: {row.get('recall_number', '정보 없음')} | 📅 리콜 시작 연도: {row.get('recall_start_date')}</div>
                </div>
                """, unsafe_allow_html=True)
            
            st.warning("👉 가까운 서비스센터 또는 제작사에 연락하여 리콜 시정을 받으세요.")
            if st.button("🚨 결함신고 하기", type="primary", use_container_width=True):
                st.switch_page("pages/report.py")
        else:
            # 리콜 내역이 없는 경우
            st.markdown("""
            <div class="safe-card" style="text-align: center; padding: 30px; background-color: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 15px;">
                <h3 style="color: #16a34a; margin-bottom: 10px;">✅ 리콜 대상이 아닙니다</h3>
                <p style="color: #166534;">해당 차량은 현재 등록된 리콜 내역이 없습니다.</p>
            </div>
            """, unsafe_allow_html=True)

    if not is_valid:
        st.caption("⚠️ 제작사와 차명을 모두 선택해야 조회할 수 있습니다.")
