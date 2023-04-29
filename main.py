from fastapi import FastAPI, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware

from core.settings import ORIGINS
from models.message import Message
from tasks.tg import tg_send_message

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/notify")
def notify(message: Message,  background_tasks: BackgroundTasks):
    background_tasks.add_task(tg_send_message, message=message.display_message)
    return {}
