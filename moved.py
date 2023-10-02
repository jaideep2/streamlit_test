import streamlit as st
st.set_page_config(page_title="Topic2Clip", page_icon="🍿", layout="centered", initial_sidebar_state="collapsed")
st.subheader("Thanks for using the service. The new service is hosted here")
st.link_button("Topic2Video Generator", "https://topic2video.streamlit.app", type="secondary")
st.caption("If you recieved a link to view a video here, you'll need to regenerate them through above link.")
st.stop()
