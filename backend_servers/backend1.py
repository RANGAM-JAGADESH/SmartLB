from fastapi import FastAPI
from datetime import datetime
import socket
from backend_servers.common import create_backend

app = create_backend(
    "Backend Server 1",
    8001
)
app = FastAPI()

SERVER_NAME = "Backend Server 1"
SERVER_PORT = 8001


@app.get("/")
def home():
    return {
        "server": SERVER_NAME,
        "message": "Welcome to SmartLB Backend Server 1",
        "timestamp": datetime.now().isoformat(),
        "hostname": socket.gethostname()
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/info")
def info():
    return {
        "server": SERVER_NAME,
        "port": SERVER_PORT,
        "status": "running"
    }