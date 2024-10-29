import streamlit as st



st.set_page_config(
    page_title="Stock sage",
    
    )

st.title("Welcome to Stock Sage !" )
st.header("Your Search ends here...")
st.markdown("StockSage makes stock market predictions easy, even for beginners. Using advanced algorithms and data analysis, our app provides clear, reliable stock forecasts without the confusing jargon. Whether you're a seasoned investor or just getting started, StockSage offers actionable insights to help you make informed decisions and grow your portfolio.")

st.header("How to use ?")
st.text("1. Select the 'predictor'navbar ")
st.text("2. Select the stock you want to predict")
st.text("3. Slide to the desired number of years and click on the load data")
st.markdown("Now you will see the stock data table and also the forcasted data for the selected stock for selected years ")
