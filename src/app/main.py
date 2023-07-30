from fastapi import FastAPI

from app.api import health, notes, es
from app.db import engine, database, metadata

metadata.create_all(engine)

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(health.router)
app.include_router(notes.router, prefix="/notes", tags=["notes"])
app.include_router(es.router, prefix="/es", tags=["es"])