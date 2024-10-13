import streamlit as st

# Set page configuration
st.set_page_config(page_title="Nice App Hub", layout="wide")

# Background design using CSS
page_bg_css = """
<style>
body {
    background-color: #f0f4f8;
    background-image: linear-gradient(135deg, #f0f4f8 25%, #dfe4f2 25%, #dfe4f2 50%, #f0f4f8 50%, #f0f4f8 75%, #dfe4f2 75%, #dfe4f2 100%);
    background-size: 40px 40px;
    color: #2C3E50;
}

.tile {
    padding: 30px;
    margin: 20px;
    background-color: #fefefe;
    border: 1px solid #ddd;
    border-radius: 20px;
    box-shadow: 0px 8px 12px rgba(0, 0, 0, 0.2);
    text-align: center;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    height: 250px;  /* Increased tile height */
    position: relative;
    overflow: hidden;
    background-image: url('https://via.placeholder.com/600x300'); /* Placeholder image */
    background-size: cover;
    background-position: center;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #fff;
}

.tile:hover {
    transform: scale(1.05);
    box-shadow: 0px 12px 16px rgba(0, 0, 0, 0.3);
}

.tile a {
    text-decoration: none;
    color: #fff;
    font-weight: bold;
    font-size: 24px;
    text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.7);
}

</style>
"""

# Inject CSS into the page
st.markdown(page_bg_css, unsafe_allow_html=True)

st.title("Nice App Hub - Explore and Navigate Applications")

# Placeholder for storing application links (this will simulate backend input)
apps = [
    {"name": "InsightsBoard", "link": "https://insightsboard.streamlit.app/", "image": "https://raw.githubusercontent.com/gauravsd.jd@gmail.com/NSSGenAIapps/main/InsightsBoard.Png"},
    {"name": "Documentor", "link": "https://legalcontractsummarizer-camzhxynfvjxeq4evgt7vj.streamlit.app/", "image": "https://via.placeholder.com/600x300"},
    {"name": "App 3", "link": "https://example-app3.com", "image": "https://via.placeholder.com/600x300"},
    # Add more apps here as needed
]

# Display tiles for each application
if apps:
    st.subheader("Available Applications")
    
    cols = st.columns(2)  # Two large columns for the big tile layout
    for idx, app in enumerate(apps):
        with cols[idx % 2]:  # Ensure tiles fill into two columns
            st.markdown(
                f"""
                <div class='tile' style="background-image: url('{app['image']}');">
                    <a href="{app['link']}" target="_blank">
                        {app['name']}
                    </a>
                </div>
                """, 
                unsafe_allow_html=True
            )
