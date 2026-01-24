import streamlit as st

# 1. 페이지 설정
st.set_page_config(page_title="made in nature | Premium Naturalism", layout="wide")

# 2. 크리드 스타일 CSS 적용
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Serif+KR:wght@300;400&display=swap');
    
    html, body, [class*="css"] { font-family: 'Noto Serif KR', serif; }
    
    /* 헤더 스타일 */
    .brand-header { text-align: center; padding: 40px 0; }
    .brand-logo { font-size: 50px; letter-spacing: 8px; font-weight: 300; color: #1A3021; margin-bottom: 0; }
    .brand-sub { font-size: 12px; letter-spacing: 3px; color: #D4AF37; }
    
    /* 내비게이션 */
    .nav-bar { display: flex; justify-content: center; gap: 40px; border-top: 1px solid #eee; border-bottom: 1px solid #eee; padding: 15px 0; margin-bottom: 30px; }
    .nav-item { font-size: 13px; font-weight: bold; cursor: pointer; color: #333; }
    
    /* 상품 카드 */
    .product-card { text-align: center; padding: 10px; transition: 0.3s; }
    .product-name { font-size: 16px; margin-top: 15px; font-weight: 400; }
    .product-price { color: #d32f2f; font-weight: bold; font-size: 15px; }
    .price-original { text-decoration: line-through; color: #999; font-size: 12px; margin-right: 5px; }
    
    /* 섹션 타이틀 */
    .section-title { text-align: center; font-size: 28px; letter-spacing: 2px; margin: 60px 0 30px 0; font-weight: 400; }
    </style>
    """, unsafe_allow_html=True)

# 3. 상단 브랜드 로고 및 내비게이션 (이미지 1 & 4 스타일)
st.markdown("""
    <div class="brand-header">
        <p class="brand-sub">ESTABLISHED 2025</p>
        <h1 class="brand-logo">MADE IN NATURE</h1>
    </div>
    <div class="nav-bar">
        <div class="nav-item">BEST</div>
        <div class="nav-item">LIVING</div>
        <div class="nav-item">KITCHEN</div>
        <div class="nav-item">BATH</div>
        <div class="nav-item">GIFT SET</div>
        <div class="nav-item">STORY</div>
    </div>
    """, unsafe_allow_html=True)

# 4. 메인 히어로 섹션 (이미지 1 스타일)
# 자연 친화적인 메인 비주얼
st.image("https://images.unsplash.com/photo-1542601906990-b4d3fb773b09?auto=format&fit=crop&w=1600&q=80", 
         caption="자연에서 온 정직한 가치, 프리미엄 제로웨이스트 라이프", use_container_width=True)

# 5. BEST 상품 랭킹 섹션 (이미지 2 스타일)
st.markdown("<h2 class='section-title'>BEST SELLER</h2>", unsafe_allow_html=True)
best_tabs = st.tabs(["실시간 인기", "주간 베스트", "선물하기"])

with best_tabs[0]:
    col1, col2, col3, col4 = st.columns(4)
    
    products = [
        {"name": "스웨덴 행주 블랙 에디션", "price": "12,000", "old": "15,000", "img": "https://via.placeholder.com/400x400/1A3021/FFFFFF?text=Black+Edition"},
        {"name": "대나무 칫솔 10색 세트", "price": "18,900", "old": "22,000", "img": "https://via.placeholder.com/400x400/F5F5F5/1A3021?text=Bamboo+Care"},
        {"name": "천연 비즈왁스랩 M", "price": "8,500", "old": "10,000", "img": "https://via.placeholder.com/400x400/D4AF37/FFFFFF?text=Beeswax+Wrap"},
        {"name": "코코넛 수세미 3종", "price": "6,000", "old": "7,500", "img": "https://via.placeholder.com/400x400/E8E8E8/1A3021?text=Coconut+Pad"}
    ]
    
    for idx, col in enumerate([col1, col2, col3, col4]):
        with col:
            st.markdown(f"""
                <div class="product-card">
                    <img src="{products[idx]['img']}" style="width:100%;">
                    <div class="product-name"><b>{idx+1}</b>. {products[idx]['name']}</div>
                    <div><span class="price-original">{products[idx]['old']}원</span><span class="product-price">10% {products[idx]['price']}원</span></div>
                </div>
            """, unsafe_allow_html=True)
            st.button("SHOP NOW", key=f"best_{idx}", use_container_width=True)

# 6. 컬렉션 스토리 섹션 (이미지 3 스타일)
st.markdown("<h2 class='section-title'>OUR COLLECTION STORY</h2>", unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)

with c1:
    st.image("https://images.unsplash.com/photo-1584622650111-993a426fbf0a?auto=format&fit=crop&w=600&q=80")
    st.subheader("KITCHEN ZERO WASTE")
    st.write("스웨덴 행주와 코코넛 수세미가 만드는 미세플라스틱 없는 주방.")
    st.caption("더 알아보기 >")

with c2:
    st.image("https://images.unsplash.com/photo-1600091106710-fb9831f6217c?auto=format&fit=crop&w=600&q=80")
    st.subheader("BAMBOO ORAL CARE")
    st.write("대나무 칫솔 10색 에디션으로 완성하는 온 가족의 건강한 양치 습관.")
    st.caption("더 알아보기 >")

with c3:
    st.image("https://images.unsplash.com/photo-1610348725531-843dff563e2c?auto=format&fit=crop&w=600&q=80")
    st.subheader("NATURAL FOOD STORAGE")
    st.write("비즈왁스랩으로 식재료의 수분은 지키고 지구는 더 깨끗하게.")
    st.caption("더 알아보기 >")

# 7. 푸터 (이미지 4 스타일)
st.markdown("""
    <div style="background-color: #f9f9f9; padding: 80px 20px; text-align: center; border-top: 1px solid #eee; margin-top: 100px;">
        <h2 style="letter-spacing: 5px; font-weight: 300;">MADE IN NATURE</h2>
        <p style="color: #666; font-size: 13px; max-width: 600px; margin: 20px auto;">
            우리는 자연 본연의 힘을 믿습니다. 불필요한 것을 덜어내고 
            지속 가능한 아름다움을 제안하는 프리미엄 네추럴리즘 브랜드입니다.
        </p>
        <div style="margin-top: 20px; font-size: 12px; color: #999;">
            © 2025 MADE IN NATURE. ALL RIGHTS RESERVED.
        </div>
    </div>
    """, unsafe_allow_html=True)
