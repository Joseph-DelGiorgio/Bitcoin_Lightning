# Import the necessary modules
import c-lightning
import bitcoin

# Set the network to testnet (you can also use mainnet if you have real Bitcoin)
bitcoin.SelectParams("testnet")

# Create a new Lightning client instance
lightning_client = c-lightning.Lightning()

# Connect to a local Lightning node
lightning_client.connect("localhost")

# Generate a new Bitcoin address for receiving payments
receiving_address = lightning_client.newaddr()

# Send a payment to the receiving address
payment_hash = lightning_client.sendpay(receiving_address, amount=0.01)

# Wait for the payment to be confirmed on the network
lightning_client.waitsendpay(payment_hash)

# Disconnect from the Lightning node
lightning_client.disconnect()
