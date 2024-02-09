import streamlit as st
from config import pagesetup as ps


# 0. Set Page Config
app_name = "FlowGenius AI"
app_icon = "🌐☁️"
app_layout = "wide"
app_sidebar = "collapsed" 

st.set_page_config(page_title=app_name, page_icon=app_icon, layout=app_layout, initial_sidebar_state=app_sidebar)

# Set Page Title
ps.set_title("FlowGenius", "AI Assistant")
