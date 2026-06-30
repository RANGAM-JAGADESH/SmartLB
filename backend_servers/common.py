from fastapi import FastAPI
from datetime import datetime
import socket


def create_backend(server_name: str, server_port: int):

    app = FastAPI()

    @app.get("/")
    def home():
        return {
            "server": server_name,
            "message": f"Welcome to {server_name}",
            "timestamp": datetime.now().isoformat(),
            "hostname": socket.gethostname(),
            "port": server_port
        }

    @app.get("/health")
    def health():
        return {
            "status": "healthy"
        }

    @app.get("/info")
    def info():
        return {
            "server": server_name,
            "port": server_port,
            "status": "running"
        }

    return app