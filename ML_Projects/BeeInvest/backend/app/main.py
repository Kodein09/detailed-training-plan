from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware


app = FastAPI(
    title="🐝Invest",
    description="Investment Website"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)