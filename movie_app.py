import streamlit as st
import os
import base64
import time
import streamlit.components.v1 as components
from typing import Optional, List, Dict

# =========================
# 0) PAGE CONFIG (MUST BE FIRST)
# =========================
st.set_page_config(page_title="Made in Nature | Official", layout="wide")

# =========================
# 1) UTILITIES
# =========================
def file_exists(path: str) -> bool:
    return bool(path) and os.path.isfile(path)

def to_data_url(path: str) -> Optional[str]:
    """Convert local image file to base64 data URL for reliable HTML/CSS embedding."""
    if not file_exists(path):
        return None
    ext = os.path.splitext(path)[1].lower().strip(".")
    if ext not in ["png", "jpg", "jpeg", "webp"]:
        return None
    mime = "image/jpeg" if ext in ["jpg", "jpeg"] else f"image/{ext}"
    with open(path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode("utf-8")
    return f"data:{mime};base64,{b64}"

def safe_image(path: str, *, use_container_width: bool = True, width: Optional[int] = None, caption: Optional[str] = None):
    """Show image if exists, otherwise show a subtle placeholder."""
    if file_exists(path):
        st.image(path, use_container_width=use_container_width, width=width, caption=caption)
    else:
        st.markdown(
            f"""
            <div class="img-missing">
                <div class="img-missing-title">IMAGE NOT FOUND</div>
                <div class="img-missing-path">{path}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

def set_defaults():
    if "selected_product" not in st.session_state:
        st.session_state.selected_product = None

set_defaults()

# =========================
# 2) GLOBAL STYLE
# - Fix header anchor/link icons
# - Improve luxury details
# =========================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Serif+KR:wght@200;400;700&display=swap');

:root{
  --deep:#1B3022;
  --gold:#C5A059;
  --paper:#FBFAF7;
  --muted:rgba(15, 26, 18, 0.62);
  --line:rgba(27, 48, 34, 0.14);
  --shadow: 0 18px 40px rgba(0,0,0,0.08);
  --shadow-soft: 0 12px 24px rgba(0,0,0,0.06);
  --radius: 14px;
}

html, body, [class*="css"]{
  font-family:'Noto Serif KR', serif;
}

.main .block-container{
  max-width: 1100px;
  margin: 0 auto;
  padding-top: 4.5rem;
  padding-bottom: 2.5rem;
}

.stApp{
  background: radial-gradient(1200px 600px at 50% -10%, rgba(197,160,89,0.10), transparent 55%),
              linear-gradient(to bottom, var(--paper), #ffffff);
}

/* ✅ Streamlit 헤더에 붙는 링크(앵커) 아이콘 제거 */
a.anchor-link { display: none !important; }
[data-testid="stHeaderActionElements"] { display: none !important; }
.stMarkdown h1 a, .stMarkdown h2 a, .stMarkdown h3 a,
.stMarkdown h4 a, .stMarkdown h5 a, .stMarkdown h6 a { display:none !important; }

/* Titles */
.section-title{
  text-align:center;
  letter-spacing:0.35rem;
  color: var(--deep);
  font-weight:200;
  margin: 92px 0 10px;
}
.section-subline{
  width: 34px;
  height: 1px;
  background: var(--gold);
  margin: 16px auto 40px;
  opacity: 0.95;
}
.soft-divider{
  width: 100%;
  height: 1px;
  background: linear-gradient(to right, transparent, var(--line), transparent);
  margin: 36px 0;
}

/* Header */
.logo-container{
  position: relative;
  padding: 54px 0 32px;
  margin-bottom: 10px;
  text-align:center;
}
.logo-text{
  font-size: 3.2rem;
  letter-spacing: 0.75rem;
  color: var(--deep);
  font-weight: 200;
  position: relative;
  z-index: 2;
  line-height: 1.2;
}
.logo-tagline{
  margin-top: 16px;
  color: var(--muted);
  letter-spacing: 0.22rem;
  font-weight: 200;
  font-size: 0.95rem;
}
.logo-bg-image{
  position: absolute;
  top: 54%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 250px;
  opacity: 0.10;
  z-index: 1;
  filter: blur(0.2px);
}

/* Hero */
.hero-wrap{ margin-top: 14px; }
.hero-banner{
  height: 450px;
  border-radius: 6px;
  overflow:hidden;
  display:flex;
  align-items:center;
  justify-content:center;
  position: relative;
  box-shadow: var(--shadow);
  border: 1px solid rgba(255,255,255,0.35);
}
.hero-overlay{
  position:absolute;
  inset:0;
  background: linear-gradient(180deg, rgba(0,0,0,0.20), rgba(0,0,0,0.45));
}
.hero-content{
  position: relative;
  z-index:2;
  text-align:center;
  padding: 0 16px;
}
.hero-content h2{
  font-size: 1.0rem;
  color: var(--gold);
  letter-spacing: 0.48rem;
  margin: 0 0 12px 0;
  font-weight: 200;
}
.hero-content h1{
  font-size: 2.9rem;
  font-weight: 200;
  color: #fff;
  margin: 0;
  letter-spacing: 0.02rem;
}
.hero-content p{
  margin: 16px auto 0;
  max-width: 720px;
  color: rgba(255,255,255,0.82);
  font-weight: 200;
  line-height: 1.9;
}

/* Cards */
.card{
  background: rgba(255,255,255,0.72);
  border: 1px solid rgba(27,48,34,0.12);
  border-radius: var(--radius);
  padding: 18px 18px 16px;
  box-shadow: var(--shadow-soft);
  transition: transform .22s ease, box-shadow .22s ease, border-color .22s ease;
}
.card:hover{
  transform: translateY(-3px);
  box-shadow: var(--shadow);
  border-color: rgba(197,160,89,0.30);
}
.card-title{
  margin: 12px 0 6px;
  color: var(--deep);
  font-weight: 200;
  font-size: 1.25rem;
  letter-spacing: 0.05rem;
  text-align:left;
}
.card-desc{
  margin: 0 0 14px;
  color: var(--muted);
  line-height: 1.8;
  text-align:left;
  font-weight: 200;
  font-size: 0.95rem;
}
.badge{
  display:inline-block;
  padding: 6px 10px;
  border-radius: 999px;
  background: rgba(197,160,89,0.12);
  border: 1px solid rgba(197,160,89,0.22);
  color: rgba(27,48,34,0.85);
  font-size: 0.78rem;
  letter-spacing: 0.08rem;
  font-weight: 200;
  margin-bottom: 8px;
}

/* Missing image placeholder */
.img-missing{
  border: 1px dashed rgba(27,48,34,0.25);
  border-radius: 12px;
  padding: 18px;
  background: rgba(255,255,255,0.55);
}
.img-missing-title{
  color: rgba(27,48,34,0.75);
  letter-spacing: 0.18rem;
  font-size: 0.8rem;
  margin-bottom: 6px;
}
.img-missing-path{
  color: rgba(27,48,34,0.45);
  font-size: 0.85rem;
  word-break: break-all;
}

/* Footer */
.footer-outer{
  background-color: var(--deep);
  color: #FFFFFF;
  padding: 96px 0 56px 0;
  margin-top: 140px;
  text-align: center;
  border-top: 2px solid var(--gold);
}
.footer-content{
  max-width: 860px;
  margin: 0 auto;
  padding: 0 18px;
}
.footer-logo{
  font-size: 1.8rem;
  letter-spacing: 0.5rem;
  color: var(--gold);
  margin-bottom: 18px;
  font-weight: 200;
}
.footer-info{
  color: rgba(255,255,255,0.70);
  font-size: 0.95rem;
  line-height: 2;
  margin-bottom: 36px;
  font-weight: 200;
}
.footer-links{
  margin-bottom: 34px;
}
.footer-links a{
  color: #FFFFFF;
  text-decoration: none;
  margin: 0 18px;
  font-size: 0.80rem;
  letter-spacing: 0.12rem;
  transition: 0.25s;
  opacity: 0.92;
}
.footer-links a:hover{
  color: #A4C639;
  opacity: 1;
}
.copyright{
  font-size: 0.78rem;
  color: rgba(255,255,255,0.40);
  margin-top: 44px;
  letter-spacing: 0.05rem;
  font-weight: 200;
}

/* Tabs */
.stTabs [data-baseweb="tab-list"]{
  justify-content: center;
  gap: 8px;
}
.stTabs [data-baseweb="tab"]{
  font-weight: 200;
  letter-spacing: 0.06rem;
}
</style>
""", unsafe_allow_html=True)

# =========================
# 3) AUTO ROTATION CAROUSEL (1000x1000)
# =========================
def auto_carousel(image_paths: List[str], interval_ms: int = 3200, max_size: int = 1000):
    """
    Large square carousel (target 1000x1000). Auto-rotates without user interaction.
    Uses base64 data URLs so it never breaks due to static file serving.
    """
    data_urls = [to_data_url(p) for p in image_paths if to_data_url(p)]
    missing = [p for p in image_paths if not to_data_url(p)]

    if not data_urls:
        st.markdown(
            "<div class='img-missing'><div class='img-missing-title'>SHOWCASE IMAGES NOT FOUND</div>"
            "<div class='img-missing-path'>img1.jpg ~ imgN.jpg 파일을 프로젝트 폴더에 넣어주세요.</div></div>",
            unsafe_allow_html=True
        )
        return

    # Build HTML
    # - responsive container: max-width 1000px
    # - aspect-ratio: 1/1 (square)
    # - fades between slides
    slides_html = "\n".join(
        [f"<img class='mn-slide' src='{u}' />" for u in data_urls]
    )

    html = f"""
    <div class="mn-carousel-wrap">
      <div class="mn-carousel" style="max-width:{max_size}px;">
        {slides_html}
        <div class="mn-glow"></div>
      </div>
    </div>

    <style>
      .mn-carousel-wrap {{
        display:flex;
        justify-content:center;
        align-items:center;
        margin: 0 auto;
        padding: 6px 0 0;
      }}
      .mn-carousel {{
        width: 100%;
        aspect-ratio: 1 / 1;
        position: relative;
        border-radius: 14px;
        overflow: hidden;
        box-shadow: 0 18px 40px rgba(0,0,0,0.10);
        border: 1px solid rgba(27,48,34,0.12);
        background: rgba(255,255,255,0.5);
      }}
      .mn-glow {{
        position:absolute;
        inset:0;
        background: radial-gradient(700px 350px at 50% 20%, rgba(197,160,89,0.12), transparent 55%);
        pointer-events:none;
      }}
      .mn-slide {{
        position:absolute;
        inset:0;
        width:100%;
        height:100%;
        object-fit: cover;
        opacity:0;
        transition: opacity 800ms ease;
        transform: scale(1.01);
      }}
      .mn-slide.active {{
        opacity:1;
      }}
    </style>

    <script>
      const slides = Array.from(document.querySelectorAll(".mn-slide"));
      let idx = 0;

      function show(i) {{
        slides.forEach((s, k) => {{
          if(k === i) s.classList.add("active");
          else s.classList.remove("active");
        }});
      }}

      if(slides.length > 0) {{
        show(0);
        setInterval(() => {{
          idx = (idx + 1) % slides.length;
          show(idx);
        }}, {interval_ms});
      }}
    </script>
    """

    # height 계산: 최대 1000px 정사각형을 유지하되 화면에 맞춰 유연하게
    # components.html은 height를 지정해야 잘림이 덜함.
    components.html(html, height=max_size + 40, scrolling=False)

    if missing:
        # 조용히 안내(에러로 터지지 않게)
        st.caption("일부 쇼케이스 이미지가 없어 제외되었습니다: " + ", ".join(missing))

# =========================
# 4) SECTION 1: HEADER
# =========================
def run_section_1():
    logo_path = "logo.png"
    logo_data_url = to_data_url(logo_path)
    logo_img_html = f'<img src="{logo_data_url}" class="logo-bg-image" alt="logo">' if logo_data_url else ""

    st.markdown(f"""
      <div class="logo-container">
        {logo_img_html}
        <div class="logo-text">MADE IN NATURE</div>
        <div class="section-subline" style="margin:26px auto 0;"></div>
        <div class="logo-tagline">Premium Naturalism & Luxury Design</div>
      </div>
    """, unsafe_allow_html=True)

# =========================
# 5) SECTION 2: HERO & SHOWCASE
# =========================
def run_section_2():
    hero_bg_path = "hero_bg.jpg"
    hero_data_url = to_data_url(hero_bg_path)

    bg_style = (
        f'background-image: url("{hero_data_url}"); background-size: cover; background-position: center;'
        if hero_data_url
        else 'background: linear-gradient(135deg, rgba(27,48,34,0.95), rgba(27,48,34,0.65));'
    )

    st.markdown(f"""
      <div class="hero-wrap">
        <div class="hero-banner" style='{bg_style}'>
          <div class="hero-overlay"></div>
          <div class="hero-content">
            <h2>Nature, defined by luxury</h2>
            <h1>자연의 가치를 증명하다</h1>
            <p>원료의 본질과 감각적인 디자인의 균형. 당신의 일상에 조용한 품격을 더합니다.</p>
          </div>
        </div>
      </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='soft-divider'></div>", unsafe_allow_html=True)

    # ✅ 헤더는 HTML로 렌더 → 앵커 아이콘 문제도 없음
    st.markdown("""
      <h3 style="text-align:center; font-weight:200; color:#1B3022; letter-spacing:0.22rem; margin-top:18px;">
        BRAND SHOWCASE
      </h3>
      <div class="section-subline"></div>
    """, unsafe_allow_html=True)

    # ✅ 1000x1000 큰 이미지 자동 로테이션 캐러셀
    showcase_images = ["img1.jpg", "img2.jpg", "img3.jpg", "img4.jpg", "img5.jpg"]
    auto_carousel(showcase_images, interval_ms=3200, max_size=1000)

# =========================
# 6) SECTION 3: COLLECTIONS
# =========================
def product_card(key: str, badge: str, title: str, desc: str, img_path: str, btn_key: str):
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown(f'<div class="badge">{badge}</div>', unsafe_allow_html=True)
    safe_image(img_path, use_container_width=True)
    st.markdown(f'<div class="card-title">{title}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="card-desc">{desc}</div>', unsafe_allow_html=True)

    if st.button("제품 상세 페이지 이동", key=btn_key, use_container_width=True):
        st.session_state.selected_product = key

    st.markdown("</div>", unsafe_allow_html=True)

def run_section_3():
    # ✅ HTML 타이틀로 렌더 → 앵커 아이콘 없음
    st.markdown("<h2 class='section-title'>COLLECTIONS</h2>", unsafe_allow_html=True)
    st.markdown("<div class='section-subline'></div>", unsafe_allow_html=True)

    tabs = st.tabs(["화장품 & 화장소품", "건강식품", "생활잡화"])

    product_images: Dict[str, str] = {
        "기름종이": "oil_paper.jpg",
        "스타페이스": "patch.jpg",
        "도파민패치": "dopamine.jpg",
        "나이트패치": "night.jpg",
        "수세미": "scrubber.jpg",
        "칫솔": "toothbrush.jpg"
    }

    with tabs[0]:
        c1, c2 = st.columns(2, gap="large")
        with c1:
            product_card(
                key="기름종이",
                badge="COSMETIC ACCESSORY",
                title="프리미엄 기름종이",
                desc="피부 유분을 자극 없이 흡수하는 천연 마 소재.",
                img_path=product_images["기름종이"],
                btn_key="det1",
            )
        with c2:
            product_card(
                key="스타페이스",
                badge="SPOT SOLUTION",
                title="스타페이스 여드름패치",
                desc="트러블을 빠르고 조용하게 진정시키는 스팟 솔루션.",
                img_path=product_images["스타페이스"],
                btn_key="det2",
            )

    with tabs[1]:
        c1, c2 = st.columns(2, gap="large")
        with c1:
            product_card(
                key="도파민패치",
                badge="WELLNESS PATCH",
                title="도파민 패치",
                desc="일상의 활력을 되찾아주는 에너제틱 솔루션.",
                img_path=product_images["도파민패치"],
                btn_key="det3",
            )
        with c2:
            product_card(
                key="나이트패치",
                badge="NIGHT RITUAL",
                title="나이트 패치",
                desc="고요한 휴식을 선사하는 아로마 릴렉싱.",
                img_path=product_images["나이트패치"],
                btn_key="det4",
            )

    with tabs[2]:
        c1, c2 = st.columns(2, gap="large")
        with c1:
            product_card(
                key="수세미",
                badge="HOME CARE",
                title="코코넛 수세미",
                desc="자연에서 온 거친 섬유의 완벽한 세척력.",
                img_path=product_images["수세미"],
                btn_key="det5",
            )
        with c2:
            product_card(
                key="칫솔",
                badge="SUSTAINABLE BATH",
                title="대나무 칫솔",
                desc="지속 가능한 욕실을 위한 친환경 선택.",
                img_path=product_images["칫솔"],
                btn_key="det6",
            )

    if st.session_state.selected_product:
        st.markdown("<div class='soft-divider'></div>", unsafe_allow_html=True)
        st.markdown("""
          <div style="text-align:center; color:#1B3022; font-weight:200; letter-spacing:0.18rem; font-size:1.1rem; margin-bottom:10px;">
            PRODUCT DETAIL
          </div>
          <div class="section-subline" style="margin:14px auto 26px;"></div>
        """, unsafe_allow_html=True)

        p = st.session_state.selected_product
        st.info(f"선택된 제품: **{p}**  ·  (여기에 상세 페이지/외부 링크/멀티페이지 연결을 추가하면 완성됩니다.)")

# =========================
# 7) SECTION 4: FOOTER (✅ 태그 구조 완전 정리)
# =========================
def run_section_4():
    # ✅ 사용자가 보여준 footer HTML이 “그대로 출력되는” 문제를 막기 위해
    # ✅ 여기서는 한 번에 완결된 HTML만 st.markdown(unsafe_allow_html=True)로 렌더
    st.markdown("""
      <div class="footer-outer">
        <div class="footer-content">
          <div class="footer-logo">MADE IN NATURE</div>
          <div class="section-subline" style="margin:0 auto 28px;"></div>

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

          <div style="color: rgba(255,255,255,0.62); font-size: 0.90rem; line-height: 1.9; font-weight:200;">
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

# =========================
# 8) MAIN
# =========================
def main():
    run_section_1()
    run_section_2()
    run_section_3()
    run_section_4()

if __name__ == "__main__":
    main()
