import streamlit as st
import os
import psycopg2
from dotenv import load_dotenv
import uuid

load_dotenv()

# Page config and styling
st.set_page_config(page_title="Savings Goal Tracker", page_icon="🏠", layout="centered")

# Custom CSS for sage green theme
st.markdown("""
<style>
    .stApp {
        background-color: #FFF5E1;
    }
    .main .block-container {
        background-color: #FFF5E1;
    }
    .main-header {
        text-align: center;
        color: #8BA68B;
        font-size: 3rem;
        margin-bottom: 2rem;
    }
    .subtitle {
        text-align: center;
        color: #8BA68B;
        font-size: 1.2rem;
        margin-bottom: 3rem;
    }
    .stButton > button {
        background-color: #6B8E6B;
        color: white;
        border-radius: 10px;
        border: none;
        padding: 0.5rem 2rem;
        font-size: 1rem;
    }
    .stButton > button:hover {
        background-color: #5A7A5A;
    }
</style>
""", unsafe_allow_html=True)


# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = 'landing'

# Landing page
if st.session_state.page == 'landing':
    st.markdown('<h1 class="main-header">🏠 Savings Goal Tracker</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Turn your dreams into achievable goals</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Sign Up", key="signup_btn", use_container_width=True):
            st.session_state.page = 'signup'
            st.rerun()
        
        if st.button("Sign In", key="signin_btn", use_container_width=True):
            st.session_state.page = 'signin'
            st.rerun()