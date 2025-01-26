import streamlit as st

# Event details
title = "Builder Hackathon"
venue = "3rd floor, HyperVerge Office, HSR"
date = "January 31 - February 1, 2025"

# Colors
primary_color = "#9d4edd"
secondary_color = "#00b4d8"
text_color = "#e2e2e2"

# Styling
glow_animation = """
    @keyframes glowPulse {
        0% { text-shadow: 0 0 10px rgba(157, 78, 221, 0.3); }
        50% { text-shadow: 0 0 20px rgba(157, 78, 221, 0.5); }
        100% { text-shadow: 0 0 10px rgba(157, 78, 221, 0.3); }
    }
"""

title_styles = {
    "text_align": "center",
    "font_size": "2.5em", 
    "margin_bottom": "30px",
    "letter_spacing": "2px",
    "color": primary_color
}

info_box_styles = {
    "background": "linear-gradient(145deg, rgba(45, 45, 68, 0.4), rgba(26, 26, 46, 0.4))",
    "border_radius": "10px",
    "padding": "20px",
    "box_shadow": f"0 4px 15px rgba(123, 44, 191, 0.15)"
}

button_styles = {
    "background": f"linear-gradient(90deg, {primary_color}, {secondary_color})",
    "color": "white",
    "padding": "10px 30px",
    "border": "none",
    "border_radius": "25px", 
    "font_size": "1.2em",
    "cursor": "pointer",
    "box_shadow": "0 4px 15px rgba(123, 44, 191, 0.2)",
    "transition": "all 0.3s ease"
}

def render_home():
    col1, col2, col3 = st.columns([1,2,1])
    
    with col2:
        # Add CSS styles
        st.markdown(f"""
            <style>
                {glow_animation}
                .hackathon-title {{
                    animation: glowPulse 2s infinite;
                    position: relative;
                    text-align: {title_styles['text_align']};
                    font-size: {title_styles['font_size']};
                    margin-bottom: {title_styles['margin_bottom']};
                    letter-spacing: {title_styles['letter_spacing']};
                    background: linear-gradient(90deg, {primary_color}, {secondary_color});
                    -webkit-background-clip: text;
                    -webkit-text-fill-color: transparent;
                }}
            </style>
        """, unsafe_allow_html=True)
        
        # Display title
        st.markdown(f'<h1 class="hackathon-title">{title}</h1>', unsafe_allow_html=True)
        
        # Display info box
        st.markdown(f"""
            <div style="background: {info_box_styles['background']}; 
                        border-radius: {info_box_styles['border_radius']}; 
                        padding: {info_box_styles['padding']};
                        box-shadow: {info_box_styles['box_shadow']};">
                <p style="text-align: center; font-size: 1.2em; margin-bottom: 15px;">
                    <span style="color: #00b4d8">Venue:</span> 
                    <span style="color: #e2e2e2">{venue}</span>
                </p>
                <p style="text-align: center; font-size: 1.2em;">
                    <span style="color: #00b4d8">Date:</span> 
                    <span style="color: #e2e2e2">{date}</span>
                </p>
            </div>
        """, unsafe_allow_html=True)

        google_form_url = "https://docs.google.com/forms/d/e/1FAIpQLSe916mxM_vVaWpjYO6gMq0ejk8WjgT8Ln4kiIWEtC96fIH4tA/viewform?usp=dialog"
        
        st.markdown(f"""
            <div style="text-align: center; margin-top: 30px;">
                <a href="{google_form_url}" target="_blank">
                    <button style="
                        background: {button_styles['background']};
                        color: {button_styles['color']};
                        padding: {button_styles['padding']};
                        border: {button_styles['border']};
                        border-radius: {button_styles['border_radius']};
                        font-size: {button_styles['font_size']};
                        cursor: {button_styles['cursor']};
                        box-shadow: {button_styles['box_shadow']};
                        transition: {button_styles['transition']};
                    ">
                        Register Now
                    </button>
                </a>
            </div>
        """, unsafe_allow_html=True)
