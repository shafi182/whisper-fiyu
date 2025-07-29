import whisper
from fastapi import FastAPI, File, UploadFile

app = FastAPI()
model = whisper.load_model("base")

@app.post("/transcribe")
async def transcribe(file: UploadFile = File(...)):
    audio_path = f"/tmp/{file.filename}"
    with open(audio_path, "wb") as f:
        f.write(await file.read())
    result = model.transcribe(audio_path)
    return {"text": result["text"]}
