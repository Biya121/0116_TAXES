import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import random
import platform
from matplotlib import font_manager, rc

# --- [수정 1] Streamlit Cloud 및 로컬 환경 통합 폰트 설정 ---
def setup_korean_font():
    plt.rcParams['axes.unicode_minus'] = False # 마이너스 기호 깨짐 방지
    
    try:
        if platform.system() == 'Windows':
            # 로컬 윈도우용
            rc('font', family='Malgun Gothic')
        elif platform.system() == 'Darwin':
            # 로컬 맥용
            rc('font', family='AppleGothic')
        else:
            # --- Streamlit Cloud (Linux) 핵심 설정 ---
            # packages.txt를 통해 설치된 나눔폰트를 적용합니다.
            rc('font', family='NanumGothic')
            
            # 서버 환경에서 폰트 캐시를 업데이트하거나 직접 경로를 지정하기 위한 코드
            font_path = "/usr/share/fonts/truetype/nanum/NanumGothic.ttf"
            if os.path.exists(font_path):
                font_prop = font_manager.FontProperties(fname=font_path)
                rc('font', family=font_prop.get_name())
    except:
        # 폰트 설정 실패 시 에러가 나지 않도록 기본 처리
        pass

import os
setup_korean_font()

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
        numbers = sorted(random.sample(range(1, 46), 6))
        lotto_sets.append(numbers)
    return lotto_sets

# --- 실행 버튼 ---
if st.button("🚀 로또 번호 생성하기"):
    data = generate_lotto(num_sets)
    df = pd.DataFrame(data, columns=[f"번호{i}" for i in range(1, 7)])
    
    # 1. 결과 보여주기
    st.subheader(f"✨ {num_sets}개의 로또 번호")
    st.dataframe(df)

    all_numbers = df.values.flatten() 
    
    st.divider()

    # 3. 데이터 시각화
    st.subheader("📊 번호 등장 빈도 분석")
    st.write("어떤 숫자가 많이 나왔을까요?")

    # --- [수정 2] 객체 지향 방식으로 폰트 적용 ---
    fig, ax = plt.subplots(figsize=(12, 6))
    
    sns.histplot(all_numbers, bins=45, kde=True, color="#FF4B4B", ax=ax)
    
    # ax 객체를 통해 직접 제목과 라벨을 설정해야 Cloud에서 더 안정적입니다.
    ax.set_title(f"생성된 {num_sets} 세트 내 번호 분포", fontsize=15, pad=20)
    ax.set_xlabel("로또 번호 (1~45)", fontsize=12)
    ax.set_ylabel("등장 횟수", fontsize=12)
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    
    st.pyplot(fig)

    # 4. 통계 요약
    col1, col2 = st.columns(2)
    with col1:
        st.info(f"가장 많이 나온 번호: {pd.Series(all_numbers).mode()[0]}")
    with col2:
        st.success(f"생성된 번호 평균값: {all_numbers.mean():.2f}")

else:
    st.info("왼쪽 사이드바에서 세트 수를 정하고 버튼을 눌러주세요!")