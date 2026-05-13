from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from app.ai_model import generate_script

router = APIRouter()

templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"request": request}
    )


@router.post("/generate", response_class=HTMLResponse)
def generate(
    request: Request,
    topic: str = Form(...),
    tone: str = Form(...),
    options: str = Form(None)
):

    result = generate_script(topic, tone, options)

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "request": request,
            "script": result
        }
    )