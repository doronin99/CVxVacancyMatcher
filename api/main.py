from fastapi import FastAPI
from pydantic import BaseModel
from nlp_model import predict_compatibility

app = FastAPI()


class CompatibilityInput(BaseModel):
    vacancy_description: str
    resume_description: str


class CompatibilityOutput(BaseModel):
    compatibility_score: float


@app.post("/compatibility", response_model=CompatibilityOutput)
async def calculate_compatibility(input_data: CompatibilityInput):
    compatibility_score = predict_compatibility(input_data.vacancy_description, input_data.resume_description)
    return {"compatibility_score": compatibility_score}
