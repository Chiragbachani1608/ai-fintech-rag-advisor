@echo off
REM Quick Start Script for Indian Stock Analysis Platform

echo.
echo ================================================================================
echo     Indian Stock Analysis Platform - Quick Start
echo ================================================================================
echo.

echo Checking Python installation...
C:\ProgramData\anaconda3\python.exe --version

echo.
echo Installing required packages (if needed)...
C:\ProgramData\anaconda3\python.exe -m pip install yfinance pandas numpy scikit-learn matplotlib -q

echo.
echo ================================================================================
echo Select an option:
echo.
echo 1 - Launch GUI Application (Recommended)
echo 2 - Run Command-Line Tool
echo 3 - Test ML Model
echo 4 - View Market Summary
echo.

set /p choice="Enter choice (1-4): "

if "%choice%"=="1" (
    echo.
    echo Launching GUI Application...
    C:\ProgramData\anaconda3\python.exe main_gui.py
) else if "%choice%"=="2" (
    echo.
    echo Launching CLI Tool...
    C:\ProgramData\anaconda3\python.exe cli_tool.py
) else if "%choice%"=="3" (
    echo.
    echo Testing ML Model...
    C:\ProgramData\anaconda3\python.exe test_ml.py
) else if "%choice%"=="4" (
    echo.
    echo Fetching Market Summary...
    C:\ProgramData\anaconda3\python.exe -c "from stocks.fetcher import StockFetcher; f = StockFetcher(); s = f.get_market_summary(); [print(f'{k}: Close=Rs{v.get(\"close\", \"N/A\"):.2f}, Change={v.get(\"change\", \"N/A\"):.2f}%%') for k, v in s.items()]"
) else (
    echo Invalid choice!
)

pause
