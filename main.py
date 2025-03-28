import requests
import schedule
import time
from telegram import Bot

# Thông tin bot Telegram
TELEGRAM_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"
bot = Bot(token=TELEGRAM_TOKEN)

# Danh sách mã cần theo dõi
STOCK_CODES = ["VIC", "VND", "TPB"]

# Hàm lấy dữ liệu từ SSI
def get_stock_price(stock_code):
    url = f"https://api.ssi.com.vn/price/{stock_code}"  # Cần thay bằng API thực tế
    response = requests.get(url)
    data = response.json()
    return {
        "price": data["current_price"],
        "change": data["price_change"],
        "high": data["high_price"],
        "low": data["low_price"],
        "volume": data["trading_volume"]
    }

# Hàm lấy dữ liệu giá vàng
def get_gold_price():
    url = "https://api.ssi.com.vn/gold-price"  # Cần thay bằng API thực tế
    response = requests.get(url)
    data = response.json()
    return data["gold_price"]

# Hàm gửi tin nhắn Telegram
def send_telegram_message(message):
    bot.send_message(chat_id=CHAT_ID, text=message)

# Hàm gửi giá cổ phiếu
def send_stock_prices():
    message = "\U0001F4C8 **Cập nhật giá cổ phiếu**\n"
    for stock in STOCK_CODES:
        data = get_stock_price(stock)
        message += f"\n🔹 **{stock}**: {data['price']} ({data['change']}%)\n"
        message += f"   - 📈 Cao: {data['high']} | 📉 Thấp: {data['low']}\n"
        message += f"   - 🔄 KL giao dịch: {data['volume']} CP\n"
    send_telegram_message(message)

# Hàm gửi giá vàng
def send_gold_price():
    price = get_gold_price()
    message = f"\U0001F4B0 **Giá vàng hôm nay**: {price} VND/ lượng"
    send_telegram_message(message)

# Lên lịch chạy bot
daily_times = ["09:00", "09:30", "11:00", "14:30"]
for t in daily_times:
    schedule.every().day.at(t).do(send_stock_prices)

schedule.every().day.at("08:00").do(send_gold_price)

# Chạy bot liên tục
while True:
    schedule.run_pending()
    time.sleep(60)
