import streamlit as st

# Page config
st.set_page_config(page_title="My Portfolio", page_icon="🌟")

# Sidebar
st.sidebar.title("Navigation")
menu = st.sidebar.radio("Go to", ["Home", "About", "Projects", "Contact"])

# Home
if menu == "Home":
    st.title("👩‍💻INNO_CORES")
    st.subheader("Aspiring Full Stack Developer")
    st.write("Welcome to my Streamlit portfolio!")

# About
elif menu == "About":
    st.header("📌 About Me")
    st.write("""
    - Beginner Full Stack Developer  
    - Learning Python, C, Streamlit  
    - Interested in Web & App Development  
    """)

# Projects
elif menu == "Projects":
    st.header("🛠 Projects")
    st.write("🔹 Student Feedback System")
    st.write("🔹 Travel Content App")
    st.write("🔹 GitHub Portfolio Website")

# Contact
elif menu == "Contact":
    st.header("📞 Contact Me")
    email = st.text_input("Enter your mail id")
    msg = st.text_area("Your message regarding issues or suggestions")

    if st.button("Send"):
        st.success("Message sent successfully ✅ ")