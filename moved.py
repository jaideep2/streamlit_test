import streamlit as st
st.set_page_config(page_title="Topic2Clip", page_icon="🍿", layout="centered", initial_sidebar_state="collapsed")
# Set header
st.markdown(f"<h1 style='text-align: center;'>Topic<font color='#ff0000'>2</font>Video🍿Generator</h2><br>", unsafe_allow_html=True)
st.markdown(f"""<h4 style='text-align: center; font-style: italic;'>Thanks for using the service. The new generation service is hosted here: </h4><br>""", unsafe_allow_html=True)
st.link_button("Topic2Video Generator", "https://topic2video.streamlit.app", use_container_width=True)
st.image(f"""<h4 style='text-align: center; font-style: italic;'>If you recieved a link to view a video here, you'll need to regenerate them through above link.</h4><br>""")
st.stop()
