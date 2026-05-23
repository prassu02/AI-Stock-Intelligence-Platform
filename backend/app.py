from fastapi import FastAPI, UploadFile, File
import pandas as pd
import io
from backend.model import predict_ensemble, generate_signal

app = FastAPI(title="AI Stock Intelligence API")


@app.get("/")
def home():
    return {"message": "API Running Successfully"}


@app.get("/predict/{ticker}")
def predict_stock(ticker: str):

    prediction = predict_ensemble(ticker)

    return {
        "ticker": ticker,
        "predicted_price": prediction,
        "signal": generate_signal(prediction)
    }


@app.post("/upload-file")
async def upload_file(file: UploadFile = File(...)):

    content = await file.read()

    if file.filename.endswith('.csv'):
        df = pd.read_csv(io.StringIO(content.decode('utf-8')))

    elif file.filename.endswith('.xlsx'):
        df = pd.read_excel(io.BytesIO(content))

    else:
        return {"error": "Only CSV/XLSX supported"}

    return {
        "rows": len(df),
        "columns": list(df.columns)
    }