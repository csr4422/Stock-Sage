import streamlit as st
import pathlib
from datetime import date

# Page configuration
st.set_page_config(
    page_title="Stock Predictor - Home",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
.main-header {
    text-align: center;
    color: #1f77b4;
    margin-bottom: 2rem;
}

.feature-card {
    background-color: #f8f9fa;
    padding: 1.5rem;
    border-radius: 10px;
    margin: 1rem 0;
    border-left: 4px solid #1f77b4;
}

.step-card {
    background-color: #e8f4f8;
    padding: 1rem;
    border-radius: 8px;
    margin: 0.5rem 0;
}

.disclaimer-box {
    background-color: #fff3cd;
    border: 1px solid #ffeaa7;
    border-radius: 8px;
    padding: 1rem;
    margin: 1rem 0;
}

.cta-button {
    background-color: #1f77b4;
    color: white;
    padding: 0.75rem 2rem;
    border: none;
    border-radius: 8px;
    font-size: 1.1rem;
    font-weight: bold;
    cursor: pointer;
    margin: 1rem 0;
}

.stats-container {
    display: flex;
    justify-content: space-around;
    margin: 2rem 0;
}

.stat-item {
    text-align: center;
    padding: 1rem;
}

.stat-number {
    font-size: 2rem;
    font-weight: bold;
    color: #1f77b4;
}

.stat-label {
    font-size: 0.9rem;
    color: #666;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="main-header">📈 Welcome to Stock Predictor</h1>', unsafe_allow_html=True)

# Hero section
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("""
    <div style="text-align: center; padding: 2rem;">
        <h2>Predict Future Stock Prices with Advanced Machine Learning</h2>
        <p style="font-size: 1.2rem; color: #666; margin-bottom: 2rem;">
            Stock Predictor uses Facebook's Prophet forecasting model to predict future stock prices. 
            Get insights into potential market movements and make informed investment decisions.
        </p>
    </div>
    """, unsafe_allow_html=True)

# Quick stats
st.markdown("""
<div class="stats-container">
    <div class="stat-item">
        <div class="stat-number">8+</div>
        <div class="stat-label">Supported Stocks</div>
    </div>
    <div class="stat-item">
        <div class="stat-number">4</div>
        <div class="stat-label">Years Prediction</div>
    </div>
    <div class="stat-item">
        <div class="stat-number">6+</div>
        <div class="stat-label">Years Historical Data</div>
    </div>
    <div class="stat-item">
        <div class="stat-number">24/7</div>
        <div class="stat-label">Real-time Updates</div>
    </div>
</div>
""", unsafe_allow_html=True)

# Features section
st.markdown("## 🚀 Key Features")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="feature-card">
        <h3>📊 Real-Time Data Analysis</h3>
        <ul>
            <li>Live stock data from Yahoo Finance</li>
            <li>Historical price analysis from 2019 onwards</li>
            <li>Interactive charts and visualizations</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="feature-card">
        <h3>🎯 Multiple Stock Support</h3>
        <ul>
            <li>Popular US stocks (AAPL, GOOG, MSFT, TSLA)</li>
            <li>Indian market stocks (TATA Motors, Asian Paints, IRFC, Union Bank)</li>
            <li>Easy stock selection with dropdown menu</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <h3>🔮 Advanced Forecasting</h3>
        <ul>
            <li>Prophet machine learning model for accurate predictions</li>
            <li>Forecast up to 4 years into the future</li>
            <li>Seasonal trend analysis and components breakdown</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="feature-card">
        <h3>💻 User-Friendly Interface</h3>
        <ul>
            <li>Clean, intuitive design</li>
            <li>Interactive Plotly charts</li>
            <li>Real-time data loading and processing</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# How it works section
st.markdown("## 📋 How It Works")

steps = [
    ("1️⃣", "Select Your Stock", "Choose from our curated list of popular stocks"),
    ("2️⃣", "Set Prediction Period", "Use the slider to select forecast duration (1-4 years)"),
    ("3️⃣", "Load Data", "Click to fetch real-time historical data"),
    ("4️⃣", "View Predictions", "Get comprehensive forecasts with trend analysis"),
    ("5️⃣", "Analyze Components", "Understand seasonal patterns and long-term trends")
]

for emoji, title, description in steps:
    st.markdown(f"""
    <div class="step-card">
        <h4>{emoji} {title}</h4>
        <p>{description}</p>
    </div>
    """, unsafe_allow_html=True)

# What you'll get section
st.markdown("## 💡 What You'll Get")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### 📈 Comprehensive Analysis
    - Historical price trends and patterns
    - Future price predictions with confidence intervals
    - Seasonal decomposition showing yearly and weekly patterns
    - Interactive charts for better visualization
    """)

with col2:
    st.markdown("""
    ### 📊 Data Insights
    - Raw historical data tables
    - Forecast data with upper and lower bounds
    - Trend components and seasonality analysis
    - Time series visualization with zoom capabilities
    """)

# Who can use this section
st.markdown("## 🎯 Who Can Use This")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    ### 👥 Individual Investors
    - Retail investors looking for stock insights
    - Personal portfolio management
    - Long-term investment planning
    """)

with col2:
    st.markdown("""
    ### 📊 Financial Analysts
    - Market research and analysis
    - Client presentations and reports
    - Investment strategy development
    """)

with col3:
    st.markdown("""
    ### 🎓 Students & Researchers
    - Financial modeling and analysis
    - Academic projects and research
    - Learning about time series forecasting
    """)

# Disclaimer section
st.markdown("## ⚠️ Important Disclaimer")

st.markdown("""
<div class="disclaimer-box">
    <h4>📢 Please Read Carefully</h4>
    <p>This tool is for <strong>educational and informational purposes only</strong>. Stock predictions are based on historical data and machine learning models, which cannot guarantee future performance. Always consult with qualified financial advisors before making investment decisions.</p>
    
    <h5>Key Points:</h5>
    <ul>
        <li>Past performance does not guarantee future results</li>
        <li>Stock markets are inherently volatile and unpredictable</li>
        <li>Use predictions as one factor among many in your analysis</li>
        <li>Consider risk tolerance and investment objectives</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Technical details section
st.markdown("## 🔧 Technical Details")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    - **Data Source**: Yahoo Finance API
    - **Model**: Facebook Prophet forecasting algorithm
    - **Update Frequency**: Real-time data fetching
    - **Supported Markets**: US and Indian stock exchanges
    """)

with col2:
    st.markdown("""
    - **Framework**: Streamlit
    - **Visualization**: Plotly
    - **Data Processing**: Pandas, NumPy
    - **Forecasting**: Prophet (Facebook)
    """)

# Call to action
st.markdown("## 🚦 Get Started")

col1, col2, col3 = st.columns([1, 1, 1])

with col2:
    st.markdown("""
    <div style="text-align: center; padding: 2rem;">
        <h3>Ready to explore stock predictions?</h3>
        <p>Navigate to the <strong>Predictor</strong> page to begin your analysis!</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🚀 Start Predicting", key="start_predicting", help="Go to Predictor page",):
        st.switch_page("pages/Predictor.py")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 1rem;">
    <p><em>Built with Streamlit, Prophet, and modern web technologies for reliable stock market forecasting.</em></p>
    <p>© 2025 Stock Predictor - For Educational Use Only</p>
</div>
""", unsafe_allow_html=True)

# Sidebar content
with st.sidebar:
    st.markdown("## 🎯 Quick Navigation")
    st.markdown("- **Home**: Overview and features")
    st.markdown("- **Predictor**: Stock prediction tool")
    
    st.markdown("## 📊 Supported Stocks")
    st.markdown("### US Stocks")
    st.markdown("- AAPL (Apple)")
    st.markdown("- GOOG (Google)")
    st.markdown("- MSFT (Microsoft)")
    st.markdown("- TSLA (Tesla)")
    
    st.markdown("### Indian Stocks")
    st.markdown("- TATAMOTORS.NS")
    st.markdown("- ASIANPAINT.NS")
    st.markdown("- IRFC.NS")
    st.markdown("- UNIONBANK.NS")
    
    st.markdown("## 📈 Quick Stats")
    current_date = date.today()
    st.markdown(f"**Last Updated**: {current_date.strftime('%B %d, %Y')}")
    st.markdown("**Data Range**: 2019 - Present")
    st.markdown("**Prediction Range**: 1-4 Years")
    
    st.markdown("## 💡 Tips")
    st.markdown("- Start with shorter prediction periods")
    st.markdown("- Compare multiple stocks")
    st.markdown("- Consider market conditions")
    st.markdown("- Use as one analysis tool among many")