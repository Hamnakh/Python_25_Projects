import streamlit as st
import random

# Set page config (MUST be the first Streamlit command)
st.set_page_config(
    page_title="Fun Mad Libs Generator 🎭",
    page_icon="📖",
    layout="centered"
)

# Custom CSS for styling
st.markdown("""
    <style>
    .title-text {
        color: #FF5733;
        text-align: center;
        font-size: 36px;
        font-weight: bold;
    }
    .subtitle-text {
        color: #2980B9;
        text-align: center;
        font-size: 20px;
    }
    .story-output {
        background-color: #FDEDEC;
        padding: 20px;
        border-radius: 10px;
        border: 2px solid #E74C3C;
        font-size: 18px;
        color: #2C3E50;
    }
    .error-text {
        color: #E74C3C;
        font-weight: bold;
    }
    .success-text {
        color: #27AE60;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Add title and description with custom styling
st.markdown("<h1 class='title-text'>🎭 Fun Mad Libs Story Generator 📖</h1>", unsafe_allow_html=True)
st.markdown("<h3 class='subtitle-text'>Create a unique and fun-filled story using your own words!</h3>", unsafe_allow_html=True)

# Input fields
noun = st.text_input("Enter a noun", placeholder="e.g., dragon 🐉")
adjective = st.text_input("Enter an adjective", placeholder="e.g., gigantic 🌟")
verb = st.text_input("Enter a verb", placeholder="e.g., dances 💃")

# Story type selection
story_type = st.radio(
    "How would you like your story to be generated?",
    ["AI-Powered Story 🤖", "Logic-Based Story 🎭"]
)

# Basic story templates for logic-based generation
story_templates = [
    "The {adj} {noun} {verb} through the enchanted forest.",
    "Once upon a time, a {adj} {noun} {verb} under the starry sky.",
    "In a mystical land, the {adj} {noun} {verb} with great joy!",
    "The entire town was amazed as the {adj} {noun} {verb} like never before!"
]

def generate_logic_story(noun, adj, verb):
    template = random.choice(story_templates)
    return template.format(noun=noun, adj=adj, verb=verb)

def generate_ai_story(noun, adj, verb):
    client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])  # Ensure API key is set in Streamlit secrets
    prompt = f"Write a short, fun, and engaging story using these words: noun='{noun}', adjective='{adj}', verb='{verb}'. Keep it light-hearted and playful."
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=100
    )
    return response.choices[0].message.content

# Generate button
if st.button("Create My Story! ✨", type="primary"):
    if not all([noun, adjective, verb]):
        st.markdown("<p class='error-text'>🚨 Oops! Please fill in all fields to generate your story.</p>", unsafe_allow_html=True)
    else:
        try:
            if story_type == "AI-Powered Story 🤖":
                story = generate_ai_story(noun, adjective, verb)
            else:
                story = generate_logic_story(noun, adjective, verb)
            
            st.markdown("<p class='success-text'>🎉 Your magical story is ready!</p>", unsafe_allow_html=True)
            st.markdown(f"<div class='story-output'>{story}</div>", unsafe_allow_html=True)
        except Exception as e:
            st.markdown(f"<p class='error-text'>❌ Oops! Something went wrong. Please try again later.</p>", unsafe_allow_html=True)
