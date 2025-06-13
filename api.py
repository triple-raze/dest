from database import execsql

from nanoid import generate
from urllib.parse import urlparse

from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

api_router = APIRouter()

symbols = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ23456789"

@api_router.post("/generate")
async def generate_url(request: Request):
    
    body = await request.json()
    origin_url = body.get("origin_url")
    short_url = generate(symbols, 5)

    parsed_url = urlparse(origin_url)
    if not (parsed_url.scheme and parsed_url.netloc):
        return {"short_url": None}
    
    while short_url in execsql("SELECT * FROM links"):
        collision_url = short_url
        short_url = generate(symbols, 5)
        print(f"collision happened: {collision_url} --> {short_url}")

    execsql("INSERT INTO links (origin_url, short_url) VALUES (%s, %s)", (origin_url, short_url))

    return {"short_url": short_url}


@api_router.get("/{short_url}")
async def redirect(short_url: str):

    origin_url = execsql("SELECT origin_url FROM links WHERE short_url = %s AND short_url != %s", (short_url, "about"), True)

    if not origin_url:
        raise HTTPException(status_code=404, detail="Short URL not found")

    return RedirectResponse(origin_url)

