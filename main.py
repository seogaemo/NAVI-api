# main.py
from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
async def root():
    return "Hello World!"


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")
