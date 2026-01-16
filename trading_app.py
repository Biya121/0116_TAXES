import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import platform
import os  # [추가] 경로 확인용
from matplotlib import font_manager, rc

# --- [수정 1] Streamlit Cloud 및 로컬 환경 통합 폰트 설정 ---
def setup_korean_font():
    plt.rcParams['axes.unicode_minus'] = False # 마이너스 기호 깨짐 방지
    
    try:
        if platform.system() == 'Windows':
            # 로컬 윈도우용
            rc('font', family='Malgun Gothic')
        elif platform.system() == 'Darwin':
            # 로컬 맥용 (Apple Silicon 포함)
            rc('font', family='AppleGothic')
        else:
            # --- Streamlit Cloud (Linux) 서버 환경 핵심 설정 ---
            # 1. 시스템에 설치된 나눔고딕을 우선 적용 (packages.txt 필요)
            rc('font', family='NanumGothic')
            
            # 2. 경로를 직접 지정하여 폰트 로드 (더 확실한 방법)
            font_path = "/usr/share/fonts/truetype/nanum/NanumGothic.ttf"
            if os.path.exists(font_path):
                font_name = font_manager.FontProperties(fname=font_path).get_name()
                rc('font', family=font_name)
    except Exception as e:
        print(f"폰트 설정 실패: {e}")

# 앱 실행 시 가장 먼저 폰트 설정 호출
setup_korean_font()

# --- 앱 UI 제목 ---
st.title("🇮🇳 한국무역보험공사: 인도 무역보험 인수현황")
st.markdown("공공데이터포털의 인도 무역보험 관련 데이터를 분석하고 시각화합니다.")

# 파일 경로 설정
file_path = "한국무역보험공사_인도 무역보험 인수현황_20191231.csv"

try:
    # 2. 데이터 불러오기 (cp949 인코딩 유지)
    df = pd.read_csv(file_path, encoding='cp949')
    st.success("👌 인도 무역보험 데이터 로드 완료!")

    # 3. 데이터 미리보기
    st.subheader("📋 데이터 미리보기")
    st.dataframe(df.head(10))

    # 4. 데이터 분석 및 시각화 영역
    st.divider()
    st.subheader("📊 항목별 분포 및 수치 분석")

    column_names = df.columns.tolist()
    selected_col = st.selectbox("시각화할 항목을 선택하세요", column_names)

    # 5. 그래프 그리기 (ax 객체를 직접 제어)
    fig, ax = plt.subplots(figsize=(10, 6))
    
    if df[selected_col].dtype in ['int64', 'float64']:
        sns.histplot(df[selected_col], ax=ax, color="#FF9900", kde=True)
        ax.set_ylabel("빈도수")
    else:
        sns.countplot(data=df, x=selected_col, ax=ax, palette="viridis")
        ax.set_ylabel("개수")

    # [수정 2] plt.title 대신 ax.set_title을 사용하여 한글 적용의 안정성을 높임
    ax.set_title(f"[{selected_col}] 항목 분석 결과", fontsize=15, pad=15)
    ax.set_xlabel(selected_col)
    plt.xticks(rotation=45) 
    
    st.pyplot(fig)

    # 6. 간단한 요약 통계
    if df[selected_col].dtype in ['int64', 'float64']:
        st.info(f"💡 {selected_col} 항목의 평균: {df[selected_col].mean():.2f}")

except FileNotFoundError:
    st.error(f"⚠️ '{file_path}' 파일을 찾을 수 없습니다.")
except Exception as e:
    st.error(f"⚠️ 오류가 발생했습니다: {e}")