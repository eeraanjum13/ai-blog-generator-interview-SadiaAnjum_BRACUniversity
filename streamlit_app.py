import streamlit as st
from datetime import datetime
import os

from ai_generator import generate_blog_post
from get_seo_data import get_seo_data

from apscheduler.schedulers.background import BackgroundScheduler

saved_folder = "saved_posts"
os.makedirs(saved_folder, exist_ok=True)

def generate_and_save(keyword):
    st.session_state["log"] = f"Generating post for: {keyword}"
    seo_data = get_seo_data(keyword)
    blog = generate_blog_post(keyword, seo_data)
    filename = f"{saved_folder}/{keyword.replace(' ', '_')}_{datetime.now().date()}.md"
    with open(filename, "w") as f:
        f.write(blog)
    st.session_state["log"] = f"✅ Saved blog: {filename}"
    return blog

# Streamlit UI
st.title("📝 AI Blog Generator")
keyword = st.text_input("Enter a keyword", value="wireless earbuds")

if st.button("Generate Blog Post"):
    with st.spinner("Generating..."):
        seo = get_seo_data(keyword)
        blog = generate_blog_post(keyword, seo)
        # blog = '# Sample content for demonstration purposes\n'
        filename = f"{saved_folder}/{keyword.replace(' ', '_')}_{datetime.now().date()}.md"
        with open(filename, "w") as f:
            f.write(blog)
        st.success(f"Blog post saved to `{filename}`")
         # Download as Markdown
        st.download_button(
            label="📥 Download as Markdown in your desired file system (.md)",
            data=blog,
            file_name=f"{keyword.replace(' ', '_')}_{datetime.now().date()}.md",
            mime="text/markdown"
        )

# Show background job status
if "log" in st.session_state:
    st.info(st.session_state["log"])

# APScheduler (start once)
if "scheduler_started" not in st.session_state:
    scheduler = BackgroundScheduler()
    scheduler.add_job(lambda: generate_and_save("wireless earbuds"), "interval", days=1)
    scheduler.start()
    st.session_state["scheduler_started"] = True
    st.success("✅ Daily blog scheduler started.")
