import streamlit as st

# 1. 페이지 설정 및 디자인 (자연주의 컨셉 컬러 반영)
st.set_page_config(page_title="made in nature | 브랜드 제품 소개", layout="wide")

# CSS를 이용한 커스텀 스타일링 (그린, 골드, 화이트 조합)
st.markdown(f"""
    <style>
    /* 전체 배경 및 폰트 설정 */
    .main {{
        background-color: #FFFFFF;
        color: #000000;
    }}
    
    /* 상단 네비게이션 바 스타일 */
    .stTabs [data-baseweb="tab-list"] {{
        gap: 50px;
        justify-content: center;
    }}
    .stTabs [data-baseweb="tab"] {{
        height: 50px;
        white-space: pre-wrap;
        font-weight: 600;
        font-size: 18px;
        color: #4B5320; /* 다크그린 */
    }}
    .stTabs [aria-selected="true"] {{
        color: #D4AF37 !important; /* 골드 포인트 */
        border-bottom-color: #D4AF37 !important;
    }}

    /* 제품 카드 스타일 */
    .product-card {{
        border: 1px solid #E0E0E0;
        padding: 20px;
        border-radius: 10px;
        background-color: #F9F9F9;
        margin-bottom: 20px;
    }}
    .gold-text {{
        color: #D4AF37;
        font-weight: bold;
    }}
    .green-title {{
        color: #2E8B57; /* 그린 */
        font-size: 24px;
        font-weight: bold;
    }}
    </style>
    """, unsafe_allow_html=True)

# 2. 상단 로고 및 제목 섹션
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    # 로고 이미지가 없다면 텍스트로 대체, 있다면 st.image("logo_path.png") 사용
    st.markdown("<h1 style='text-align: center; color: #2E8B57;'>🍃 made in nature</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #888888;'>자연에서 온 정직한 가치, 프리미엄 자연주의 라이프스타일</p>", unsafe_allow_html=True)

# 3. 메뉴 구성 (2단계 레이아웃 참고: 클릭 시 섹션 이동 효과)
tabs = st.tabs(["HOME", "스웨덴 행주", "대나무 칫솔", "비즈왁스랩", "코코넛 수세미"])

# --- HOME 섹션 ---
with tabs[0]:
    st.image("https://images.unsplash.com/photo-1542601906990-b4d3fb773b09?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80", caption="made in nature: Sustainable Lifestyle")
    st.markdown("---")
    st.header("Brand Story")
    st.write("made in nature는 화장품, 건강식품, 생활잡화를 아우르는 자연주의 브랜드입니다.")
    st.write("지구와 사람 모두에게 무해한 제로웨이스트 가치를 제안합니다.")

# --- 스웨덴 행주 섹션 ---
with tabs[1]:
    col_img, col_txt = st.columns([1, 1])
    with col_img:
        st.image("https://via.placeholder.com/500x500?text=Swedish+Dishcloth", caption="스웨덴 행주 블랙 에디션")
    with col_txt:
        st.markdown("<p class='green-title'>스웨덴 행주 (Swedish Dishcloth)</p>", unsafe_allow_html=True)
        st.markdown("<p class='gold-text'>Since 1949 전통 북유럽 행주</p>", unsafe_allow_html=True)
        st.write("- **강력한 성능**: 자기 무게 15배 흡수, 일반 행주보다 4배 빠른 건조")
        st.write("- **친환경성**: 1장으로 키친타올 15롤 대체 가능")
        st.write("- **디자인**: 블랙 에디션, 네이처, 플라워 라인업")
        st.button("제품 구매하기", key="btn1")

# --- 대나무 칫솔 섹션 ---
with tabs[2]:
    col_img, col_txt = st.columns([1, 1])
    with col_img:
        st.image("https://via.placeholder.com/500x500?text=Bamboo+Toothbrush", caption="10색 대나무 칫솔")
    with col_txt:
        st.markdown("<p class='green-title'>대나무 칫솔 (Bamboo Toothbrush)</p>", unsafe_allow_html=True)
        st.markdown("<p class='gold-text'>지구와 나를 위한 제로웨이스트의 시작</p>", unsafe_allow_html=True)
        st.write("- **미세모**: PBT 이중 미세모로 부드럽고 탄탄한 세정력")
        st.write("- **곰팡이 방지**: 밀랍 이중 코팅으로 위생적인 관리 가능")
        st.write("- **다양성**: 취향에 맞는 10가지 컬러 옵션")
        st.button("제품 구매하기", key="btn2")

# --- 비즈왁스랩 섹션 ---
with tabs[3]:
    col_img, col_txt = st.columns([1, 1])
    with col_img:
        st.image("https://via.placeholder.com/500x500?text=Beeswax+Wrap", caption="프리미엄 비즈왁스랩")
    with col_txt:
        st.markdown("<p class='green-title'>비즈왁스랩 (Beeswax Wrap)</p>", unsafe_allow_html=True)
        st.markdown("<p class='gold-text'>FDA & GOTS 인증 천연 식품 포장재</p>", unsafe_allow_html=True)
        st.write("- **천연 소재**: 천연 밀랍, 호호바 오일, 유기농 면 사용")
        st.write("- **신선함**: 뛰어난 밀착력으로 음식 수분 완벽 유지")
        st.write("- **재사용**: 최대 1년까지 사용 가능한 경제적 선택")
        st.button("제품 구매하기", key="btn3")

# --- 코코넛 수세미 섹션 ---
with tabs[4]:
    col_img, col_txt = st.columns([1, 1])
    with col_img:
        st.image("https://via.placeholder.com/500x500?text=Coconut+Scrubber", caption="생분해 코코넛 수세미")
    with col_txt:
        st.markdown("<p class='green-title'>코코넛 수세미 (Coconut Scrubber)</p>", unsafe_allow_html=True)
        st.markdown("<p class='gold-text'>S자형 인체공학 디자인의 강력한 세척</p>", unsafe_allow_html=True)
        st.write("- **소재**: 천연 코코넛 섬유와 퇴비화 가능한 셀룰로오스")
        st.write("- **옵션**: 오리지널, 노스크래치, 헤비듀티 3종 구성")
        st.write("- **위생**: 소량의 세제로도 풍성한 거품, 빠른 건조")
        st.button("제품 구매하기", key="btn4")

# 4. 푸터(Footer)
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: #AAAAAA; padding: 20px;'>
        <p>© 2026 made in nature. All Rights Reserved.</p>
        <p>화장품 & 화장소품 | 건강식품 | 생활잡화 전문 브랜드</p>
    </div>
    """, unsafe_allow_html=True)
