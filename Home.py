import streamlit as st


# 0. Set Page Config
app_name = "AppName"
app_icon = "🌐☁️"
app_layout = "wide"
app_sidebar = "collapsed" 

st.set_page_config(page_title=app_name, page_icon=app_icon, layout=app_layout, initial_sidebar_state=app_sidebar)
