from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from telegram_a import sendMsg
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
app = FastAPI()


lista={}
lista['1134'] = '-778541371'


templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read(request: Request):
    return templates.TemplateResponse("item.html",
        {"request": request})

@app.get("/{item_id}", response_class=HTMLResponse)
async def read_item(item_id, request: Request):
    try:
        bot_chatID = lista[str(item_id)]
        sendMsg(item_id, bot_chatID)
        return templates.TemplateResponse("success.html",
        {"request": request})
    except:
        return templates.TemplateResponse("failure.html",
        {"request": request})

    