import math  # ✅ 추가: math.ceil() 사용 때문에 필요
import base64
import os
from typing import Optional

import streamlit as st
import streamlit.components.v1 as components

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(page_title="Made in Nature | Official", layout="wide")

# =========================
# OPTIONAL: auto-refresh support (showcase rotation)
# pip install streamlit-autorefresh
# =========================
try:
    from streamlit_autorefresh import st_autorefresh  # type: ignore
    HAS_AUTOREFRESH = True
except Exception:
    HAS_AUTOREFRESH = False


# =========================
# UTIL
# =========================
def file_exists(path: Optional[str]) -> bool:
    """Path가 문자열이고 실제 파일이면 True."""
    return bool(path) and isinstance(path, str) and os.path.isfile(path)

def image_or_placeholder(path: str, *, height: int = 420, radius: int = 14):
    """Show image if exists; otherwise show a clean placeholder (no warning blocks)."""
    if file_exists(path):
        st.image(path, use_container_width=True)
    else:
        st.markdown(
            f"""
            <div style="
                width:100%;
                height:{height}px;
                border-radius:{radius}px;
                border:1px solid rgba(27,48,34,0.12);
                background: rgba(255,255,255,0.70);
                display:flex;
                align-items:center;
                justify-content:center;
                box-shadow: 0 12px 24px rgba(0,0,0,0.05);
            ">
              <div style="
                    color: rgba(15,26,18,0.55);
                    font-weight:200;
                    letter-spacing:0.06rem;
                    line-height:1.6;
                    text-align:center;
                    padding:18px;
              ">
                IMAGE PLACEHOLDER<br>
                <span style="font-size:0.9rem; opacity:0.75;">{path}</span>
              </div>
            </div>
            """,
            unsafe_allow_html=True
        )

def square_placeholder(path: str, *, size: int = 500, radius: int = 14):
    st.markdown(
        f"""
        <div style="
            width:{size}px;
            height:{size}px;
            border-radius:{radius}px;
            border:1px solid rgba(27,48,34,0.12);
            background: rgba(255,255,255,0.70);
            display:flex;
            align-items:center;
            justify-content:center;
            box-shadow: 0 12px 24px rgba(0,0,0,0.05);
            margin: 0 auto;
        ">
          <div style="
                color: rgba(15,26,18,0.55);
                font-weight:200;
                letter-spacing:0.06rem;
                line-height:1.6;
                text-align:center;
                padding:18px;
          ">
            IMAGE PLACEHOLDER<br>
            <span style="font-size:0.9rem; opacity:0.75;">{path}</span>
          </div>
        </div>
        """,
        unsafe_allow_html=True
    )

