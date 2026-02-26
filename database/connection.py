import streamlit as st
import pandas as pd
import mysql.connector

# DB연결
def get_db_connection():
    """DB 연결 객체를 반환합니다. (한 번 연결되면 재사용됨)"""
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='root1234',
        database='carReCall'
    )

# FAQ 질문 로드
@st.cache_data(ttl=600) # 10분 동안 데이터를 메모리에 보관하여 DB 부하를 줄입니다.
def get_faq_data():
    """이미 연결된 통로를 통해 쿼리만 실행합니다."""
    conn = get_db_connection()
    query = "SELECT question, answer FROM faq"
    
    # st.connection 객체의 query 메소드를 사용하면 
    # 내부적으로 커넥션 유지 및 데이터 프레임 변환까지 한 번에 처리합니다.
    df = pd.read_sql(query, conn)
    return df

# 질문 - 답변 로드
@st.cache_data(ttl=600) # 10분 동안 데이터를 메모리에 보관하여 DB 부하를 줄입니다.
def get_recall_data():
    """이미 연결된 통로를 통해 쿼리만 실행합니다."""
    conn = get_db_connection()
    query = "SELECT question, answer FROM recall"
    
    # st.connection 객체의 query 메소드를 사용하면 
    # 내부적으로 커넥션 유지 및 데이터 프레임 변환까지 한 번에 처리합니다.
    df = pd.read_sql(query, conn)
    return df

# 회사 - 차량 조회
@st.cache_data(ttl=600) # 10분 동안 데이터를 메모리에 보관하여 DB 부하를 줄입니다.
def get_recall_select_data():
    """이미 연결된 통로를 통해 쿼리만 실행합니다."""
    conn = get_db_connection()
    query = """
        SELECT 
            m.name_ko AS manufacturer_name, 
            v.model_name                              
        FROM 
            vehicle_models v
        INNER JOIN 
            manufacturers m ON v.manufacturer_id = m.manufacturer_id;
    """
    
    # st.connection 객체의 query 메소드를 사용하면 
    # 내부적으로 커넥션 유지 및 데이터 프레임 변환까지 한 번에 처리합니다.
    df = pd.read_sql(query, conn)
    return df

# 리콜 조건 조회
@st.cache_data(ttl=600)
def get_recall_history_data(name_ko, model_name, recall_start_date):
    """안전하게 파라미터를 바인딩하여 리콜 내역을 가져옵니다."""
    conn = get_db_connection()
    
    # 변수 자리에는 %s (또는 DB 드라이버에 따라 ?)를 사용합니다.
    query = """
        SELECT 
            m.name_ko AS manufacturer_name,
            v.model_name,
            r.recall_number,
            r.component,
            r.description AS recall_reason,
            YEAR(r.recall_start_date) AS recall_start_date
        FROM 
            recall_history r
        JOIN 
            vehicle_models v ON r.model_id = v.model_id
        JOIN 
            manufacturers m ON v.manufacturer_id = m.manufacturer_id
        WHERE 
            m.name_ko = %s
            AND v.model_name = %s
            AND year(r.recall_start_date) = %s;
    """
    
    try:
        # params 인자에 튜플 형태로 변수를 넘겨주면 판다스가 안전하게 처리합니다.
        df = pd.read_sql(query, conn, params=(name_ko, model_name, recall_start_date))
        return df
    except Exception as e:
        st.error(f"데이터 조회 중 오류가 발생했습니다: {e}")
        return pd.DataFrame()



# 리콜 차량 리스트 조회
@st.cache_data(ttl=600)
def get_recall_list_data(name_ko, model_name, target_year):
    """안전하게 파라미터를 바인딩하여 리콜 내역을 가져옵니다."""
    conn = get_db_connection()
    
    query = """
        SELECT 
            m.name_ko AS manufacturer_name,
            v.model_name,
            r.recall_number,
            r.component,
            r.description AS recall_reason,
            r.target_production_start_date AS start_date,
            r.target_production_end_date AS end_date,
            YEAR(r.recall_start_date) AS recall_start_date
        FROM 
            recall_history r
        JOIN 
            vehicle_models v ON r.model_id = v.model_id
        JOIN 
            manufacturers m ON v.manufacturer_id = m.manufacturer_id
        WHERE 
            m.name_ko = %s
            AND v.model_name = %s
            AND %s BETWEEN YEAR(r.target_production_start_date) AND YEAR(r.target_production_end_date);
    """
    
    try:
        # params에 target_year를 추가하여 총 3개의 인자를 넘겨줍니다.
        # 순서가 SQL 쿼리의 %s 순서와 일치해야 합니다.
        df = pd.read_sql(query, conn, params=(name_ko, model_name, target_year))
        return df
    except Exception as e:
        st.error(f"데이터 조회 중 오류가 발생했습니다: {e}")
        return pd.DataFrame()
    finally:
        # 데이터베이스 연결을 닫아주는 것이 좋습니다 (세션 관리)
        conn.close()