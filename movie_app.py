import streamlit as st

# 1. 페이지 설정
st.set_page_config(page_title="made in nature", layout="wide")

# 2. 강력한 중앙 정렬 및 인터랙션을 위한 CSS
st.markdown("""
    <style>
    /* 폰트 설정 */
    @import url('https://fonts.googleapis.com/css2?family=Noto+Serif+KR:wght@300;700&display=swap');
    html, body, [class*="css"] { font-family: 'Noto Serif KR', serif; }

    /* 로고 중앙 정렬 */
    .brand-container { text-align: center; padding: 40px 0; }
    .brand-logo { font-size: 50px; letter-spacing: 12px; color: #1A3021; margin-bottom: 0px; }
    .brand-sub { color: #D4AF37; font-size: 14px; letter-spacing: 5px; margin-top: -10px; }

    /* 메뉴 버튼 중앙 정렬 스타일 */
    .stHorizontalBlock { justify-content: center !important; }
    div[data-testid="stHorizontalBlock"] > div { flex: 0 1 auto !important; min-width: auto !important; }
    
    /* 버튼 투명 배경 (메뉴처럼 보이게) */
    div.stButton > button {
        border: none;
        background-color: transparent;
        color: #000000;
        font-weight: 400;
        padding: 5px 20px;
        font-size: 15px;
    }
    div.stButton > button:hover { color: #228B22; background-color: transparent; }
    
    /* 제품 섹션 박스 */
    .product-box { 
        padding: 80px 10%; 
        border-bottom: 1px solid #f0f0f0; 
        text-align: center;
    }
    .gold-tag { color: #D4AF37; font-size: 12px; letter-spacing: 2px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# 3. [상단] 브랜드 로고 (중앙 정렬)
st.markdown("""
    <div class="brand-container">
        <h1 class="brand-logo">MADE IN NATURE</h1>
        <p class="brand-sub">PREMIUM NATURALISM</p>
    </div>
    """, unsafe_allow_html=True)

# 4. [메뉴] Interactive Navigation Bar (실제 작동하는 버튼)
# Streamlit의 버튼은 클릭 시 스크립트를 재실행하므로, 이를 이용해 화면 위치를 잡습니다.
col_m1, col_m2, col_m3, col_m4, col_m5 = st.columns(5)
with col_m1:
    if st.button("HOME"): st.rerun() # 홈은 최상단
with col_m2:
    if st.button("SWEDISH CLOTH"): st.session_state.target = "cloth"
with col_m3:
    if st.button("BAMBOO BRUSH"): st.session_state.target = "brush"
with col_m4:
    if st.button("BEESWAX WRAP"): st.session_state.target = "wrap"
with col_m5:
    if st.button("COCONUT PADS"): st.session_state.target = "coco"

st.divider()

# --- 제품 데이터 정의 ---
products = {
    "cloth": {
        "title": "스웨덴 행주 블랙 에디션",
        "tag": "ZERO WASTE KITCHEN",
        "desc": "1949년 전통의 북유럽 기술력. 자기 무게의 15배를 흡수하는 혁신적 원단.",
        "img": "https://images.unsplash.com/photo-1584622650111-993a426fbf0a?w=800"
    },
    "brush": {
        "title": "대나무 칫솔 10색 에디션",
        "tag": "SUSTAINABLE ORAL CARE",
        "desc": "천연 밀랍 코팅으로 위생을 더한 온 가족을 위한 컬러풀한 선택.",
        "img": "https://images.unsplash.com/photo-1600091106710-fb9831f6217c?w=800"
    },
    "wrap": {
        "title": "프리미엄 비즈왁스랩",
        "tag": "NATURAL FOOD STORAGE",
        "desc": "유기농 면과 천연 밀랍의 조화. 다시 쓰는 신선함으로 지구를 지키세요.",
        "img": "https://images.unsplash.com/photo-1610348725531-843dff563e2c?w=800"
    },
    "coco": {
        "title": "생분해 코코넛 수세미",
        "tag": "PLANT-BASED CLEANING",
        "desc": "미세 플라스틱 걱정 없는 100% 생분해 코코넛 섬유 세척력.",
        "img": "https://images.unsplash.com/photo-1583947215259-38e31be8751f?w=800"
    }
}

# 5. [메인 화면] 
# 클릭한 버튼에 따라 특정 제품을 최상단에 보여주거나, 전체를 보여주는 로직
target = st.session_state.get("target", "all")

if target == "all":
    # 전체 보기 (스크롤 레이아웃)
    st.image("https://images.unsplash.com/photo-1542601906990-b4d3fb773b09?w=1600", use_container_width=True)
    for key, p in products.items():
        st.markdown(f"""
            <div class="product-box">
                <p class="gold-tag">{p['tag']}</p>
                <h2 style="color: #1A3021;">{p['title']}</h2>
                <p style="color: #666; max-width: 600px; margin: 0 auto;">{p['desc']}</p>
            </div>
        """, unsafe_allow_html=True)
        st.image(p['img'], use_container_width=True)
else:
    # 특정 카테고리 클릭 시 해당 상품만 크게 보여줌 (Interactive)
    p = products[target]
    col_img, col_txt = st.columns([1.5, 1])
    with col_img:
        st.image(p['img'], use_container_width=True)
    with col_txt:
        st.markdown(f"<p class='gold-tag' style='margin-top:100px;'>{p['tag']}</p>", unsafe_allow_html=True)
        st.header(p['title'])
        st.write(p['desc'])
        if st.button("Back to All Products"):
            st.session_state.target = "all"
            st.rerun()

# 6. [푸터]
st.markdown("""
    <div style="background-color: white; padding: 100px 0; text-align: center; border-top: 1px solid #D3D3D3; margin-top: 50px;">
        <h2 style="letter-spacing: 10px; font-weight: 300; color: #1A3021;">MADE IN NATURE</h2>
        <p style="color: #D3D3D3; font-size: 12px;">서울특별시 그린구 에코로 123 | COPYRIGHT © MADE IN NATURE</p>
    </div>
""", unsafe_allow_html=True)
