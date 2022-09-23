import streamlit as st
st.set_page_config(page_title="Home", page_icon="🏠",)

"""
# High Throughput Bayesian Optimization App

This is an app for high throughput Bayesian optimization.
"""

# st.download_button("Download template", "static/template.xlsx", "template.xlsx")

with open('static/HTBO.xlsx', 'rb') as f:
   st.download_button('Download template', f, file_name='htbo.xlsx') 