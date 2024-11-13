from fastapi import FastAPI, Response, status
import omr
import os
import requests

SESSION_TELEGRAM_BOT_TOKEN = os.getenv('SESSION_TELEGRAM_BOT_TOKEN')
TELEGRAM_API_URL: str = f'https://api.telegram.org/file/bot{SESSION_TELEGRAM_BOT_TOKEN}/'

app = FastAPI()


@app.get("/file-path")
async def process_file_by_path(path: str):
    try:
        response = requests.get(TELEGRAM_API_URL + path)
        if response.status_code != 200:
            raise RuntimeError("Failed to get file from Telegram")
        return omr.get_answers(response.content)
    except Exception as e:
        return Response(str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
