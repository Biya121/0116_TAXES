import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import platform
from matplotlib import font_manager, rc

# --- [필수] 폰트 설정을 최상단에 배치 (India 코드 방식) ---
plt.rcParams['axes.unicode_minus'] = False 
if platform.system() == 'Windows':
    rc('font', family='Malgun Gothic')
elif platform.system() == 'Darwin': # Mac
    rc('font', family='AppleGothic')
else:
    # 리눅스/서버 환경 대비
    rc('font', family='NanumGothic')

# --- 앱 UI 제목 ---
st.title("🎬 영화 상세정보 통합 분석기")
st.markdown("영화별 매출, 관객수 및 장르 분포를 시각화하여 분석합니다.")

# 파일 경로 (파일명이 정확해야 합니다)
file_path = "영화상세정보(통합)_1129.csv"

try:
    # 1. 데이터 불러오기
    # 영화 데이터는 파일에 따라 인코딩이 'utf-8' 혹은 'cp949'일 수 있습니다.
    df = pd.read_csv(file_path, encoding='cp949')
    st.success("👌 영화 데이터 로드 성공!")

    # 2. 데이터 미리보기
    st.subheader("📋 데이터 미리보기")
    st.dataframe(df.head(10))

    # 3. 항목 선택 및 시각화
    st.divider()
    st.subheader("📊 데이터 시각화 분석")

    column_names = df.columns.tolist()
    selected_col = st.selectbox("분석하고 싶은 항목을 선택하세요", column_names)

    # 4. 그래프 그리기 (ax 객체 사용으로 한글 깨짐 방지)
    fig, ax = plt.subplots(figsize=(12, 6))

    # 데이터 타입에 따른 자동 그래프 선택
    if df[selected_col].dtype in ['int64', 'float64']:
        # 숫자 데이터 (예: 매출액, 관객수) -> 히스토그램
        sns.histplot(df[selected_col], ax=ax, color="#1E90FF", kde=True)
        ax.set_ylabel("빈도수")
    else:
        # 문자 데이터 (예: 장르, 제작국가) -> 막대 그래프 (상위 15개만)
        top_n = df[selected_col].value_counts().head(15)
        sns.barplot(x=top_n.index, y=top_n.values, ax=ax, palette="coolwarm")
        ax.set_ylabel("데이터 개수")
        plt.xticks(rotation=45) # 라벨이 겹치지 않게 회전

    # 제목 및 축 설정 (한글 적용)
    ax.set_title(f"[{selected_col}] 항목 분석 결과", fontsize=16)
    ax.set_xlabel(selected_col)
    
    # Streamlit 화면 출력
    st.pyplot(fig)

    # 5. 요약 정보
    if df[selected_col].dtype in ['int64', 'float64']:
        st.info(f"💡 {selected_col} 총합: {df[selected_col].sum():,.0f} / 평균: {df[selected_col].mean():,.2f}")

except FileNotFoundError:
    st.error(f"⚠️ '{file_path}' 파일을 찾을 수 없습니다. 파일명을 다시 확인해주세요.")
except Exception as e:
    st.error(f"⚠️ 오류가 발생했습니다: {e}")