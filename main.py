import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

st.write('プレグレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i + 1)
    time.sleep(0, 1)

#st.write('Interactive Widgets')



left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ1')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ2')
expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせ3')

text = st.text_input('あなたの趣味を教えて下さい。')
'あなたの趣味は', text, 'です'

condition = st.slider('あなたの今の調子は?', 0, 100, 50)
'コンディション:', condition

st.write('Display Image')

if st.checkbox('Show Image'):
    img = Image.open('cat.jpeg')
    st.image(img, caption='neko', use_column_width=True)

option = st.selectbox(
    'あなたが好きな数字を教えてください、',
    list(range(1, 11))
)

'あなたの好きな数字は、', option, 'です'

st.write('DataFrame')

df = pd.DataFrame({
    '1列目': [1, 2, 3, 4],
    '2列目': [10, 20, 30, 40]
})

st.dataframe(df.style.highlight_max(axis=0), width=400, height=200,)

st.table(df.style.highlight_max(axis=0))

"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```

"""

df2 = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c']
)

st.area_chart(df2)

df3 = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon',]
)

st.map(df3)
