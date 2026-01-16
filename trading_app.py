import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import platform
from matplotlib import font_manager, rc

# 1. 한글 폰트 및 마이너스 기호 설정 (그래프 한글 깨짐 방지)
plt.rcParams['axes.unicode_minus'] = False
if platform.system() == 'Windows':
    rc('font', family='Malgun Gothic')
elif platform.system() == 'Darwin': # Mac
    rc('font', family='AppleGothic')

# --- 앱 UI 제목 ---
st.title("🇮🇳 한국무역보험공사: 인도 무역보험 인수현황")
st.markdown("공공데이터포털의 인도 무역보험 관련 데이터를 분석하고 시각화합니다.")

# 파일 경로 설정 (사용자 환경에 맞게 수정)
file_path = "한국무역보험공사_인도 무역보험 인수현황_20191231.csv"

try:
    # 2. 데이터 불러오기 (보통 공공데이터 CSV는 cp949 인코딩이 많습니다)
    df = pd.read_csv(file_path, encoding='cp949')
    st.success("👌 인도 무역보험 데이터 로드 완료!")

    # 3. 데이터 미리보기
    st.subheader("📋 데이터 미리보기")
    st.write("데이터의 상위 10개 행을 확인합니다.")
    st.dataframe(df.head(10))

    # 4. 데이터 분석 및 시각화 영역
    st.divider() # 구분선
    st.subheader("📊 항목별 분포 및 수치 분석")

    # 분석할 열 선택 (수치 데이터가 있는 컬럼 선택 유도)
    column_names = df.columns.tolist()
    selected_col = st.selectbox("시각화할 항목을 선택하세요 (예: 인수금액, 건수 등)", column_names)

    # 5. 그래프 그리기 (첫 번째 코드 스타일 유지)
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # 데이터가 범주형(연도 등)인지 수치형인지에 따라 자동으로 적절한 그래프 형태 제공
    if df[selected_col].dtype in ['int64', 'float64']:
        # 수치 데이터일 경우 히스토그램 + 밀도 곡선
        sns.histplot(df[selected_col], ax=ax, color="#FF9900", kde=True)
        plt.ylabel("빈도수")
    else:
        # 문자열(범주형) 데이터일 경우 빈도수 막대 그래프
        sns.countplot(data=df, x=selected_col, ax=ax, palette="viridis")
        plt.ylabel("개수")

    plt.title(f"[{selected_col}] 항목 분석 결과", fontsize=15)
    plt.xlabel(selected_col)
    plt.xticks(rotation=45) # 라벨이 길 경우를 대비해 회전
    
    # 웹 화면에 출력
    st.pyplot(fig)

    # 6. 간단한 요약 통계
    if df[selected_col].dtype in ['int64', 'float64']:
        st.info(f"💡 {selected_col} 항목의 평균: {df[selected_col].mean():.2f}")

except FileNotFoundError:
    st.error(f"⚠️ '{file_path}' 파일을 찾을 수 없습니다. 파일명을 확인해 주세요.")
except Exception as e:
    st.error(f"⚠️ 오류가 발생했습니다: {e}")