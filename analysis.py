import os
import streamlit as st
from dotenv import load_dotenv
load_dotenv()

import google.generativeai as genai
from pdf import extractpdf

# Configure the api key
key = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=key)


#Call the model
model = genai.GenerativeModel('gemini-1.5-flash')

# Create the def function to analyze pdf anf jd(job des)

def analyze_resume(pdf_doc,job_des):
    if pdf_doc is not None:
        pdf_text = extractpdf(pdf_doc)
        st.write('Extracted Successfully')
    else:
        st.warning('Drop file in PDF format')
    
    ats_score=model.generate_content(f'''Compare the resume {pdf_text} with job
                                     description {job_des} and get the ATS Score''') 
    
    return st.write(ats_score.text)           