import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import platform

# ---------------------------
# 0) 기본 UI 설정
# ---------------------------

st.set_page_config(
    page_title="🎰 Streamlit Lotto",
    page_icon="🎰",
    layout="centered"
)

st.title("🎰 로또 번호 생성기 (Streamlit)")
st.caption("원하는 게임 수 만큼 로또 번호를 생성하고, 번호 출현 빈도를 그래프로 확인합니다.")

# ---------------------------
# 1) 한글 폰트 설정 (네 코드 방식 유지)
# ---------------------------

from matplotlib import rc
plt.rcParams['axes.unicode_minus'] = False  # 마이너스 기호 깨짐 방지

if platform.system() == 'Windows':
    rc('font', family='Malgun Gothic')
elif platform.system() == 'Darwin':  # Mac
    rc('font', family='AppleGothic')
# Linux(서버/클라우드)는 폰트가 없을 수 있어 기본 폰트로 표시될 수 있음

# ---------------------------
# 2) 로또 번호 생성 함수
# ---------------------------

def generate_lotto(n_games: int, seed: int | None = None):
    """
    로또 번호를 n_games(게임 수) 만큼 생성
    - 1~45 숫자 중 6개를 중복 없이 뽑음
    - seed를 주면 매번 같은 결과(재현 가능)
    반환: (n_games, 6) 형태의 numpy 배열
    """
    if seed is not None:
        np.random.seed(seed)

    results = []
    for _ in range(n_games):
        # replace=False => 중복 없이 추출
        nums = np.random.choice(np.arange(1, 46), size=6, replace=False)
        nums.sort()  # 보기 좋게 오름차순 정렬
        results.append(nums)

    return np.array(results)

# ---------------------------
# 3) 입력 위젯 (네 코드의 selectbox/slider 구조 응용)
# ---------------------------

st.subheader("⚙️ 설정")

# 몇 게임(몇 줄) 뽑을지
n_games = st.slider("몇 게임(줄)을 생성할까요?", min_value=1, max_value=20, value=5, step=1)

# 랜덤 고정(Seed) 옵션
use_seed = st.checkbox("🎯 랜덤 고정(Seed) 사용", value=False)
seed = None
if use_seed:
    seed = st.number_input("Seed 값(정수)", min_value=0, max_value=999999, value=2026, step=1)

# 그래프 표시 옵션
show_chart = st.checkbox("📊 번호 출현 빈도 그래프 보기", value=True)

# ---------------------------
# 4) 버튼 클릭 시 실행 (Streamlit에서 매우 중요!)
# ---------------------------

st.subheader("✅ 로또 번호 생성")

if st.button("🎲 로또 번호 뽑기"):
    try:
        # 4-1) 로또 번호 생성
        games = generate_lotto(n_games=n_games, seed=seed)

        # 4-2) 표(DataFrame)로 보기 좋게 만들기
        df_lotto = pd.DataFrame(games, columns=[f"No{i}" for i in range(1, 7)])
        df_lotto.index = np.arange(1, len(df_lotto) + 1)
        df_lotto.index.name = "게임"

        st.success("🎉 생성 완료!")
        st.dataframe(df_lotto, use_container_width=True)

        # ---------------------------
        # 5) 번호 출현 빈도 계산 + 그래프
        # ---------------------------
        if show_chart:
            st.subheader("📊 번호 출현 빈도")

            # 모든 번호를 한 줄로 펼치기 (예: 5게임이면 총 30개 숫자)
            flat_nums = df_lotto.values.flatten()

            # 빈도 계산: 1~45에 대해 각각 몇 번 나왔는지
            # bincount는 0부터 세므로 길이를 46으로 만들고 [1:]로 1~45만 사용
            counts = np.bincount(flat_nums, minlength=46)[1:]
            numbers = np.arange(1, 46)

            freq_df = pd.DataFrame({"번호": numbers, "출현횟수": counts})

            # 상위 10개 표
            st.write("✅ 가장 많이 나온 번호 TOP 10")
            st.dataframe(
                freq_df.sort_values("출현횟수", ascending=False).head(10),
                use_container_width=True
            )

            # 그래프 그리기 (네 코드처럼 fig, ax 만들고 seaborn 사용)
            fig, ax = plt.subplots(figsize=(12, 4))
            sns.barplot(data=freq_df, x="번호", y="출현횟수", ax=ax)

            ax.set_title("번호별 출현 빈도")
            ax.set_xlabel("번호")
            ax.set_ylabel("출현횟수")

            st.pyplot(fig)

    except Exception as e:
        st.error(f"⚠️ 알 수 없는 오류가 발생했습니다. {e}")

# ---------------------------
# 6) 안내
# ---------------------------

st.info("📌 연습용 랜덤 생성기입니다. 당첨을 보장하지 않습니다 🙂")
