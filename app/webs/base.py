from fastapi import APIRouter

from app.webs.routers import jobs, users, login

web_router = APIRouter()
web_router.include_router(jobs.router, prefix="", tags=["job-webapp"])
web_router.include_router(users.router, prefix="", tags=["user-webapp"])
web_router.include_router(login.router, prefix="", tags=["login-webapp"])