def section_title(text: str):
    """Centered title without Streamlit heading anchors."""
    st.markdown(
        """
        <style>
        .mn-title{
          text-align:center;
          letter-spacing:0.32rem;
          color:#1B3022;
          font-weight:200;
          margin: 72px 0 10px;
          font-size: 1.35rem;
        }
        .mn-subline{
          width:34px;
          height:1px;
          background:#C5A059;
          margin: 16px auto 34px;
          opacity:0.95;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.markdown(f"<div class='mn-title'>{text}</div>", unsafe_allow_html=True)
    st.markdown("<div class='mn-subline'></div>", unsafe_allow_html=True)

# ---- (Collections) HTML-only image to prevent the “white box above image” ----
@st.cache_data(show_spinner=False)
def _to_data_uri(path: str) -> Optional[str]:
    if not file_exists(path):
        return None
    ext = os.path.splitext(path)[1].lower().replace(".", "")
    mime = {"png": "image/png", "jpg": "image/jpeg", "jpeg": "image/jpeg", "webp": "image/webp"}.get(ext, "image/png")
    try:
        with open(path, "rb") as f:
            b64 = base64.b64encode(f.read()).decode("utf-8")
        return f"data:{mime};base64,{b64}"
    except Exception:
        return None

def html_square_image_or_placeholder(path: str, *, size_px: int, radius: int = 14) -> str:
    """
    Collections 이미지용: HTML 한 덩어리로만 렌더링(흰색 박스/태그 노출 방지)
    size_px=1000 요청 반영
    """
    uri = _to_data_uri(path)
    if uri:
        return f"""
        <div style="width:100%; display:flex; justify-content:center;">
          <div style="width:100%; max-width:{size_px}px;">
            <div style="
              width:100%;
              aspect-ratio: 1 / 1;
              border-radius:{radius}px;
              overflow:hidden;
              border:1px solid rgba(27,48,34,0.12);
              box-shadow: 0 12px 24px rgba(0,0,0,0.05);
              background: rgba(255,255,255,0.55);
            ">
              <img src="{uri}" style="
                width:100%;
                height:100%;
                object-fit:cover;
                display:block;
              "/>
            </div>
          </div>
        </div>
        """
    return f"""
    <div style="width:100%; display:flex; justify-content:center;">
      <div style="
          width:100%;
          max-width:{size_px}px;
          aspect-ratio: 1 / 1;
          border-radius:{radius}px;
          border:1px solid rgba(27,48,34,0.12);
          background: rgba(255,255,255,0.70);
          display:flex;
          align-items:center;
          justify-content:center;
          box-shadow: 0 12px 24px rgba(0,0,0,0.05);
      ">
        <div style="
              color: rgba(15,26,18,0.55);
              font-weight:200;
              letter-spacing:0.06rem;
              line-height:1.6;
              text-align:center;
              padding:18px;
        ">
          IMAGE PLACEHOLDER<br>
          <span style="font-size:0.9rem; opacity:0.75;">{path}</span>
        </div>
      </div>
    </div>
    """


# =========================
# GLOBAL STYLE
# =========================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Serif+KR:wght@200;400;700&display=swap');

:root{
  --deep:#1B3022;
  --gold:#C5A059;
  --paper:#FBFAF7;
  --muted:rgba(15, 26, 18, 0.62);
  --shadow-soft: 0 12px 24px rgba(0,0,0,0.06);
  --shadow: 0 18px 40px rgba(0,0,0,0.08);
  --radius: 14px;
}

html, body, [class*="css"]{
  font-family:'Noto Serif KR', serif;
}

.main .block-container{
  max-width: 1100px;
  margin: 0 auto;
  padding-top: 4.2rem;
  padding-bottom: 2.5rem;
}

.stApp{
  background: radial-gradient(1200px 600px at 50% -10%, rgba(197,160,89,0.10), transparent 55%),
              linear-gradient(to bottom, var(--paper), #ffffff);
}

/* Header */
.mn-logo-wrap{ text-align:center; padding: 44px 0 22px; }
.mn-logo-text{
  font-size: 3.0rem; letter-spacing: 0.75rem; color: var(--deep); font-weight: 200;
}
.mn-line{ width:34px; height:1px; background: var(--gold); margin: 22px auto 0; }
.mn-logo-tag{
  margin-top: 12px; color: rgba(15,26,18,0.58); letter-spacing: 0.22rem; font-weight: 200; font-size: 0.95rem;
}

/* logo slot */
.mn-logo-slot{
  width: 74px;
  height: 74px;
  margin: 0 auto 14px;
  border-radius: 999px;
  border: 1px solid rgba(27,48,34,0.10);
  background: rgba(255,255,255,0.55);
  display:flex;
  align-items:center;
  justify-content:center;
  box-shadow: 0 12px 24px rgba(0,0,0,0.04);
}
.mn-logo-img{
  width: 58px;
  height: 58px;
  object-fit: contain;
  display:block;
  opacity: 0.98;
}

/* Hero */
.mn-hero{
  height: 450px;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: var(--shadow);
  border: 1px solid rgba(255,255,255,0.35);
  position: relative;
}
.mn-hero-overlay{
  position:absolute; inset:0;
  background: linear-gradient(180deg, rgba(0,0,0,0.20), rgba(0,0,0,0.45));
}
.mn-hero-content{
  position:absolute; inset:0;
  display:flex; align-items:center; justify-content:center;
  flex-direction:column; text-align:center; padding: 0 16px;
}
.mn-hero-h2{ font-size: 1.0rem; color: var(--gold); letter-spacing: 0.48rem; margin:0 0 12px 0; font-weight:200; }
.mn-hero-h1{ font-size: 2.8rem; font-weight: 200; color: #fff; margin: 0; }
.mn-hero-p{
  margin: 16px auto 0; max-width: 720px;
  color: rgba(255,255,255,0.82); font-weight: 200; line-height: 1.9;
}

/* Product card */
.mn-card{
  background: rgba(255,255,255,0.75);
  border: 1px solid rgba(27,48,34,0.12);
  border-radius: var(--radius);
  padding: 18px;
  box-shadow: var(--shadow-soft);
}
.mn-card-title{
  margin: 14px 0 6px;
  color: var(--deep);
  font-weight: 200;
  font-size: 1.28rem;
  letter-spacing: 0.05rem;
}
.mn-card-desc{
  margin: 0 0 14px;
  color: rgba(15,26,18,0.62);
  line-height: 1.85;
  font-weight: 200;
  font-size: 0.95rem;
}

/* Back button styling */
.back-btn button{
  border-radius: 999px !important;
  font-weight: 200 !important;
  border: 1px solid rgba(27,48,34,0.20) !important;
}

/* Detail page fade-in */
.mn-fadein{
  animation: mnFadeIn 520ms ease-out both;
}
@keyframes mnFadeIn{
  from{ opacity:0; transform: translateY(10px); }
  to{ opacity:1; transform: translateY(0); }
}

/* Footer */
.mn-footer{
  margin-top: 120px;
  padding: 34px 0 10px;
  border-top: 1px solid rgba(27,48,34,0.18);
  text-align:center;
}
.mn-footer-brand{ letter-spacing: 0.45rem; color: #1B3022; font-weight: 200; font-size: 1.1rem; }
.mn-footer-muted{ color: rgba(15, 26, 18, 0.55); font-weight: 200; line-height: 1.9; }

/* Tabs center */
.stTabs [data-baseweb="tab-list"]{ justify-content: center; }
</style>
""", unsafe_allow_html=True)


