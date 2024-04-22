from web3 import Web3
from backend.config import RPC_URLS

class WalletService:
    def __init__(self, network="ethereum"):
        self.web3 = Web3(Web3.HTTPProvider(RPC_URLS[network]))

    def get_balance(self, address: str):
        balance = self.web3.eth.get_balance(address)
        return {
            "address": address,
            "balance_wei": balance,
            "balance_eth": self.web3.fromWei(balance, "ether")
        }
# commit
# commit
# commit
# commit
# commit
# commit
# commit
# commit
# commit
# commit
# commit
# commit
# commit
# commit
# commit
# commit
# commit
# commit
# commit
# commit
# commit
# commit
# commit
# commit
# commit
# commit
# commit
# commit
# commit
# commit
# commit
# commit
# commit
# commit
# commit
# commit
# commit
# commit
# commit
# commit
# commit
# commit
# commit
# commit
# commit
# commit
# commit
# commit
# commit
# commit
# commit
# commit
# commit
# commit
# commit
# commit
# commit
# commit
# commit
# commit
# commit
# commit
# commit
# commit
# commit
# commit
# commit
# commit
# commit
# commit
# commit
# commit
# commit
# commit
# commit
# commit
# commit
# commit
# commit
# commit
# commit
# commit
# commit
# commit
# commit
# commit
# commit
# commit
# commit
# commit
# commit
# commit
