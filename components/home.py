import streamlit as st

def render_home():
    col1, col2, col3 = st.columns([1,2,1])
    
    with col2:
        st.markdown("""
            <h1 style='text-align: center; font-size: 2.5em; margin-bottom: 30px; letter-spacing: 2px; color: #9d4edd; text-shadow: 0 0 10px rgba(157, 78, 221, 0.3);'>
            Builder Hackathon
            </h1>
        """, unsafe_allow_html=True)
        
        st.markdown("""
            <p style='text-align: center; font-size: 1.2em; margin-bottom: 15px;'>
                <span style='color: #00b4d8'>Venue:</span> 
                <span style='color: #e2e2e2'>3rd floor, HyperVerge Office, HSR</span>
            </p>
            <p style='text-align: center; font-size: 1.2em;'>
                <span style='color: #00b4d8'>Date:</span> 
                <span style='color: #e2e2e2'>January 31 - February 1, 2025</span>
            </p>
        """, unsafe_allow_html=True)