# =========================
# DATA (Products)
# =========================
PRODUCTS = {
    "기름종이": {
        "category": "화장품 & 화장소품",
        "title": "프리미엄 기름종이",
        "desc": "피부 유분을 자극 없이 흡수하는 천연 마 소재.",
        "list_image": "oil_paper.png",
        "detail_image": "oil_paper_detail1.png",
        "detail_image": "oil_paper_detail2.png",
        "detail_image": "oil_paper_detail3.png"
    },
    "스타페이스": {
        "category": "화장품 & 화장소품",
        "title": "스타페이스 여드름패치",
        "desc": "트러블을 빠르고 조용하게 진정시키는 스팟 솔루션.",
        "list_image": "patch.png",
        "detail_image": "patch_detail1.png",
        "detail_image": "patch_detail2.png",
        "detail_image": "patch_detail3.png"
    },
    "도파민패치": {
        "category": "건강식품",
        "title": "도파민 패치",
        "desc": "일상의 활력을 되찾아주는 에너제틱 솔루션.",
        "list_image": "dopamine.png",
        "detail_image": "dopamine_detail1.png",
        "detail_image": "dopamine_detail2.png",
        "detail_image": "dopamine_detail3.png",
        "detail_image": "dopamine_detail4.png",
        "detail_image": "dopamine_detail5.png"
    },
    "나이트패치": {
        "category": "건강식품",
        "title": "나이트 패치",
        "desc": "고요한 휴식을 선사하는 아로마 릴렉싱.",
        "list_image": "night.png",
        "detail_image": "night_detail1.png",
        "detail_image": "night_detail2.png",
        "detail_image": "night_detail3.png",
        "detail_image": "night_detail4.png"
    },

    "비즈왁스랩": {
        "category": "생활잡화",
        "title": "비즈왁스 랩",
        "desc": "일회용 랩 대신, 자연을 감싸는 재사용 가능한 보관 솔루션.",
        "list_image": "beeswax_wrap.png",
        "detail_image": [
            "beeswax_wrap_detail1.png",
            "beeswax_wrap_detail2.png",
            "beeswax_wrap_detail3.png",
            "beeswax_wrap_detail4.png",
            "beeswax_wrap_detail5.png",
            "beeswax_wrap_detail6.png",
            "beeswax_wrap_detail7.png",
            "beeswax_wrap_detail8.png",
            "beeswax_wrap_detail9.png",
            "beeswax_wrap_detail10.png",
            "beeswax_wrap_detail11.png"
        ],
    },

    "칫솔": {
        "category": "생활잡화",
        "title": "대나무 칫솔",
        "desc": "지속 가능한 욕실을 위한 친환경 선택.",
        "list_image": "toothbrush.png",
        "detail_image": [
            "toothbrush_detail1.png",
            "toothbrush_detail2.png",
            "toothbrush_detail3.png",
            "toothbrush_detail4.png",
            "toothbrush_detail5.png",
        ],
    },
}


