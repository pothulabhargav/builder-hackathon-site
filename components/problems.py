import streamlit as st
import yaml
import os
from pathlib import Path

def render_problems():
    # Get all problem YAML files from config/problems directory
    problems_dir = Path("config/problems")
    problem_files = sorted(problems_dir.glob("*.yml"))
    
    for file in problem_files:
        with open(file, 'r') as f:
            problem = yaml.safe_load(f)
            
        # Create expandable section for each problem
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
                    <p style="color: var(--text-primary); font-size: 16px; margin-bottom: 15px;">
                        <strong style="color: var(--ai-primary)">Theme:</strong> {problem['theme']}
                    </p>
                    <p style="color: var(--text-primary); font-size: 16px; margin-bottom: 15px;">
                        <strong style="color: var(--ai-primary)">Objective:</strong> {problem['objective']}
                    </p>
                    <p style="color: var(--text-primary); font-size: 16px; margin-bottom: 15px;">
                        <strong style="color: var(--ai-primary)">Description:</strong> {problem['description']}
                    </p>
                    <p style="color: var(--text-primary); font-size: 16px;">
                        <strong style="color: var(--ai-primary)">Target Users:</strong> {problem['target_users']}
                    </p>
                </div>
            """, unsafe_allow_html=True)