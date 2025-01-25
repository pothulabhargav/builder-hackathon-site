# Import required libraries
import streamlit as st
from components.home import render_home
from components.problems import render_problems
from components.teams import render_teams

# Configure page settings
st.set_page_config(layout="wide")

# Load CSS
with open('styles/main.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Add navigation using tabs
tab1, tab2, tab3 = st.tabs(["Home", "Problem Statements", "Teams"])

with tab1:
    render_home()

with tab2:
    render_problems()

with tab3:
    render_teams()