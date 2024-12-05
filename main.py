import uvicorn
from fastapi import FastAPI

from utils.config import Settings

app = FastAPI()
settings = Settings()


@app.get("/")
async def root():
    return "Hello World!"


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")
