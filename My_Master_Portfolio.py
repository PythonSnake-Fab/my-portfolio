# ============================================================
# WEEK 10: MY GRADUATION PYTHON & AI PORTFOLIO LAB
# ============================================================

# STEP 1: IMPORT THE WEB ENGINE TOOLKIT
import streamlit as st

# STEP 2: BUILD THE DEVELOPER SIDEBAR
# This uses the sidebar tool to create a slide-out profile card on the left side
with st.sidebar:
    st.title("🎒 Dev Profile")
    st.write("**Age:** 9")
    st.write("**Language:** Python 3")
    st.write("**Specialty:** AI & Game Math")
    st.markdown("---")
    st.write("Special thanks to my Masterclass Coach for the coding rules!")

# STEP 3: MAIN PAGE HEADLINES
st.title("🚀 PythonSnake-Fab's AI & Tech Lab")
st.subheader("Welcome! I am a 9-year-old developer showcasing my top inventions.")
st.write("I spent 10 weeks learning how to build game physics engines, cryptographic tools, and computer vision models.")

st.markdown("---")

# STEP 4: CREATE SIDE-BY-SIDE COLUMNS FOR THE PROJECTS
col1, col2 = st.columns(2)

# LEFT COLUMN: THE PHYSICS GAMES
with col1:
    st.subheader("🎮 Phase 1: Visual Games")
    st.write("Built a 4-way Kaleidoscope Mirror Engine and Neon Pong using mouse coordinates and bouncing math vector angles.")
    if st.button("🕹️ Activate Game Intel"):
        st.success("System loaded! Native Pygame coordinates verified.")

# RIGHT COLUMN: THE AI GESTURE TRACKER
with col2:
    st.subheader("👁️ Phase 3: AI Vision")
    st.write("Trained a computer to detect ur hand and draw when u pinch ur index finger and thumb together using MediaPipe landmark distances.")
    if st.button("⚡ Activate AI Intel"):
        st.info("System loaded! HandLandmarker node tracing activated.")

st.markdown("---")

# STEP 5: THE GRADUATION FOOTER
st.header("🎓 Week 10 Graduation Status")
st.write("This active, interactive website serves as my official graduation project. The code runs entirely on a Python backend framework!")
