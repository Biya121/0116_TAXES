import streamlit as st
import pandas as pd # pandas = 그래픽 그려주는 거임
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# 데이터 불러오기

st.title("📊 국세청 근로소득 데이터 분석기")
file_path = "국세청_근로소득 백분위(천분위) 자료_20241231.csv" 
# 경로 설정 예시 : "./data/국세청_근로소득 백분위(천분위) 자료_20241231.csv" 

try : 
    # 자료 읽기
    df = pd.read_csv(file_path, encoding='cp949')
    st.success("👌데이터 불러오기 성공!")

    # 데이터 미리보기
    st.subheader("🫢 데이터를 미리 확인하기")
    st.dataframe(df.head(10)) # 상위 5개 행 보여주기 - 괄호 안에 아무것도 입력하지 않으면 5개가 기본값

    # 데이터 분석 그래프 그리기
    st.subheader("📊 항목별 분포 그래프")

    # 분석하고 싶은 열 이름을 선택
    # 예를 들어 급여나 인원 같은 숫자 데이터가 있는 칸을 골라야 한다.

    column_names = df.columns.tolist()
    selected_col = st.selectbox("분석할 항목을 선택하세요", column_names)

    # 그래프 그리기 (seaborn 사용 - 다양한 그래프 그리기 가능)
    fig, ax = plt.subplots(figsize=(10,5)) 
    # ax = 그래프가 그려질 영역 / fig = 전체 그림 (표를 그리는 것)
    sns.histplot(df[selected_col], ax=ax, color="#00FF7F")
    plt.title(f"{selected_col} 분포 확인") # 그래프 맨 위 제목
    plt.xlabel(selected_col) # x축 제목(가로)
    plt.ylabel("빈도수") # y축 제목(세로)
    
    # Streamlit 웹 화면에 그래프 보여주기
    st.pyplot(fig)


except FileNotFoundError :
    st.error(f"⚠️ {file_path} 파일을 찾을 수 없습니다.")
except Exception as e :
    st.error(f"⚠️ 알 수 없는 오류가 발생했습니다. {e}")


import platform

# 한글 폰트 설정 (OS에 따라 다름)
from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus'] = False # 마이너스 기호 깨짐 방지

if platform.system() == 'Windows':
    rc('font', family='Malgun Gothic')
elif platform.system() == 'Darwin': # Mac
    rc('font', family='AppleGothic')