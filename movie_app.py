import streamlit as st
import os
import base64
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
    """로컬 이미지를 HTML/CSS 임베딩을 위해 base64 데이터 URL로 변환"""
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
  padding-bottom: 0px; /* 푸터 밀착을 위해 조정 */
}

.stApp{
  background: radial-gradient(1200px 600px at 50% -10%, rgba(197,160,89,0.10), transparent 55%),
              linear-gradient(to bottom, var(--paper), #ffffff);
}

a.anchor-link { display: none !important; }
[data-testid="stHeaderActionElements"] { display: none !important; }
.stMarkdown h1 a, .stMarkdown h2 a, .stMarkdown h3 a,
.stMarkdown h4 a, .stMarkdown h5 a, .stMarkdown h6 a { display:none !important; }

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

/* Header & Logo */
.logo-container{ position: relative; padding: 54px 0 32px; text-align:center; }
.logo-text{ font-size: 3.2rem; letter-spacing: 0.75rem; color: var(--deep); font-weight: 200; line-height: 1.2; }
.logo-tagline{ margin-top: 16px; color: var(--muted); letter-spacing: 0.22rem; font-weight: 200; font-size: 0.95rem; }

/* Hero */
.hero-wrap{ margin-top: 14px; }
.hero-banner{
  height: 450px; border-radius: 6px; overflow:hidden; display:flex;
  align-items:center; justify-content:center; position: relative;
  box-shadow: var(--shadow); border: 1px solid rgba(255,255,255,0.35);
}
.hero-overlay{ position:absolute; inset:0; background: linear-gradient(180deg, rgba(0,0,0,0.20), rgba(0,0,0,0.45)); }
.hero-content{ position: relative; z-index:2; text-align:center; padding: 0 16px; }
.hero-content h2{ font-size: 1.0rem; color: var(--gold); letter-spacing: 0.48rem; margin: 0 0 12px 0; font-weight: 200; }
.hero-content h1{ font-size: 2.9rem; font-weight: 200; color: #fff; margin: 0; letter-spacing: 0.02rem; }
.hero-content p{ margin: 16px auto 0; max-width: 720px; color: rgba(255,255,255,0.82); font-weight: 200; line-height: 1.9; }

/* Product Cards */
.card{ background: rgba(255,255,255,0.72); border: 1px solid rgba(27,48,34,0.12); border-radius: var(--radius); padding: 18px 18px 16px; box-shadow: var(--shadow-soft); transition: all .22s ease; }
.card:hover{ transform: translateY(-3px); box-shadow: var(--shadow); border-color: rgba(197,160,89,0.30); }
.card-title{ margin: 12px 0 6px; color: var(--deep); font-weight: 200; font-size: 1.25rem; letter-spacing: 0.05rem; }
.card-desc{ margin: 0 0 14px; color: var(--muted); line-height: 1.8; font-weight: 200; font-size: 0.95rem; }
.badge{ display:inline-block; padding: 6px 10px; border-radius: 999px; background: rgba(197,160,89,0.12); border: 1px solid rgba(197,160,89,0.22); color: rgba(27,48,34,0.85); font-size: 0.78rem; letter-spacing: 0.08rem; font-weight: 200; margin-bottom: 8px; }

.img-missing{ border: 1px dashed rgba(27,48,34,0.25); border-radius: 12px; padding: 18px; background: rgba(255,255,255,0.55); }
</style>
""", unsafe_allow_html=True)

# =========================
# 3) CAROUSEL COMPONENT
# =========================
def auto_carousel(image_paths: List[str], interval_ms: int = 3200, max_size: int = 1000):
    data_urls = [u for p in image_paths if (u := to_data_url(p))]
    if not data_urls:
        st.markdown("<div class='img-missing'>SHOWCASE IMAGES NOT FOUND</div>", unsafe_allow_html=True)
        return

    slides_html = "\n".join([f"<img class='mn-slide' src='{u}' />" for u in data_urls])
    html = f"""
    <div class="mn-carousel" style="max-width:{max_size}px; aspect-ratio:1/1; position:relative; margin:0 auto; border-radius:14px; overflow:hidden; box-shadow:0 18px 40px rgba(0,0,0,0.1);">
        {slides_html}
        <div style="position:absolute; inset:0; background:radial-gradient(circle at 50% 20%, rgba(197,160,89,0.1), transparent 60%); pointer-events:none;"></div>
    </div>
    <style>
        .mn-slide {{ position:absolute; inset:0; width:100%; height:100%; object-fit:cover; opacity:0; transition:opacity 800ms; }}
        .mn-slide.active {{ opacity:1; }}
    </style>
    <script>
        const slides = document.querySelectorAll(".mn-slide");
        let idx = 0;
        function show(i) {{ slides.forEach((s, k) => s.classList.toggle("active", k === i)); }}
        if(slides.length > 0) {{
            show(0);
            setInterval(() => {{ idx = (idx + 1) % slides.length; show(idx); }}, {interval_ms});
        }}
    </script>
    """
    components.html(html, height=max_size + 20)

# =========================
# 4) RUN SECTIONS
# =========================
def run_section_1():
    st.markdown("""
      <div class="logo-container">
        <div class="logo-text">MADE IN NATURE</div>
        <div class="section-subline" style="margin:26px auto 0;"></div>
        <div class="logo-tagline">Premium Naturalism & Luxury Design</div>
      </div>
    """, unsafe_allow_html=True)

def run_section_2():
    hero_url = to_data_url("hero_bg.jpg")
    bg_style = f'background-image: url("{hero_url}"); background-size: cover;' if hero_url else 'background: #1B3022;'
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
    st.markdown("<h3 style='text-align:center; font-weight:200; color:#1B3022; letter-spacing:0.22rem;'>BRAND SHOWCASE</h3><div class='section-subline'></div>", unsafe_allow_html=True)
    auto_carousel(["img1.jpg", "img2.jpg", "img3.jpg", "img4.jpg", "img5.jpg"], max_size=800)

def product_card(key: str, badge: str, title: str, desc: str, img_path: str, btn_key: str):
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown(f'<div class="badge">{badge}</div>', unsafe_allow_html=True)
    safe_image(img_path)
    st.markdown(f'<div class="card-title">{title}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="card-desc">{desc}</div>', unsafe_allow_html=True)
    if st.button("제품 상세 페이지 이동", key=btn_key, use_container_width=True):
        st.session_state.selected_product = key
    st.markdown("</div>", unsafe_allow_html=True)

def run_section_3():
    st.markdown("<h2 class='section-title'>COLLECTIONS</h2><div class='section-subline'></div>", unsafe_allow_html=True)
    tabs = st.tabs(["화장품 & 화장소품", "건강식품", "생활잡화"])
    with tabs[0]:
        c1, c2 = st.columns(2, gap="large")
        with c1: product_card("기름종이", "COSMETIC ACCESSORY", "프리미엄 기름종이", "천연 마 소재.", "oil_paper.jpg", "det1")
        with c2: product_card("스타페이스", "SPOT SOLUTION", "스타페이스 여드름패치", "진정 스팟 솔루션.", "patch.jpg", "det2")
    # ... (생략된 탭들도 동일한 로직으로 구성 가능)

# =========================
# 5) FOOTER (에러 해결 핵심 부분)
# =========================
def run_section_4():
    """st.markdown 대신 iframe(components.html)을 사용하여 코드 노출 에러를 방지합니다."""
    footer_html = """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Noto+Serif+KR:wght@200;400&display=swap');
        .footer-outer {
            background-color: #1B3022; color: white; padding: 80px 20px; text-align: center;
            font-family: 'Noto Serif KR', serif; margin: 0;
        }
        .footer-logo { font-size: 1.8rem; letter-spacing: 0.5rem; color: #C5A059; margin-bottom: 20px; font-weight: 200; }
        .footer-info { color: rgba(255,255,255,0.7); font-size: 0.95rem; line-height: 2; margin-bottom: 40px; font-weight: 200; }
        .footer-links a { color: white; text-decoration: none; margin: 0 15px; font-size: 0.85rem; opacity: 0.8; }
        .copyright { font-size: 0.8rem; color: rgba(255,255,255,0.4); margin-top: 50px; font-weight: 200; }
    </style>
    <div class="footer-outer">
        <div class="footer-logo">MADE IN NATURE</div>
        <div style="width: 30px; height: 1px; background: #C5A059; margin: 0 auto 30px;"></div>
        <p class="footer-info">
            자연의 본질을 연구하고 지속 가능한 가치를 디자인합니다.<br>
            최상의 원료와 장인 정신을 고집합니다.
        </p>
        <div class="footer-links">
            <a href="#">BRAND STORY</a> <a href="#">COLLECTIONS</a> <a href="#">CONTACT</a>
        </div>
        <div style="color: rgba(255,255,255,0.5); font-size: 0.85rem; margin-top: 40px; font-weight: 200;">
            주식회사 메이드인네이처 | 서울특별시 성동구 성수동 자연길 123<br>
            Customer Care. 02-1234-5678 | Instagram. @madeinnature_official
        </div>
        <div class="copyright">© 2026 MADE IN NATURE. ALL RIGHTS RESERVED.</div>
    </div>
    """
    st.write("---") # 구분선
    components.html(footer_html, height=550)

# =========================
# 6) MAIN
# =========================
def main():
    run_section_1()
    run_section_2()
    run_section_3()
    run_section_4()

if __name__ == "__main__":
    main()

