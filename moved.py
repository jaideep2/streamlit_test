import streamlit as st
st.set_page_config(page_title="Topic2Clip", page_icon="🍿", layout="centered", initial_sidebar_state="collapsed")
# Set page padding to minimal and button css https://www.freecodecamp.org/news/css-button-style-hover-color-and-background/
st.markdown("""
    <style>
        .appview-container .main .block-container {{
            padding-top: {padding_top}rem;
            padding-bottom: {padding_bottom}rem;
        }}
        div[data-testid="stFormSubmitButton"] > button, div[data-testid="stDownloadButton"] > button {{
            border-color: rgb({red}, {green}, {blue});
            color: rgb({red}, {green}, {blue});
        }}
        div[data-testid="stFormSubmitButton"] > button:hover, div[data-testid="stDownloadButton"] > button:hover {{
            border-color: rgb({red}, {green}, {blue});
            color: rgb({red}, {green}, {blue});
        }}
        div[data-testid="stFormSubmitButton"] > button:active, div[data-testid="stDownloadButton"] > button:active {{
            border-color: rgb({red}, {green}, {blue});
            color: rgb(255, 255, 255);
            background-color: rgb({red}, {green}, {blue});
        }}
        div[data-testid="stFormSubmitButton"] > button:focus, div[data-testid="stDownloadButton"] > button:focus {{
            border-color: rgb({red}, {green}, {blue});
            color: rgb({red}, {green}, {blue});
        }}
        div[data-testid="stFormSubmitButton"] > button:focus:not(:active), div[data-testid="stDownloadButton"] > button:focus:not(:active) {{
            border-color: rgb({red}, {green}, {blue});
            color: rgb({red}, {green}, {blue});
        }}
        div[data-testid="stFormSubmitButton"] > button:focus-visible, div[data-testid="stDownloadButton"] > button:focus-visible {{
            box-shadow: rgba(255, 255, 255, 0.5) 0px 0px 0px 0.2rem;
        }}
        button[title="View fullscreen"] {{
            visibility: hidden;
        }}
        div[data-testid="stImage"] {{
            text-align: center;
            display: block;
            margin-left: auto;
            margin-right: auto;
        }}
        .stProgress > div > div > div > div {{
            background-image: linear-gradient(to right, #C10505, yellow, #15FF0D);
        }}
    </style>
    """.format(
        padding_top=2, padding_bottom=2, red=21, green=130, blue=55
    ),
    unsafe_allow_html=True,
)

# Set header
st.markdown(f"<h1 style='text-align: center;'>Topic<font color='#ff0000'>2</font>Video🍿Generator</h2><br>", unsafe_allow_html=True)
st.markdown(f"""<h4 style='text-align: center; font-style: italic;'>Thanks for using the service. The new generation service is hosted here: </h4><br>""", unsafe_allow_html=True)
st.link_button("Topic2Video Generator", "https://topic2video.streamlit.app", use_container_width=True)
st.image(f"""<h4 style='text-align: center; font-style: italic;'>If you recieved a link to view a video here, you'll need to regenerate them through above link.</h4><br>""")
st.stop()
