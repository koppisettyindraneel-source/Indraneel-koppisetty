import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="BoardGame Buddy",
    page_icon="🎲",
    layout="wide"
)

# Title
st.title("🎲 BoardGame Buddy")
st.subheader("Learn Board Games Through Easy Video Tutorials")

# Sidebar
st.sidebar.title("Navigation")
page = st.sidebar.selectbox(
    "Choose a Section",
    ["Home", "Game Library", "About"]
)

# Sample Game Data
games = {
    "Chess": {
        "description": "Learn the basics of Chess.",
        "video": "https://www.youtube.com/watch?v=OCSbzArwB10"
    },
    "Monopoly": {
        "description": "Learn how to play Monopoly.",
        "video": "https://www.youtube.com/watch?v=GQ1vWJYh8do"
    },
    "Catan": {
        "description": "Learn Settlers of Catan.",
        "video": "https://www.youtube.com/watch?v=oiQ6SgBzfqY"
    }
}

# Home Page
if page == "Home":
    st.header("Welcome to BoardGame Buddy")
    st.write("""
    Children often find board game rulebooks confusing.
    BoardGame Buddy helps players learn games quickly through
    simple video tutorials.
    """)

    search = st.text_input("🔍 Search a Board Game")

    if search:
        found = False
        for game, details in games.items():
            if search.lower() in game.lower():
                st.success(f"Found: {game}")
                st.write(details["description"])
                st.video(details["video"])
                found = True

        if not found:
            st.error("Game not found.")

# Game Library
elif page == "Game Library":
    st.header("📚 Game Library")

    selected_game = st.selectbox(
        "Select a Game",
        list(games.keys())
    )

    st.subheader(selected_game)
    st.write(games[selected_game]["description"])
    st.video(games[selected_game]["video"])

# About
elif page == "About":
    st.header("About the Project")
    st.write("""
    **BoardGame Buddy** is an EdTech and Gaming application
    designed to help children, parents, teachers, and casual
    players understand board game rules through official video
    tutorials.

    ### Main Goal
    Help users learn board games quickly and correctly without
    reading complicated rulebooks.
    """)

# Footer
st.markdown("---")
st.caption("© 2026 BoardGame Buddy")
