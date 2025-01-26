import streamlit as st


slack_channel_link = "https://app.slack.com/client/T04CAHQGR/C08A4QA1CJZ"


def render_resources():
    
    with st.expander("Learning Resources", expanded=False):
        # Main content/documentation
        st.components.v1.iframe(
            "https://docs.google.com/document/d/1zY5AJZ6xjBJ4mPEYRTeU_HDy59ymTyMO-ch-Rz6Tqnw/edit?tab=t.0#heading=h.31kwpt1oagm3",
            height=600
        )

    with st.expander("Knowledge Sharing Session Recordings", expanded=False):
        # Knowledge Sharing Session Recordings
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("[Video 1: prototyping with LLMs - CaseStudy with Sensai](https://drive.google.com/file/d/1-2_BU3M_syAL_xP13rSkRkslnQXQtGpS/view)")
            # st.markdown("[Watch Video 1](https://drive.google.com/file/d/1-2_BU3M_syAL_xP13rSkRkslnQXQtGpS/view)")
            st.markdown("Use LLMs, Cursor, Streamlit etc to hyper accelerate development, solve problems with advanced application of LLMs - Multi-modality, RAG etc. Prototyping mindset and other learnings")
        
        with col2:
            st.markdown('[Video 2: Making RAG work in production](https://drive.google.com/file/d/1Ta1NdmHWzR_HDM0B5ukPcYVAhitweGZo/view)')
            # st.markdown("[Watch Video 2](https://drive.google.com/file/d/1Ta1NdmHWzR_HDM0B5ukPcYVAhitweGZo/view)")
            st.markdown("Initial approach, drawbacks of that approach, the intuition behind pivoting to RAG, the lessons learnt and design patterns uncovered over the last 20 months of iterating.")


    st.markdown("---")
    st.markdown(f"""
        <div style='margin-top: 20px;'>
            <p>Join this Slack channel <a href='{slack_channel_link}' target='_blank'>#builder-hackathon-2025</a> to connect with other participants, ask questions, and share your ideas!</p>
        </div>
    """, unsafe_allow_html=True)