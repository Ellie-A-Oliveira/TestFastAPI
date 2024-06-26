from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os


app = FastAPI()

origins = [
    "https://test-fast-api-ashy.vercel.app/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}


uvicorn.run(app, host="0.0.0.0", port=os.getenv("PORT", 8000))