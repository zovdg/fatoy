from fastapi import APIRouter
from fastapi import Request, Depends
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.db.repository.jobs import list_jobs, retrieve_job
from app.db.session import get_db


templates = Jinja2Templates(directory="templates")
router = APIRouter(include_in_schema=False)


@router.get("/")
async def home(request: Request, db: Session = Depends(get_db), msg:str = None):
    jobs = list_jobs(db=db)
    print("jobs: ", jobs)
    return templates.TemplateResponse(
        "homepage.html", {"request": request, "jobs": jobs, "msg": msg}
    )


@router.get("/details/{id}")
async def job_detail(id: int, request: Request, db: Session = Depends(get_db)):
    job = retrieve_job(id=id, db=db)
    return templates.TemplateResponse(
        "jobs/detail.html", {"request": request, "job": job}
    )
