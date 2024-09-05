import streamlit as st
import FinanceDataReader as fdr
import datetime

# Finance Data Reader
# https://github.com/financedata-org/FinanceDataReader

date = st.date_input(
    "조회 시작일을 선택해 주세요",
    datetime.datetime(2024, 1, 1)
)

# 국내주식 -> 네이버금융에서 숫자로된 종목코드 입력
# 해외주식 -> 티커명을 입력하면 됨
code = st.text_input(
    '종목코드',
    value='',
    placeholder='종목코드를 입력해 주세요'
)

if code and date:
    df = fdr.DataReader(code, date)
    data = df.sort_index(ascending=True).loc[:, 'Close'] # 날짜를 기준으로 정렬을 하고 종가(Close) 데이터를 가져옴
    st.line_chart(data)