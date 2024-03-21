import logging
import os
import random

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


logger = logging.getLogger(__name__)

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
    randnum = random.randrange(3)
    msg = f"Hello World {randnum}"
    if randnum:
        logger.warn(f"Warn - randnum: {randnum}")
    else:
        logger.error(f"Error - randnum: {randnum}")
    return {"message": msg}
