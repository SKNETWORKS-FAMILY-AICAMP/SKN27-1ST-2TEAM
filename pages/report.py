import streamlit as st

#헤더 페이지 추가 
from header import render_header



st.set_page_config(
    page_title="결함신고 - 리콜체커",
    page_icon="🚨",
    layout="wide"
)
render_header(current_page="report")

col_left, col_main, col_right = st.columns([1, 8, 1])
with col_main:

    st.markdown("""
    <style>
    @import url('https://cdn.jsdelivr.net/gh/webfontworld/paperlogy/Paperlogy.css');
    * { font-family: 'Paperlogy', sans-serif; }
    .stApp { background-color: #f8fafc; }
    section[data-testid="stSidebar"] { background-color: #ffffff; border-right: 1px solid #e2e8f0; }

    .page-header h1 { font-size: 30px; font-weight: 800; color: #0f172a; margin-bottom: 6px; }
    .page-header p  { color: #64748b; font-size: 15px; }

    .info-box {
        background: #fef2f2; border-left: 4px solid #dc2626;
        border-radius: 0 12px 12px 0; padding: 20px 24px; margin-bottom: 24px;
    }
    .info-box h4 { color: #991b1b; font-size: 15px; font-weight: 700; margin-bottom: 12px; }
    .info-box ul { color: #7f1d1d; font-size: 13px; line-height: 2; margin: 0; padding-left: 20px; }

    .exclude-box {
        background: #fff7ed; border-left: 4px solid #f97316;
        border-radius: 0 12px 12px 0; padding: 20px 24px; margin-bottom: 24px;
    }
    .exclude-box h4 { color: #9a3412; font-size: 15px; font-weight: 700; margin-bottom: 12px; }
    .exclude-box ul { color: #7c2d12; font-size: 13px; line-height: 2; margin: 0; padding-left: 20px; }

    .contact-box {
        background: #eff6ff; border-left: 4px solid #2563eb;
        border-radius: 0 12px 12px 0; padding: 16px 24px; margin-bottom: 24px;
    }
    .contact-box p { color: #1e40af; font-size: 14px; margin: 0; }

    .card { background: white; border-radius: 16px; padding: 28px; box-shadow: 0 4px 24px rgba(0,0,0,0.07); margin-bottom: 24px; }
    .card-header { font-size: 17px; font-weight: 700; color: #1e293b; padding-bottom: 16px; border-bottom: 1px solid #f1f5f9; margin-bottom: 20px; }

    .agree-item {
        background: #f8fafc; border: 1px solid #e2e8f0;
        border-radius: 10px; padding: 16px; margin-bottom: 12px;
    }
    .agree-item p { font-size: 13px; color: #475569; line-height: 1.7; margin-bottom: 10px; }

    .step-badge {
        display: inline-block;
        background: #dc2626; color: white;
        font-size: 12px; font-weight: 700;
        padding: 3px 10px; border-radius: 20px; margin-bottom: 8px;
    }
    .success-box {
        background: #f0fdf4; border: 1.5px solid #86efac;
        border-radius: 16px; padding: 40px; text-align: center;
    }
    .success-box h2 { color: #166534; font-size: 26px; font-weight: 800; margin-bottom: 12px; }
    .success-box p  { color: #15803d; font-size: 15px; line-height: 1.8; }
    </style>
    """, unsafe_allow_html=True)

    # ── 헤더 ──
    st.markdown("""
    <div class="page-header">
        <h1>🚨 결함신고</h1>
        <p>자동차가 안전기준에 적합하지 않거나 안전운행에 지장을 주는 결함이 있는 경우 신고합니다.</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    # ── 단계 관리 ──
    if "report_step" not in st.session_state:
        st.session_state["report_step"] = 1

    step = st.session_state["report_step"]

    # ── STEP 1: 신고 안내 ──
    if step == 1:
        st.markdown('<div class="step-badge">STEP 1 / 3 &nbsp; 신고 안내</div>', unsafe_allow_html=True)

        st.markdown("""
        <div class="info-box">
            <h4>📌 자동차 제작결함이란?</h4>
            <ul>
                <li>자동차안전기준 또는 부품안전기준에 적합하지 않은 경우</li>
                <li>설계, 제조 또는 성능상의 문제로 안전에 지장을 주는 결함</li>
                <li>다수의 같은 종류 자동차에서 <strong>공통적</strong>으로 나타나는 문제</li>
                <li>사망 또는 부상 등 인명 피해를 초래하거나 우려가 있는 문제</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="exclude-box">
            <h4>⚠️ 리콜 대상에서 제외되는 사항 (일부 예시)</h4>
            <ul>
                <li>승객 편의장치(에어컨, 오디오, 내비게이션 등)의 품질 불량</li>
                <li>주기적 점검·교환이 필요한 소모성 부품</li>
                <li>차체 도색 불량 및 단순 녹 발생</li>
                <li>주행 시 소음, 차체 진동 등 안전과 직접 연관 없는 현상</li>
                <li>차량 관리 소홀로 인해 발생되는 고장</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="contact-box">
            <p>📞 온라인 신고가 불편할 경우 <strong>☏ 080-357-2500</strong> (무료통화)를 이용해 주세요.</p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("다음 단계 →", use_container_width=True, type="primary"):
            st.session_state["report_step"] = 2
            st.rerun()

    # ── STEP 2: 동의 ──
    elif step == 2:
        st.markdown('<div class="step-badge">STEP 2 / 3 &nbsp; 약관 동의</div>', unsafe_allow_html=True)
        st.markdown('<div class="card"><div class="card-header">✅ 아래 내용을 확인 후 동의해주세요</div>', unsafe_allow_html=True)

        agrees = [
            ("agree1", "리콜센터는 일정기간 모니터링 후 분석·조사·심의 과정에서 상당기간이 소요될 수 있습니다."),
            ("agree2", "리콜센터는 결함정보를 수집하는 기관으로, 개인 차량 불만사항의 해결 또는 중재를 하지 않습니다."),
            ("agree3", "신고 내용 확인을 위해 신고자의 개인정보(전화번호, 주소 제외)를 자동차 제작사와 공유할 수 있습니다."),
            ("agree4", "폭언 등 적정 범위를 벗어난 행위가 있을 경우 산업안전보건법에 따라 상담이 종료될 수 있습니다."),
        ]

        all_agreed = True
        for key, text in agrees:
            st.markdown(f'<div class="agree-item"><p>{text}</p>', unsafe_allow_html=True)
            val = st.checkbox("동의합니다", key=key)
            if not val:
                all_agreed = False
            st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            if st.button("← 이전", use_container_width=True):
                st.session_state["report_step"] = 1
                st.rerun()
        with col2:
            if st.button("다음 단계 →", use_container_width=True, type="primary", disabled=not all_agreed):
                st.session_state["report_step"] = 3
                st.rerun()

    # ── STEP 3: 신고 등록 ──
    elif step == 3:
        st.markdown('<div class="step-badge">STEP 3 / 3 &nbsp; 결함신고 등록</div>', unsafe_allow_html=True)

        # 조회 결과에서 차량 정보 자동 입력
        check_input = st.session_state.get("check_input", {})

        st.markdown('<div class="card"><div class="card-header">🚗 차량 정보</div>', unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            manufacturer = st.text_input("제작사", value=check_input.get("manufacturer", ""))
            car_name     = st.text_input("차명",   value=check_input.get("car_name", ""))
        with col2:
            prod_year = st.number_input("생산연도", min_value=1990, max_value=2024,
                                        value=int(check_input.get("prod_year", 2020)))
            vin = st.text_input("차대번호 (선택)", placeholder="예: KMHXX00XXXX000000")
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="card"><div class="card-header">👤 신고자 정보</div>', unsafe_allow_html=True)
        col3, col4 = st.columns(2)
        with col3:
            reporter_name  = st.text_input("성명 *", placeholder="홍길동")
            reporter_phone = st.text_input("연락처 *", placeholder="010-0000-0000")
        with col4:
            reporter_email = st.text_input("이메일 (선택)", placeholder="example@email.com")
            reporter_addr  = st.text_input("주소 (선택)", placeholder="시/도 시/군/구")
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="card"><div class="card-header">📋 결함 내용</div>', unsafe_allow_html=True)
        defect_part = st.selectbox("결함 부위", [
            "선택하세요", "엔진", "변속기", "제동장치", "조향장치", "연료장치",
            "에어백", "전기·전자장치", "차체", "기타"
        ])
        defect_symptom = st.text_area("결함 증상 *", placeholder="결함 증상을 구체적으로 입력해주세요.\n예: 주행 중 엔진이 갑자기 꺼지는 현상이 반복적으로 발생함", height=120)
        defect_date    = st.date_input("결함 발생일")
        defect_mileage = st.text_input("결함 발생 시 주행거리 (km)", placeholder="예: 45000")
        accident       = st.radio("사고 발생 여부", ["없음", "있음"], horizontal=True)
        if accident == "있음":
            st.text_area("사고 내용", placeholder="사고 내용을 입력해주세요", height=80)
        st.markdown('</div>', unsafe_allow_html=True)

        is_valid = all([
            manufacturer.strip(), car_name.strip(),
            reporter_name.strip(), reporter_phone.strip(),
            defect_part != "선택하세요", defect_symptom.strip()
        ])

        col_b1, col_b2 = st.columns(2)
        with col_b1:
            if st.button("← 이전", use_container_width=True):
                st.session_state["report_step"] = 2
                st.rerun()
        with col_b2:
            if st.button("🚨 결함신고 접수", use_container_width=True, type="primary", disabled=not is_valid):
                st.session_state["report_step"] = 4
                st.rerun()

        if not is_valid:
            st.caption("⚠️ * 표시된 항목은 필수 입력 사항입니다.")

    # ── STEP 4: 완료 ──
    elif step == 4:
        st.markdown("""
        <div class="success-box">
            <h2>✅ 결함신고가 접수되었습니다</h2>
            <p>신고해 주셔서 감사합니다.<br>
            접수된 내용은 한국교통안전공단에서 검토 후 처리됩니다.<br><br>
            문의사항은 <strong>☏ 080-357-2500</strong> (무료통화)로 연락해 주세요.</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🔍 리콜 조회로 돌아가기", use_container_width=False):
            st.session_state["report_step"] = 1
            st.switch_page("pages/check.py")