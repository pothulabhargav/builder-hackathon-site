import streamlit as st
import time

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
    # Add auto-refresh using time and st.rerun()
    if 'last_refresh' not in st.session_state:
        st.session_state.last_refresh = time.time()
    
    current_time = time.time()
    if current_time - st.session_state.last_refresh >= 5:
        st.session_state.last_refresh = current_time
        time.sleep(0.1)  # Small delay to prevent excessive CPU usage
        st.rerun()

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

        # Replace the async timer implementation with a simpler one
        from datetime import datetime
        import pytz

        # Set event times (IST timezone)
        ist = pytz.timezone('Asia/Kolkata')
        start_time = ist.localize(datetime(2025, 1, 31, 10, 30))
        end_time = ist.localize(datetime(2025, 2, 1, 15, 30))

        def format_time(time_delta):
            days = time_delta.days
            hours = time_delta.seconds // 3600
            minutes = (time_delta.seconds % 3600) // 60
            return f"{days}d {hours}h {minutes}m"

        now = datetime.now(ist)
        
        if now < start_time:
            time_to_start = start_time - now
            status = "Event Starts In"
            time_text = format_time(time_to_start)
        elif now > end_time:
            status = "Event Status"
            time_text = "Event Completed"
        else:
            time_to_end = end_time - now
            status = "Event Ends In"
            time_text = format_time(time_to_end)

        # Display timer using st.markdown
        st.markdown(f"""
            <style>
                .timer-container {{
                    background: linear-gradient(145deg, #2d2d44 0%, #1a1a2e 100%);
                    border: 1px solid #4d4d7d;
                    border-radius: 10px;
                    padding: 20px;
                    margin: 30px auto;
                    text-align: center;
                    max-width: 600px;
                    box-shadow: 0 4px 15px rgba(123, 44, 191, 0.15);
                    z-index: 100;
                    position: relative;
                }}
                .timer-heading {{
                    color: #00b4d8;
                    margin-bottom: 15px;
                    font-size: 1.2em;
                    font-weight: 500;
                }}
                .timer-value {{
                    color: #e2e2e2;
                    font-size: 2em;
                    font-weight: bold;
                    text-shadow: 0 2px 4px rgba(0,0,0,0.2);
                }}
            </style>
            <div class="timer-container">
                <div class="timer-heading">{status}</div>
                <div class="timer-value">{time_text}</div>
            </div>
        """, unsafe_allow_html=True)

        # Add refresh button next to timer with larger icon
        st.markdown("""
            <style>
                .refresh-button {
                    position: absolute;
                    right: 20px;
                    top: 50%;
                    transform: translateY(-50%);
                    font-size: 24px;
                }
            </style>
        """, unsafe_allow_html=True)
        
        # col1, col2 = st.columns([0.9, 0.1])
        # with col2:
        #     if st.button("↻", key="refresh_timer", help="Refresh timer"):
        #         st.rerun()
