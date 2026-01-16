import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import platform
from matplotlib import font_manager, rc

# [해결책] 폰트 설정을 아예 함수로 만들어서 최상단에서 실행
def setup_korean_font():
    plt.rcParams['axes.unicode_minus'] = False
    try:
        if platform.system() == 'Windows':
            # 윈도우 맑은 고딕
            rc('font', family='Malgun Gothic')
        elif platform.system() == 'Darwin':
            # 맥 애플 고딕
            rc('font', family='AppleGothic')
        else:
            # 리눅스/서버 환경 (폰트가 없을 경우 대비)
            st.warning("⚠️ 시스템에 한글 폰트가 없어 기본 폰트를 사용합니다.")
    except Exception as e:
        print(f"폰트 설정 중 오류 발생: {e}")

# 1. 시작하자마자 폰트 설정 실행
setup_korean_font()

st.title("📊 국세청 근로소득 데이터 분석기")
file_path = "국세청_근로소득 백분위(천분위) 자료_20241231.csv" 

try:
    df = pd.read_csv(file_path, encoding='cp949')
    st.success("👌 데이터 불러오기 성공!")

    # ... 중간 데이터 미리보기 생략 ...

    column_names = df.columns.tolist()
    selected_col = st.selectbox("분석할 항목을 선택하세요", column_names)

    # 2. 그래프 그리기 직전에 다시 확인 (가장 확실한 방법)
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.histplot(df[selected_col], ax=ax, color="#00FF7F")
    
    ax.set_title(f"{selected_col} 분포 확인") # plt.title 대신 ax.set_title 권장
    ax.set_xlabel(selected_col)
    ax.set_ylabel("빈도수")
    
    st.pyplot(fig)

except Exception as e:
    st.error(f"오류 발생: {e}")