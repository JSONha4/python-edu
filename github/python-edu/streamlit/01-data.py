import streamlit as st
import pandas as pd
import numpy as np

st.title('데이터프레임 튜토리얼')

# Dataframe 생성
dataframe = pd.DataFrame({
    'first column': [1,2,3,4],
    'second column': [10,20,30,40],
})

# DataFrame
# use_container_width 기능은 데이터프레임을 컨테이너 크기에 확장할 때 사용합니다. (True:테이블 넓게/False: 테이블 좁게)
st.dataframe(dataframe, use_container_width=False)

# 테이블(static)
# DataFrame과는 다르게 interactive 한 UI를 제공하지 않습니다.
st.table(dataframe)

# 메트릭
st.metric(label='온도', value='10ºC', delta='1.2ºC')
st.metric(label='LG전자', value='61,000 원', delta='-1,200 원')

# 컬럼으로 영역을 나누어 표기한 경우
col1, col2, col3 = st.columns(3)
col1.metric(label='달러USD', value='1,228 원', delta='-12.00 원')
col2.metric(label='일본JPY(100엔)', value='958.63 원', delta='-7.44 원')
col3.metric(label='유럽연합EUR', value='1,335.82 원', delta='11.44 원')