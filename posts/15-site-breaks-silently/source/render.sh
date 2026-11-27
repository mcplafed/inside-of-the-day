#!/bin/sh
# Renders infographic.html to a 1080x1350 PNG with headless Chrome.
cd "$(dirname "$0")" && "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --hide-scrollbars --force-device-scale-factor=2 --window-size=1080,1350 --virtual-time-budget=4000 --screenshot=infographic.png "file://$PWD/infographic.html" 2>/dev/null && ls -la infographic.png
