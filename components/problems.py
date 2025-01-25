import streamlit as st
import yaml
import os
from pathlib import Path
from collections import defaultdict

def render_problems():
    # Get all problem YAML files from config/problems directory
    problems_dir = Path("config/problems")
    problem_files = sorted(problems_dir.glob("*.yml"))
    
    # Group problems by theme
    problems_by_theme = defaultdict(list)
    for file in problem_files:
        with open(file, 'r') as f:
            problem = yaml.safe_load(f)
            problems_by_theme[problem['theme']].append(problem)
    
    # Create two columns - themes on left, problems on right
    col1, col2 = st.columns([1, 3])
    
    # Track selected theme and whether any theme is clicked
    if 'selected_theme' not in st.session_state:
        st.session_state.selected_theme = None
        
    # Display theme selector on left
    with col1:
        st.markdown("""
            <h3 style="
                color: #9d4edd;
                margin: 20px 0;
                font-size: 20px;
            ">Themes</h3>
        """, unsafe_allow_html=True)
        
        for theme in problems_by_theme.keys():
            if st.button(theme, key=f"theme_{theme}",
                        use_container_width=True,
                        type="secondary",
                    ):
                st.session_state.selected_theme = theme
                
    # Display problems for selected theme on right only when a theme is selected
    with col2:
        if st.session_state.selected_theme:
            st.markdown("""
                <h3 style="
                    color: #9d4edd;
                    margin: 20px 0;
                    font-size: 20px;
                ">Problem Statements</h3>
            """, unsafe_allow_html=True)
            
            selected_problems = problems_by_theme[st.session_state.selected_theme]
            for problem in selected_problems:
                with st.expander(f"{problem['id']} - {problem['problem']}", expanded=False):
                    st.markdown(f"""
                        <div style="
                            background: linear-gradient(145deg, #2d2d44 0%, #1a1a2e 100%);
                            border: 1px solid #4d4d7d;
                            border-radius: 10px;
                            padding: 20px;
                            margin: 10px 0;
                            box-shadow: 0 4px 15px rgba(123, 44, 191, 0.15);
                        ">
                            <p style="color: #e2e2e2; font-size: 16px; margin-bottom: 15px;">
                                <strong style="color: #00b4d8">Objective:</strong> {problem['objective']}
                            </p>
                            <p style="color: #e2e2e2; font-size: 16px; margin-bottom: 15px;">
                                <strong style="color: #00b4d8">Description:</strong> {problem['description']}
                            </p>
                            <p style="color: #e2e2e2; font-size: 16px;">
                                <strong style="color: #00b4d8">Target Users:</strong> {problem['target_users']}
                            </p>
                        </div>
                    """, unsafe_allow_html=True)