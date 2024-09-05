import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import matplotlib.font_manager as fm

# 한글 폰트 설정
font_name = fm.FontProperties(fname='c:/Windows/Fonts/malgun.ttf').get_name()
plt.rcParams['font.family'] = font_name
plt.rcParams['axes.unicode_minus'] = False

# Dataframe 생성
data = pd.DataFrame({
    '이름':['영식','철수','영희'],
    '나이':[22,31,25],
    '몸무게':[75.5,80.2,55.1]
})

st.dataframe(data, use_container_width=True) # 생성한 데이터 프레임 출력

fig, ax = plt.subplots() # 우선 캔버스를 만들어줌
ax.bar(data['이름'], data['나이']) # x축 : 이름, y축 : 나이
st.pyplot(fig) # matplotlib으로 생성한 fig를 넣어주면 됨

# 위 그래프는 투박하므로 아래 seaborn을 주로 이용함
barplot = sns.barplot(x='이름', y='나이', data=data, ax=ax, palette='Set2')
fig = barplot.get_figure()
st.pyplot(fig)

################################

species = ('Adelie', 'Chinstrap', 'Gentoo')
sex_counts = {
    'Male': np.array([73, 34, 61]),
    'Female': np.array([73, 34, 58]),
}
width = 0.6  # the width of the bars: can also be len(x) sequence

fig, ax = plt.subplots()
bottom = np.zeros(3)

for sex, sex_count in sex_counts.items():
    p = ax.bar(species, sex_count, width, label=sex, bottom=bottom)
    bottom += sex_count

    ax.bar_label(p, label_type='center')

ax.set_title('Number of penguins by sex')
ax.legend()

st.pyplot(fig)

################ bar code 예제
code = np.array([
    1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1,
    0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0,
    1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1,
    1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1])

pixel_per_bar = 4
dpi = 100

fig = plt.figure(figsize=(len(code) * pixel_per_bar / dpi, 2), dpi=dpi)
ax = fig.add_axes([0, 0, 1, 1])  # span the whole figure
ax.set_axis_off()
ax.imshow(code.reshape(1, -1), cmap='binary', aspect='auto',
          interpolation='nearest')
st.pyplot(fig)