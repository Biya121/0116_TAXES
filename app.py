import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import platform
from matplotlib import font_manager, rc

# --- [수정 1] 한글 폰트 설정을 최상단으로 이동 ---
# 그래프를 그리기 전에 폰트가 먼저 설정되어야 깨지지 않습니다.
plt.rcParams['axes.unicode_minus'] = False 

if platform.system() == 'Windows':
    rc('font', family='Malgun Gothic')
elif platform.system() == 'Darwin': # Mac
    rc('font', family='AppleGothic')
else:
    # 리눅스(Streamlit Cloud 등) 환경을 위한 나눔폰트 설정 (선택사항)
    rc('font', family='NanumGothic')

# --- [유지] 데이터 로드 및 제목 ---
st.title("📊 국세청 근로소득 데이터 분석기")
file_path = "국세청_근로소득 백분위(천분위) 자료_20241231.csv" 

try : 
    # 자료 읽기
    df = pd.read_csv(file_path, encoding='cp949')
    st.success("👌데이터 불러오기 성공!")

    # 데이터 미리보기
    st.subheader("🫢 데이터를 미리 확인하기")
    st.dataframe(df.head(10)) 

    # --- [유지] 그래프 그리기 ---
    st.subheader("📊 항목별 분포 그래프")

    column_names = df.columns.tolist()
    selected_col = st.selectbox("분석할 항목을 선택하세요", column_names)

    # 그래프 그리기
    fig, ax = plt.subplots(figsize=(10,5)) 
    sns.histplot(df[selected_col], ax=ax, color="#00FF7F")
    
    # 이제 여기서 한글이 정상적으로 출력됩니다.
    plt.title(f"{selected_col} 분포 확인") 
    plt.xlabel(selected_col) 
    plt.ylabel("빈도수") 
    
    st.pyplot(fig)

except FileNotFoundError :
    st.error(f"⚠️ {file_path} 파일을 찾을 수 없습니다.")
except Exception as e :
    st.error(f"⚠️ 알 수 없는 오류가 발생했습니다. {e}")