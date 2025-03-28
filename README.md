# stock-bot
This project config 1 chatbot call telegram for people
# Stock & Gold Price Bot

This bot fetches stock prices (VIC, VND, TPB) from SSI and gold prices daily, then sends updates to a Telegram chat.

## Setup Instructions

### 1️⃣ Install Dependencies

```bash
sudo apt update && sudo apt install python3-pip -y
pip3 install requests schedule python-telegram-bot
```

### 2️⃣ Clone the Repository

```bash
git clone https://github.com/your-repo/stock-gold-bot.git
cd stock-gold-bot
```

### 3️⃣ Configure the Bot

Edit `bot.py` and replace:

- `YOUR_TELEGRAM_BOT_TOKEN` with your Telegram bot token
- `YOUR_CHAT_ID` with your Telegram chat ID

### 4️⃣ Run the Bot

```bash
python3 bot.py
```

To run in the background:

```bash
screen -S stockbot
python3 bot.py
# Press Ctrl + A, then D to detach
```

### 5️⃣ Auto-Start on Reboot

Edit the crontab:

```bash
crontab -e
```

Add this line:

```bash
@reboot python3 /path/to/bot.py &
```

### 6️⃣ Stop the Bot

If running in a `screen` session:

```bash
screen -r stockbot
Ctrl + C to stop
```

If running normally:

```bash
pkill -f bot.py
```

