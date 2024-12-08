import uvicorn
from fastapi import FastAPI

from api.common.utils.config import Settings

from api.routers import image, pedestrian, root

app = FastAPI()
settings = Settings()

app.include_router(root.router)
app.include_router(pedestrian.router)
app.include_router(image.router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")
