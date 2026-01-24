import streamlit as st

# 1. 페이지 설정 및 디자인 테마
st.set_page_config(
    page_title="made in nature | Official",
    page_icon="🍃",
    layout="wide"
)

# 2. 브랜드 컬러 팔레트 및 세련된 폰트 적용
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@200;400;600&family=Noto+Serif+KR:wght@300;600&display=swap');

    /* 기본 텍스트 및 배경 */
    html, body, [class*="css"] {
        font-family: 'Noto Serif KR', serif;
        color: #000000;
        background-color: #FFFFFF;
    }

    /* 로고 & 슬로건 중앙 정렬 */
    .brand-hero {
        text-align: center;
        padding: 80px 0 40px 0;
    }
    .brand-title {
        font-family: 'Montserrat', sans-serif;
        font-size: 55px;
        letter-spacing: 15px;
        font-weight: 200;
        color: #1A3021; /* 다크그린 */
        margin-bottom: 0;
    }
    .brand-tagline {
        font-size: 14px;
        letter-spacing: 5px;
        color: #D4AF37; /* 골드 */
        margin-top: 10px;
        text-transform: uppercase;
    }

    /* 네비게이션 버튼 스타일 */
    div[data-testid="stHorizontalBlock"] {
        border-top: 1px solid #F0F0F0;
        border-bottom: 1px solid #F0F0F0;
        padding: 10px 0;
        margin-bottom: 50px;
    }

    /* 카드 스타일링 */
    .product-container {
        padding: 20px;
        text-align: center;
    }
    .price-tag {
        color: #1A3021;
        font-weight: 600;
        font-size: 18px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. 상단 브랜드 아이덴티티 (중앙 정렬)
st.markdown("""
    <div class="brand-hero">
        <h1 class="brand-title">MADE IN NATURE</h1>
        <p class="brand-tagline">Premium Eco-Luxury Naturalism</p>
    </div>
""", unsafe_allow_html=True)

# 4. 중앙 정렬 네비게이션 (Session State 활용)
if 'page' not in st.session_state:
    st.session_state.page = 'HOME'

_, col1, col2, col3, col4, col5, _ = st.columns([1, 1, 1, 1, 1, 1, 1])
with col1: 
    if st.button("HOME", use_container_width=True): st.session_state.page = 'HOME'
with col2: 
    if st.button("LIVING", use_container_width=True): st.session_state.page = 'LIVING'
with col3: 
    if st.button("KITCHEN", use_container_width=True): st.session_state.page = 'KITCHEN'
with col4: 
    if st.button("BATH", use_container_width=True): st.session_state.page = 'BATH'
with col5: 
    if st.button("STORY", use_container_width=True): st.session_state.page = 'STORY'

# 5. 제품 콘텐츠 데이터
products = {
    "스웨덴 행주": {"cat": "KITCHEN", "price": "12,000원", "img": "https://images.unsplash.com/photo-1584622650111-993a426fbf0a?w=600", "desc": "북유럽의 실용성과 자연의 순수함을 담은 블랙 에디션"},
    "대나무 칫솔": {"cat": "BATH", "price": "18,900원", "img": "https://images.unsplash.com/photo-1600091106710-fb9831f6217c?w=600", "desc": "당신의 욕실을 채우는 10가지 자연의 색상"},
    "비즈왁스랩": {"cat": "KITCHEN", "price": "15,500원", "img": "https://images.unsplash.com/photo-1610348725531-843dff563e2c?w=600", "desc": "지속 가능한 신선함, 다시 쓰는 밀랍의 생명력"},
    "코코넛 수세미": {"cat": "KITCHEN", "price": "6,500원", "img": "https://images.unsplash.com/photo-1583947215259-38e31be8751f?w=600", "desc": "미세 플라스틱 없는 코코넛 섬유의 강력한 세척력"}
}

# 6. 페이지 로직
if st.session_state.page == 'HOME':
    # 메인 배너
    st.image("https://images.unsplash.com/photo-1542601906990-b4d3fb773b09?w=1600", caption="자연에서 온 정직한 가치")
    
    st.markdown("<br><br><h3 style='text-align:center; color:#1A3021;'>BEST SELLER</h3>", unsafe_allow_html=True)
    st.markdown("<div style='width:30px; height:2px; background:#D4AF37; margin:0 auto 40px auto;'></div>", unsafe_allow_html=True)
    
    cols = st.columns(4)
    for i, (name, info) in enumerate(products.items()):
        with cols[i]:
            st.image(info['img'])
            st.markdown(f"**{name}**")
            st.markdown(f"<p style='color:#888; font-size:12px;'>{info['cat']}</p>", unsafe_allow_html=True)
            st.markdown(f"<p class='price-tag'>{info['price']}</p>", unsafe_allow_html=True)
            if st.button("VIEW DETAIL", key=f"view_{i}"):
                st.toast(f"{name} 페이지로 이동합니다.")

elif st.session_state.page == 'KITCHEN':
    st.subheader("KITCHEN COLLECTION")
    for name, info in products.items():
        if info['cat'] == "KITCHEN":
            c1, c2 = st.columns([1, 1.5])
            with c1: st.image(info['img'])
            with c2:
                st.markdown(f"<p style='color:#D4AF37;'>{info['cat']}</p>", unsafe_allow_html=True)
                st.title(name)
                st.write(info['desc'])
                st.markdown(f"### {info['price']}")
                st.button("ADD TO CART", key=name)
            st.divider()

# 7. 푸터 (심플 & 고급)
st.markdown("""
    <div style="margin-top:100px; padding:60px 0; border-top:1px solid #EEE; text-align:center;">
        <p style="font-family:'Montserrat'; letter-spacing:5px; color:#1A3021; font-weight:600;">MADE IN NATURE</p>
        <p style="color:#BBB; font-size:11px;">
            서울특별시 그린구 에코로 123 | 고객센터 1588-0000<br>
            자연을 생각하는 프리미엄 네추럴리즘
        </p>
    </div>
""", unsafe_allow_html=True)
