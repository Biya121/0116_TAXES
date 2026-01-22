import streamlit as st

# 1. 페이지 설정
st.set_page_config(page_title="Premium Brand Home", layout="wide")

# 2. 브랜드 컬러 및 스타일 정의 (CSS)
st.markdown("""
    <style>
    /* 전체 배경색 및 기본 폰트 설정 */
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@100;400;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Noto Sans KR', sans-serif;
    }

    .main {
        background-color: #FFFFFF;
    }

    /* 상단 배너 섹션 */
    .hero-container {
        background: linear-gradient(135deg, #1E3932 0%, #000000 100%);
        padding: 80px 40px;
        border-radius: 0px 0px 50px 50px;
        text-align: center;
        color: #D4AF37;
        margin-bottom: 50px;
        border-bottom: 4px solid #D4AF37;
    }

    /* 골드 포인트 텍스트 */
    .gold-text {
        color: #D4AF37;
        font-weight: bold;
    }

    /* 제품 카드 스타일 */
    .product-box {
        background-color: #F9F9F9;
        padding: 25px;
        border-radius: 15px;
        border: 1px solid #E0E0E0;
        border-top: 5px solid #1E3932; /* 그린 포인트 */
        transition: all 0.3s ease;
        height: 100%;
    }
    
    .product-box:hover {
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        transform: translateY(-5px);
    }

    /* 버튼 스타일 통일 */
    div.stButton > button {
        background-color: #000000;
        color: #D4AF37;
        border: 1px solid #D4AF37;
        border-radius: 5px;
        padding: 10px 20px;
        font-weight: bold;
    }
    
    div.stButton > button:hover {
        background-color: #D4AF37;
        color: #000000;
        border: 1px solid #000000;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. 메인 콘텐츠 - 히어로 섹션
st.markdown("""
    <div class="hero-container">
        <h1 style='font-size: 3.5rem; letter-spacing: 2px;'>THE ESSENCE OF NATURE</h1>
        <p style='font-size: 1.3rem; color: #FFFFFF; opacity: 0.9;'>
            시간이 흘러도 변하지 않는 <span class="gold-text">골드 클래스</span>의 가치를 경험하세요.
        </p>
    </div>
    """, unsafe_allow_html=True)

# 4. 제품 소개 및 브랜드 스토리 (2단 구성)
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    # 고급스러운 느낌의 무료 이미지 사용
    st.image("https://images.unsplash.com/photo-1615485242231-3141384a377d?auto=format&fit=crop&q=80&w=800", 
             use_container_width=True)

with col2:
    st.markdown("<h2 style='color: #1E3932;'>Our Heritage</h2>", unsafe_allow_html=True)
    st.write("""
    저희 브랜드는 자연에서 얻은 가장 순수한 원료만을 고집합니다. 
    전문가의 손길을 거쳐 완성된 프리미엄 라인은 당신의 일상에 특별함을 더해줍니다.
    """)
    
    # 특징 리스트
    st.markdown("""
    - **🌿 Sustainable**: 지속 가능한 환경을 생각하는 공정
    - **✨ Premium**: 엄선된 원료와 철저한 품질 관리
    - **🖤 Timeless**: 유행을 타지 않는 클래식한 가치
    """)
    
    st.button("브랜드 스토리 더보기")

st.markdown("<br><br>", unsafe_allow_html=True)
st.divider()

# 5. 제품 컬렉션 (3단 그리드)
st.markdown("<h2 style='text-align: center; color: #1E3932;'>Collections</h2>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

p_col1, p_col2, p_col3 = st.columns(3)

# 카드형 UI 배치
with p_col1:
    st.markdown("""
        <div class="product-box">
            <h4 style='color: #1E3932;'>Forest Green</h4>
            <p style='color: #666;'>자연의 싱그러움을 담은 베이직 라인</p>
            <h5 class="gold-text">₩55,000</h5>
        </div>
    """, unsafe_allow_html=True)
    st.button("Green 상세", key="p1")

with p_col2:
    st.markdown("""
        <div class="product-box" style="border-top: 5px solid #D4AF37;">
            <h4 style='color: #D4AF37;'>Royal Gold</h4>
            <p style='color: #666;'>최고의 성분만을 담은 리미티드 에디션</p>
            <h5 class="gold-text">₩189,000</h5>
        </div>
    """, unsafe_allow_html=True)
    st.button("Gold 상세", key="p2")

with p_col3:
    st.markdown("""
        <div class="product-box" style="border-top: 5px solid #000000;">
            <h4 style='color: #000000;'>Night Black</h4>
            <p style='color: #666;'>강렬하고 세련된 시그니처 퍼포먼스</p>
            <h5 class="gold-text">₩95,000</h5>
        </div>
    """, unsafe_allow_html=True)
    st.button("Black 상세", key="p3")

# 6. 하단 푸터
st.markdown("""
    <br><br><br>
    <div style='text-align: center; padding: 40px; background-color: #f8f9fa; border-top: 1px solid #eee;'>
        <p style='color: #1E3932; font-weight: bold;'>PREMIUM BRAND Co.</p>
        <p style='color: #999; font-size: 0.8rem;'>서울특별시 강남구 테헤란로 | CS: 1588-0000 | 2026 Premium All Rights Reserved.</p>
    </div>
    """, unsafe_allow_html=True)
