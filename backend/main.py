import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


allowed_origin = os.getenv('CORS_ALLOWED_ORIGIN') 
origins = [
    allowed_origin
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins
)


@app.get("/")
async def root():
    return {"message": "Hello World"}

