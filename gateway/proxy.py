from fastapi import FastAPI
import httpx
from config.settings import BACKENDS

app = FastAPI()

@app.get("/")
async def proxy_request():

    backend = BACKENDS[0]

    async with httpx.AsyncClient() as client:
        response = await client.get(backend["url"])

    return {
        "gateway": "SmartLB",
        "selected_backend": backend["name"],
        "backend_response": response.json()
    }