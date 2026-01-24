import streamlit as st
import base64

# --- SECTION 1: GLOBAL STYLE & HEADER ---

def run_section_1():
    st.set_page_config(page_title="Made in Nature | Official", layout="wide")

    # 중앙 정렬 및 브랜드 컬러 CSS
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Noto+Serif+KR:wght@200;400;700&display=swap');
        
        /* 전체 요소 중앙 정렬 및 배경 */
        html, body, [class*="css"], .stMarkdown {
            font-family: 'Noto Serif KR', serif;
            text-align: center;
            justify-content: center;
        }
        
        .main .block-container {
            max-width: 1100px;
            margin: 0 auto;
            padding-top: 5rem;
        }

        /* 로고 헤더 스타일 */
        .logo-container {
            position: relative;
            padding: 60px 0;
            margin-bottom: 20px;
        }
        .logo-text {
            font-size: 3.5rem;
            letter-spacing: 0.8rem;
            color: #1B3022;
            font-weight: 200;
            position: relative;
            z-index: 2;
        }
        .logo-bg-image {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 250px; /* 로고 크기 조절 */
            opacity: 0.15;
            z-index: 1;
        }
        </style>
    """, unsafe_allow_html=True)

    # 헤더 구현
    # 'your_logo_path.png'에 실제 파일 경로를 입력하세요.
    logo_path = "logo.png" 
    
    st.markdown(f"""
        <div class="logo-container">
            <img src="{logo_path}" class="logo-bg-image">
            <h1 class="logo-text">MADE IN NATURE</h1>
            <div style="width:50px; height:1px; background:#C5A059; margin:30px auto;"></div>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    run_section_1()

# --- SECTION 2: HERO & AUTOMATIC SHOWCASE ---

