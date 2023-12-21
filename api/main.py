from fastapi import FastAPI
from pydantic import BaseModel
from starlette.requests import Request
from starlette.responses import Response
import json
from contextlib import asynccontextmanager
from sentence_transformers import SentenceTransformer
import pandas as pd
from nlp_model import predict_cv, predict_vaccancy
import uvicorn


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the ML model
    global model
    model = SentenceTransformer('cointegrated/rubert-tiny2')

    global df_cv
    df_cv = pd.read_csv("../data/datasets_with_embeddings/cv.csv")
    
    global df_vac
    df_vac = pd.read_csv("../data/datasets_with_embeddings/vac.csv")

    yield


app = FastAPI(lifespan=lifespan)


@app.post("/get_resumes")
async def get_resumes(request: Request):
    request = json.loads((await request.body()).decode())
    vaccancy = request["text"]

    cvs = predict_cv(vaccancy, model, df_cv)

    return Response(cvs, media_type='text/plain')

@app.post("/get_vaccancies")
async def get_resumes(request: Request):
    request = json.loads((await request.body()).decode())
    cv = request["text"]

    vacs = predict_vaccancy(cv, model, df_vac)

    return Response(vacs, media_type='text/plain')


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8080, reload=True)