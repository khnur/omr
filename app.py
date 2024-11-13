from fastapi import FastAPI, File, UploadFile
import omr

app = FastAPI()


@app.post("/upload-file/")
async def upload_file(file: UploadFile = File(...)) -> dict[int, str | list[str]]:
    file_bytes = await file.read()
    return omr.get_answers(file_bytes)