def run_section_2():
    # 1. Hero 배너 (배경 이미지 지정)
    # hero_bg.jpg 파일 경로를 직접 지정하세요.
    hero_bg_path = "hero_bg.jpg" 

    st.markdown(f"""
        <style>
        .hero-banner {{
            background: linear-gradient(rgba(0,0,0,0.3), rgba(0,0,0,0.3)), url("{hero_bg_path}");
            background-size: cover;
            background-position: center;
            height: 450px;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 5px;
            color: white;
        }}
        .hero-content h2 {{
            font-size: 1.2rem;
            color: #C5A059;
            letter-spacing: 0.5rem;
            margin-bottom: 15px;
        }}
        .hero-content h1 {{
            font-size: 3rem;
            font-weight: 200;
        }}
        </style>
        <div class="hero-banner">
            <div class="hero-content">
                <h2>Nature, defined by luxury</h2>
                <h1>자연의 가치를 증명하다</h1>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # 2. 이미지 쇼케이스 (5개 이미지 슬라이드 효과)
    st.markdown("<h3 style='margin-top:80px; font-weight:200; color:#1B3022;'>BRAND SHOWCASE</h3>", unsafe_allow_html=True)
    st.markdown("<div style='width:30px; height:1px; background:#C5A059; margin:15px auto 40px;'></div>", unsafe_allow_html=True)

    # 쇼케이스 이미지 경로 리스트 (실제 파일 경로로 수정)
    showcase_images = ["img1.jpg", "img2.jpg", "img3.jpg", "img4.jpg", "img5.jpg"]
    
    # 슬라이드 쇼 (Streamlit 순환 구현)
    # 실제 운영 시에는 간단한 HTML/JS 코드로 자동 슬라이드를 구현하거나 
    # 아래와 같이 정적인 정렬 후 캡션과 함께 배치합니다.
    
    cols = st.columns(5)
    for idx, img_path in enumerate(showcase_images):
        with cols[idx]:
            # 코드상에 이미지를 직접 넣기 (파일 업로드 옵션 제거)
            st.image(img_path, use_container_width=True)
            st.caption(f"Showcase {idx+1}")

if __name__ == "__main__":
    run_section_2()

# --- SECTION 3: COLLECTION & PRODUCT DETAILS ---

def run_section_3():
    st.markdown("<h2 style='margin-top:100px; letter-spacing:0.3rem;'>COLLECTIONS</h2>", unsafe_allow_html=True)
    
    tabs = st.tabs(["화장품 & 화장소품", "건강식품", "생활잡화"])
    
    # 제품별 이미지 경로 매핑 (실제 경로로 수정 필요)
    product_images = {
        "기름종이": "oil_paper.jpg",
        "스타페이스": "patch.jpg",
        "도파민패치": "dopamine.jpg",
        "나이트패치": "night.jpg",
        "수세미": "scrubber.jpg",
        "칫솔": "toothbrush.jpg"
    }

    with tabs[0]: # 화장품
        c1, c2 = st.columns(2)
        with c1:
            st.image(product_images["기름종이"], width=300)
            st.markdown("### 프리미엄 기름종이")
            st.write("피부 유분을 자극 없이 흡수하는 천연 마 소재.")
            st.button("제품 상세 페이지 이동", key="det1")
        with c2:
            st.image(product_images["스타페이스"], width=300)
            st.markdown("### 스타페이스 여드름패치")
            st.write("트러블을 빠르고 조용하게 진정시키는 스팟 솔루션.")
            st.button("제품 상세 페이지 이동", key="det2")

    with tabs[1]: # 건강식품
        c1, c2 = st.columns(2)
        with c1:
            st.image(product_images["도파민패치"], width=300)
            st.markdown("### 도파민 패치")
            st.write("일상의 활력을 되찾아주는 에너제틱 솔루션.")
            st.button("제품 상세 페이지 이동", key="det3")
        with c2:
            st.image(product_images["나이트패치"], width=300)
            st.markdown("### 나이트 패치")
            st.write("고요한 휴식을 선사하는 아로마 릴렉싱.")
            st.button("제품 상세 페이지 이동", key="det4")

    with tabs[2]: # 생활잡화
        c1, c2 = st.columns(2)
        with c1:
            st.image(product_images["수세미"], width=300)
            st.markdown("### 코코넛 수세미")
            st.write("자연에서 온 거친 섬유의 완벽한 세척력.")
            st.button("제품 상세 페이지 이동", key="det5")
        with c2:
            st.image(product_images["칫솔"], width=300)
            st.markdown("### 대나무 칫솔")
            st.write("지속 가능한 욕실을 위한 친환경 선택.")
            st.button("제품 상세 페이지 이동", key="det6")

if __name__ == "__main__":
    run_section_3()

# --- SECTION 4: FOOTER & CONTACT ---

def run_section_4():
    import streamlit as st

    # 1. 푸터 전용 스타일 (중앙 정렬 강조)
    st.markdown("""
        <style>
        .footer-outer {
            background-color: #1B3022; /* 다크 그린 */
            color: #FFFFFF;
            padding: 100px 0 60px 0;
            margin-top: 150px;
            text-align: center;
            border-top: 2px solid #C5A059; /* 골드 포인트 라인 */
        }
        .footer-content {
            max-width: 800px;
            margin: 0 auto;
        }
        .footer-logo {
            font-size: 1.8rem;
            letter-spacing: 0.5rem;
            color: #C5A059;
            margin-bottom: 20px;
            font-weight: 200;
        }
        .footer-info {
            color: #BBBBBB;
            font-size: 0.9rem;
            line-height: 2;
            margin-bottom: 40px;
        }
        .footer-links {
            margin-bottom: 40px;
        }
        .footer-links a {
            color: #FFFFFF;
            text-decoration: none;
            margin: 0 20px;
            font-size: 0.8rem;
            letter-spacing: 0.1rem;
            transition: 0.3s;
        }
        .footer-links a:hover {
            color: #A4C639; /* 라임 그린 호버 */
        }
        .copyright {
            font-size: 0.75rem;
            color: #666666;
            margin-top: 50px;
            letter-spacing: 0.05rem;
        }
        </style>
    """, unsafe_allow_html=True)

    # 2. 하단 디자인 구현
    st.markdown("""
        <div class="footer-outer">
            <div class="footer-content">
                <div class="footer-logo">MADE IN NATURE</div>
                <div style="width:30px; height:1px; background:#C5A059; margin:0 auto 30px;"></div>
                
                <p class="footer-info">
                    자연의 본질을 연구하고 지속 가능한 가치를 디자인합니다.<br>
                    우리는 당신의 일상이 자연과 더 가까워질 수 있도록<br>
                    최상의 원료와 장인 정신을 고집합니다.
                </p>

                <div class="footer-links">
                    <a href="#">BRAND STORY</a>
                    <a href="#">COLLECTIONS</a>
                    <a href="#">SUSTAINABILITY</a>
                    <a href="#">CONTACT</a>
                </div>

                <div style="color: #888; font-size: 0.85rem; line-height: 1.8;">
                    주식회사 메이드인네이처 | 서울특별시 성동구 성수동 자연길 123<br>
                    Customer Care. 02-1234-5678 | Email. official@madeinnature.com<br>
                    Instagram. @madeinnature_official
                </div>

                <div class="copyright">
                    © 2026 MADE IN NATURE. ALL RIGHTS RESERVED.<br>
                    PREMIUM NATURALISM & LUXURY DESIGN.
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    run_section_4()
    
