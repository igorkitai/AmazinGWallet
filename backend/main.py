from fastapi import FastAPI
from backend.services.wallet import WalletService

app = FastAPI()

@app.get("/")
def root():
    return {"message": "AmazinGWallet backend is running"}

@app.get("/balance/{address}")
def get_balance(address: str):
    return WalletService().get_balance(address)
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
