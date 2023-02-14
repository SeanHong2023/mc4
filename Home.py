import streamlit as st
st.set_page_config(page_title='Mon Chaton - Care your cat', layout='wide')
st.title('Mon Chaton')
st.markdown('### 당신의 반려묘를 위한 AI 안심 케어')

html='''
<style>
.stApp {
  background-image: url("https://img.freepik.com/free-vector/minimal-cat-background-line-art-illustration-vector_53876-151371.jpg?w=2000");
  background-size: cover;
}
</style>
'''
st.markdown(html, unsafe_allow_html=True)

st.sidebar.markdown('#')
