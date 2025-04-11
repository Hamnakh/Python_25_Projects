import streamlit as st
import random

# Set page config and custom CSS
st.set_page_config(page_title="AI Number Guessing Game")

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        background-color: #2C3E50;  /* Darker blue background */
        color: #ECF0F1;  /* Light gray text */
    }
    .stButton>button {
        width: 100%;
        background-color: #E74C3C;  /* Red buttons */
        color: white;
        padding: 15px;
        border-radius: 10px;
        border: none;
        margin: 5px 0;
    }
    .big-number {
        font-size: 72px;
        text-align: center;
        color: #F1C40F;  /* Yellow number */
        margin: 20px 0;
    }
    .attempt-text {
        text-align: center;
        color: #BDC3C7;  /* Lighter gray */
        font-size: 20px;
    }
    .title {
        background: linear-gradient(45deg, #E74C3C, #F1C40F);  /* Red to yellow gradient */
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 40px;
        text-align: center;
        padding: 20px 0;
    }
    </style>
    """, unsafe_allow_html=True)

# Initialize session state
if 'number' not in st.session_state:
    st.session_state.number = random.randint(1, 10)
if 'attempts' not in st.session_state:
    st.session_state.attempts = 0
if 'game_over' not in st.session_state:
    st.session_state.game_over = False

# Title
st.markdown("<h1 class='title'>🎮 Number Guessing Challenge</h1>", unsafe_allow_html=True)

# Main game container
with st.container():
    st.markdown("<p style='text-align: center; font-size: 24px;'>I'm thinking of a number from 1 to 10. Can you guess it? 🤔</p>", unsafe_allow_html=True)
    
    # Display user guess
    if 'guess' in st.session_state:
        st.markdown(f"<div class='big-number'>{st.session_state.guess}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='attempt-text'>Try #{st.session_state.attempts}</div>", unsafe_allow_html=True)

    # Game logic
    if not st.session_state.game_over:
        guess = st.number_input("Type your guess here:", min_value=1, max_value=10, step=1)
        if st.button("Make a Guess!"):
            st.session_state.attempts += 1
            st.session_state.guess = guess
            
            if guess == st.session_state.number:
                st.success("🎉 Fantastic! You got it right! 🎉")
                st.session_state.game_over = True
            else:
                st.error("Not quite right! Give it another shot!")
                hint = "bigger" if guess < st.session_state.number else "smaller"
                st.info(f"💡 Hint: Try a {hint} number")

    # Try Again button
    if st.session_state.game_over:
        if st.button("Try Again"):
            st.session_state.number = random.randint(1, 10)
            st.session_state.attempts = 0
            st.session_state.game_over = False
            st.session_state.pop('guess', None)
            st.experimental_rerun()
