import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import platform
import os
from matplotlib import font_manager, rc

# --- [수정 1] 한글 폰트 설정을 최상단으로 이동 및 로직 보강 ---
def setup_korean_font():
    plt.rcParams['axes.unicode_minus'] = False # 마이너스 기호 깨짐 방지
    
    try:
        if platform.system() == 'Windows':
            # 로컬 윈도우 환경
            rc('font', family='Malgun Gothic')
        elif platform.system() == 'Darwin':
            # 로컬 맥 환경
            rc('font', family='AppleGothic')
        else:
            # --- Streamlit Cloud (Linux) 서버 환경 ---
            # 1. 시스템에 설치된 나눔고딕을 우선 적용
            rc('font', family='NanumGothic')
            
            # 2. 만약 적용되지 않을 경우를 대비해 직접 경로 지정 (가장 확실함)
            font_path = "/usr/share/fonts/truetype/nanum/NanumGothic.ttf"
            if os.path.exists(font_path):
                font_name = font_manager.FontProperties(fname=font_path).get_name()
                rc('font', family=font_name)
    except Exception as e:
        # 설정 실패 시 로그만 출력하고 프로그램은 계속 실행
        print(f"폰트 설정 실패: {e}")

# 폰트 설정을 앱 시작과 동시에 실행
setup_korean_font()

# --- [이하 데이터 로드 및 UI 코드] ---
st.title("📊 국세청 근로소득 데이터 분석기")
file_path = "국세청_근로소득 백분위(천분위) 자료_20241231.csv" 

try : 
    # 자료 읽기 (cp949 또는 utf-8 중 맞는 것 사용)
    df = pd.read_csv(file_path, encoding='cp949')
    st.success("👌데이터 불러오기 성공!")

    st.subheader("🫢 데이터를 미리 확인하기")
    st.dataframe(df.head(10))

    st.subheader("📊 항목별 분포 그래프")
    column_names = df.columns.tolist()
    selected_col = st.selectbox("분석할 항목을 선택하세요", column_names)

    # --- [수정 2] 그래프 생성 시 ax 객체를 사용하여 설정 적용 ---
    fig, ax = plt.subplots(figsize=(10,5)) 
    sns.histplot(df[selected_col], ax=ax, color="#00FF7F")
    
    # plt.title 대신 ax.set_title 등을 사용하면 폰트 적용이 더 안정적입니다.
    ax.set_title(f"{selected_col} 분포 확인") 
    ax.set_xlabel(selected_col)
    ax.set_ylabel("빈도수")
    
    st.pyplot(fig)

except FileNotFoundError :
    st.error(f"⚠️ {file_path} 파일을 찾을 수 없습니다.")
except Exception as e :
    st.error(f"⚠️ 오류가 발생했습니다: {e}")