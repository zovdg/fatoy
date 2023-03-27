from fastapi import APIRouter

from .v1 import users
from .v1 import general_pages
from .v1 import jobs
from .v1 import login

api_router = APIRouter()
api_router.include_router(general_pages.router, prefix="", tags=["general_pages"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(jobs.router, prefix="/jobs", tags=["jobs"])
api_router.include_router(login.router, prefix="/login", tags=["login"])
