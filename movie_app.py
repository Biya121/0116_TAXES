import streamlit as st

# 1. 페이지 기본 설정
st.set_page_config(
    page_title="made in nature | Premium Naturalism",
    page_icon="🍃",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. 고급 브랜드 아이덴티티를 위한 커스텀 CSS
# 주색상: 그린 계열 / 포인트: 골드 (#D4AF37) / 보조: 화이트 & 그레이
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Serif+KR:wght@300;400;700&family=Roboto:wght@100;300;400&display=swap');

    /* 전체 배경 및 폰트 */
    html, body, [class*="css"] {
        font-family: 'Noto Serif KR', serif;
        background-color: #FFFFFF;
    }

    /* 네비게이션 바 (고정형 느낌 구현) */
    .nav-container {
        display: flex;
        justify-content: center;
        gap: 30px;
        padding: 20px 0;
        border-bottom: 1px solid #F0F0F0;
        position: sticky;
        top: 0;
        background-color: white;
        z-index: 999;
    }
    .nav-item {
        text-decoration: none;
        color: #333;
        font-weight: 400;
        font-size: 15px;
        transition: 0.3s;
    }
    .nav-item:hover {
        color: #D4AF37;
    }

    /* 프리미엄 섹션 타이틀 */
    .section-header {
        text-align: center;
        padding: 100px 0 50px 0;
    }
    .brand-name {
        font-family: 'Roboto', sans-serif;
        letter-spacing: 5px;
        color: #1A3021; /* 다크그린 */
        font-weight: 100;
        font-size: 45px;
        margin-bottom: 10px;
    }
    .gold-divider {
        width: 50px;
        height: 2px;
        background-color: #D4AF37;
        margin: 20px auto;
    }

    /* 제품 상세 레이아웃 */
    .product-box {
        padding: 60px 0;
        border-bottom: 1px solid #F5F5F5;
    }
    .product-title {
        font-size: 32px;
        color: #1A3021;
        margin-bottom: 20px;
    }
    .product-subtitle {
        color: #D4AF37;
        font-size: 14px;
        letter-spacing: 2px;
        margin-bottom: 10px;
        text-transform: uppercase;
    }
    .desc-text {
        color: #555;
        line-height: 1.8;
        font-size: 16px;
    }

    /* 버튼 스타일링 */
    .stButton>button {
        background-color: #1A3021;
        color: white;
        border: none;
        padding: 10px 30px;
        border-radius: 0;
        transition: 0.4s;
    }
    .stButton>button:hover {
        background-color: #D4AF37;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. 로고 및 상단 헤더
st.markdown("""
    <div class="section-header">
        <p style="color: #D4AF37; letter-spacing: 3px; font-size: 12px;">ESTABLISHED 2025</p>
        <h1 class="brand-name">MADE IN NATURE</h1>
        <div class="gold-divider"></div>
        <p style="color: #888; font-size: 14px;">화장품 · 건강식품 · 생활잡화</p>
    </div>
    """, unsafe_allow_html=True)

# 4. 네비게이션 (앵커 링크 기능 포함)
# Streamlit에서 특정 위치 이동은 query_params나 스크롤 위치를 활용하지만, 
# 여기서는 탭 형식을 사용하여 각 제품 섹션을 고급스럽게 분리했습니다.
menu = ["HOME", "스웨덴 행주", "대나무 칫솔", "비즈왁스랩", "코코넛 수세미"]
selected_tab = st.tabs(menu)

# --- [1] HOME 섹션 ---
with selected_tab[0]:
    st.markdown("<div class='product-box'>", unsafe_allow_html=True)
    col_hero1, col_hero2 = st.columns([1, 1])
    with col_hero1:
        # 자연주의 브랜드 이미지 배치
        st.image("https://images.unsplash.com/photo-1542601906990-b4d3fb773b09?auto=format&fit=crop&w=800&q=80")
    with col_hero2:
        st.markdown("<p class='product-subtitle'>Premium Naturalism</p>", unsafe_allow_html=True)
        st.markdown("<h2 class='product-title'>자연에서 온 정직한 가치</h2>", unsafe_allow_html=True)
        st.markdown("""
            <p class='desc-text'>
            made in nature는 불필요한 화학 성분을 걷어내고,<br>
            자연이 주는 본연의 생명력을 생활 속에 전달합니다.<br><br>
            우리는 지속 가능한 제로웨이스트 라이프스타일을 통해<br>
            지구와 사람 모두에게 무해한 아름다움을 지향합니다.
            </p>
        """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# --- [2] 스웨덴 행주 섹션 ---
with selected_tab[1]:
    st.markdown("<div class='product-box'>", unsafe_allow_html=True)
    col_left, col_right = st.columns([1.2, 1])
    with col_left:
        # 숙지한 이미지 특징 반영 (블랙 에디션 위주)
        st.image("https://via.placeholder.com/800x600/1A3021/FFFFFF?text=Swedish+Dishcloth+Black+Edition")
    with col_right:
        st.markdown("<p class='product-subtitle'>Zero Waste Kitchen</p>", unsafe_allow_html=True)
        st.markdown("<h2 class='product-title'>스웨덴 행주 블랙 에디션</h2>", unsafe_allow_html=True)
        st.markdown("""
            <p class='desc-text'>
            <b>1949년 전통의 북유럽 기술력</b><br>
            - 자기 무게의 15배를 흡수하는 혁신적 원단<br>
            - 일반 행주보다 4배 빠른 건조로 세균 번식 억제<br>
            - 50회 이상 세탁 가능한 강력한 내구성<br><br>
            한 장의 스웨덴 행주가 키친타올 15롤의 가치를 대체합니다.
            </p>
        """, unsafe_allow_html=True)
        st.button("DISCOVER MORE", key="btn_cloth")
    st.markdown("</div>", unsafe_allow_html=True)

# --- [3] 대나무 칫솔 섹션 ---
with selected_tab[2]:
    st.markdown("<div class='product-box'>", unsafe_allow_html=True)
    col_left, col_right = st.columns([1, 1.2])
    with col_left:
        st.markdown("<p class='product-subtitle'>Sustainable Oral Care</p>", unsafe_allow_html=True)
        st.markdown("<h2 class='product-title'>대나무 칫솔 10색 에디션</h2>", unsafe_allow_html=True)
        st.markdown("""
            <p class='desc-text'>
            <b>당신의 욕실을 컬러풀한 자연으로</b><br>
            - PBT 이중 미세모로 잇몸 자극 최소화<br>
            - 천연 밀랍 코팅으로 대나무 특유의 곰팡이 방지<br>
            - 탄탄하면서도 부드러운 그립감의 인체공학 설계<br><br>
            10가지 자연의 색상으로 가족 모두의 건강을 지키세요.
            </p>
        """, unsafe_allow_html=True)
        st.button("DISCOVER MORE", key="btn_brush")
    with col_right:
        st.image("https://via.placeholder.com/800x600/F5F5F5/1A3021?text=Bamboo+Toothbrush+Collection")
    st.markdown("</div>", unsafe_allow_html=True)

# --- [4] 비즈왁스랩 섹션 ---
with selected_tab[3]:
    st.markdown("<div class='product-box'>", unsafe_allow_html=True)
    col_left, col_right = st.columns([1.2, 1])
    with col_left:
        st.image("https://via.placeholder.com/800x600/D4AF37/FFFFFF?text=Beeswax+Wrap+Premium")
    with col_right:
        st.markdown("<p class='product-subtitle'>Natural Food Storage</p>", unsafe_allow_html=True)
        st.markdown("<h2 class='product-title'>비즈왁스랩 (밀랍랩)</h2>", unsafe_allow_html=True)
        st.markdown("""
            <p class='desc-text'>
            <b>지구도 지키고 음식도 신선하게</b><br>
            - 유기농 면과 천연 밀랍, 호호바 오일의 완벽한 조화<br>
            - 뛰어난 밀착력으로 식재료의 수분 보존 극대화<br>
            - FDA, GOTS 글로벌 인증을 마친 안전한 소재<br><br>
            씻어서 다시 쓰는 랩으로 주방의 플라스틱을 줄여보세요.
            </p>
        """, unsafe_allow_html=True)
        st.button("DISCOVER MORE", key="btn_wrap")
    st.markdown("</div>", unsafe_allow_html=True)

# --- [5] 코코넛 수세미 섹션 ---
with selected_tab[4]:
    st.markdown("<div class='product-box'>", unsafe_allow_html=True)
    col_left, col_right = st.columns([1, 1.2])
    with col_left:
        st.markdown("<p class='product-subtitle'>Plant-Based Cleaning</p>", unsafe_allow_html=True)
        st.markdown("<h2 class='product-title'>생분해 코코넛 수세미</h2>", unsafe_allow_html=True)
        st.markdown("""
            <p class='desc-text'>
            <b>스크래치 없는 완벽한 세척</b><br>
            - 천연 코코넛 섬유와 셀룰로오스의 2중 구조<br>
            - S자형 디자인으로 손에 착 감기는 편안한 사용감<br>
            - 용도별 3종 (오리지널, 노스크래치, 헤비듀티)<br><br>
            미세 플라스틱 걱정 없는 건강한 설거지를 경험하세요.
            </p>
        """, unsafe_allow_html=True)
        st.button("DISCOVER MORE", key="btn_coco")
    with col_right:
        st.image("https://via.placeholder.com/800x600/E8E8E8/1A3021?text=Coconut+Scrubber+Series")
    st.markdown("</div>", unsafe_allow_html=True)

# 5. 푸터 영역
st.markdown("""
    <div style="background-color: #1A3021; padding: 60px; text-align: center; margin-top: 100px;">
        <h3 style="color: #D4AF37; font-family: 'Roboto'; letter-spacing: 3px;">MADE IN NATURE</h3>
        <p style="color: #F0F0F0; font-size: 13px; margin-top: 20px;">
            서울특별시 OO구 OO로 123 (본사) | Tel. 02-123-4567<br>
            자연주의 화장품 · 건강식품 · 생활잡화 전문 브랜드
        </p>
        <div style="margin-top: 30px;">
            <span style="color: #D4AF37; margin: 0 10px;">Instagram</span>
            <span style="color: #D4AF37; margin: 0 10px;">Naver Store</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
