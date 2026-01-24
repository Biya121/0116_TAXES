import os
import time
import streamlit as st

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(page_title="Made in Nature | Official", layout="wide")

# =========================
# UTIL
# =========================
def file_exists(path: str) -> bool:
    return bool(path) and os.path.isfile(path)

def image_or_placeholder(path: str, *, height: int = 420, radius: int = 14):
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
            ">
              <div style="color:#666;">{path}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

def section_title(text):
    st.markdown(
        f"""
        <div style="text-align:center;margin:70px 0 14px;
                    letter-spacing:0.3rem;font-weight:200;color:#1B3022;">
            {text}
        </div>
        <div style="width:32px;height:1px;background:#C5A059;margin:0 auto 36px;"></div>
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

.mn-logo {
  text-align:center;
  margin-bottom:30px;
}
.mn-logo h1 {
  font-weight:200;
  letter-spacing:0.7rem;
}
.mn-logo p {
  color:#777;
  letter-spacing:0.2rem;
}

.mn-card {
  background:#fff;
  border-radius:14px;
  padding:18px;
  box-shadow:0 10px 25px rgba(0,0,0,0.06);
}

.back-btn button {
  border-radius:999px !important;
  border:1px solid rgba(0,0,0,0.2) !important;
}

.showcase-nav {
  display:flex;
  justify-content:center;
  gap:16px;
  margin-bottom:10px;
}
.showcase-nav button {
  border-radius:50%;
  width:42px;
  height:42px;
  font-size:20px;
  border:1px solid rgba(0,0,0,0.25);
}
</style>
""", unsafe_allow_html=True)


# =========================
# DATA
# =========================
SHOWCASE_IMAGES = [
    "img1.png",
    "img2.png",
    "img3.png",
    "img4.png",
    "img5.png"
]

PRODUCTS = {
    "기름종이": {
        "category": "화장품 & 화장소품",
        "title": "프리미엄 기름종이",
        "desc": "피부 유분을 자극 없이 흡수하는 천연 마 소재.",
        "list_image": "oil_paper.png",
        "detail_image": "oil_paper_detail.png",
    },
    "스타페이스": {
        "category": "화장품 & 화장소품",
        "title": "스타페이스 여드름패치",
        "desc": "트러블을 빠르고 조용하게 진정시키는 스팟 솔루션.",
        "list_image": "patch.png",
        "detail_image": "patch_detail.png",
    },
    "도파민패치": {
        "category": "건강식품",
        "title": "도파민 패치",
        "desc": "일상의 활력을 되찾아주는 에너제틱 솔루션.",
        "list_image": "dopamine.png",
        "detail_image": "dopamine_detail.png",
    },
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
<div class="mn-logo">
  <h1>MADE IN NATURE</h1>
  <p>Premium Naturalism & Luxury Design</p>
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

    st.markdown(f"<h2 style='text-align:center;font-weight:200'>{p['title']}</h2>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align:center;color:#777'>{p['desc']}</p>", unsafe_allow_html=True)

    image_or_placeholder(p["detail_image"], height=600)


# =========================
# HOME PAGE
# =========================
def render_home():

    # ---------- SHOWCASE ----------
    section_title("BRAND SHOWCASE")

    cols = st.columns([1,2,1])
    with cols[1]:
        c1, c2 = st.columns([1,1])
        with c1:
            if st.button("‹"):
                st.session_state.showcase_idx = (st.session_state.showcase_idx - 1) % len(SHOWCASE_IMAGES)
        with c2:
            if st.button("›"):
                st.session_state.showcase_idx = (st.session_state.showcase_idx + 1) % len(SHOWCASE_IMAGES)

    st.markdown("<div style='max-width:900px;margin:0 auto;'>", unsafe_allow_html=True)
    image_or_placeholder(SHOWCASE_IMAGES[st.session_state.showcase_idx], height=520)
    st.markdown("</div>", unsafe_allow_html=True)

    # ---------- COLLECTION ----------
    section_title("COLLECTIONS")
    tabs = st.tabs(["화장품 & 화장소품", "건강식품"])

    with tabs[0]:
        for k, v in PRODUCTS.items():
            if v["category"] == "화장품 & 화장소품":
                st.markdown("<div class='mn-card'>", unsafe_allow_html=True)
                image_or_placeholder(v["list_image"], height=300)
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
                image_or_placeholder(v["list_image"], height=300)
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





