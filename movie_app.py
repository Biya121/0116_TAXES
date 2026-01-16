import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import platform
from matplotlib import font_manager, rc

# 1. 폰트 설정 (최상단 유지)
plt.rcParams['axes.unicode_minus'] = False 
if platform.system() == 'Windows':
    rc('font', family='Malgun Gothic')
elif platform.system() == 'Darwin': # Mac
    rc('font', family='AppleGothic')
else:
    rc('font', family='NanumGothic')

st.title("🎬 영화 상세정보 통합 분석기")

file_path = "영화상세정보(통합)_1129.csv"

try:
    # --- [수정 부분] 인코딩을 utf-8로 변경 ---
    # 오류 메시지의 '0x85' 패턴은 보통 UTF-8 파일을 CP949로 읽을 때 발생합니다.
    df = pd.read_csv(file_path, encoding='utf-8') 
    st.success("👌 영화 데이터 로드 성공 (UTF-8)!")

except UnicodeDecodeError:
    # 만약 utf-8도 안 된다면 마지막으로 cp949 시도
    df = pd.read_csv(file_path, encoding='cp949')
    st.success("👌 영화 데이터 로드 성공 (CP949)!")
except FileNotFoundError:
    st.error(f"⚠️ '{file_path}' 파일을 찾을 수 없습니다.")
    st.stop() # 파일이 없으면 이후 코드 실행 중단

# --- 이후 시각화 코드는 동일하게 유지 ---
if 'df' in locals():
    st.subheader("📋 데이터 미리보기")
    st.dataframe(df.head(10))

    st.divider()
    column_names = df.columns.tolist()
    selected_col = st.selectbox("분석하고 싶은 항목을 선택하세요", column_names)

    fig, ax = plt.subplots(figsize=(12, 6))

    if df[selected_col].dtype in ['int64', 'float64']:
        sns.histplot(df[selected_col], ax=ax, color="#1E90FF", kde=True)
    else:
        top_n = df[selected_col].value_counts().head(15)
        sns.barplot(x=top_n.index, y=top_n.values, ax=ax, palette="coolwarm")
        plt.xticks(rotation=45)

    ax.set_title(f"[{selected_col}] 항목 분석 결과", fontsize=16)
    ax.set_xlabel(selected_col)
    st.pyplot(fig)