import streamlit as st
from config.app_config import PRIMARY_COLOR

def show_footer(in_sidebar=False):
    base_styles = f"""
        text-align: center;
        padding: 1rem;
        background: transparent;
        margin-top: {'0' if in_sidebar else '2rem'};
        {'width: 100%' if not in_sidebar else ''};
    """
    
    st.markdown(
        f"""
        <div style='{base_styles}'>
            <p style='
                font-family: "Source Sans Pro", sans-serif;
                color: #64B5F6;
                font-size: 0.8rem;
                margin: 0;
                opacity: 0.7;
            '>
                © {st.session_state.get('app_year', 2026)} Health Insights Agent
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
