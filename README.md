# 📱 Portfolio On The Go

A mobile-optimized web interface for viewing your cryptocurrency portfolio across multiple exchanges. Access your portfolio from anywhere using your iPhone or any mobile device!

## 🌟 Features

- **📱 Mobile-First Design**: Optimized for iPhone and mobile devices
- **🔄 Real-Time Data**: Fetches live balances from 6 major exchanges
- **⚡ Fast Loading**: Pre-generated data prevents timeouts
- **🎨 Beautiful UI**: Modern gradient design with touch-friendly interface
- **🔄 Auto-Refresh**: Updates every 5 minutes automatically
- **👆 Pull-to-Refresh**: Swipe down to refresh on mobile
- **📊 Complete Overview**: Total value, asset breakdowns, and exchange summaries

## 🏢 Supported Exchanges

- **Binance** - Spot trading balances
- **Bybit** - Unified account balances
- **Kraken** - Spot and futures balances
- **Bitfinex** - Exchange balances
- **Bitstamp** - Trading balances
- **BitMEX** - Futures balances

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure API Keys
Edit `portfolio_app.py` and add your exchange API credentials:
```python
BINANCE_API_KEY = 'your_binance_api_key'
BINANCE_API_SECRET = 'your_binance_secret'
BYBIT_API_KEY = 'your_bybit_api_key'
BYBIT_API_SECRET = 'your_bybit_secret'
# ... add other exchange credentials
```

### 3. Run the Portfolio Script
```bash
python3 portfolio_app.py
```

### 4. Start the Web Server
```bash
# Option 1: Simple HTML server (recommended)
sudo python3 -m http.server 80 --directory /home/ubuntu/PORTFOLIO_ON_THE_GO

# Option 2: Flask web server
python3 static_portfolio.py
```

### 5. Set Up Automatic Updates (Recommended)
```bash
# Run the keep-alive setup script
./setup_keepalive.sh
```

### 6. Access from Mobile
Open your mobile browser and navigate to:
```
http://YOUR_SERVER_IP/portfolio.html
```

## 📁 Project Structure

```
PORTFOLIO_ON_THE_GO/
├── portfolio_app.py          # Main portfolio fetching script
├── portfolio.html            # Mobile-optimized web interface
├── static_portfolio.py       # Flask web server (alternative)
├── keep_alive.sh             # Automatic web server monitoring
├── setup_keepalive.sh        # Keep-alive system setup script
├── requirements.txt          # Python dependencies
├── scripts/                  # Exchange-specific balance scripts
│   ├── binance_balances.py
│   ├── bybit_balances.py
│   ├── kraken_balances.py
│   ├── bitfinex_balances.py
│   ├── bitstamp_balances.py
│   └── bitmex_balances.py
└── templates/                # HTML templates
    ├── portfolio.html
    ├── static_portfolio.html
    └── simple_portfolio.html
```

## 🔧 Configuration

### API Permissions Required
- **Binance**: Read-only access
- **Bybit**: Read-only access
- **Kraken**: Read-only access
- **Bitfinex**: Read-only access
- **Bitstamp**: Read-only access
- **BitMEX**: Read-only access

### Security Notes
- Store API keys securely
- Use read-only permissions only
- Consider using environment variables for production
- Regularly rotate API keys

## 📱 Mobile Features

- **Responsive Design**: Works on all screen sizes
- **Touch Gestures**: Pull-to-refresh functionality
- **Auto-Refresh**: Updates every 5 minutes
- **Fast Loading**: Pre-generated data prevents delays
- **Offline Viewing**: Last data remains visible

## 🛠️ Deployment Options

### AWS Lightsail (Current Setup)
- Deploy on Ubuntu instance
- Use port 80 for HTTP access
- Configure firewall rules
- Set up auto-start scripts

### Other Cloud Providers
- DigitalOcean Droplets
- Google Cloud Platform
- Microsoft Azure
- Heroku (with modifications)

## 📊 Sample Output

```
================================================================================
                         --- Consolidated Portfolio ---
================================================================================
Asset      Amount       Price    Value (USD)  Exchange
-------  --------  ----------  -------------  ----------
BTC          0.27  115,387.32      30,911.78  BitMEX
BTC          0.08  115,387.32       9,125.96  Kraken
USDT     2,189.13        1.00       2,189.13  Binance
ETH          1.42    4,471.78       6,329.09  Bitstamp
...
--------------------------------------------------------------------------------
                       Total Portfolio Value: $59,838.88
--------------------------------------------------------------------------------
```

## 🔄 Auto-Update Setup

To keep your portfolio data fresh, set up a cron job:

```bash
# Edit crontab
crontab -e

# Add this line to update every 5 minutes
*/5 * * * * cd /home/ubuntu/PORTFOLIO_ON_THE_GO && python3 portfolio_app.py > portfolio_data.txt 2>&1
```

## 🐛 Troubleshooting

### Common Issues

1. **API Key Expired**: Update your exchange API credentials
2. **Port Blocked**: Use port 80 instead of 5000
3. **Permission Denied**: Run with sudo for port 80
4. **Module Not Found**: Install requirements.txt

### Debug Mode
```bash
# Run with debug output
python3 portfolio_app.py --debug

# Check web server logs
tail -f /var/log/apache2/error.log
```

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📞 Support

For issues and questions:
- Create an issue on GitHub
- Check the troubleshooting section
- Review exchange API documentation

---

**Happy Trading! 📈💰**
