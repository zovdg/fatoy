from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

router = APIRouter()


@router.get("/")
async def home(request: Request):
    return templates.TemplateResponse("homepage.html", {"request": request})
