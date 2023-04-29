import traceback
import requests

from core.settings import TG_BOT_TOKEN, TG_NOTIFY_CHANNEL


def tg_send_message(message):
    url_message = f'https://api.telegram.org/bot{TG_BOT_TOKEN}/sendMessage?' \
                  f'chat_id={TG_NOTIFY_CHANNEL}&text={message}'
    try:
        response = requests.get(url_message)
        return response.text
    except:
        traceback.print_exc()
