import streamlit as st
import base64

# Set page configuration
st.set_page_config(page_title="Nice App Hub", layout="wide")

# Function to encode the image to base64
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Function to set the background image
def set_bg_hack(main_bg):
    '''
    A function to unpack an image from root folder and set as bg.
    '''
    bin_str = get_base64_of_bin_file(main_bg)
    page_bg_img = '''
    <style>
    .stApp {
        background-image: url("data:image/png;base64,%s");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-position: center center;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

# Set the background image
set_bg_hack('Icon/background_UI.png')

# Display company logo in the header
logo = get_base64_of_bin_file('Icon/Nice_logo.png')
st.markdown(f'<img src="data:image/png;base64,{logo}" style="width: 150px; margin-left: 0; margin-right: auto; display: block;"/>', unsafe_allow_html=True)

# Rest of your existing CSS (for tiles, etc.)
page_bg_css = """
<style>
body {
    color: #2C3E50;
}

.tile {
    padding: 30px;
    margin: 20px;
    background-size: cover; /* Ensure the background image covers the tile */
    background-repeat: no-repeat; /* Prevent the background from repeating */
    background-attachment: fixed; /* Keep the background fixed */
    background-position: center; /* Center the background image */
    border: 1px solid #ddd;
    border-radius: 20px;
    box-shadow: 0px 8px 12px rgba(0, 0, 0, 0.2);
    text-align: center;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    height: 250px;
    position: relative;
    overflow: hidden;
    display: flex;
    flex-direction: row; /* Change to row layout for two columns */
    align-items: center; /* Center items horizontally */
    justify-content: flex-start; /* Center items vertically */
    color: #fff;
}

.tile img {
    width: 50px; /* Set a fixed width for the icon */
    height: auto; /* Maintain aspect ratio */
    margin-bottom: 10px; /* Space between icon and app name */
    margin-left: auto; /* Center icon in the first column */
    margin-right: auto; /* Center icon in the first column */
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

st.markdown('<h1 style="color: white; margin-left: 0; margin-right: auto; display: block;">Nice App Hub - Explore and Navigate Applications</h1>', unsafe_allow_html=True)

# Placeholder for storing application links (this will simulate backend input)
apps = [
    {"name": "InsightsBoard", "link": "https://insightsboard.streamlit.app/", "image": "Icon/InsightsBoard_Icons.png", "bg_image": "Icon/KPI_bg.png", "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."},
    {"name": "Documentor", "link": "https://legalcontractsummarizer-camzhxynfvjxeq4evgt7vj.streamlit.app/", "image": "Icon/Documentor_Icon.png", "bg_image": "Icon/KPI_bg.png", "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."},
    {"name": "App 3", "link": "https://example-app3.com", "image": "Icon/KPI_bg.png", "bg_image": "Icon/KPI_bg.png", "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."},
    # Add more apps here as needed
]

# Display tiles for each application
if apps:
    st.markdown('<h3 style="color: white; margin-left: 0; margin-right: auto; display: block;">Available Applications</h3>', unsafe_allow_html=True)
    st.markdown('<p style="color: white; margin-left: 0; margin-right: auto; display: block;">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>', unsafe_allow_html=True)
    
    cols = st.columns(2)  # Two large columns for the big tile layout
    for idx, app in enumerate(apps):
        with cols[idx % 2]:  # Ensure tiles fill into two columns
            icon_base64 = get_base64_of_bin_file(app['image'])
            bg_base64 = get_base64_of_bin_file(app['bg_image'])
            st.markdown(
                f"""
                <div class='tile' style="background-image: url('data:image/png;base64,{bg_base64}');">
                <a href="{app['link']}" target="_blank" style="text-decoration: none; color: #fff; font-weight: bold; font-size: 24px; text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.7);">
                    <div style="display: flex; flex-direction: row; justify-content: flex-start; width: 80%; height: 50%;">
                        <div style="width: 20%; display: flex; justify-content: center; align-items: center; margin-left: 20px; margin-right: 50px; margin-top: 90px;">
                            <img src="data:image/png;base64,{icon_base64}" alt="{app['name']} icon" style="width: 100%; height: auto;"/>
                        </div>
                        <div style="width: 80%; display: flex; flex-direction: column; justify-content: center; align-items: center;"> <!-- Changed justify-content to center to center the h2 element -->
                            <h2 style="color: #fff; font-weight: bold; font-size: 24px; text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.7); text-align: center; margin-top: 0px; margin-bottom: 10px;">{app['name']}</h2>
                            <p style="color: #fff; width:100%; text-align: left;">{app['description']}</p>
                        </div>
                    </div>
                </a>
                </div>
                """, 
                unsafe_allow_html=True
            )