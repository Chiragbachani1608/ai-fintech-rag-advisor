#!/usr/bin/env python
"""
🚀 Indian Stock Analysis Platform - Main Application
Complete AI-powered financial advisory system with Real-time NSE/BSE data and ML predictions
"""

import sys
import os
from pathlib import Path

# Add project root to path
PROJECT_ROOT = Path(__file__).parent
sys.path.insert(0, str(PROJECT_ROOT))

def initialize_system():
    """Initialize all system components"""
    print("\n" + "=" * 90)
    print("🚀 INDIAN STOCK ANALYSIS PLATFORM - INITIALIZATION")
    print("=" * 90)
    
    try:
        print("\n✓ Step 1: Loading Configuration...")
        from config.settings import VECTOR_DIM, TOP_K, MAX_SENTENCES
        print(f"  - Vector Dimension: {VECTOR_DIM}")
        print(f"  - Top K Results: {TOP_K}")
        print(f"  - Max Sentences: {MAX_SENTENCES}")
        
        print("\n✓ Step 2: Initializing RAG System...")
        from ingestion.pdf_loader import load_pdf
        from ingestion.csv_loader import load_csv
        from embeddings.embedder import Embedder
        from vectorstore.faiss_store import FAISSStore
        from rag.retriever import Retriever
        from rag.advisor import FintechAdvisor
        
        # Load fintech knowledge base
        docs = []
        docs.extend(load_pdf('data/reports/comprehensive_fintech_report.txt'))
        docs.extend(load_pdf('data/reports/market_trends.txt'))
        docs.extend(load_pdf('data/reports/sample_report.txt'))
        print(f"  - Loaded {len(docs)} documents")
        
        # Create embeddings
        embedder = Embedder()
        embeddings = embedder.embed(docs)
        print(f"  - Created embeddings (dim={embeddings.shape[1]})")
        
        # Store in vector database
        store = FAISSStore(VECTOR_DIM)
        store.add(embeddings, docs)
        print(f"  - Initialized FAISS store")
        
        # Initialize RAG components
        retriever = Retriever(store)
        advisor = FintechAdvisor()
        print("  - RAG system ready")
        
        print("\n✓ Step 3: Initializing Stock Data Module...")
        from stocks.fetcher import StockFetcher, POPULAR_STOCKS
        fetcher = StockFetcher()
        print(f"  - Stock Fetcher ready ({len(POPULAR_STOCKS)} stocks)")
        
        print("\n✓ Step 4: Initializing ML Predictor...")
        from ml_models.predictor import StockPredictor
        predictor = StockPredictor()
        print("  - ML Model ready")
        
        print("\n✓ Step 5: Initializing GUI Application...")
        import tkinter as tk
        from gui.app_gui import StockAnalysisGUI
        
        # Create and show GUI
        root = tk.Tk()
        app = StockAnalysisGUI(root)
        print("  - GUI initialized")
        
        print("\n" + "=" * 90)
        print("✅ ALL SYSTEMS INITIALIZED AND READY!")
        print("=" * 90)
        print("\n📊 Application Features:")
        print("  • Real-time NSE/BSE stock prices from Yahoo Finance")
        print("  • 15+ Indian stocks (SBIN, RELIANCE, INFY, TCS, HDFC, etc.)")
        print("  • Machine Learning price predictions (5-day forecast)")
        print("  • Technical Indicators (MA, RSI, MACD, Volatility)")
        print("  • AI-powered Market Analysis (RAG)")
        print("  • Interactive GUI with live charts")
        print("  • CLI tool for command-line use")
        print("\n" + "=" * 90 + "\n")
        
        # Launch GUI
        root.mainloop()
        
    except ImportError as e:
        print(f"\n❌ ERROR: Missing dependency - {e}")
        print("\nInstall required packages:")
        print("  pip install yfinance pandas numpy scikit-learn matplotlib")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ INITIALIZATION ERROR: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

def main():
    """Main entry point"""
    try:
        initialize_system()
    except KeyboardInterrupt:
        print("\n\n👋 Application terminated by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Fatal Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
