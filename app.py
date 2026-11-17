# app.py
import streamlit as st
import re

# -----------------------------
# STUDYMATE AI - FIRST VERSION
# -----------------------------

st.set_page_config(
    page_title="StudyMate AI",
    page_icon="📚",
    layout="wide"
)

# Styling
st.markdown("""
<style>
.main {
    background-color: #f8fafc;
}
h1 {
    color: #243b53;
}
.stButton>button {
    background-color: #315c75;
    color: white;
    border-radius: 10px;
    padding: 10px 20px;
}
</style>
""", unsafe_allow_html=True)

# Header
st.title("📚 StudyMate AI")
st.subheader("Learn smarter. Understand deeper. Remember longer.")

st.write(
    "Your personal study companion. "
    "Turn your learning materials into revision notes and practice questions."
)

st.divider()

# Sidebar
st.sidebar.title("StudyMate AI")
page = st.sidebar.radio(
    "Navigation",
    ["Dashboard", "Notes Assistant", "Quiz Generator", "About"]
)

# -----------------------------
# DASHBOARD
# -----------------------------
if page == "Dashboard":

    st.header("Welcome to your study space 👋")

    col1, col2, col3 = st.columns(3)

    col1.metric("Study materials", "0")
    col2.metric("Quizzes completed", "0")
    col3.metric("Revision progress", "0%")

    st.info(
        "Your learning journey starts here. "
        "Choose a tool from the sidebar to get started."
    )

    st.subheader("What would you like to do today?")

    st.write("📖 Simplify difficult study topics")
    st.write("📝 Create revision notes")
    st.write("🧠 Practise examination questions")
    st.write("🎯 Improve your understanding")

# -----------------------------
# NOTES ASSISTANT
# -----------------------------
elif page == "Notes Assistant":

    st.header("📝 AI Notes Assistant")

    st.write("Paste your study material below.")

    notes = st.text_area(
        "Your study material",
        height=250,
        placeholder="Paste your nursing or university notes here..."
    )

    if st.button("Generate Revision Notes"):

        if not notes.strip():
            st.warning("Please enter some study material first.")

        else:
            sentences = re.split(r'(?<=[.!?])\s+', notes.strip())

            st.subheader("Your Study Material")
            st.write(notes)

            st.subheader("Key Revision Points")

            for sentence in sentences:
                if len(sentence.split()) >= 5:
                    st.write("• " + sentence)

            st.success(
                "Demo revision notes generated. "
                "AI-powered summarisation will be added in the next version."
            )

# -----------------------------
# QUIZ GENERATOR
# -----------------------------
elif page == "Quiz Generator":

    st.header("🧠 Quiz Generator")

    st.write(
        "Paste your notes to prepare for a practice quiz."
    )

    quiz_notes = st.text_area(
        "Study material",
        height=200,
        placeholder="Paste your notes here..."
    )

    if st.button("Prepare Quiz"):

        if not quiz_notes.strip():
            st.warning("Please enter your notes.")

        else:
            words = quiz_notes.split()

            st.success("Your study material has been received!")

            st.write(
                f"You entered approximately {len(words)} words."
            )

            st.info(
                "Automatic MCQ generation and answer explanations "
                "will be added in the next development stage."
            )

# -----------------------------
# ABOUT
# -----------------------------
elif page == "About":

    st.header("About StudyMate AI")


  st.write("""
    StudyMate AI is an educational platform designed to help
    university students learn more effectively.

    Our mission is to make studying easier, more interactive,
    and more accessible.

    **Our tagline:**

    Learn smarter. Understand deeper. Remember longer.
    """)

    st.write("Created for students, by a student.")
