import streamlit as st

st.set_page_config(page_title="Crypto Sentiment Dashboard", page_icon="📈", layout="centered")

st.title("📈 Real-Time Crypto & Stock Sentiment Dashboard")
st.write("Analyze market mood and asset sentiment instantly.")

asset = st.selectbox("Select Asset", ["Bitcoin (BTC)", "Ethereum (ETH)", "TATA Motors", "Reliance"])
news_text = st.text_area("Paste Recent Market News or Tweets:")

if st.button("Analyze Sentiment"):
    if news_text:
        text_lower = news_text.lower()
        positive_words = ["bull", "surge", "profit", "high", "growth", "moon", "gain"]
        negative_words = ["bear", "crash", "loss", "down", "drop", "risk", "fall"]
        
        pos_count = sum(1 for word in positive_words if word in text_lower)
        neg_count = sum(1 for word in negative_words if word in text_lower)
        
        st.subheader("📊 Market Sentiment Result")
        if pos_count > neg_count:
            st.success(f"Sentiment: BULLISH / POSITIVE (Score: +{pos_count})")
        elif neg_count > pos_count:
            st.error(f"Sentiment: BEARISH / NEGATIVE (Score: -{neg_count})")
        else:
            st.info("Sentiment: NEUTRAL / SIDEWAYS")
    else:
        st.warning("Please enter market news to analyze.")
