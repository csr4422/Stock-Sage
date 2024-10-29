import streamlit as st
import pathlib 
from datetime import date
import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go 
# Nav bar

 #def load_css(file_path):
    #with open (file_path)as f:
       # st.html(f"<style>{f.read()}</style>")
#loading css
#css_path=pathlib.Path("demo/proto.css")
#load_css(css_path)
#prooject tab


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
        data = yf.download(ticker,START,TODAY)
        data.reset_index(inplace=True)
        return data

    data_load_state = st.text("Loading data ...")
    data_load_state.text("Loading data...Done!")
    data=load_data(selected_stocks)
    st.subheader('Raw data')
    st.write(data.tail())

    def plot_raw_data():
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=data['Date'],y=data['Open'],    name='stock_open',marker={'color':'white'}))
        fig.add_trace(go.Scatter(x=data['Date'],y=data['Close'],       name='stock_cLose',marker={'color':'red'}))
        fig.layout.update(title_text="Time Series Data",       xaxis_rangeslider_visible=True)
        st.plotly_chart(fig)

    plot_raw_data()
     
    

    df_train = data[['Date','Close']]
    df_train=df_train.rename(columns={"Date":"ds","Close":"y"})
    m =Prophet()
    m.fit(df_train)
    
    future=m.make_future_dataframe(periods=period)
    forecast=m.predict(future)
    
    st.subheader('Forecast data')
    st.write(forecast.tail())
    
    st.write(f'Forecast plot for {n_year} years')
    fig1 = plot_plotly(m, forecast)
    st.plotly_chart(fig1)

    st.write("Forecast components")
    fig2 = m.plot_components(forecast)
    st.write(fig2)
