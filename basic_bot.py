
import logging
from binance.client import Client
from binance.exceptions import BinanceAPIException

# Logging Setup
logging.basicConfig(
    filename='trading_bot.log',
    level=logging.INFO,
    format='%(asctime)s:%(levelname)s:%(message)s'
)

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.api_key = api_key
        self.api_secret = api_secret
        self.testnet = testnet
        self.base_url = "https://testnet.binancefuture.com" if testnet else "https://fapi.binance.com"
        self.client = Client(api_key, api_secret)
        self.client.FUTURES_URL = self.base_url
        logging.info("Bot initialized with testnet=%s", testnet)

    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            if order_type == 'MARKET':
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type=order_type,
                    quantity=quantity
                )
            elif order_type == 'LIMIT':
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type=order_type,
                    timeInForce='GTC',
                    quantity=quantity,
                    price=price
                )
            elif order_type == 'STOP_MARKET':
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type=order_type,
                    stopPrice=price,
                    quantity=quantity,
                    timeInForce='GTC'
                )
            else:
                raise ValueError("Unsupported order type")

            logging.info(f"Order placed: {order}")
            return order
        except BinanceAPIException as e:
            logging.error(f"Binance API error: {e}")
        except Exception as e:
            logging.error(f"General error: {e}")

    def show_balance(self):
        try:
            balance = self.client.futures_account_balance()
            logging.info("Fetched balance")
            return balance
        except Exception as e:
            logging.error("Balance fetch failed: %s", str(e))
            return None
