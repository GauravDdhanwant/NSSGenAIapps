import streamlit as st

# Set page configuration
st.set_page_config(page_title="App Hub", layout="wide")

# Background design using CSS
page_bg_css = """
<style>
body {
    background-color: #f0f4f8;
    background-image: linear-gradient(135deg, #f0f4f8 25%, #dfe4ea 25%, #dfe4ea 50%, #f0f4f8 50%, #f0f4f8 75%, #dfe4ea 75%, #dfe4ea 100%);
    background-size: 28px 28px;
    color: #2C3E50;
}

.tile {
    padding: 15px;
    margin: 10px;
    background-color: #fefefe;
    border: 1px solid #eee;
    border-radius: 10px;
    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
    text-align: center;
    transition: transform 0.2s ease;
}

.tile:hover {
    transform: scale(1.05);
}

.tile a {
    text-decoration: none;
    color: #2980b9;
    font-weight: bold;
}

.upload-section {
    padding: 15px;
    margin: 15px 0;
    background-color: #FFFFFF;
    border-radius: 10px;
    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
}
</style>
"""

# Inject CSS into the page
st.markdown(page_bg_css, unsafe_allow_html=True)

st.title("App Hub - Host and Discover Applications")

# Container for link upload
with st.container():
    st.markdown("<div class='upload-section'>", unsafe_allow_html=True)
    st.subheader("Upload Application Link")
    
    # Form for link upload
    with st.form("link_form", clear_on_submit=True):
        app_name = st.text_input("Enter the Application Name")
        app_link = st.text_input("Enter the Application URL")
        submitted = st.form_submit_button("Add Application")

        if submitted and app_name and app_link:
            st.success(f"Added {app_name} successfully!")
    
    st.markdown("</div>", unsafe_allow_html=True)

# Placeholder for storing application links
if "apps" not in st.session_state:
    st.session_state.apps = []

# Add app to session state if submitted
if submitted and app_name and app_link:
    st.session_state.apps.append({"name": app_name, "link": app_link})

# Display tiles for each application
if st.session_state.apps:
    st.subheader("Available Applications")
    
    cols = st.columns(3)  # Adjust the number of columns for tile layout
    for idx, app in enumerate(st.session_state.apps):
        with cols[idx % 3]:  # Ensure tiles fill into columns
            st.markdown(
                f"""
                <div class='tile'>
                    <a href="{app['link']}" target="_blank">
                        {app['name']}
                    </a>
                </div>
                """, 
                unsafe_allow_html=True
            )
