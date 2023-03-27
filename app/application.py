from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.core.config import settings
from app.routers import homepage

from app.db.session import engine
from app.db.base import Base
from app.db import models as _
from app.apis.base import api_router


def create_app():
    api = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    api.include_router(homepage.router)
    api.include_router(api_router)
    api.mount("/static", StaticFiles(directory="static"), name="static")

    # create tables.
    print("Create tables...")
    Base.metadata.create_all(bind=engine)

    return api


app = create_app()
