from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

views_router = APIRouter()

templates = Jinja2Templates("./templates")

@views_router.get("/")
async def main(request: Request):
    return templates.TemplateResponse("main.html", {"request": request})


@views_router.get("/faq")
async def main(request: Request):
    return templates.TemplateResponse("faq.html", {"request": request})


@views_router.get("/about")
async def main(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})
