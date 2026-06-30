from fastapi import FastAPI
import httpx

from config.settings import BACKENDS
from logs.logger import logger

app = FastAPI()


@app.get("/")
async def proxy_request():

    logger.info("Gateway received request")

    # Currently selecting the first backend.
    # Later this will be replaced by the scheduler.
    backend = BACKENDS[0]

    logger.info(f"Selected backend: {backend['name']}")

    async with httpx.AsyncClient() as client:
        response = await client.get(backend["url"])

    logger.info("Response received from backend")

    result = {
        "gateway": "SmartLB",
        "selected_backend": backend["name"],
        "backend_response": response.json()
    }

    logger.info("Response returned to client")

    return result