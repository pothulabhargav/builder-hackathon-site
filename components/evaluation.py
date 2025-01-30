import streamlit as st
import yaml
from pathlib import Path

def render_evaluation():
    # Read evaluation criteria from config file
    evaluation_path = Path("config/evaluation.yml")
    with open(evaluation_path, 'r') as f:
        config = yaml.safe_load(f)
    
    # Title
    st.markdown("""
        <h3 style="
            color: var(--ai-primary);
            margin: 20px 0;
            font-size: 20px;
        ">Evaluation Criteria</h3>
    """, unsafe_allow_html=True)
    
    # Display each criterion
    for criterion in config['criteria']:
        with st.expander(criterion['name'], expanded=False):
            st.markdown(f"""
                <div style="
                    background: linear-gradient(145deg, var(--darker-bg) 0%, var(--dark-bg) 100%);
                    border: 1px solid var(--border-primary);
                    border-radius: 10px;
                    padding: 20px;
                    margin: 10px 0;
                    box-shadow: 0 4px 15px rgba(123, 44, 191, 0.15);
                ">
                    <p style="color: var(--text-primary); font-size: 16px; margin-bottom: 15px;">
                        <strong style="color: var(--ai-tertiary)">Description:</strong> {criterion['description']}
                    </p>
                    <div style="color: var(--text-primary); font-size: 16px;">
                        <strong style="color: var(--ai-tertiary)">Key Questions:</strong>
                        <ul style="list-style-type: none; padding-left: 0; margin-top: 10px;">
                            {"".join(f'<li style="margin-bottom: 10px;">• {q}</li>' for q in criterion['key_questions'])}
                        </ul>
                    </div>
                </div>
            """, unsafe_allow_html=True)
    
    def render_note(title, content):
        st.markdown(f"""
            <div style="
                margin-top: 30px;
                padding: 20px;
                background: linear-gradient(145deg, var(--darker-bg) 0%, var(--dark-bg) 100%);
                border: 1px solid var(--border-primary);
                border-radius: 10px;
                box-shadow: 0 4px 15px rgba(123, 44, 191, 0.15);
            ">
                <p style="
                    color: var(--text-primary);
                    font-size: 16px;
                    margin: 0;
                ">
                    <strong style="color: var(--ai-tertiary)">{title}:</strong> {content}
                </p>
            </div>
        """, unsafe_allow_html=True)


    # Footer notes
    with st.expander("Additional Notes", expanded=False):
        render_note("Evaluation Process",
            "Each evaluation criterion will be weighted differently based on the unique challenges and complexity of the specific problem statement.")
        
        render_note("Presentation",
            "A clear and engaging presentation of your solution will earn additional points. This includes effectively communicating the problem statement, solution design, approach, and implementation plan.")