import os
import streamlit as st

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(page_title="Made in Nature | Official", layout="wide")

# =========================
# UTIL
# =========================
def file_exists(path):
    return os.path.isfile(path)

def image_or_placeholder(path, height=420):
    if file_exists(path):
        st.image(path, use_container_width=True)
    else:
        st.markdown(
            f"""
            <div style="
                height:{height}px;
                border-radius:14px;
                border:1px solid rgba(0,0,0,0.15);
                display:flex;
                align-items:center;
                justify-content:center;
                color:#777;">
                {path}
            </div>
            """,
            unsafe_allow_html=True
        )

def section_title(text):
    st.markdown(
        f"""
        <div style="text-align:center; margin:70px 0 10px;
                    letter-spacing:0.3rem; font-weight:200; color:#1B3022;">
            {text}
        </div>
        <div style="width:34px;height:1px;background:#C5A059;margin:0 auto 36px;"></div>
        """,
        unsafe_allow_html=True
    )

# =========================
# STYLE
# =========================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Serif+KR:wght@200;400;700&display=swap');

html, body, [class*="css"] {
  font-family: 'Noto Serif KR', serif;
}

.main .block-container {
  max-width: 1100px;
  margin: 0 auto;
  padding-top: 3rem;
}

.mn-card {
  background:#fff;
  border-radius:14px;
  padding:18px;
  box-shadow:0 10px 25px rgba(0,0,0,0.06);
}

.showcase-wrap {
  max-width:900px;
  margin:0 auto;
  animation: fadein 0.5s ease;
}

@keyframes fadein {
  from {opacity:0;}
  to {opacity:1;}
}

.showcase-nav {
  display:flex;
  justify-content:flex-end;
  gap:0;
  margin-bottom:8px;
}

.showcase-nav button {
  width:38px;
  height:38px;
  border-radius:50%;
  border:1px solid rgba(0,0,0,0.25);
  background:white;
  font-size:20px;
}

@media (max-width: 768px) {
  .showcase-wrap img {
    aspect-ratio: 4 / 5;
    object-fit: cover;
  }
}
</style>
""", unsafe_allow_html=True)

# =========================
# DATA
# =========================
SHOWCASE_IMAGES = [
    "img1.png", "img2.png", "img3.png", "img4.png", "img5.png"
]

PRODUCTS = {
    "기름종이": {
        "category": "화장품 & 화장소품",
        "title": "프리미엄 기름종이",
        "desc": "피부 유분을 자극 없이 흡수하는 천연 마 소재.",
        "list": "oil_paper.png",
        "detail": "oil_paper_detail.png",
    },
    "스타페이스": {
        "category": "화장품 & 화장소품",
        "title": "스타페이스 여드름패치",
        "desc": "트러블을 빠르고 조용하게 진정시키는 스팟 솔루션.",
        "list": "patch.png",
        "detail": "patch_detail.png",
    },
    "도파민패치": {
        "category": "건강식품",
        "title": "도파민 패치",
        "desc": "일상의 활력을 되찾아주는 에너제틱 솔루션.",
        "list": "dopamine.png",
        "detail": "dopamine_detail.png",
    }
}

# =========================
# STATE
# =========================
if "page" not in st.session_state:
    st.session_state.page = "home"
if "product" not in st.session_state:
    st.session_state.product = None
if "showcase_idx" not in st.session_state:
    st.session_state.showcase_idx = 0

# =========================
# HEADER
# =========================
st.markdown("""
<div style="text-align:center">
  <h1 style="letter-spacing:0.7rem;font-weight:200;">MADE IN NATURE</h1>
  <p style="color:#777;">Premium Naturalism & Luxury Design</p>
</div>
""", unsafe_allow_html=True)

# =========================
# DETAIL PAGE
# =========================
def render_detail():
    p = PRODUCTS[st.session_state.product]

    if st.button("← 컬렉션으로 돌아가기"):
        st.session_state.page = "home"
        st.session_state.product = None
        st.rerun()

    section_title("PRODUCT DETAIL")
    st.markdown(f"<h2 style='text-align:center'>{p['title']}</h2>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align:center;color:#666'>{p['desc']}</p>", unsafe_allow_html=True)
    image_or_placeholder(p["detail"], 600)

# =========================
# HOME
# =========================
def render_home():
    # SHOWCASE
    section_title("BRAND SHOWCASE")

    nav_l, nav_r = st.columns([8,1])
    with nav_r:
        st.markdown('<div class="showcase-nav">', unsafe_allow_html=True)
        if st.button("‹"):
            st.session_state.showcase_idx = (st.session_state.showcase_idx - 1) % len(SHOWCASE_IMAGES)
        if st.button("›"):
            st.session_state.showcase_idx = (st.session_state.showcase_idx + 1) % len(SHOWCASE_IMAGES)
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div class="showcase-wrap">', unsafe_allow_html=True)
    image_or_placeholder(SHOWCASE_IMAGES[st.session_state.showcase_idx], 520)
    st.markdown("</div>", unsafe_allow_html=True)

    # COLLECTIONS
    section_title("COLLECTIONS")
    tabs = st.tabs(["화장품 & 화장소품", "건강식품"])

    with tabs[0]:
        for k, v in PRODUCTS.items():
            if v["category"] == "화장품 & 화장소품":
                st.markdown("<div class='mn-card'>", unsafe_allow_html=True)
                image_or_placeholder(v["list"], 300)
                st.markdown(f"<h4>{v['title']}</h4>", unsafe_allow_html=True)
                st.markdown(f"<p>{v['desc']}</p>", unsafe_allow_html=True)
                if st.button("제품 상세 보기", key=k):
                    st.session_state.page = "detail"
                    st.session_state.product = k
                    st.rerun()
                st.markdown("</div>", unsafe_allow_html=True)

    with tabs[1]:
        for k, v in PRODUCTS.items():
            if v["category"] == "건강식품":
                st.markdown("<div class='mn-card'>", unsafe_allow_html=True)
                image_or_placeholder(v["list"], 300)
                st.markdown(f"<h4>{v['title']}</h4>", unsafe_allow_html=True)
                st.markdown(f"<p>{v['desc']}</p>", unsafe_allow_html=True)
                if st.button("제품 상세 보기", key=k+"2"):
                    st.session_state.page = "detail"
                    st.session_state.product = k
                    st.rerun()
                st.markdown("</div>", unsafe_allow_html=True)

# =========================
# ROUTER
# =========================
if st.session_state.page == "detail":
    render_detail()
else:
    render_home()





