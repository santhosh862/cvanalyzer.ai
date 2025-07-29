import streamlit as st
from analysis import analyze_resume
st.title('CV Analyze')

st.header('''This page helps you compare resume with the given Job description''')

st.sidebar.subheader('Drop your resume here')

pdf_doc = st.sidebar.file_uploader('Click here to browse', type=['pdf'])

job_des = st.text_area('Copy paste the job description here', max_chars=10000)

submit = st.button('Generate ATS score')

if submit:
    with st.spinner('Getting Result...'):
        analyze_resume(pdf_doc,job_des)