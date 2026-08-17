import streamlit as st

st.set_page_config(page_title="Live AI Trading Assistant")

st.title("📈 Live AI Trading Assistant")

st.write("Welcome to your AI-powered trading dashboard!")

symbol = st.text_input("Enter a trading symbol", "BTCUSDT")

if st.button("Analyze"):
    st.success(f"Analysis for {symbol} will appear here.")
