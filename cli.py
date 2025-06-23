
from basic_bot import BasicBot
import getpass

def main():
    print("==== Binance Testnet Trading Bot ====")
    api_key = input("Enter your Binance API Key: ")
    api_secret = getpass.getpass("Enter your Binance API Secret: ")

    bot = BasicBot(api_key, api_secret)

    while True:
        symbol = input("Enter trading pair (e.g., BTCUSDT): ").upper()
        side = input("Order side (BUY/SELL): ").upper()
        order_type = input("Order type (MARKET/LIMIT/STOP_MARKET): ").upper()
        quantity = float(input("Quantity: "))
        price = None
        if order_type in ["LIMIT", "STOP_MARKET"]:
            price = float(input("Price or Stop Price: "))

        order = bot.place_order(symbol, side, order_type, quantity, price)
        if order:
            print("✅ Order placed successfully")
        else:
            print("❌ Failed to place order")

        cont = input("Place another order? (yes/no): ").lower()
        if cont != 'yes':
            break

if __name__ == "__main__":
    main()
