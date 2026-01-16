import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import random
import platform
from matplotlib import font_manager, rc

# 1. 한글 폰트 설정 (그래프 깨짐 방지)
plt.rcParams['axes.unicode_minus'] = False
if platform.system() == 'Windows':
    rc('font', family='Malgun Gothic')
elif platform.system() == 'Darwin': # Mac
    rc('font', family='AppleGothic')

# --- 앱 제목 및 설명 ---
st.title("🍀 로또 번호를 만들고, 생성 분석도 하고!")
st.write("단순한 번호 생성을 넘어, 생성된 번호들의 통계도 볼 수 있어요.")

# --- 사이드바: 설정 ---
st.sidebar.header("⚙️ 설정")
num_sets = st.sidebar.number_input("생성할 로또 수", min_value=1, max_value=100, value=5)

# --- 로또 번호 생성 로직 ---
def generate_lotto(n):
    lotto_sets = []
    for _ in range(n):
        # 1~45 사이의 숫자 중 6개 중복 없이 추출 후 정렬
        numbers = sorted(random.sample(range(1, 46), 6))
        lotto_sets.append(numbers)
    return lotto_sets

# --- 실행 버튼 ---
if st.button("🚀 로또 번호 생성하기"):
    # 데이터 생성
    data = generate_lotto(num_sets)
    
    # pandas 데이터프레임으로 변환 (컬럼명: 번호1 ~ 번호6)
    df = pd.DataFrame(data, columns=[f"번호{i}" for i in range(1, 7)])
    
    # 1. 결과 보여주기
    st.subheader(f"✨ {num_sets}개의 로또 번호")
    st.dataframe(df)

    # 2. 모든 번호를 하나의 리스트로 합쳐서 분포 분석
    all_numbers = df.values.flatten() # 2차원 배열을 1차원으로 펼침
    
    st.divider() # 구분선

    # 3. 데이터 시각화 (Matplotlib & Seaborn)
    st.subheader("📊 번호 등장 빈도 분석")
    st.write("어떤 숫자가 많이 나왔을까요?")

    fig, ax = plt.subplots(figsize=(12, 6))
    
    # 히스토그램 및 밀도 그래프 그리기
    sns.histplot(all_numbers, bins=45, kde=True, color="#FF4B4B", ax=ax)
    
    plt.title(f"생성된 {num_sets} 세트 내 번호 분포", fontsize=15)
    plt.xlabel("로또 번호 (1~45)")
    plt.ylabel("등장 횟수")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Streamlit에 그래프 출력
    st.pyplot(fig)

    # 4. 간단한 통계 요약
    col1, col2 = st.columns(2)
    with col1:
        st.info(f"가장 많이 나온 번호: {pd.Series(all_numbers).mode()[0]}")
    with col2:
        st.success(f"생성된 번호 평균값: {all_numbers.mean():.2f}")

else:
    st.info("왼쪽 사이드바에서 세트 수를 정하고 버튼을 눌러주세요!")