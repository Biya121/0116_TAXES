import streamlit as st
from PIL import Image
import base64

# --- SECTION 1: GLOBAL STYLE & HEADER ---

def run_section_1():
    # 1. 페이지 레이아웃 및 폰트 설정
    st.set_page_config(page_title="Made in Nature | Premium Luxury", layout="wide")

    # 2. 고급스러운 디자인을 위한 CSS (Custom Styling)
    st.markdown("""
        <style>
        /* 기본 배경 및 폰트 */
        @import url('https://fonts.googleapis.com/css2?family=Noto+Serif+KR:wght@200;400;700&display=swap');
        
        html, body, [class*="css"] {
            font-family: 'Noto Serif KR', serif;
            background-color: #FDFDFD;
            color: #1A2E1A;
        }

        /* 메인 컬러 정의 */
        :root {
            --dark-green: #1B3022;
            --mid-green: #2D5A27;
            --lime-green: #A4C639;
            --luxury-gold: #C5A059;
            --soft-grey: #F2F2F2;
        }

        /* 헤더 스타일 */
        .header-container {
            padding: 2rem 0rem;
            text-align: center;
            border-bottom: 1px solid var(--soft-grey);
            margin-bottom: 2rem;
        }
        
        .logo-text {
            font-size: 2.5rem;
            letter-spacing: 0.5rem;
            color: var(--dark-green);
            font-weight: 200;
            text-transform: uppercase;
        }

        .gold-divider {
            width: 50px;
            height: 2px;
            background-color: var(--luxury-gold);
            margin: 10px auto;
        }

        /* 버튼 및 입력창 커스텀 */
        .stButton>button {
            border: 1px solid var(--luxury-gold);
            background-color: transparent;
            color: var(--luxury-gold);
            transition: 0.3s;
            padding: 0.5rem 2rem;
        }
        .stButton>button:hover {
            background-color: var(--luxury-gold);
            color: white;
        }
        </style>
    """, unsafe_allow_html=True)

    # 3. 헤더 영역 구현
    st.markdown("""
        <div class="header-container">
            <div class="logo-text">MADE IN NATURE</div>
            <div class="gold-divider"></div>
            <p style="font-size: 0.9rem; color: #888; letter-spacing: 0.2rem;">PURE • ORGANIC • LUXURY</p>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    run_section_1()

# --- SECTION 2: HERO & BRAND STORY ---

def run_section_2():
    import streamlit as st

    # 1. Hero 섹션 전용 스타일 (그라데이션 및 애니메이션)
    st.markdown("""
        <style>
        .hero-container {
            position: relative;
            background: linear-gradient(rgba(27, 48, 34, 0.6), rgba(27, 48, 34, 0.6)), 
                        url('https://images.unsplash.com/photo-1542601906990-b4d3fb773b09?auto=format&fit=crop&q=80&w=2000');
            background-size: cover;
            background-position: center;
            height: 600px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            flex-direction: column;
            text-align: center;
            border-radius: 15px;
            margin-bottom: 50px;
        }
        
        .hero-title {
            font-size: 3.5rem;
            font-weight: 200;
            margin-bottom: 10px;
            letter-spacing: 0.3rem;
            animation: fadeInDown 1.5s;
        }
        
        .hero-subtitle {
            font-size: 1.2rem;
            color: #C5A059; /* 포인트 골드 */
            letter-spacing: 0.5rem;
            margin-bottom: 30px;
            animation: fadeInUp 1.5s;
        }

        .brand-story-box {
            padding: 80px 10%;
            background-color: #FFFFFF;
            text-align: center;
        }

        .story-label {
            color: #A4C639; /* 라임 그린 */
            font-size: 0.9rem;
            font-weight: bold;
            letter-spacing: 0.2rem;
            margin-bottom: 20px;
        }

        .story-text {
            font-size: 1.8rem;
            line-height: 1.6;
            color: #1B3022;
            font-weight: 400;
            max-width: 800px;
            margin: 0 auto;
        }

        @keyframes fadeInUp {
            from { opacity: 0; transform: translateY(30px); }
            to { opacity: 1; transform: translateY(0); }
        }
        @keyframes fadeInDown {
            from { opacity: 0; transform: translateY(-30px); }
            to { opacity: 1; transform: translateY(0); }
        }
        </style>
    """, unsafe_allow_html=True)

    # 2. Hero 비주얼 구현
    st.markdown("""
        <div class="hero-container">
            <div class="hero-title">Nature, Defined by Luxury</div>
            <div class="hero-subtitle">가장 순수한 자연이 전하는 고귀한 휴식</div>
        </div>
    """, unsafe_allow_html=True)

    # 3. 브랜드 스토리 구현 (3단 구성)
    st.markdown('<div class="brand-story-box">', unsafe_allow_html=True)
    st.markdown('<p class="story-label">OUR PHILOSOPHY</p>', unsafe_allow_html=True)
    st.markdown('<p class="story-text">"인위적인 것을 걷어내고,<br>오직 자연의 생명력만을 남겼습니다."</p>', unsafe_allow_html=True)
    
    st.write("") # 간격 조절
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("<h4 style='color:#C5A059;'>Pure Source</h4>", unsafe_allow_html=True)
        st.caption("청정 지역에서 선별된 최상급 원료")
    with col2:
        st.markdown("<h4 style='color:#C5A059;'>Sustainability</h4>", unsafe_allow_html=True)
        st.caption("지구와 함께 공존하는 패키징")
    with col3:
        st.markdown("<h4 style='color:#C5A059;'>Artisanship</h4>", unsafe_allow_html=True)
        st.caption("장인 정신으로 빚어낸 품질")
    
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    run_section_2()

# --- SECTION 3: INTERACTIVE SHOP ---

def run_section_3():
    import streamlit as st
    from PIL import Image

    # 1. 제품 섹션 전용 스타일 (카드 디자인 및 골드 포인트)
    st.markdown("""
        <style>
        .shop-header {
            text-align: center;
            padding: 50px 0;
            background-color: #f9fbf9;
            margin-top: 50px;
        }
        .product-card-container {
            border: 1px solid #e0e0e0;
            border-radius: 10px;
            padding: 25px;
            background-color: white;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            margin-bottom: 20px;
        }
        .product-card-container:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 25px rgba(27, 48, 34, 0.1);
            border-color: #C5A059; /* 골드 포인트 */
        }
        .price-tag {
            color: #C5A059;
            font-size: 1.2rem;
            font-weight: 700;
        }
        .upload-hint {
            font-size: 0.8rem;
            color: #888;
            margin-bottom: 10px;
        }
        /* 스트림릿 기본 탭 스타일 수정 */
        .stTabs [data-baseweb="tab-list"] {
            gap: 24px;
        }
        .stTabs [data-baseweb="tab"] {
            height: 50px;
            white-space: pre-wrap;
            background-color: transparent;
            border-radius: 4px 4px 0px 0px;
            color: #1B3022;
        }
        </style>
    """, unsafe_allow_html=True)

    # 2. 상단 타이틀 및 필터
    st.markdown("""
        <div class="shop-header">
            <h2 style='letter-spacing: 0.3rem;'>COLLECTION</h2>
            <p style='color: #666;'>당신이 머무는 공간과 몸에 자연의 품격을 더하세요.</p>
        </div>
    """, unsafe_allow_html=True)

    # 사이드바 필터 (Section 1에서 정의하지 않았다면 여기서 추가 가능)
    st.sidebar.markdown("---")
    st.sidebar.header("Filter Options")
    category = st.sidebar.radio("Collection", ["All", "Skin Care", "Body Care", "Home Fragrance"])
    price_range = st.sidebar.slider("Price Range (₩10,000)", 0, 300000, (30000, 200000), step=5000)

    # 3. 제품 데이터베이스 (디테일한 정보 추가)
    products = [
        {"id": 1, "name": "Deep Forest Essence", "category": "Skin Care", "price": 89000, "desc": "깊은 숲의 생명력을 담은 고농축 진정 에센스", "origin": "Jeju, Korea"},
        {"id": 2, "name": "Golden Honey Balm", "category": "Skin Care", "price": 56000, "desc": "천연 꿀 성분의 고보습 멀티 밤", "origin": "Provence, France"},
        {"id": 3, "name": "Ancient Wood Candle", "category": "Home Fragrance", "price": 42000, "desc": "차분한 샌달우드 향의 소이 캔들", "origin": "Kyoto, Japan"},
        {"id": 4, "name": "Emerald Bath Salt", "category": "Body Care", "price": 38000, "desc": "미네랄이 풍부한 프리미엄 사해 소금", "origin": "Dead Sea, Israel"},
        {"id": 5, "name": "Wild Bloom Perfume", "category": "Home Fragrance", "price": 125000, "desc": "야생화의 우아함을 담은 시그니처 향수", "origin": "Grasse, France"},
        {"id": 6, "name": "Silk Moss Body Lotion", "category": "Body Care", "price": 64000, "desc": "이끼의 싱그러움을 담은 실키 제형 로션", "origin": "Black Forest, Germany"},
    ]

    # 필터링 로직
    filtered = [p for p in products if (category == "All" or p["category"] == category) and (price_range[0] <= p["price"] <= price_range[1])]

    # 4. 제품 그리드 출력 (3열 구성)
    if not filtered:
        st.warning("선택하신 조건에 맞는 제품이 없습니다.")
    else:
        # 제품 리스트를 3개씩 끊어서 행 생성
        for i in range(0, len(filtered), 3):
            cols = st.columns(3)
            for j, product in enumerate(filtered[i:i+3]):
                with cols[j]:
                    st.markdown(f"""
                        <div class="product-card-container">
                            <span style="font-size: 0.7rem; color: #A4C639; font-weight: bold;">{product['category']}</span>
                            <h3 style="margin: 5px 0;">{product['name']}</h3>
                            <p class="price-tag">₩{product['price']:,}</p>
                            <p style="font-size: 0.85rem; color: #555;">{product['desc']}</p>
                        </div>
                    """, unsafe_allow_html=True)
                    
                    # --- 이미지 업로드 및 디테일 뷰 기능 ---
                    st.markdown("<p class='upload-hint'>📷 제품 이미지를 업로드하세요</p>", unsafe_allow_html=True)
                    img_file = st.file_uploader(f"Upload for {product['name']}", type=['jpg', 'png'], key=f"img_{product['id']}", label_visibility="collapsed")
                    
                    if img_file:
                        st.image(img_file, use_container_width=True)
                    else:
                        # 이미지가 없을 때 보여줄 플레이스홀더 (그레이 톤)
                        st.markdown("<div style='height:200px; background-color:#F2F2F2; border-radius:5px; display:flex; align-items:center; justify-content:center; color:#AAA;'>No Image</div>", unsafe_allow_html=True)
                    
                    with st.expander("View Product Details"):
                        tab1, tab2 = st.tabs(["Story", "Spec"])
                        with tab1:
                            st.write(f"**{product['name']}**은(는) {product['origin']}의 영감을 받아 제작되었습니다. 자연의 생명력을 가장 신선한 상태로 전달합니다.")
                        with tab2:
                            st.write(f"- 원산지: {product['origin']}")
                            st.write(f"- 용량: 50ml / 1.7 fl.oz.")
                            st.write("- 인증: ECOCERT Organic Certified")
                            st.markdown("<button style='width:100%; padding:10px; background-color:#1B3022; color:white; border:none;'>ADD TO CART</button>", unsafe_allow_html=True)

if __name__ == "__main__":
    run_section_3()

# --- SECTION 4: FOOTER & CONTACT ---

def run_section_4():
    import streamlit as st

    # 1. 푸터 전용 스타일 (다크 그린 배경 & 골드 텍스트)
    st.markdown("""
        <style>
        .footer-container {
            background-color: #1B3022; /* 다크 그린 */
            color: #FFFFFF;
            padding: 80px 10% 40px 10%;
            margin-top: 100px;
            border-top: 3px solid #C5A059; /* 골드 라인 */
        }
        .footer-column h4 {
            color: #C5A059; /* 골드 */
            font-size: 1.1rem;
            letter-spacing: 0.1rem;
            margin-bottom: 25px;
        }
        .footer-link {
            color: #CCC;
            text-decoration: none;
            font-size: 0.9rem;
            display: block;
            margin-bottom: 10px;
            transition: 0.3s;
        }
        .footer-link:hover {
            color: #A4C639; /* 라임 그린 */
            padding-left: 5px;
        }
        .contact-input input, .contact-input textarea {
            background-color: rgba(255,255,255,0.05) !important;
            border: 1px solid rgba(197, 160, 89, 0.3) !important;
            color: white !important;
        }
        .copyright {
            text-align: center;
            padding-top: 50px;
            margin-top: 50px;
            border-top: 1px solid rgba(255,255,255,0.1);
            font-size: 0.8rem;
            color: #888;
        }
        </style>
    """, unsafe_allow_html=True)

    # 2. 컨택 포인트 및 뉴스레터 섹션 (2컬럼)
    st.markdown("<h2 style='text-align:center; margin-top:80px; letter-spacing:0.2rem;'>CONTACT US</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#666; margin-bottom:40px;'>브랜드 협업 및 대량 구매 문의는 아래 양식을 이용해 주세요.</p>", unsafe_allow_html=True)

    c1, c2 = st.columns([1, 1])
    with c1:
        st.text_input("Full Name", placeholder="성함을 입력하세요.")
        st.text_input("Email Address", placeholder="이메일 주소를 입력하세요.")
    with c2:
        st.text_area("Message", placeholder="문의 내용을 작성해 주세요.", height=115)
    
    st.markdown("<div style='text-align:right;'>", unsafe_allow_html=True)
    if st.button("SEND MESSAGE"):
        st.success("메시지가 성공적으로 전달되었습니다. 24시간 이내에 답변드리겠습니다.")
    st.markdown("</div>", unsafe_allow_html=True)

    # 3. 푸터 레이아웃
    st.markdown("""
        <div class="footer-container">
            <div style="display: flex; justify-content: space-between; flex-wrap: wrap;">
                <div class="footer-column" style="flex: 1; min-width: 250px;">
                    <h4>MADE IN NATURE</h4>
                    <p style="font-size: 0.85rem; line-height: 1.8; color: #AAA;">
                        우리는 자연의 본질적인 아름다움을 연구합니다.<br>
                        지속 가능한 럭셔리를 향한 우리의 여정에<br>
                        함께해 주셔서 감사합니다.
                    </p>
                </div>
                <div class="footer-column" style="flex: 1; min-width: 150px;">
                    <h4>EXPLORE</h4>
                    <a class="footer-link" href="#">About Our Story</a>
                    <a class="footer-link" href="#">Ingredients List</a>
                    <a class="footer-link" href="#">Sustainability Report</a>
                    <a class="footer-link" href="#">Store Locator</a>
                </div>
                <div class="footer-column" style="flex: 1; min-width: 150px;">
                    <h4>CUSTOMER CARE</h4>
                    <a class="footer-link" href="#">Shipping & Returns</a>
                    <a class="footer-link" href="#">Privacy Policy</a>
                    <a class="footer-link" href="#">Membership Benefits</a>
                    <a class="footer-link" href="#">FAQ</a>
                </div>
                <div class="footer-column" style="flex: 1; min-width: 200px;">
                    <h4>CONNECT</h4>
                    <p style="font-size: 0.85rem; color: #AAA;">Instagram | Pinterest | YouTube</p>
                    <p style="font-size: 0.85rem; color: #AAA;">+82 (0)2 1234 5678</p>
                    <p style="font-size: 0.85rem; color: #AAA;">concierge@madeinnature.com</p>
                </div>
            </div>
            <div class="copyright">
                © 2026 MADE IN NATURE. DESIGNED FOR PREMIUM EXPERIENCE.<br>
                Primary: Lime Green - Green | Secondary: White & Grey | Point: Gold
            </div>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    run_section_4()
