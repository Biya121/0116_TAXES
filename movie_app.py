import streamlit as st

# 1. 페이지 설정
st.set_page_config(page_title="Premium Eco-Luxury Brand", layout="wide")

# 2. 고도화된 스타일링 (CSS)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Noto+Sans+KR:wght@300;500&display=swap');
    
    /* 전체 배경 및 기본 폰트 */
    .main {
        background-color: #FFFFFF;
        color: #1A1A1A;
    }
    h1, h2, h3 {
        font-family: 'Playfair Display', serif;
        color: #1E3932; /* 메인 초록 */
    }
    p, div {
        font-family: 'Noto Sans KR', sans-serif;
    }

    /* 네비게이션바 느낌의 상단 여백 */
    .nav-spacer {
        padding: 20px 0;
        text-align: center;
        border-bottom: 1px solid #F0F0F0;
        margin-bottom: 50px;
    }

    /* 히어로 섹션: 화이트 배경에 그린/골드 포인트 */
    .hero-box {
        padding: 100px 50px;
        background-color: #FFFFFF;
        border-left: 8px solid #1E3932;
        margin-bottom: 80px;
    }

    .gold-accent {
        color: #C5A059; /* 세련된 샴페인 골드 */
        font-weight: bold;
        letter-spacing: 2px;
        text-transform: uppercase;
        font-size: 0.9rem;
    }

    /* 제품 카드: 화이트 배경 + 그린 테두리 + 골드 하이라이트 */
    .product-card-v2 {
        background-color: #FFFFFF;
        padding: 40px 30px;
        border: 1px solid #EAEAEA;
        border-radius: 0px; /* 미니멀한 직각 디자인 */
        transition: all 0.4s ease;
        text-align: center;
    }
    
    .product-card-v2:hover {
        border: 1px solid #1E3932;
        box-shadow: 0 20px 40px rgba(30, 57, 50, 0.05);
    }

    .category-tag {
        background-color: #1E3932;
        color: #FFFFFF;
        padding: 4px 12px;
        font-size: 0.7rem;
        text-transform: uppercase;
        margin-bottom: 15px;
        display: inline-block;
    }

    /* 버튼: 블랙 보조색 활용 */
    div.stButton > button {
        background-color: #1A1A1A; /* 블랙 보조색 */
        color: #FFFFFF;
        border: none;
        border-radius: 0px;
        padding: 12px 30px;
        font-size: 0.8rem;
        letter-spacing: 1px;
        transition: all 0.3s;
    }
    
    div.stButton > button:hover {
        background-color: #C5A059; /* 호버 시 골드 */
        color: white;
    }

    /* 하단 섹션 */
    .footer-section {
        background-color: #1E3932;
        color: #FFFFFF;
        padding: 60px;
        margin-top: 100px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. 상단 네비게이션 로고 (텍스트)
st.markdown('<div class="nav-spacer"><h2 style="letter-spacing:5px;">HERITAGE</h2></div>', unsafe_allow_html=True)

# 4. 히어로 섹션 (비대칭 레이아웃)
h_col1, h_col2 = st.columns([1.2, 1])

with h_col1:
    st.markdown("""
        <div class="hero-box">
            <p class="gold-accent">ESTABLISHED 2026</p>
            <h1 style="font-size: 4rem; line-height: 1.1; margin-bottom: 20px;">
                Pure Green,<br><span style="color:#C5A059">True Luxury.</span>
            </h1>
            <p style="color: #666; font-size: 1.1rem; max-width: 500px; line-height: 1.8;">
                우리는 자연의 깊은 녹색에서 영감을 얻습니다. 가장 순수한 화이트의 깨끗함과 
                시대를 초월하는 골드의 가치를 결합하여 당신만의 특별한 일상을 제안합니다.
            </p>
        </div>
    """, unsafe_allow_html=True)
    st.button("COLLECTION VIEW")

with h_col2:
    # 세로로 긴 세련된 이미지 배치
    st.image("https://images.unsplash.com/photo-1581605405669-fcdf81165afa?auto=format&fit=crop&q=80&w=800", 
             use_container_width=True)

st.markdown("<br><br><br>", unsafe_allow_html=True)

# 5. 제품 섹션 (화이트 & 그린 톤)
st.markdown("<h2 style='text-align: center; margin-bottom: 50px;'>Featured Products</h2>", unsafe_allow_html=True)

p_col1, p_col2, p_col3 = st.columns(3, gap="medium")

# 제품 데이터
products = [
    {"title": "The First Dew", "cat": "Skin Care", "img": "https://images.unsplash.com/photo-1556228720-195a672e8a03?q=80&w=400"},
    {"title": "Golden Leaf", "cat": "Interior", "img": "https://images.unsplash.com/photo-1513519245088-0e12902e5a38?q=80&w=400"},
    {"title": "Forest Essence", "cat": "Fragrance", "img": "https://images.unsplash.com/photo-1547887538-e3a2f32cb1cc?q=80&w=400"}
]

cols = [p_col1, p_col2, p_col3]

for i, col in enumerate(cols):
    with col:
        st.image(products[i]["img"], use_container_width=True)
        st.markdown(f"""
            <div class="product-card-v2">
                <span class="category-tag">{products[i]['cat']}</span>
                <h3 style="font-size: 1.5rem; margin-bottom: 15px;">{products[i]['title']}</h3>
                <p style="color: #888; font-size: 0.9rem; margin-bottom: 20px;">
                    자연 유래 성분과 고귀한 금빛 디테일의 조화.
                </p>
                <p class="gold-accent" style="font-size: 1.1rem;">KRW 85,000</p>
            </div>
        """, unsafe_allow_html=True)
        st.button("DETAILS", key=f"details_{i}", use_container_width=True)

# 6. 브랜드 푸터 (딥 그린 & 화이트)
st.markdown("""
    <div class="footer-section">
        <div style="max-width: 800px; margin: 0 auto; text-align: center;">
            <h2 style="color: #C5A059; margin-bottom: 20px;">Join the Heritage</h2>
            <p style="opacity: 0.8; line-height: 2;">
                브랜드의 새로운 소식과 프라이빗 이벤트를 가장 먼저 만나보세요.<br>
                우리는 지속 가능한 럭셔리를 지향하며, 모든 제품은 자연에 대한 존중을 담아 제작됩니다.
            </p>
            <br>
            <p style="font-size: 0.8rem; opacity: 0.5; margin-top: 40px;">
                © 2026 HERITAGE GREEN. PRIVACY POLICY | TERMS OF SERVICE
            </p>
        </div>
    </div>
""", unsafe_allow_html=True)
