import streamlit as st

st.set_page_config(
    page_title="Edanur DOĞAN  Portfolyo", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

st.markdown("""
    <style>
        .block-container { padding-top: 2rem; padding-bottom: 2rem; max-width: 85%; }
        header { visibility: hidden; }
        footer { visibility: hidden; }
        h1 { text-align: center; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; font-weight: 600; margin-bottom: 2rem; }
        img { border-radius: 8px; box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1); }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1>Edanurdogan Portfolyo</h1>", unsafe_allow_html=True)

try:
    st.image("portfolyo.jpg", use_container_width=True)
except Exception:
    st.error("'portfolyo.jpg' dosyası dizinde bulunamadı. Lütfen github deponuzdaki dosya adının büyük/küçük harf uyumunu (örneğin Portfolyo.jpg veya portfolyo.JPG) kontrol edin.")
