from binance.client import Client
from binance.enums import *
from binance.exceptions import BinanceAPIException
from time import sleep
from sys import exit

api_secret = 'enter secret key here'
api_key = 'enter key here'

# Program supports BNB, BTC, and ETH markets only. No USDT.

done = False

client = Client(api_key, api_secret)

print("")
print("Welcome! type 'OPTIONS' to view list of commands.")

while True:
	print("Enter command:")
	command = input('> ')
	command = command.upper()

	if command == "OPTIONS":
		print("STOP / BALANCE")

	elif command == "STOP":
		exit()

	elif command == "BALANCE":
		print("Enter coin to view balance:")
		coin = input('> ')
		coin = coin.upper()

		# Displays asset balance
		balance = client.get_asset_balance(asset=coin)
		assetBalance = balance['free']
		assetName = balance['asset']
		print(assetBalance + " units of " + assetName + " available.")
