import streamlit as st
from PIL import Image

# --- SECTION 1: GLOBAL STYLE & HEADER ---

def run_section_1():
    st.set_page_config(page_title="Made in Nature | Premium", layout="wide")

    # 고급스러운 디자인을 위한 통합 CSS
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Noto+Serif+KR:wght@200;400;700&display=swap');
        html, body, [class*="css"] {
            font-family: 'Noto Serif KR', serif;
            background-color: #FDFDFD;
        }
        /* 사이드바 제거를 위해 메인 컨텐츠 너비 확장 */
        .main .block-container {
            padding-top: 2rem;
            max-width: 1200px;
        }
        .header-wrapper {
            text-align: center;
            padding: 40px 0;
            position: relative;
        }
        .logo-title {
            font-size: 3rem;
            letter-spacing: 0.8rem;
            color: #1B3022;
            font-weight: 200;
            margin-bottom: 0;
            z-index: 2;
            position: relative;
        }
        .logo-image-bg {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            opacity: 0.3; /* 로고가 문구 뒤에 은은하게 깔리도록 설정 */
            z-index: 1;
        }
        </style>
    """, unsafe_allow_html=True)

    # 헤더 및 로고 업로드 기능
    with st.container():
        st.markdown('<div class="header-wrapper">', unsafe_allow_html=True)
        
        # 로고 이미지 업로드 (문구 뒤 배치용)
        logo_file = st.file_uploader("상단 로고 이미지 업로드 (MADE IN NATURE 문구 뒤에 배치됩니다)", type=['png', 'jpg', 'svg'], key="main_logo")
        
        if logo_file:
            # 로고가 있을 경우 문구 뒤에 배경처럼 배치
            st.image(logo_file, width=200) # 실제 구현 시 CSS position으로 문구 뒤 배치 유도
            
        st.markdown('<h1 class="logo-title">MADE IN NATURE</h1>', unsafe_allow_html=True)
        st.markdown('<div style="width:60px; height:1px; background:#C5A059; margin:20px auto;"></div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    run_section_1()

# --- SECTION 2: HERO & BRAND STORY ---

def run_section_2():
    st.markdown("---")
    
    # Hero 배경 이미지 업로드
    hero_bg = st.file_uploader("Hero 섹션 배경 이미지를 선택하세요 (Nature, defined by luxury 배경)", type=['jpg', 'jpeg', 'png'], key="hero_bg_upload")
    
    # 배경 이미지 유무에 따른 스타일 동적 생성
    bg_url = ""
    if hero_bg:
        # 업로드된 이미지를 임시 경로로 사용 (실제 앱에선 base64 변환 권장)
        st.image(hero_bg, caption="현재 설정된 배경", use_container_width=True)
    
    st.markdown(f"""
        <style>
        .hero-section {{
            height: 500px;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            background-color: #1B3022; /* 기본 다크그린 */
            border-radius: 20px;
            color: white;
            margin: 40px 0;
            overflow: hidden;
        }}
        .hero-text-gold {{
            color: #C5A059;
            font-size: 1.2rem;
            letter-spacing: 0.4rem;
            text-transform: uppercase;
        }}
        .hero-main-title {{
            font-size: 3.5rem;
            font-weight: 200;
            letter-spacing: 0.2rem;
        }}
        </style>
        <div class="hero-section">
            <div>
                <p class="hero-text-gold">Nature, defined by luxury</p>
                <h2 class="hero-main-title">자연의 본질을 디자인하다</h2>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # 브랜드 스토리
    st.markdown("""
        <div style="text-align:center; padding: 60px 0;">
            <p style="color:#A4C639; font-weight:bold; letter-spacing:0.1rem;">PHILOSOPHY</p>
            <h3 style="font-size:2rem; color:#1B3022;">"우리는 자연의 결을 살리는 최소한의 개입을 지향합니다."</h3>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    run_section_2()

# --- SECTION 3: COLLECTION & INTERACTIVE SHOP ---

def run_section_3():
    import streamlit as st
    from PIL import Image

    # 1. 컬렉션 섹션 전용 스타일
    st.markdown("""
        <style>
        /* 카테고리 탭 디자인 */
        .stTabs [data-baseweb="tab-list"] {
            display: flex;
            justify-content: center;
            gap: 50px;
            border-bottom: 1px solid #E0E0E0;
        }
        .stTabs [data-baseweb="tab"] {
            font-size: 1.1rem;
            color: #888;
            padding: 10px 20px;
        }
        .stTabs [data-baseweb="tab-highlight"] {
            background-color: #C5A059; /* 골드 하이라이트 */
        }
        
        /* 제품 카드 디자인 */
        .product-box {
            border: 1px solid #F0F0F0;
            border-radius: 12px;
            padding: 30px;
            text-align: center;
            background-color: #FFFFFF;
            margin-bottom: 30px;
            transition: 0.3s;
        }
        .product-box:hover {
            border-color: #C5A059;
            box-shadow: 0 10px 20px rgba(0,0,0,0.05);
        }
        .detail-btn {
            display: inline-block;
            margin-top: 15px;
            padding: 8px 20px;
            border: 1px solid #1B3022;
            color: #1B3022;
            text-decoration: none;
            font-size: 0.85rem;
            transition: 0.3s;
            cursor: pointer;
        }
        .detail-btn:hover {
            background-color: #1B3022;
            color: white;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<h2 style='text-align:center; letter-spacing:0.3rem; margin-top:50px;'>OUR COLLECTIONS</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#666; margin-bottom:50px;'>카테고리를 선택하여 제품의 상세 정보를 확인하세요.</p>", unsafe_allow_html=True)

    # 2. 카테고리 설정 (요청하신 3가지 그룹)
    tabs = st.tabs(["화장품 & 화장소품", "건강식품", "생활잡화"])

    # 제품 데이터 정의
    product_data = {
        "화장품 & 화장소품": [
            {"name": "프리미엄 기름종이", "desc": "피부 본연의 수분은 남기고 유분만 섬세하게 제거합니다.", "price": "12,000", "spec": "100매입 / 천연 마 소재"},
            {"name": "스타페이스 여드름패치", "desc": "자연 유래 성분으로 트러블을 빠르게 진정시키는 스팟 케어.", "price": "15,000", "spec": "36패치 / 하이드로콜로이드"}
        ],
        "건강식품": [
            {"name": "도파민 패치", "desc": "활기찬 하루를 위한 에너지 부스팅 패치 솔루션.", "price": "28,000", "spec": "10매입 / 비타민B군 복합체"},
            {"name": "나이트 패치", "desc": "깊고 편안한 밤을 위한 아로마 테라피 릴렉싱 패치.", "price": "28,000", "spec": "10매입 / 라벤더 추출물"}
        ],
        "생활잡화": [
            {"name": "코코넛 수세미", "desc": "미세 플라스틱 걱정 없는 100% 생분해성 천연 수세미.", "price": "5,500", "spec": "코코넛 섬유 / 핸드메이드"},
            {"name": "대나무 칫솔", "desc": "플라스틱 사용을 줄이는 친환경 대나무 소재와 미세모.", "price": "4,000", "spec": "탄화 대나무 / BPA Free"}
        ]
    }

    # 3. 탭별 제품 리스트 구현
    for idx, (cat_name, products) in enumerate(product_data.items()):
        with tabs[idx]:
            cols = st.columns(2)
            for i, product in enumerate(products):
                with cols[i % 2]:
                    st.markdown(f"""
                        <div class="product-box">
                            <p style="color:#A4C639; font-size:0.8rem; font-weight:bold;">MADE IN NATURE</p>
                            <h3 style="margin-bottom:10px;">{product['name']}</h3>
                            <p style="color:#666; font-size:0.9rem; min-height:50px;">{product['desc']}</p>
                            <p style="color:#C5A059; font-weight:bold; font-size:1.1rem;">₩{product['price']}</p>
                        </div>
                    """, unsafe_allow_html=True)
                    
                    # 이미지 업로드 기능 (직접 넣기)
                    img_file = st.file_uploader(f"{product['name']} 이미지 등록", type=['jpg', 'png'], key=f"img_{cat_name}_{i}")
                    if img_file:
                        st.image(img_file, use_container_width=True)
                    else:
                        st.info("제품 이미지를 업로드해주세요.")

                    # 상세 페이지 이동 시뮬레이션
                    if st.button(f"제품 상세 페이지 이동", key=f"btn_{cat_name}_{i}"):
                        st.session_state['selected_product'] = product
                        st.session_state['page'] = 'detail'
                        st.rerun()

    # 4. (참고) 상세 페이지 전환 로직 (세션 상태 활용)
    if 'page' in st.session_state and st.session_state['page'] == 'detail':
        st.divider()
        p = st.session_state['selected_product']
        st.markdown(f"### [Detailed View] {p['name']}")
        st.write(f"**제품 상세 스펙:** {p['spec']}")
        st.write("이곳은 제품의 상세한 성분, 사용 방법, 고객 리뷰 등이 들어가는 페이지입니다.")
        if st.button("목록으로 돌아가기"):
            st.session_state['page'] = 'main'
            st.rerun()

if __name__ == "__main__":
    run_section_3()

# --- SECTION 4: FOOTER & CONTACT ---

def run_section_4():
    import streamlit as st

    # 1. 푸터 전용 스타일 (사이드바 없는 와이드 레이아웃 최적화)
    st.markdown("""
        <style>
        .footer-wrapper {
            background-color: #1B3022; /* 다크 그린 */
            color: #FFFFFF;
            padding: 100px 5% 50px 5%;
            margin-top: 120px;
            border-top: 4px solid #C5A059; /* 골드 포인트 라인 */
        }
        .contact-section {
            max-width: 900px;
            margin: 0 auto;
            text-align: center;
            padding-bottom: 80px;
        }
        .footer-grid {
            display: grid;
            grid-template-columns: 2fr 1fr 1fr 1.5fr;
            gap: 40px;
            border-top: 1px solid rgba(255,255,255,0.1);
            padding-top: 60px;
        }
        .footer-col h4 {
            color: #C5A059;
            font-size: 1.1rem;
            margin-bottom: 25px;
            letter-spacing: 0.1rem;
        }
        .footer-col p, .footer-col a {
            color: #BBBBBB;
            font-size: 0.85rem;
            line-height: 1.8;
            text-decoration: none;
            display: block;
        }
        .footer-col a:hover {
            color: #A4C639; /* 라임 그린 호버 */
        }
        .copyright-text {
            text-align: center;
            margin-top: 80px;
            font-size: 0.75rem;
            color: #666666;
            letter-spacing: 0.05rem;
        }
        </style>
    """, unsafe_allow_html=True)

    # 2. Contact Us 섹션 (와이드 화면 중앙 배치)
    st.markdown("<div class='contact-section'>", unsafe_allow_html=True)
    st.markdown("<h2 style='letter-spacing: 0.3rem; color: #1B3022;'>GET IN TOUCH</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #888;'>메이드인네이처의 프리미엄 파트너십 및 제품 문의</p>", unsafe_allow_html=True)
    
    # 폼 레이아웃
    c1, c2 = st.columns(2)
    with c1:
        st.text_input("Name", key="footer_name", placeholder="성함을 입력하세요")
    with c2:
        st.text_input("Email", key="footer_email", placeholder="이메일을 입력하세요")
    
    st.text_area("Message", key="footer_msg", placeholder="문의 내용을 입력해 주세요", height=150)
    
    if st.button("SUBMIT INQUIRY", use_container_width=True):
        st.success("소중한 문의가 접수되었습니다. 담당자가 곧 연락드리겠습니다.")
    st.markdown("</div>", unsafe_allow_html=True)

    # 3. 하단 푸터 레이아웃
    st.markdown(f"""
        <div class="footer-wrapper">
            <div class="footer-grid">
                <div class="footer-col">
                    <h4>MADE IN NATURE</h4>
                    <p>자연의 순수함을 현대적 감각으로 재해석한 프리미엄 라이프스타일 브랜드입니다. 우리는 지속 가능한 아름다움의 가치를 믿습니다.</p>
                </div>
                <div class="footer-col">
                    <h4>SHOP</h4>
                    <a href="#">Cosmetics</a>
                    <a href="#">Health Food</a>
                    <a href="#">Lifestyle</a>
                </div>
                <div class="footer-col">
                    <h4>SUPPORT</h4>
                    <a href="#">FAQ</a>
                    <a href="#">Shipping</a>
                    <a href="#">Privacy Policy</a>
                </div>
                <div class="footer-col">
                    <h4>CONTACT</h4>
                    <p>서울특별시 성동구 성수동 자연길 123</p>
                    <p>T. 02-1234-5678</p>
                    <p>E. official@madeinnature.com</p>
                </div>
            </div>
            <div class="copyright-text">
                © 2026 MADE IN NATURE. ALL RIGHTS RESERVED. <br>
                DESIGNED WITH LIME GREEN, GOLD, AND DEEP FOREST GREEN.
            </div>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    run_section_4()
