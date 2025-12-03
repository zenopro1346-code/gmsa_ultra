from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from router import router as main_router

app = FastAPI(title="GMSA Ultra Core")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(main_router)

@app.get("/")
def root():
    return {"status": "GMSA Ultra API Online"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=10000)
