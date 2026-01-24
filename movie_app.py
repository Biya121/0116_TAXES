import os
import time
import streamlit as st

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(page_title="Made in Nature | Official", layout="wide")

# =========================
# OPTIONAL: auto-refresh support
# (If installed: pip install streamlit-autorefresh)
# =========================
try:
    from streamlit_autorefresh import st_autorefresh  # type: ignore
    HAS_AUTOREFRESH = True
except Exception:
    HAS_AUTOREFRESH = False

# =========================
# UTIL
# =========================
def file_exists(path: str) -> bool:
    return bool(path) and os.path.isfile(path)

def safe_image(path: str, *, caption: str | None = None, use_container_width: bool = True, width: int | None = None):
    if file_exists(path):
        st.image(path, caption=caption, use_container_width=use_container_width, width=width)
    else:
        st.warning(f"이미지 파일을 찾을 수 없어요: {path}")

def section_title(text: str, *, subline: bool = True):
    # ✅ Streamlit 헤딩 문법(#, ##)을 쓰지 않음 → 제목 옆 링크(앵커) 아이콘 발생 가능성 자체 차단
    st.markdown(
        f"""
        <style>
        .mn-title {{
          text-align:center;
          letter-spacing:0.28rem;
          color:#1B3022;
          font-weight:200;
          margin: 70px 0 8px;
          font-size: 1.25rem;
        }}
        .mn-subline {{
          width: 34px;
          height: 1px;
          background: #C5A059;
          margin: 14px auto 28px;
          opacity: 0.95;
        }}
        </style>
        <div class="mn-title">{text}</div>
        {"<div class='mn-subline'></div>" if subline else ""}
        """,
        unsafe_allow_html=True
    )

# =========================
# GLOBAL STYLE (CSS only)
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
  padding-top: 4.2rem;
  padding-bottom: 2.5rem;
}

