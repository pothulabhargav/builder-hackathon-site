import streamlit as st

def render_schedule():
    st.header("Event Schedule")
    
    # Create a schedule using streamlit components
    st.markdown("""
    ### Day 1 - Friday - Kickoff
    - 10:00 AM - Opening Ceremony
    - 10:15 AM - Access to Hackathon AWS Accounts and other resources
    - 10:30 AM - Hackathon Begins!
    - 1:00 PM - Lunch Break
    - 2:00 PM - Continued Building
    - 7:00 PM - Dinner Break
    
    ### Day 2 - Saturday - Final Day
    - 9:00 AM - Morning Check-in
    - 2:00 PM - Lunch
    - 3:00 PM - Code Freeze
    - 3:30 PM - Presentations Begin
    - 5:30 PM - Judging
    - 6:30 PM - Awards Ceremony
    """)