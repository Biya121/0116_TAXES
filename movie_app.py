import streamlit as st

# 1. 페이지 설정
st.set_page_config(
    page_title="made in nature | Premium Naturalism",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. 상세 컬러 팔레트 및 디자인 (CSS)
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Serif+KR:wght@300;400;700&display=swap');

    /* 컬러 정의 */
    :root {{
        --dark-green: #1A3021;
        --green: #2D5A27;
        --light-green: #9DC08B;
        --lime-green: #EDF1D6;
        --gold: #D4AF37;
        --black: #000000;
        --light-gray: #D3D3D3;
        --white: #FFFFFF;
    }}

    html, body, [class*="css"] {{
        font-family: 'Noto Serif KR', serif;
        color: var(--black);
    }}

    /* 상단 중앙 정렬 헤더 */
    .header-container {{
        text-align: center;
        padding: 50px 0 20px 0;
    }}
    .brand-name {{
        font-size: 55px;
        letter-spacing: 10px;
        font-weight: 300;
        color: var(--dark-green);
        margin-bottom: 5px;
    }}
    .brand-sub {{
        color: var(--gold);
        font-size: 14px;
        letter-spacing: 4px;
        text-transform: uppercase;
    }}

    /* 제품 카드 스타일 */
    .product-card {{
        border: 1px solid #f0f0f0;
        padding: 15px;
        text-align: center;
        background-color: var(--white);
        transition: 0.3s;
        margin-bottom: 20px;
    }}
    .product-card:hover {{
        border: 1px solid var(--light-green);
        box-shadow: 0 10px 20px rgba(0,0,0,0.05);
    }}
    .category-label {{
        color: var(--light-gray);
        font-size: 11px;
        margin-bottom: 5px;
    }}
    </style>
    """, unsafe_allow_html=True)

# 3. 상단 헤더 & 브랜드 아이덴티티
st.markdown("""
    <div class="header-container">
        <p class="brand-sub">Premium Naturalism</p>
        <h1 class="brand-name">made in nature</h1>
    </div>
    """, unsafe_allow_html=True)

# 4. Interactive 상단 바 (중앙 정렬 메뉴)
# 클릭 시 해당 섹션으로 이동하도록 세션 상태 활용
menu = ["HOME", "화장품&화장소품", "건강식품", "생활잡화"]
cols = st.columns([2, 1, 1.2, 1, 1, 2]) # 중앙 정렬을 위한 비율 조정

if 'target' not in st.session_state:
    st.session_state.target = "HOME"

with cols[1]:
    if st.button("HOME", use_container_width=True): st.session_state.target = "HOME"
with cols[2]:
    if st.button("COSMETIC", use_container_width=True): st.session_state.target = "COSMETIC"
with cols[3]:
    if st.button("HEALTH", use_container_width=True): st.session_state.target = "HEALTH"
with cols[4]:
    if st.button("LIVING", use_container_width=True): st.session_state.target = "LIVING"

st.divider()

# 5. 제품 데이터 정의
products = {
    "COSMETIC": [
        ("기름종이", "천연 마 소재의 흡수력"), ("화장솜 & 케이스", "무표백 순면 화장솜"),
        ("페이스스타 패치", "감각적인 여드름 케어"), ("LHM 두피마사지기", "4종 타입 맞춤형 케어")
    ],
    "HEALTH": [
        ("도파민 패치", "집중력이 필요한 순간"), ("NAD+ 패치", "활력 에너지를 위한 선택"),
        ("나이트 패치", "편안한 휴식을 위한 패치")
    ],
    "LIVING": [
        ("노스크래치 수세미", "그릇 손상 없는 세척"), ("코코넛 수세미", "친환경 생분해 소재"),
        ("금강사 수세미", "강력한 찌든 때 제거"), ("철수세미 세트", "본품 1+리필 5 구성"),
        ("스웨덴 행주", "압도적 흡수와 건조"), ("비즈왁스랩", "씻어서 다시 쓰는 랩"),
        ("대나무 칫솔", "탄소 중립 실천의 시작"), ("슈즈커버 필름", "신발을 깨끗하게 보호"),
        ("UV+ 우산 시리즈", "카멜리아/브리티쉬 라인업")
    ]
}

# 6. 섹션별 렌더링
if st.session_state.target == "HOME":
    st.image("https://images.unsplash.com/photo-1542601906990-b4d3fb773b09?auto=format&fit=crop&w=1600&q=80", use_container_width=True)
    st.markdown("<h2 style='text-align:center; color:#1A3021;'>자연에서 온 정직한 가치</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#888;'>불필요한 화학 성분을 걷어내고 자연 본연의 생명력을 전달합니다.</p>", unsafe_allow_html=True)

elif st.session_state.target == "COSMETIC":
    st.markdown(f"<h2 style='text-align:center; color:#D4AF37;'>화장품 & 화장소품</h2>", unsafe_allow_html=True)
    cols = st.columns(4)
    for i, (name, desc) in enumerate(products["COSMETIC"]):
        with cols[i % 4]:
            st.markdown(f"""<div class='product-card'>
                <div class='category-label'>COSMETIC</div>
                <h4>{name}</h4>
                <p style='font-size:12px; color:#666;'>{desc}</p>
            </div>""", unsafe_allow_html=True)
            st.button("상세보기", key=f"cos_{i}")

elif st.session_state.target == "HEALTH":
    st.markdown(f"<h2 style='text-align:center; color:#2D5A27;'>건강식품 (헬스케어)</h2>", unsafe_allow_html=True)
    cols = st.columns(3)
    for i, (name, desc) in enumerate(products["HEALTH"]):
        with cols[i % 3]:
            st.markdown(f"""<div class='product-card' style='background-color:#EDF1D6;'>
                <div class='category-label'>HEALTH CARE</div>
                <h4>{name}</h4>
                <p style='font-size:12px; color:#666;'>{desc}</p>
            </div>""", unsafe_allow_html=True)
            st.button("주문하기", key=f"health_{i}")

elif st.session_state.target == "LIVING":
    st.markdown(f"<h2 style='text-align:center; color:#1A3021;'>생활잡화 (제로웨이스트)</h2>", unsafe_allow_html=True)
    cols = st.columns(3)
    for i, (name, desc) in enumerate(products["LIVING"]):
        with cols[i % 3]:
            st.markdown(f"""<div class='product-card'>
                <div class='category-label'>LIVING & LIFE</div>
                <h4>{name}</h4>
                <p style='font-size:12px; color:#666;'>{desc}</p>
            </div>""", unsafe_allow_html=True)
            st.button("장바구니", key=f"living_{i}")

# 7. 하단 정보
st.markdown("<br><br>", unsafe_allow_html=True)
st.divider()
f_col1, f_col2 = st.columns([1, 1])
with f_col1:
    st.markdown("<p style='color: #D3D3D3;'>© 2026 made in nature. All rights reserved.</p>", unsafe_allow_html=True)
with f_col2:
    st.markdown("<p style='text-align: right; color: #D4AF37;'>Instagram | Naver Store | Kakao Talk</p>", unsafe_allow_html=True)