.stApp{
  background: radial-gradient(1200px 600px at 50% -10%, rgba(197,160,89,0.10), transparent 55%),
              linear-gradient(to bottom, var(--paper), #ffffff);
}

/* Card */
.mn-card{
  background: rgba(255,255,255,0.75);
  border: 1px solid rgba(27,48,34,0.12);
  border-radius: 14px;
  padding: 18px;
  box-shadow: var(--shadow-soft);
}
.mn-badge{
  display:inline-block;
  padding: 6px 10px;
  border-radius: 999px;
  background: rgba(197,160,89,0.12);
  border: 1px solid rgba(197,160,89,0.22);
  color: rgba(27,48,34,0.85);
  font-size: 0.78rem;
  letter-spacing: 0.08rem;
  font-weight: 200;
  margin-bottom: 10px;
}
.mn-card-title{
  margin: 10px 0 6px;
  color: var(--deep);
  font-weight: 200;
  font-size: 1.25rem;
  letter-spacing: 0.05rem;
}
.mn-card-desc{
  margin: 0 0 14px;
  color: var(--muted);
  line-height: 1.8;
  font-weight: 200;
  font-size: 0.95rem;
}

/* Header */
.mn-logo-wrap{
  text-align:center;
  padding: 44px 0 22px;
}
.mn-logo-text{
  font-size: 3.0rem;
  letter-spacing: 0.75rem;
  color: var(--deep);
  font-weight: 200;
}
.mn-logo-tag{
  margin-top: 12px;
  color: rgba(15, 26, 18, 0.58);
  letter-spacing: 0.22rem;
  font-weight: 200;
  font-size: 0.95rem;
}
.mn-line{
  width: 34px;
  height: 1px;
  background: var(--gold);
  margin: 22px auto 0;
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
  position:absolute;
  inset:0;
  background: linear-gradient(180deg, rgba(0,0,0,0.20), rgba(0,0,0,0.45));
}
.mn-hero-content{
  position: absolute;
  inset: 0;
  display:flex;
  align-items:center;
  justify-content:center;
  flex-direction:column;
  text-align:center;
  padding: 0 16px;
}
.mn-hero-h2{
  font-size: 1.0rem;
  color: var(--gold);
  letter-spacing: 0.48rem;
  margin: 0 0 12px 0;
  font-weight: 200;
}
.mn-hero-h1{
  font-size: 2.8rem;
  font-weight: 200;
  color: #fff;
  margin: 0;
}
.mn-hero-p{
  margin: 16px auto 0;
  max-width: 720px;
  color: rgba(255,255,255,0.82);
  font-weight: 200;
  line-height: 1.9;
}

/* Footer (no HTML blocks; just style helpers) */
.mn-footer{
  margin-top: 120px;
  padding: 34px 0 10px;
  border-top: 1px solid rgba(27,48,34,0.18);
  text-align:center;
}
.mn-footer-brand{
  letter-spacing: 0.45rem;
  color: #1B3022;
  font-weight: 200;
  font-size: 1.1rem;
}
.mn-footer-muted{
  color: rgba(15, 26, 18, 0.55);
  font-weight: 200;
  line-height: 1.9;
}
.mn-footer-links a{
  margin: 0 14px;
  text-decoration: none;
  color: rgba(27,48,34,0.85);
  letter-spacing: 0.1rem;
  font-size: 0.85rem;
}
.mn-footer-links a:hover{
  color: #C5A059;
}
</style>
""", unsafe_allow_html=True)

# =========================
# STATE
# =========================
if "selected_product" not in st.session_state:
    st.session_state.selected_product = None
if "showcase_i" not in st.session_state:
    st.session_state.showcase_i = 0


# =========================
# SECTION 1: HEADER (no fragile <img> HTML)
# =========================
st.markdown("""
<div class="mn-logo-wrap">
  <div class="mn-logo-text">MADE IN NATURE</div>
  <div class="mn-line"></div>
  <div class="mn-logo-tag">Premium Naturalism & Luxury Design</div>
</div>
""", unsafe_allow_html=True)


# =========================
# SECTION 2: HERO
# =========================
hero_bg = "hero_bg.jpg"
if file_exists(hero_bg):
    st.image(hero_bg, use_container_width=True)  # 가장 안정적인 방법: 그냥 이미지로
    # 오버레이 텍스트는 아래에 분리해서(HTML 배경 url 의존 제거)
    st.markdown(
        "<div style='text-align:center; margin-top:-360px; position:relative; z-index:2;'>"
        "<div class='mn-hero-h2'>Nature, defined by luxury</div>"
        "<div class='mn-hero-h1'>자연의 가치를 증명하다</div>"
        "<div class='mn-hero-p'>원료의 본질과 감각적인 디자인의 균형. 당신의 일상에 조용한 품격을 더합니다.</div>"
        "</div>",
        unsafe_allow_html=True
    )
    st.markdown("<div style='height:260px;'></div>", unsafe_allow_html=True)  # 레이아웃 보정
else:
    # 배경 이미지가 없으면 HTML hero 박스만 표시
    st.markdown("""
    <div class="mn-hero" style="background: linear-gradient(135deg, rgba(27,48,34,0.95), rgba(27,48,34,0.65));">
      <div class="mn-hero-overlay"></div>
      <div class="mn-hero-content">
        <div class="mn-hero-h2">Nature, defined by luxury</div>
        <div class="mn-hero-h1">자연의 가치를 증명하다</div>
        <div class="mn-hero-p">원료의 본질과 감각적인 디자인의 균형. 당신의 일상에 조용한 품격을 더합니다.</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# =========================
# BRAND SHOWCASE (1000x1000) - no HTML/JS carousel
# =========================
section_title("BRAND SHOWCASE")

showcase_images = ["img1.jpg", "img2.jpg", "img3.jpg", "img4.jpg", "img5.jpg"]
valid_showcase = [p for p in showcase_images if file_exists(p)]

if not valid_showcase:
    st.warning("쇼케이스 이미지를 찾을 수 없어요. img1.jpg ~ img5.jpg 를 프로젝트 폴더에 넣어주세요.")
else:
    # ✅ 자동 로테이션: streamlit-autorefresh가 있으면 주기적으로 인덱스 변경
    if HAS_AUTOREFRESH:
        # 3.2초마다 리런
        st_autorefresh(interval=3200, key="showcase_refresh")
        st.session_state.showcase_i = (st.session_state.showcase_i + 1) % len(valid_showcase)
    else:
        # 패키지 없으면 앱은 깨지지 않게 정적 표시 + 안내
        st.caption("자동 로테이션을 원하면: `pip install streamlit-autorefresh` 설치 후 다시 실행하세요.")

    # 1000x1000 “크게” 보여주기: 컨테이너 폭에 맞추되 최대 1000px 느낌으로
    # Streamlit은 픽셀 고정이 어려워서, wide 레이아웃에서 거의 1000px 가까이 나옴
    st.image(valid_showcase[st.session_state.showcase_i], use_container_width=True)


# =========================
# COLLECTIONS
# =========================
section_title("COLLECTIONS")

tabs = st.tabs(["화장품 & 화장소품", "건강식품", "생활잡화"])

product_images: Dict[str, str] = {
    "기름종이": "oil_paper.jpg",
    "스타페이스": "patch.jpg",
    "도파민패치": "dopamine.jpg",
    "나이트패치": "night.jpg",
    "수세미": "scrubber.jpg",
    "칫솔": "toothbrush.jpg",
}

def product_card(key: str, badge: str, title: str, desc: str, img_path: str, btn_key: str):
    st.markdown("<div class='mn-card'>", unsafe_allow_html=True)
    st.markdown(f"<span class='mn-badge'>{badge}</span>", unsafe_allow_html=True)
    safe_image(img_path, use_container_width=True)
    st.markdown(f"<div class='mn-card-title'>{title}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='mn-card-desc'>{desc}</div>", unsafe_allow_html=True)
    if st.button("제품 상세 페이지 이동", key=btn_key, use_container_width=True):
        st.session_state.selected_product = key
    st.markdown("</div>", unsafe_allow_html=True)

with tabs[0]:
    c1, c2 = st.columns(2, gap="large")
    with c1:
        product_card("기름종이", "COSMETIC ACCESSORY", "프리미엄 기름종이",
                     "피부 유분을 자극 없이 흡수하는 천연 마 소재.",
                     product_images["기름종이"], "det1")
    with c2:
        product_card("스타페이스", "SPOT SOLUTION", "스타페이스 여드름패치",
                     "트러블을 빠르고 조용하게 진정시키는 스팟 솔루션.",
                     product_images["스타페이스"], "det2")

with tabs[1]:
    c1, c2 = st.columns(2, gap="large")
    with c1:
        product_card("도파민패치", "WELLNESS PATCH", "도파민 패치",
                     "일상의 활력을 되찾아주는 에너제틱 솔루션.",
                     product_images["도파민패치"], "det3")
    with c2:
        product_card("나이트패치", "NIGHT RITUAL", "나이트 패치",
                     "고요한 휴식을 선사하는 아로마 릴렉싱.",
                     product_images["나이트패치"], "det4")

with tabs[2]:
    c1, c2 = st.columns(2, gap="large")
    with c1:
        product_card("수세미", "HOME CARE", "코코넛 수세미",
                     "자연에서 온 거친 섬유의 완벽한 세척력.",
                     product_images["수세미"], "det5")
    with c2:
        product_card("칫솔", "SUSTAINABLE BATH", "대나무 칫솔",
                     "지속 가능한 욕실을 위한 친환경 선택.",
                     product_images["칫솔"], "det6")

if st.session_state.selected_product:
    st.divider()
    st.info(f"선택된 제품: **{st.session_state.selected_product}**  ·  (여기에 상세 페이지/외부 링크/멀티페이지 연결을 추가하면 완성됩니다.)")


# =========================
# FOOTER (✅ NO HTML TAGS as content)
# =========================
st.markdown("<div class='mn-footer'>", unsafe_allow_html=True)
st.markdown("<div class='mn-footer-brand'>MADE IN NATURE</div>", unsafe_allow_html=True)
st.markdown("<div style='width:34px;height:1px;background:#C5A059;margin:18px auto 22px;'></div>", unsafe_allow_html=True)

# ✅ 여기부터는 HTML 태그를 '콘텐츠'로 넣지 않고, Streamlit 텍스트만 사용
st.markdown(
    "<div class='mn-footer-muted'>"
    "자연의 본질을 연구하고 지속 가능한 가치를 디자인합니다.<br>"
    "우리는 당신의 일상이 자연과 더 가까워질 수 있도록<br>"
    "최상의 원료와 장인 정신을 고집합니다."
    "</div>",
    unsafe_allow_html=True
)

# 링크는 Streamlit 기본 link_button(가능하면) / 아니면 그냥 텍스트로
st.markdown("<div style='height:18px;'></div>", unsafe_allow_html=True)

link_cols = st.columns(4)
with link_cols[0]:
    st.link_button("BRAND STORY", "https://example.com")
with link_cols[1]:
    st.link_button("COLLECTIONS", "https://example.com")
with link_cols[2]:
    st.link_button("SUSTAINABILITY", "https://example.com")
with link_cols[3]:
    st.link_button("CONTACT", "https://example.com")

st.markdown("<div style='height:20px;'></div>", unsafe_allow_html=True)

st.caption("주식회사 메이드인네이처 | 서울특별시 성동구 성수동 자연길 123")
st.caption("Customer Care. 02-1234-5678 | Email. official@madeinnature.com")
st.caption("Instagram. @madeinnature_official")
st.markdown("<div style='height:14px;'></div>", unsafe_allow_html=True)
st.caption("© 2026 MADE IN NATURE. ALL RIGHTS RESERVED.  ·  PREMIUM NATURALISM & LUXURY DESIGN.")
st.markdown("</div>", unsafe_allow_html=True)

