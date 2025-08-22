import streamlit as st
import os
import psycopg2
from dotenv import load_dotenv
import uuid

load_dotenv()

st.title("Savings Goal Tracker")
st.write("Welcome to your personal savings tracker!")

# User Registration Form
st.header("Create Account")

email = st.text_input("Email")
password = st.text_input("Password", type="password")
first_name = st.text_input("First Name")

if st.button("Register"):
    if email and password and first_name:
        st.success(f"Account created for {first_name}!")
        # TODO: Save to database
    else:
        st.error("Please fill in all fields")