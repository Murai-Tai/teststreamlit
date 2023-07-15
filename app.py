import streamlit as st

st.title('web app')
st.caption('test')
st.subheader('plofile')
st.text('My name is sapuu')

code = '''
import streamlit as st

st.title('web application')
'''
st.code(code, language='python')