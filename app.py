import streamlit as st
from scoring.tradfi_engine import score_tradfi
from scoring.defi_engine import score_defi

st.title("Buffett-Style Hybrid Scoring Engine")

option = st.selectbox("Choose Asset Type", ["S&P 500", "DeFi Protocol"])

if option == "S&P 500":
    ticker = st.text_input("Enter stock ticker (e.g. AAPL)")
    if st.button("Score"):
        result = score_tradfi(ticker)
        st.json(result)
else:
    protocol = st.selectbox("Choose Protocol", ["LINK", "AAVE", "UNI"])
    if st.button("Score"):
        result = score_defi(protocol)
        st.json(result)
