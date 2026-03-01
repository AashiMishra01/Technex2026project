from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import sys
import os
import shutil

sys.path.append(os.path.join(os.path.dirname(__file__), 'model'))
from classifier import classify_image

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "SortSmart AI backend running"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    # Save uploaded file temporarily
    temp_path = f"temp_{file.filename}"
    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Classify using Roboflow model
    result = classify_image(temp_path)

    # Cleanup
    os.remove(temp_path)

    # Return in same format your frontend expects
    return {
        "prediction": result["waste_category"],
        "object_detected": result["object_detected"],
        "confidence": result["confidence"],
        "second_life": result["second_life"]
    }