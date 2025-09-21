#!/bin/bash

# Keep Portfolio Web Server Alive Script
# This script ensures the web server stays running

PORTFOLIO_DIR="/home/ubuntu/PORTFOLIO"
WEB_SERVER_PID=$(pgrep -f "python3 -m http.server 80")

echo "$(date): Checking web server status..."

if [ -z "$WEB_SERVER_PID" ]; then
    echo "$(date): Web server not running, starting it..."
    cd $PORTFOLIO_DIR
    sudo python3 -m http.server 80 --directory $PORTFOLIO_DIR &
    echo "$(date): Web server started with PID $!"
else
    echo "$(date): Web server is running with PID $WEB_SERVER_PID"
fi

# Update portfolio data
echo "$(date): Updating portfolio data..."
cd $PORTFOLIO_DIR
source venv/bin/activate
python3 portfolio_web_clean.py > portfolio_data.txt 2>&1
echo "$(date): Portfolio data updated"
