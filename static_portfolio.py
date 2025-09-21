import os
import re
from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

def parse_portfolio_data():
    """Parse the portfolio data from the text file"""
    try:
        with open('/home/ubuntu/PORTFOLIO/portfolio_data.txt', 'r') as f:
            content = f.read()
        
        # Extract total value
        total_match = re.search(r'Total Portfolio Value: \$([0-9,]+\.?[0-9]*)', content)
        total_value = 0
        if total_match:
            total_value = float(total_match.group(1).replace(',', ''))
        
        # Extract BTC total
        btc_match = re.search(r'Total BTC: ([0-9.]+)', content)
        btc_total = btc_match.group(1) if btc_match else "0"
        
        # Extract ETH total
        eth_match = re.search(r'Total ETH: ([0-9.]+)', content)
        eth_total = eth_match.group(1) if eth_match else "0"
        
        # Extract stablecoin total
        stable_match = re.search(r'Total Stablecoins.*?: ([0-9,]+\.?[0-9]*)', content)
        stable_total = stable_match.group(1).replace(',', '') if stable_match else "0"
        
        return {
            'total_value': total_value,
            'btc_total': btc_total,
            'eth_total': eth_total,
            'stable_total': stable_total,
            'raw_output': content,
            'last_updated': datetime.now().strftime('%H:%M:%S'),
            'status': 'success'
        }
    except Exception as e:
        return {
            'total_value': 0,
            'btc_total': "0",
            'eth_total': "0", 
            'stable_total': "0",
            'raw_output': f"Error reading portfolio data: {str(e)}",
            'last_updated': datetime.now().strftime('%H:%M:%S'),
            'status': 'error'
        }

@app.route('/')
def index():
    data = parse_portfolio_data()
    return render_template('static_portfolio.html', **data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=False)
