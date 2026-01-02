# Indian Stock Analysis Platform with AI & ML

A comprehensive application for analyzing Indian stocks (NSE/BSE) with Machine Learning price predictions and AI-powered advisory.

## Features

### 📊 Stock Data (Real Yahoo Finance)
- **NSE (National Stock Exchange)** - SBIN, RELIANCE, INFY, TCS, HDFC, ICICI, WIPRO, etc.
- **Real-time price data** with historical charts
- **52-week highs/lows** and market statistics
- **Options data** for selected stocks
- Multi-stock portfolio tracking

### 🤖 Machine Learning
- **Price Prediction** - 5-day forecast using Random Forest
- **Technical Indicators** - RSI, MACD, Moving Averages
- **Model Training** - Train/test split with R² accuracy
- **Feature Engineering** - Automated feature creation from OHLCV data

### 💡 AI Advisory (RAG)
- Smart retrieval of fintech information
- Contextual recommendations based on market trends
- Real-time analysis generation

### 🎯 GUI Interface
- Interactive Tkinter GUI with matplotlib charts
- Real-time stock price visualization
- ML predictions display
- AI analysis panel

## Installation

```bash
# Install required packages
pip install yfinance pandas numpy scikit-learn matplotlib

# Run the application
python main_gui.py
```

## Supported Indian Stocks

| Symbol | Company | Exchange |
|--------|---------|----------|
| SBIN | State Bank of India | NSE |
| RELIANCE | Reliance Industries | NSE |
| INFY | Infosys | NSE |
| TCS | Tata Consultancy Services | NSE |
| HDFC | HDFC Bank | NSE |
| ICICI | ICICI Bank | NSE |
| ITC | ITC Limited | NSE |
| WIPRO | Wipro | NSE |
| HUL | Hindustan Unilever | NSE |
| MARUTI | Maruti Suzuki | NSE |

## How to Use

1. **Select Stock** - Choose from dropdown (NSE format)
2. **Fetch Data** - Load 1-year historical data
3. **Train Model** - Train ML predictor (takes ~1-2 min)
4. **Get Predictions** - See next 5-day price predictions
5. **AI Analysis** - Get insights from AI advisor

## Architecture

```
├── stocks/
│   └── fetcher.py          # Yahoo Finance integration
├── ml_models/
│   └── predictor.py        # ML price prediction
├── gui/
│   └── app_gui.py          # Tkinter GUI
├── rag/
│   └── advisor.py          # AI advisory
├── embeddings/
│   └── embedder.py         # Text embeddings
├── vectorstore/
│   └── faiss_store.py      # Vector database
└── main_gui.py             # Application launcher
```

## ML Model Details

- **Algorithm**: Random Forest Regressor (100 trees)
- **Features**: Close, MA_7, MA_30, RSI, MACD, Volatility
- **Lookback**: 30 days
- **Output**: 5-day price predictions
- **Accuracy**: R² score displayed after training

## Data Flow

1. **Yahoo Finance** → Stock data (OHLCV)
2. **Feature Engineering** → Technical indicators
3. **ML Model** → Price predictions
4. **RAG Advisor** → Market insights
5. **GUI Display** → Charts & analysis

## Performance

- Data Loading: ~2-5 seconds
- Model Training: ~30-60 seconds (first time)
- Prediction: ~1-2 seconds
- Real-time Updates: Automatic

## Requirements

- Python 3.8+
- yfinance >= 0.2.28
- pandas >= 1.3
- numpy >= 1.20
- scikit-learn >= 1.0
- matplotlib >= 3.4
- tkinter (included with Python)

## Notes

- All prices in INR (Indian Rupees)
- Historical data: 1 year
- Predictions: Next 5 days
- Update frequency: Daily

## Future Enhancements

- [ ] Multi-stock portfolio optimization
- [ ] Real-time price alerts
- [ ] Advanced charting with TradingView
- [ ] Sentiment analysis from news
- [ ] Deep learning models (LSTM)
- [ ] Risk management tools
- [ ] Backtesting engine

## License

MIT License
