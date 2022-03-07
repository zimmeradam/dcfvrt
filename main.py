from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from telegram_a import sendMsg
from html_pages import Success, Failure
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
app = FastAPI()


lista={}
lista['1134'] = '-778541371'

@app.get("/{item_id}", response_class=HTMLResponse)
async def read_item(item_id):
    try:
        bot_chatID = lista[str(item_id)]
        sendMsg(item_id, bot_chatID)
        return Success() #{"chat_id": bot_chatID}
    except:
        return Failure()

    