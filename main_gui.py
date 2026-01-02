#!/usr/bin/env python
"""Main launcher for Indian Stock Analysis Application"""

import sys
import tkinter as tk
from tkinter import messagebox
import threading
from gui.app_gui import StockAnalysisGUI

def main():
    print("=" * 80)
    print("     Indian Stock Analysis Platform - NSE/BSE with AI & Machine Learning")
    print("=" * 80)
    print("\nLaunching GUI Application...\n")
    
    try:
        root = tk.Tk()
        app = StockAnalysisGUI(root)
        root.mainloop()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to launch application:\n{str(e)}")
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
