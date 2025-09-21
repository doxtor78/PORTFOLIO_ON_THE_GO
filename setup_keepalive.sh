#!/bin/bash

# Portfolio Keep-Alive Setup Script
# This script sets up automatic portfolio updates and web server monitoring

echo "Setting up Portfolio Keep-Alive System..."

# Set up crontab for automatic updates every 5 minutes
echo "*/5 * * * * /home/ubuntu/PORTFOLIO_ON_THE_GO/keep_alive.sh >> /home/ubuntu/portfolio_keepalive.log 2>&1" | crontab -

echo "✅ Crontab configured for automatic updates every 5 minutes"

# Make keep_alive.sh executable
chmod +x /home/ubuntu/PORTFOLIO_ON_THE_GO/keep_alive.sh

echo "✅ Keep-alive script made executable"

# Test the keep-alive script
echo "Testing keep-alive script..."
/home/ubuntu/PORTFOLIO_ON_THE_GO/keep_alive.sh

echo "✅ Keep-alive system setup complete!"
echo ""
echo "Your portfolio will now:"
echo "- Update automatically every 5 minutes"
echo "- Restart web server if it goes down"
echo "- Log all activities to /home/ubuntu/portfolio_keepalive.log"
echo ""
echo "Access your portfolio at: http://15.236.190.19/portfolio.html"
