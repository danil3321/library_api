from fastapi import FastAPI
from app.routers import authors

app = FastAPI()

app.include_router(authors.router, prefix="/api/v1/authors", tags=["Authors"])

@app.get("/")
def root():
    return {"message": "Welcome to the Library API!"}
