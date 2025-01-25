import streamlit as st

def render_home():
    col1, col2, col3 = st.columns([1,2,1])
    
    with col2:
        st.markdown("""
            <style>
                @keyframes glowPulse {
                    0% { text-shadow: 0 0 10px rgba(157, 78, 221, 0.3); }
                    50% { text-shadow: 0 0 20px rgba(157, 78, 221, 0.5); }
                    100% { text-shadow: 0 0 10px rgba(157, 78, 221, 0.3); }
                }
                
                .hackathon-title {
                    animation: glowPulse 2s infinite;
                    position: relative;
                }
            </style>
            
            <h1 class='hackathon-title' style='text-align: center; font-size: 2.5em; margin-bottom: 30px; letter-spacing: 2px; color: #9d4edd;'>
                <span style='background: linear-gradient(120deg, #9d4edd, #00b4d8); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'>
                    Builder Hackathon
                </span>
            </h1>
        """, unsafe_allow_html=True)
        
        st.markdown("""
            <div style='background: linear-gradient(145deg, rgba(45, 45, 68, 0.4), rgba(26, 26, 46, 0.4)); 
                        border-radius: 10px; 
                        padding: 20px;
                        box-shadow: 0 4px 15px rgba(123, 44, 191, 0.15);'>
                <p style='text-align: center; font-size: 1.2em; margin-bottom: 15px;'>
                    <span style='color: #00b4d8'>Venue:</span> 
                    <span style='color: #e2e2e2'>3rd floor, HyperVerge Office, HSR</span>
                </p>
                <p style='text-align: center; font-size: 1.2em;'>
                    <span style='color: #00b4d8'>Date:</span> 
                    <span style='color: #e2e2e2'>January 31 - February 1, 2025</span>
                </p>
            </div>
        """, unsafe_allow_html=True)