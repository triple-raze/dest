from routers.api import api_router
from routers.views import views_router

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

Instrumentator().instrument(app).expose(app)

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(views_router)
app.include_router(api_router)


# if __name__ == "__main__":
#     uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)