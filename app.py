import streamlit as st
import json
from urllib.request import urlopen, Request

st.set_page_config(page_title="Live AI Trading Assistant", page_icon="📈")

st.title("📈 Live AI Trading Assistant")
st.write("Welcome to your AI-powered trading dashboard!")

symbol = st.text_input("Enter a trading symbol", "BTCUSDT").upper().strip()

if st.button("Analyze"):
    if not symbol:
        st.error("Please enter a trading symbol.")
    else:
        try:
            url = f"https://api.binance.com/api/v3/ticker/24hr?symbol={symbol}"
            request = Request(url, headers={"User-Agent": "Mozilla/5.0"})

            with urlopen(request, timeout=10) as response:
                data = json.loads(response.read().decode())

            price = float(data["lastPrice"])
            change = float(data["priceChangePercent"])
            high = float(data["highPrice"])
            low = float(data["lowPrice"])
            volume = float(data["volume"])

            st.success(f"Live analysis for {symbol}")

            st.metric("Current Price", f"${price:,.4f}")
            st.metric("24h Change", f"{change:.2f}%")

            st.write(f"**24h High:** ${high:,.4f}")
            st.write(f"**24h Low:** ${low:,.4f}")
            st.write(f"**24h Volume:** {volume:,.2f}")

            if change > 2:
                st.success("📈 Market momentum is currently bullish.")
            elif change < -2:
                st.error("📉 Market momentum is currently bearish.")
            else:
                st.info("➡️ Market momentum is currently neutral.")

            st.warning(
                "Educational information only. This is not financial advice."
            )

        except Exception as e:
            st.error(f"Could not retrieve market data for {symbol}.")
            st.write(str(e))