# =========================
# STATE (Simple routing)
# =========================
if "page" not in st.session_state:
    st.session_state.page = "home"   # "home" or "detail"
if "selected_product_key" not in st.session_state:
    st.session_state.selected_product_key = None
if "showcase_page" not in st.session_state:
    st.session_state.showcase_page = 0
if "animate_detail" not in st.session_state:
    st.session_state.animate_detail = False


# =========================
# UI: HEADER
# =========================
logo_path = "logo.png"
logo_uri = _to_data_uri(logo_path) if file_exists(logo_path) else None

if logo_uri:
    logo_block = f"<div class='mn-logo-slot'><img class='mn-logo-img' src='{logo_uri}' alt='logo'/></div>"
else:
    logo_block = "<div class='mn-logo-slot'></div>"

st.markdown(f"""
<div class="mn-logo-wrap">
  {logo_block}
  <div class="mn-logo-text">MADE IN NATURE</div>
  <div class="mn-line"></div>
  <div class="mn-logo-tag">Nature on Genesis</div>
</div>
""", unsafe_allow_html=True)


# =========================
# UI: HERO
# =========================
hero_bg = "hero_bg.jpg"
if file_exists(hero_bg):
    st.image(hero_bg, use_container_width=True)
    st.markdown(
        "<div style='text-align:center; margin-top:-360px; position:relative; z-index:2;'>"
        "<div class='mn-hero-h2'>Nature on Genesis</div>"
        "<div class='mn-hero-h1'>비워서 채운 자연</div>"
        "<div class='mn-hero-p'>당신의 일상에 조용한 품격을 더합니다.</div>"
        "</div>",
        unsafe_allow_html=True
    )
    st.markdown("<div style='height:260px;'></div>", unsafe_allow_html=True)
else:
    st.markdown("""
    <div class="mn-hero" style="background: linear-gradient(135deg, rgba(27,48,34,0.95), rgba(27,48,34,0.65));">
      <div class="mn-hero-overlay"></div>
      <div class="mn-hero-content">
        <div class="mn-hero-h2">Nature on Genesis</div>
        <div class="mn-hero-h1">자연의 가치를 증명하다</div>
        <div class="mn-hero-p">당신의 일상에 조용한 품격을 더합니다.</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

st.divider()


# =========================
# PAGE: DETAIL
# =========================
def render_detail_page(product_key: str):
    p = PRODUCTS.get(product_key)
    if not p:
        st.session_state.page = "home"
        st.session_state.selected_product_key = None
        st.rerun()

    components.html("<script>window.scrollTo(0,0);</script>", height=0)
    if st.session_state.animate_detail:
        st.markdown("<div class='mn-fadein'>", unsafe_allow_html=True)
        st.session_state.animate_detail = False
    else:
        st.markdown("<div>", unsafe_allow_html=True)

    section_title("PRODUCT DETAIL")

    st.markdown(
        f"""
        <div style="text-align:center; margin-top: 8px;">
          <div style="color:#1B3022; font-weight:200; font-size:2.0rem; letter-spacing:0.06rem;">
            {p["title"]}
          </div>
          <div style="color: rgba(15,26,18,0.62); font-weight:200; margin-top:10px; line-height:1.9;">
            {p["desc"]}
          </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<div style='height:26px;'></div>", unsafe_allow_html=True)

    detail = p.get("detail_image")
    if isinstance(detail, (list, tuple)):
        for i, img_path in enumerate(detail):
            image_or_placeholder(img_path, height=740, radius=14)
            if i != len(detail) - 1:
                st.markdown("<div style='height:18px;'></div>", unsafe_allow_html=True)
    else:
        image_or_placeholder(str(detail), height=740, radius=14)

    st.markdown("<div style='height:22px;'></div>", unsafe_allow_html=True)
    col_l, col_c, col_r = st.columns([1, 2, 1])
    with col_c:
        st.markdown('<div class="back-btn">', unsafe_allow_html=True)
        if st.button("← 컬렉션으로 돌아가기", use_container_width=True, key="back_bottom"):
            st.session_state.page = "home"
            st.session_state.selected_product_key = None
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)


