import uvicorn
from fastapi import FastAPI

from utils.config import Settings

from routers import root

app = FastAPI()
settings = Settings()

app.include_router(root.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")
