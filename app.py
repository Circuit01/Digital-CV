from pathlib import Path
import streamlit as st
from PIL import Image

# Path Settings
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic_path = current_dir / "assets" / "profile_pic.png"  

# General Settings
PAGE_TITLE = "Digital CV | Noah Sherry"
PAGE_ICON = "📄"  
NAME = "Noah Sherry"
DESCRIPTION = """
**Aspiring Software Developer, Specialising in Python.**\n

Currently pursuing studies in Cyber Security and IT, with additional knowledge in PHP and SQL.
"""
st.write("---")

EMAIL = "noahsherry1@gmail.com"
SOCIAL_MEDIA = {
    "Youtube": "https://www.youtube.com/channel/UCupTDTxhdZ5oGHqCJLleMRA",
    "LinkedIn": "https://www.linkedin.com/in/noah-sherry-b7379b297/",
    "GitHub": "https://github.com/Circuit01",
    "Instagram": "https://www.instagram.com/circu1t.dev/",
}
PROJECTS = {
    " 🛠️ Password Manager - Effortlessly Generate, Securely Save, and Always Remember Your Passwords": "https://github.com/Circuit01/Task-Manager",
    " 🛠️ File Organiser - Streamline, Sort, and Simplify Your Digital Life": "https://github.com/Circuit01/File-Organiser",
    " 🛠️ Finance Manager - Track, Manage, and Master Your Finances with Ease (currently a work in progress)": "https://github.com/Circuit01/Finance-Manager",
    " 🛠️ Begginners Tkinter Tutorial - Learn to make your first GUI using Python and Tkinter!": "https://www.youtube.com/watch?v=PuMMfHq5i2Q&list=PLTaOLV--gGiYrpT3OdPvcxKhTwiqHGiRO",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# Load CSS & Profile Pic
with open(css_file) as f:
    css_content = f.read()
    st.markdown(f'<style>{css_content}</style>', unsafe_allow_html=True)
profile_pic = Image.open(profile_pic_path)

# Hero Section
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="📥 Download Resume",
        data=b'PDFbyte', 
        file_name='CV.pdf',  
        mime="application/pdf",
    )
    st.write("📬", EMAIL)

# Social Links
st.write('#')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# Experience & Qualifications
st.write('#')
st.subheader("Experience & Qualifications")
st.write(
    """
- • 1 year of professional experience as a Python developer, including proficiency in SQL and HTML
- • Extensive hands on experience and expertise in Python and Excel
- • Currently pursuing a Certificate III  TAFE course in ICT and Cyber Security
- • Owner and content creator of an educational YouTube channel focused on Python tutorials
- • 4 years of comprehensive experience in Python programming
"""
)

# Skills
st.write('#')
st.subheader("Hard Skills")
st.write(
    """
- 💻 Programming: Python, SQL, JS
- 📊 Data Visulisation: MS Excel, Plotly, Matplotlib 
- 🛢️ Databases: MySQL, MongoDB
"""
)


# Work History
st.write('#')
st.subheader("Work History")
st.write("---")

# Job 1
st.write("👨‍💻", "**Python Software Devoloper, HTML, SQL | Cider House ICT**")
st.write("2023-28/07/2024")
st.write(
    """
- ► Used Python to create software for clients
- ► Designed and implemented custom HTML forms tailored to client specifications
- ► Proficiently managed databases using MySQL for efficient data storage and retrieval
- ► Extended use of programs such as TeamViewer
- ► Demonstrated expertise in assembling and configuring PCs and laptops to meet client requirements
"""
)

# Job 2
st.write('#')
st.write("🛎️", "Customer Service | Wooloworths")
st.write("2023-current")
st.write(
    """
- ► Provided customer service at registers, ensuring smooth transactions
- ► Assisted customers with troubleshooting and support at self-service checkouts
- ► Managed online orders, picking and delivering items promptly to customers
- ► Maintained organized and fully stocked shelves across multiple departments
"""
)

# Projects
st.write('#')
st.subheader("Projects")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
