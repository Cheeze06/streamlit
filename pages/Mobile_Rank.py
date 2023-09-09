import streamlit as st
import pandas as pd

st.title('2023년 2월 PC 게임 순위 🏆')

path = 'pages/Mobile.csv'
# CSV 파일을 데이터프레임으로 읽기
data1 = pd.read_csv(path, encoding='cp949')

st.sidebar.title('Filter')

# data1['장르']
a = data1['장르']
b = set(a)
c = list(b)

# 서비스 목록 얻기
services = data1['서비스'].unique()

# 장르 선택
options_genre = st.sidebar.multiselect(
    '장르로 구분하기',
    c,
)

# 서비스 선택
options_service = st.sidebar.multiselect(
    '서비스로 구분하기',
    services,
)

# 장르와 서비스로 필터링
filtered_data = data1
if options_genre:
    filtered_data = filtered_data[filtered_data['장르'].isin(options_genre)]
if options_service:
    filtered_data = filtered_data[filtered_data['서비스'].isin(options_service)]

# 데이터프레임 출력
if not options_genre and not options_service:
    st.dataframe(data1, use_container_width=True)
else:
    st.dataframe(filtered_data, use_container_width=True)

st.subheader('Copyright ⓒ ParkCheeze ALL RIGHTS RESERVED.')
