# Main FastAPI app
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def read_root():
    return {'message': 'Welcome to Solana NFT Platform API!'}