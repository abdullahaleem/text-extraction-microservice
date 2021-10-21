"""
We are create a microserver that would take off load from our main app.
This microservice can be used any apps in the future that require this functionality

app
- init
- main

The flask development server is not suited for produtction its not able to take in multiple requires and not good for scailbilty
Something like WSGI server: gunicorn fixes this and makes it much more suitable for production enivornment

path to our api is app.main:app
we will use univorn to grab that: uvicorn app.main:app --reload

REST API:  app to app communication.

FASTAPI makes every endpoint by default return json (unless you change it) so we dont have to do json.dumps

Flush out testing before going to production to make sure we dont have any bugs at production
"""

import os
from fastapi import FastAPI, Request
from fastapi import templating
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

BASE_DIR = "app"


app = FastAPI()
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

@app.get("/", response_class=HTMLResponse) # http GET -> JSON
def home_view(request: Request):
    #print(request)
    return templates.TemplateResponse("home.html", {"request": request, "test_arg": 123})


@app.post("/") # http POST -> JSON
def home_detail_view():
    return {"hello": "world"}