#!/usr/bin/env python
"""Command-line tool for Indian Stock Analysis"""

from stocks.fetcher import StockFetcher, POPULAR_STOCKS
from ml_models.predictor import StockPredictor
import pandas as pd

def main():
    print("\n" + "=" * 80)
    print("     Indian Stock Analysis - Command Line Tool (NSE/BSE)")
    print("=" * 80 + "\n")
    
    fetcher = StockFetcher()
    predictor = StockPredictor()
    
    # Get market summary
    print("📈 MARKET SUMMARY (Top 6 Stocks)")
    print("-" * 80)
    summary = fetcher.get_market_summary()
    for symbol, data in summary.items():
        if 'error' not in data:
            print(f"{symbol:12} | Close: ₹{data['close']:8.2f} | "
                  f"Change: {data['change']:+7.2f}% | "
                  f"Volume: {data['volume']:>12,.0f}")
    
    print("\n" + "-" * 80)
    print("\n📊 DETAILED STOCK ANALYSIS")
    print("-" * 80)
    
    # Analyze individual stock
    stock = input("\nSelect stock (default: SBIN): ").upper() or "SBIN"
    
    if stock not in POPULAR_STOCKS:
        print(f"❌ Stock {stock} not found!")
        return
    
    print(f"\n🔄 Fetching data for {stock}...")
    data, error = fetcher.get_stock_data(stock, days=365)
    
    if error:
        print(f"❌ Error: {error}")
        return
    
    # Display current info
    print("\n" + "=" * 80)
    print(f"✅ Current Price: ₹{data['Close'].iloc[-1]:.2f}")
    print(f"   52-Week High: ₹{data['Close'].max():.2f}")
    print(f"   52-Week Low: ₹{data['Close'].min():.2f}")
    print(f"   Avg Volume: {data['Volume'].mean():,.0f}")
    print("=" * 80)
    
    # Train model
    print("\n🤖 Training ML Model...")
    result = predictor.train(data)
    
    if 'error' in result:
        print(f"❌ Training error: {result['error']}")
        return
    
    print(f"✅ Model Training Complete:")
    print(f"   Train R² Score: {result['train_r2']:.4f}")
    print(f"   Test R² Score: {result['test_r2']:.4f}")
    print(f"   Training Samples: {result['train_samples']}")
    print(f"   Test Samples: {result['test_samples']}")
    
    # Generate predictions
    print("\n🔮 Generating 5-Day Price Predictions...")
    predictions, error = predictor.predict_next(data, days=5)
    
    if error:
        print(f"❌ Prediction error: {error}")
        return
    
    print("\n📈 Next 5 Days Prediction:")
    print("-" * 80)
    last_price = data['Close'].iloc[-1]
    for i, price in enumerate(predictions, 1):
        change = ((price - last_price) / last_price) * 100
        print(f"   Day {i}: ₹{price:8.2f} ({change:+7.2f}%)")
    
    # Get options data
    print("\n📊 Options Data:")
    print("-" * 80)
    options, error = fetcher.get_options_data(stock)
    
    if error:
        print(f"⚠️  Options data not available: {error}")
    else:
        print(f"✅ Expiration Date: {options['expiration']}")
        print(f"   Calls Available: {len(options['calls'])}")
        print(f"   Puts Available: {len(options['puts'])}")
        
        if len(options['calls']) > 0:
            print("\n   Sample Call Options:")
            calls_df = options['calls'].head(3)[['strike', 'lastPrice', 'bid', 'ask', 'openInterest']]
            print(calls_df.to_string(index=False))
    
    print("\n" + "=" * 80)
    print("✨ Analysis Complete!")
    print("=" * 80 + "\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Application terminated by user")
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
