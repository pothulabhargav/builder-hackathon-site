import streamlit as st

# Define teams data directly in the component for now
# Later we can move this to a proper database or API
import yaml

with open('config/teams.yml', 'r') as f:
    teams_data = yaml.safe_load(f)

teams = []
for team in teams_data['teams']:
    # Load problem details from corresponding YAML file
    problem_file = f"config/problems/{team['problem_statement']}.yml"
    with open(problem_file, 'r') as f:
        problem_data = yaml.safe_load(f)
        
    teams.append({
        "name": team['name'],
        "members": team['members'],
        "problem": f'{problem_data["id"]} -  {problem_data["problem"]}'  # Get problem title from problem YAML file
    })

def render_teams():
    
    # Create rows with 2 teams per row
    for i in range(0, len(teams), 2):
        cols = st.columns(2)
        
        # Add teams to columns
        for j in range(2):
            if i + j < len(teams):
                team = teams[i + j]
                with cols[j]:
                    st.markdown(f"""
                        <div style="
                            background: linear-gradient(145deg, #2d2d44 0%, #1a1a2e 100%);
                            border: 1px solid #4d4d7d;
                            border-radius: 10px;
                            padding: 20px;
                            margin: 20px 0;
                            box-shadow: 0 4px 15px rgba(123, 44, 191, 0.15);
                            height: 100%;
                        ">
                            <h3 style="color: #9d4edd; margin-bottom: 10px;">{team['name']}</h3>
                            <p style="color: #00b4d8; font-size: 18px;"><strong>Problem Statement:</strong> {team['problem']}</p>
                            <p style="color: #e2e2e2; font-size: 16px;"><strong>Team Members:</strong></p>
                            <ul style="color: #e2e2e2; font-size: 16px;">
                                {''.join([f'<li>{member}</li>' for member in team['members']])}
                            </ul>
                        </div>
                    """, unsafe_allow_html=True)