# =========================
# PAGE: HOME (Showcase + Collections)
# =========================
def render_home_page():
    section_title("BRAND SHOWCASE")

    showcase_images = ["img1.png", "img2.png", "img3.png", "img4.png", "img5.png", "img6.png", "img7.png", "img8.png"]
    src = showcase_images

    per_page = 2
    total_pages = max(1, math.ceil(len(src) / per_page))
    st.session_state.showcase_page = st.session_state.showcase_page % total_pages

    spacer_l, nav_c, spacer_r = st.columns([3, 2, 3])
    with nav_c:
        b1, b2, b3 = st.columns([1, 2, 1])
        with b1:
            if st.button("◀", key="showcase_prev", use_container_width=True):
                st.session_state.showcase_page = (st.session_state.showcase_page - 1) % total_pages
                st.rerun()
        with b2:
            st.markdown(
                f"<div style='text-align:center; color:rgba(15,26,18,0.55); font-weight:200; letter-spacing:0.10rem;'>"
                f"{st.session_state.showcase_page + 1} / {total_pages}"
                f"</div>",
                unsafe_allow_html=True
            )
        with b3:
            if st.button("▶", key="showcase_next", use_container_width=True):
                st.session_state.showcase_page = (st.session_state.showcase_page + 1) % total_pages
                st.rerun()

    start = st.session_state.showcase_page * per_page
    page_imgs = src[start:start + per_page]

    if len(page_imgs) == 1:
        l, c, r = st.columns([1, 2, 1])
        with c:
            if file_exists(page_imgs[0]):
                st.image(page_imgs[0], width=500)
            else:
                square_placeholder(page_imgs[0], size=500, radius=14)
    else:
        l, c1, c2, r = st.columns([1, 2, 2, 1])
        with c1:
            if file_exists(page_imgs[0]):
                st.image(page_imgs[0], width=500)
            else:
                square_placeholder(page_imgs[0], size=500, radius=14)
        with c2:
            if file_exists(page_imgs[1]):
                st.image(page_imgs[1], width=500)
            else:
                square_placeholder(page_imgs[1], size=500, radius=14)

    section_title("COLLECTIONS")

    tabs = st.tabs(["화장품 & 화장소품", "건강식품", "생활잡화"])

    def product_card(product_key: str):
        p = PRODUCTS[product_key]

        st.markdown("<div class='mn-card'>", unsafe_allow_html=True)
        st.markdown(html_square_image_or_placeholder(p["list_image"], size_px=1000, radius=14), unsafe_allow_html=True)
        st.markdown(f"<div class='mn-card-title'>{p['title']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='mn-card-desc'>{p['desc']}</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        if st.button("제품 상세 보기", key=f"view_{product_key}", use_container_width=True):
            st.session_state.page = "detail"
            st.session_state.selected_product_key = product_key
            st.session_state.animate_detail = True
            st.rerun()

    with tabs[0]:
        keys = [k for k, v in PRODUCTS.items() if v["category"] == "화장품 & 화장소품"]
        c1, c2 = st.columns(2, gap="large")
        if len(keys) > 0:
            with c1: product_card(keys[0])
        if len(keys) > 1:
            with c2: product_card(keys[1])

    with tabs[1]:
        keys = [k for k, v in PRODUCTS.items() if v["category"] == "건강식품"]
        c1, c2 = st.columns(2, gap="large")
        if len(keys) > 0:
            with c1: product_card(keys[0])
        if len(keys) > 1:
            with c2: product_card(keys[1])

    with tabs[2]:
        keys = [k for k, v in PRODUCTS.items() if v["category"] == "생활잡화"]
        c1, c2 = st.columns(2, gap="large")
        if len(keys) > 0:
            with c1: product_card(keys[0])
        if len(keys) > 1:
            with c2: product_card(keys[1])


# =========================
# ROUTER
# =========================
if st.session_state.page == "detail" and st.session_state.selected_product_key:
    render_detail_page(st.session_state.selected_product_key)
else:
    render_home_page()












