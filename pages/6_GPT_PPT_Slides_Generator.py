import streamlit as st
from config import pagesetup as ps
from app.app_generate_slides import app_create_slides

# 0. Set Page Title and Page Overview
page_title = "AI Assistant"
page_subtitle = "Slide Generator"
page_description = "Allow users to create powerpoint slides based on a topic of choice."
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
    with container1: 
        topic = st.text_input(
            label="PowerPoint Topic",
            key="input_ppt_topic"
        )
        btn_submit = st.button("Submit", key="btn_topic_submit")

        if btn_submit:
            if topic:
                app_create_slides(topic)
                st.success(f"Creating slides for topic: {topic}") and topic:
            else:
                st.warning("Please enter a topic before submitting.")


