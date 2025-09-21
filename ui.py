import streamlit as st
from models.cultural_classifier import OptimizedCulturalEngine

st.set_page_config(page_title="Cultural Intelligence Engine", layout="wide")
st.title("🌏 Free Cultural Intelligence Engine")

if 'engine' not in st.session_state:
    st.session_state.engine = OptimizedCulturalEngine()

user_id = st.text_input("User ID", value="user_01")
region = st.text_input("Region", value="Maharashtra")
text_input = st.text_area("Enter Text to Analyze", "")

col_analyze, col_clear = st.columns([3,1])
if col_analyze.button("Analyze Text"):
    if not text_input.strip():
        st.warning("Please enter some text to analyze!")
    else:
        with st.spinner("Analyzing..."):
            result = st.session_state.engine.analyze_cultural_context(
                text_input,
                {"user_id": user_id, "region": region}
            )
        st.success("Analysis Complete!")
        st.json(result)
if col_clear.button("Clear Input"):
    text_input = ""
