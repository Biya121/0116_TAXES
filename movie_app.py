import streamlit as st
from streamlit_lottie import st_lottie
import requests

# 1. 페이지 기본 설정 및 디자인 (CSS)
st.set_page_config(page_title="Premium Brand Page", layout="wide")

st.markdown("""
    <style>
    /* 전체 배경색 */
    .main {
        background-color: #FFFFFF;
        color: #1A1A1A;
    }
    
    /* 헤더 스타일 (그린 & 골드) */
    .hero-section {
        background-color: #1E3932; /* 딥 그린 */
        padding: 60px;
        border-radius: 20px;
        color: #D4AF37; /* 골드 */
        text-align: center;
        margin-bottom: 40px;
        border: 2px solid #D4AF37;
    }
    
    /* 제품 카드 스타일 */
    .product-card {
        background-color: #000000; /* 블랙 */
        color: white;
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #D4AF37; /* 골드 포인트 */
        transition: transform 0.3s;
    }
    .product-card:hover {
        transform: scale(1.02);
    }
    
    /* 버튼 스타일 커스텀 */
    div.stButton > button:first-child {
        background-color: #D4AF37;
        color: white;
        border-radius: 10px;
        border: none;
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

# Lottie 애니메이션 로드 함수
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_status_code != 200:
        return None
    return r.json()

# 2. 메인 화면 구성
# 히어로 섹션
st.markdown(f"""
    <div class="hero-section">
        <h1 style='font-size: 3rem;'>PREMIUM SELECTION</h1>
        <p style='font-size: 1.2rem; color: #FFFFFF;'>가장 순수한 자연에서 온 특별한 가치</p>
    </div>
    """, unsafe_allow_html=True)

# 3. 레이아웃: 제품 소개 섹션
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.image("https://images.unsplash.com/photo-1544333346-64e3273ed2ec?auto=format&fit=crop&q=80&w=800", 
             caption="Signature Product Line", use_container_width=True)

with col2:
    st.markdown("### ⚜️ Brand Philosophy")
    st.write("""
    저희 브랜드는 **그린(Nature)**의 생명력과 **화이트(Purity)**의 깨끗함, 
    그리고 **골드(Premium)**의 변치 않는 가치를 지향합니다. 
    최상의 블랙(Authority) 라벨 제품을 만나보세요.
    """)
    
    # 특징 하이라이트 (Annotated Text 효과 대용)
    st.info("✓ 100% Organic Material")
    st.info("✓ Gold-Standard Quality Control")
    
    if st.button("카탈로그 다운로드"):
        st.success("준비 중입니다!")

st.divider()

# 4. 제품 그리드 (블랙 & 골드 카드 디자인)
st.markdown("### 🛍 Our Collections")
p_col1, p_col2, p_col3 = st.columns(3)

products = [
    {"name": "Green Label", "desc": "신선한 원재료의 풍미", "price": "₩45,000"},
    {"name": "Gold Edition", "desc": "한정판 프리미엄 세트", "price": "₩120,000"},
    {"name": "Black Signature", "desc": "장인 정신의 결정체", "price": "₩89,000"}
]

for i, col in enumerate([p_col1, p_col2, p_col3]):
    with col:
        st.markdown(f"""
            <div class="product-card">
                <h4 style='color: #D4AF37;'>{products[i]['name']}</h4>
                <p>{products[i]['desc']}</p>
                <hr style='border: 0.5px solid #333;'>
                <p style='font-weight: bold;'>{products[i]['price']}</p>
            </div>
            """, unsafe_allow_html=True)
        st.button(f"{products[i]['name']} 상세보기", key=f"btn_{i}")

# 하단 푸터
st.markdown("---")
st.caption("© 2026 Premium Brand. All rights reserved. | Contact: info@brand.com")
