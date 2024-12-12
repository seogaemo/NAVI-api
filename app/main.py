import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.common.utils.config import Settings

from api.routers import image, location, pedestrian, poi, root

app = FastAPI()
settings = Settings()

app.include_router(root.router)
app.include_router(pedestrian.router)
app.include_router(image.router)
app.include_router(location.router)
app.include_router(poi.router)

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")
