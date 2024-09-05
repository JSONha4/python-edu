import streamlit as st
import random
import datetime

st.title(':sparkles:로또 생성기:sparkles:')

def generate_lotto(): # 로또 생성 파이썬 코드
    lotto = set() # 로또는 중복되는 숫자가 없기 때문에 set를 이용함

    while len(lotto) < 6:
        number = random.randint(1, 46) # 1~45 사이의 랜덤한 난수 생성
        lotto.add(number)

    lotto = list(lotto) # sort를 하기 위해 list로 변형
    lotto.sort()
    return lotto

# 1. 6개 로또 번호 1가지만 생성
# st.subheader(f'행운의 번호: :green[{generate_lotto()}]') # 6개의 번호가 생성됨
# st.write(f'생성된 시각: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}')

# 2. 버튼을 누르면 6개 로또 번호 5가지가 생성
button = st.button('로또를 생성해 주세요!')

if button:
    for i in range(1,6): # 5가지 로또 번호 6개가 생성됨
        st.subheader(f'{i}. 행운의 번호: :green[{generate_lotto()}]')
    st.write(f'생성된 시각: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}')