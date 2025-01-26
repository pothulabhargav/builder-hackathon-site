# Import required libraries
import streamlit as st
from components.home import render_home
from components.problems import render_problems
from components.teams import render_teams
from components.schedule import render_schedule
from components.gallery import render_gallery

# Configure page settings
st.set_page_config(page_title="Builder Hackathon", layout="wide")

def load_css():
    # Load all CSS files in the correct order
    css_files = [
        'styles/fonts.css',
        'styles/main.css',
        'styles/custom.css'
    ]
    for css_file in css_files:
        with open(css_file) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def main():
    load_css()
    
    # Initialize session state for page if not exists
    if 'page' not in st.session_state:
        st.session_state.page = 'home'
    
    # Add logo/home link
    st.markdown("""
        <div class="home-link-container">
            <span class="home-link">Builder Hackathon</span>
        </div>
        """, unsafe_allow_html=True)

    # Create tabs
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Home", "Problem Statements", "Teams", "Schedule", "Gallery"])
    
    with tab1:
        render_home()
    
    with tab2:
        render_problems()
        
    with tab3:
        render_teams()
        
    with tab4:
        render_schedule()
        
    with tab5:
        render_gallery()

if __name__ == "__main__":
    main()