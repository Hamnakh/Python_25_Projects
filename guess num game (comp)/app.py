import streamlit as st
import random

# -------------------- Page Configuration --------------------
st.set_page_config(page_title="🎯 Number Guessing Game", layout="centered")

# -------------------- Custom CSS Styling --------------------
st.markdown("""
    <style>
        .stApp {
            background-color: #f9f9f9;
            font-family: 'Segoe UI', sans-serif;
        }
        .title {
            text-align: center;
            font-size: 36px;
            font-weight: bold;
            margin-bottom: 20px;
            color: #333;
        }
        .stRadio > label {
            font-size: 18px;
        }
        .stNumberInput > label, .stTextInput > label {
            font-weight: 500;
            color: #444;
        }
        .stButton > button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            border-radius: 8px;
            border: none;
            font-size: 16px;
        }
        .stButton > button:hover {
            background-color: #45a049;
        }
    </style>
""", unsafe_allow_html=True)

# -------------------- Initialize Session State --------------------
def init_session():
    if 'game_mode' not in st.session_state:
        st.session_state.game_mode = "You Guess the Number"
    if 'target' not in st.session_state:
        st.session_state.target = random.randint(1, 100)
    if 'range_limit' not in st.session_state:
        st.session_state.range_limit = 100
    if 'attempts' not in st.session_state:
        st.session_state.attempts = 0
    if 'message' not in st.session_state:
        st.session_state.message = ""

init_session()

# -------------------- Title --------------------
st.markdown("<div class='title'>🎮 Number Guessing Game</div>", unsafe_allow_html=True)

# -------------------- Mode Selection --------------------
st.session_state.game_mode = st.radio(
    "Select a Game Mode:",
    ["You Guess the Number", "Computer Guesses Your Number"],
    index=0
)

# -------------------- Game 1: You Guess the Number --------------------
def user_guesses():
    range_limit = st.number_input(
        "Select the range (1 to X):",
        min_value=10, max_value=1000, value=100, step=10
    )

    # Reset game if range changes
    if range_limit != st.session_state.range_limit:
        st.session_state.range_limit = range_limit
        st.session_state.target = random.randint(1, range_limit)
        st.session_state.attempts = 0
        st.session_state.message = ""

    user_guess = st.number_input(
        "Enter your guess:",
        min_value=1,
        max_value=st.session_state.range_limit,
        step=1,
        key="user_guess"
    )

    if st.button("Submit Guess"):
        st.session_state.attempts += 1
        if user_guess == st.session_state.target:
            st.success(f"🎉 Correct! You guessed it in {st.session_state.attempts} attempts.")
            st.balloons()
        elif user_guess < st.session_state.target:
            st.session_state.message = "🔼 Try a higher number!"
        else:
            st.session_state.message = "🔽 Try a lower number!"

        if user_guess != st.session_state.target:
            st.info(st.session_state.message)

    if st.button("🔁 Restart Game"):
        st.session_state.target = random.randint(1, st.session_state.range_limit)
        st.session_state.attempts = 0
        st.session_state.message = ""
        st.rerun()

# -------------------- Game 2: Computer Guesses Your Number (Placeholder) --------------------
def computer_guesses():
    st.warning("🚧 This mode is under construction. Coming soon!")

# -------------------- Run Selected Mode --------------------
if st.session_state.game_mode == "You Guess the Number":
    user_guesses()
else:
    computer_guesses()
