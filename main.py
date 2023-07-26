from fastapi import FastAPI, Request, Depends, HTTPException
from typing import Optional
from dbconnection import engine, sessionLocal, Base
from sqlalchemy.orm import Session
import models
from sqlalchemy import or_
import re
import uvicorn

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Matrixian Data Engineering API",
    redoc_url=None,
    version="0.0.1",
)


def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"API": "To do management "}



if __name__ == "__main__":
    uvicorn.run(
        app=app,
        host="0.0.0.0",
        port=8000,
    )
