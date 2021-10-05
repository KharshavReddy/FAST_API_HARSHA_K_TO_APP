from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from . import models
from .database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


from .api import task_router

app.include_router(task_router)