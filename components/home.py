import streamlit as st

def render_home():
    col1, col2, col3 = st.columns([1,2,1])
    
    with col2:
        st.markdown("<div class='main-content'>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align: center; color: #FF4B4B; text-shadow: 2px 2px 4px #000000;'>Builder Hackathon 2025</h1>", unsafe_allow_html=True)
        st.markdown("<h2 style='text-align: center; color: #0096D7;'>Venue: 3rd floor, HyperVerge Office, HSR</h2>", unsafe_allow_html=True)
        st.markdown("<h2 style='text-align: center; color: #0096D7;'>Date: January 31 - February 1, 2025</h2>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True) 