from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from ai_backend import router as ai_router
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ai_router)
app.mount("/static", StaticFiles(directory="frontend/build/static"), name="static")

@app.get("/{full_path:path}")
async def serve_frontend(full_path: str = ""):
    return FileResponse("frontend/build/index.html")