import streamlit as st
from config import pagesetup as ps

# 0. Set Page Title and Page Overview
page_title = "AI Assistant"
page_subtitle = "GPT vs. GPT"
page_description = "Allows users to setup two GPTs and watch them have a conversation with eachother."
overview_section_header = "Overview"
overview_section_text = f"**{page_subtitle}** {page_description.lower()}."
ps.set_title(page_title, page_subtitle)
ps.set_page_overview(overview_section_header, overview_section_text)

#1. Set Page Section
section_1_header = "Demo"
section_1_text = f"Try out the **{page_subtitle}** app below!"
section_1_placeholder = ps.set_page_section(section_1_header, section_1_text)
with section_1_placeholder:
    container1 = st.container()
