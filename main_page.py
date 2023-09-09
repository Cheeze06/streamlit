import streamlit as st

st.title('2023 february Game Ranking 🏆')

st.header('MORE INFORMATION')


# 각 열에 하이퍼링크 추가
st.image('https://d1.awsstatic.com/002_RG_2021_FULL_LOCKUP_RED.5627f0de6611fcc949c7966209c7b802a0724ddd.png')
st.markdown('<a href="https://www.riotgames.com/ko">RIOT GAMES 상세 정보</a>', unsafe_allow_html=True)
st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/3/3b/Nexon_Logo.svg/799px-Nexon_Logo.svg.png')
st.markdown('<a href="https://www.nexon.com/Home/Game">NEXON 상세 정보</a>', unsafe_allow_html=True)
st.image('https://res.cloudinary.com/linkareer/image/fetch/f_auto,q_50/https://api.linkareer.com/attachments/44829')
st.markdown('<a href="https://kr.ncsoft.com/kr/index.do">NCSOFT 상세 정보</a>', unsafe_allow_html=True)

font_dirs = [os.getcwd() + '/customFonts']
font_files = fm.findSystemFonts(fontpaths=font_dirs)

for font_file in font_files:
    fm.fontManager.addfont(font_file)
fm._load_fontmanager(try_read_cache=False)
