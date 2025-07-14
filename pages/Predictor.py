import streamlit as st
import pathlib 
from datetime import date
import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go 
import pandas as pd
import numpy as np


#initiating dates
START ="2019-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

st.title ("Stock Predictor")

stocks = ("AAPL","GOOG","MSFT","TSLA","TATAMOTORS.NS","ASIANPAINT.NS","IRFC.NS","UNIONBANK.NS")
selected_stocks = st.selectbox("Select dataset for prediction", stocks)

n_year =st.slider("Years of prediction:",1,4)
period = n_year *365

#load button 
load_button=st.button("load data")
if load_button:
    @st.cache_data
    def load_data(ticker):
        # Fix: Add auto_adjust=False to maintain consistent behavior
        data = yf.download(ticker, START, TODAY, auto_adjust=False)
        data.reset_index(inplace=True)
        
        # Handle MultiIndex columns if they exist
        if isinstance(data.columns, pd.MultiIndex):
            data.columns = data.columns.droplevel(1)
        
        return data

    data_load_state = st.text("Loading data ...")
    data = load_data(selected_stocks)
    data_load_state.text("Loading data...Done!")
    
    # Check if data is empty
    if data.empty:
        st.error("No data found for the selected stock. Please try a different stock.")
        st.stop()
    
  #  st.write("Data columns:", data.columns.tolist())
    st.write("Data shape:", data.shape)
    
    st.subheader('Raw data')
    st.write(data.tail())

    def plot_raw_data():
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=data['Date'],y=data['Open'], name='stock_open',marker={'color':'white'}))
        fig.add_trace(go.Scatter(x=data['Date'],y=data['Close'], name='stock_close',marker={'color':'red'}))
        fig.layout.update(title_text="Time Series Data", xaxis_rangeslider_visible=True)
        st.plotly_chart(fig)

    plot_raw_data()
     
    # Prepare data for Prophet
    df_train = data[['Date','Close']].copy()
    
    # Clean the data
    df_train = df_train.dropna()  # Remove any NaN values
    
    df_train['Date'] = pd.to_datetime(df_train['Date'])
    
    if df_train['Close'].dtype == 'object':
        df_train['Close'] = pd.to_numeric(df_train['Close'], errors='coerce')
    else:
        df_train['Close'] = df_train['Close'].astype(float)
    
    df_train = df_train.dropna()
    df_train = df_train[df_train['Close'] > 0]
    
    df_train = df_train.reset_index(drop=True)
    
    df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})
    
    #st.write("Data shape:", df_train.shape)
    st.write("Data types:")
    st.write(df_train.dtypes)
    st.write("Sample data:")
    st.write(df_train.head())
    
    if len(df_train) < 2:
        st.error("Not enough data points for forecasting. Please select a different stock or date range.")
        st.stop()
    
    try:
        # Create and fit Prophet model
        m = Prophet(
            daily_seasonality=False,  # Disable daily seasonality for stock data
            weekly_seasonality=True,
            yearly_seasonality=True
        )
        
        # Additional debugging
        st.write("Training Prophet model...")
        st.write(f"Training data shape: {df_train.shape}")
        st.write(f"Date range: {df_train['ds'].min()} to {df_train['ds'].max()}")
        
        m.fit(df_train)
        
        future = m.make_future_dataframe(periods=period)
        
        st.write("Making predictions...")
        forecast = m.predict(future)
        
        st.subheader('Forecast data')
        st.write(forecast.tail())
        
        st.write(f'Forecast plot for {n_year} years')
        fig1 = plot_plotly(m, forecast)
        st.plotly_chart(fig1)

        st.write("Forecast components")
        fig2 = m.plot_components(forecast)
        st.write(fig2)
        
    except Exception as e:
        st.error(f"Error in forecasting: {str(e)}")
        st.write("This might be due to insufficient data or data quality issues.")
        st.write("Try selecting a different stock or reducing the prediction period.")
        
        st.write("Debug info:")
        st.write(f"df_train columns: {list(df_train.columns)}")
        st.write(f"df_train shape: {df_train.shape}")
        st.write(f"df_train dtypes: {df_train.dtypes}")
        st.write("First few rows:")
        st.write(df_train.head())
        
        # Show the full error traceback
        import traceback
        st.code(traceback.format_exc())