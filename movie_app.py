import streamlit as st

# 1. 페이지 설정
st.set_page_config(page_title="made in nature | Premium Naturalism", layout="wide")

# 2. 상세 컬러 가이드 및 CSS 적용
# 주색상: #32CD32(라임), #90EE90(라이트), #228B22(그린), #1A3021(다크)
# 포인트: #D4AF37(골드) / 글씨: #000000(블랙), #D3D3D3(라이트그레이)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Serif+KR:wght@300;700&family=Montserrat:wght@300;500&display=swap');
    
    html { scroll-behavior: smooth; }
    body { font-family: 'Noto Serif KR', serif; color: #000000; }
    
    /* 중앙 정렬 헤더 & 로고 */
    .header-container { text-align: center; padding: 50px 0 20px 0; }
    .brand-logo { font-family: 'Montserrat', sans-serif; font-size: 48px; letter-spacing: 10px; color: #1A3021; margin-bottom: 5px; }
    .brand-sub { font-size: 13px; letter-spacing: 4px; color: #D4AF37; font-weight: 300; }
    
    /* 중앙 정렬 내비게이션 바 */
    .nav-container {
        display: flex;
        justify-content: center;
        gap: 35px;
        border-top: 1px solid #D3D3D3;
        border-bottom: 1px solid #D3D3D3;
        padding: 15px 0;
        position: sticky;
        top: 0;
        background-color: white;
        z-index: 1000;
    }
    .nav-item {
        text-decoration: none;
        color: #000000;
        font-size: 14px;
        font-weight: 500;
        transition: 0.3s;
    }
    .nav-item:hover { color: #228B22; }

    /* 제품 섹션 스타일 */
    .section-box { padding: 100px 10% 60px 10%; border-bottom: 1px solid #f0f0f0; }
    .product-tag { color: #D4AF37; font-size: 12px; letter-spacing: 2px; }
    .product-title { font-size: 36px; color: #1A3021; margin: 10px 0; }
    .product-desc { color: #555; line-height: 1.8; font-size: 17px; }
    
    /* 버튼 커스텀 */
    .stButton>button {
        border: 1px solid #1A3021;
        background-color: transparent;
        color: #1A3021;
        border-radius: 0;
        padding: 10px 40px;
        transition: 0.4s;
    }
    .stButton>button:hover {
        background-color: #1A3021;
        color: white;
        border-color: #1A3021;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. 상단 헤더 및 중앙 정렬 로고
st.markdown("""
    <div class="header-container">
        <p class="brand-sub">PREMIUM NATURALISM</p>
        <h1 class="brand-logo">MADE IN NATURE</h1>
    </div>
    """, unsafe_allow_html=True)

# 4. Interactive Navigation Bar (중앙 정렬 및 앵커 이동)
st.markdown("""
    <div class="nav-container">
        <a class="nav-item" href="#home">HOME</a>
        <a class="nav-item" href="#dishcloth">SWEDISH CLOTH</a>
        <a class="nav-item" href="#toothbrush">BAMBOO BRUSH</a>
        <a class="nav-item" href="#beeswax">BEESWAX WRAP</a>
        <a class="nav-item" href="#coconut">COCONUT PADS</a>
    </div>
    """, unsafe_allow_html=True)

# --- 5. 제품 섹션 정의 ---

# [HOME]
st.markdown('<div id="home"></div>', unsafe_allow_html=True)
st.image("https://images.unsplash.com/photo-1542601906990-b4d3fb773b09?auto=format&fit=crop&w=1600&q=80")
st.markdown("""
    <div style="text-align: center; padding: 60px 0;">
        <h2 style="color: #1A3021; font-weight: 300;">Nature's Honest Value</h2>
        <p style="color: #D3D3D3;">자연에서 온 정직한 가치로 당신의 일상을 채웁니다.</p>
    </div>
""", unsafe_allow_html=True)

# [스웨덴 행주]
st.markdown('<div id="dishcloth" class="section-box">', unsafe_allow_html=True)
col1, col2 = st.columns([1.2, 1])
with col1:
    st.image("https://images.unsplash.com/photo-1584622650111-993a426fbf0a?auto=format&fit=crop&w=800&q=80")
with col2:
    st.markdown("""
        <p class="product-tag">ZERO WASTE KITCHEN</p>
        <h2 class="product-title">스웨덴 행주 블랙 에디션</h2>
        <p class="product-desc">
            1949년 전통의 북유럽 기술력으로 탄생한 혁신적인 원단.<br>
            자기 무게의 15배를 흡수하며 일반 면 행주보다 4배 빠르게 건조됩니다.<br>
            <b>미세플라스틱 없는 깨끗한 주방의 시작.</b>
        </p>
    """, unsafe_allow_html=True)
    st.button("EXPLORE COLLECTION", key="btn1")
st.markdown('</div>', unsafe_allow_html=True)

# [대나무 칫솔]
st.markdown('<div id="toothbrush" class="section-box">', unsafe_allow_html=True)
col1, col2 = st.columns([1, 1.2])
with col1:
    st.markdown("""
        <p class="product-tag">SUSTAINABLE ORAL CARE</p>
        <h2 class="product-title">대나무 칫솔 10색 에디션</h2>
        <p class="product-desc">
            천연 밀랍 코팅으로 곰팡이 걱정 없이 위생적으로 사용하세요.<br>
            PBT 이중 미세모가 잇몸 자극은 줄이고 세정력은 높였습니다.<br>
            <b>10가지 자연의 색상으로 가족 모두의 건강을 선물하세요.</b>
        </p>
    """, unsafe_allow_html=True)
    st.button("EXPLORE COLLECTION", key="btn2")
with col2:
    st.image("https://images.unsplash.com/photo-1600091106710-fb9831f6217c?auto=format&fit=crop&w=800&q=80")
st.markdown('</div>', unsafe_allow_html=True)

# [비즈왁스랩]
st.markdown('<div id="beeswax" class="section-box">', unsafe_allow_html=True)
col1, col2 = st.columns([1.2, 1])
with col1:
    st.image("https://images.unsplash.com/photo-1610348725531-843dff563e2c?auto=format&fit=crop&w=800&q=80")
with col2:
    st.markdown("""
        <p class="product-tag">NATURAL FOOD STORAGE</p>
        <h2 class="product-title">프리미엄 비즈왁스랩</h2>
        <p class="product-desc">
            유기농 면과 천연 밀랍, 호호바 오일로 빚어낸 친환경 랩.<br>
            식재료의 수분 보존력은 높이고 일회용 비닐 사용은 줄여줍니다.<br>
            <b>씻어서 다시 쓰는 지속 가능한 신선함.</b>
        </p>
    """, unsafe_allow_html=True)
    st.button("EXPLORE COLLECTION", key="btn3")
st.markdown('</div>', unsafe_allow_html=True)

# [코코넛 수세미]
st.markdown('<div id="coconut" class="section-box">', unsafe_allow_html=True)
col1, col2 = st.columns([1, 1.2])
with col1:
    st.markdown("""
        <p class="product-tag">PLANT-BASED CLEANING</p>
        <h2 class="product-title">생분해 코코넛 수세미</h2>
        <p class="product-desc">
            천연 코코넛 섬유로 스크래치 걱정 없는 완벽한 설거지.<br>
            미세 플라스틱 걱정 없이 자연으로 100% 돌아갑니다.<br>
            <b>환경과 그릇 모두를 생각하는 건강한 습관.</b>
        </p>
    """, unsafe_allow_html=True)
    st.button("EXPLORE COLLECTION", key="btn4")
with col2:
    st.image("https://images.unsplash.com/photo-1583947215259-38e31be8751f?auto=format&fit=crop&w=800&q=80")
st.markdown('</div>', unsafe_allow_html=True)

# 6. 푸터 (이미지 4 스타일 재현)
st.markdown("""
    <div style="background-color: white; padding: 100px 20px; text-align: center; border-top: 1px solid #D3D3D3;">
        <p style="color: #D4AF37; letter-spacing: 5px; font-size: 14px;">SINCE 2025</p>
        <h2 style="font-family: 'Montserrat'; letter-spacing: 8px; font-weight: 300; color: #1A3021;">MADE IN NATURE</h2>
        <div style="width: 40px; height: 1px; background-color: #D4AF37; margin: 20px auto;"></div>
        <p style="color: #D3D3D3; font-size: 12px; margin-top: 20px;">
            서울특별시 그린구 에코로 123 | MADE IN NATURE 공식 스토어<br>
            COPYRIGHT © MADE IN NATURE. ALL RIGHTS RESERVED.
        </p>
    </div>
""", unsafe_allow_html=True)
