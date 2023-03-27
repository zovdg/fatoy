
from fastapi import APIRouter

from app.webs.routers import jobs, users

web_router = APIRouter()
web_router.include_router(jobs.router, prefix="", tags=["job-webapp"])
web_router.include_router(users.router, prefix="", tags=["user-webapp"])
