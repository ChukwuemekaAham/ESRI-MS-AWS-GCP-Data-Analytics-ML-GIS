from typing import List

import joblib
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define the labels corresponding to the target classes
LABELS = [
    "Verdante",  # A vibrant and fresh wine, inspired by its balanced acidity and crisp flavors.
    "Rubresco",  # A rich and robust wine, named for its deep, ruby color and bold taste profile.
    "Floralis",  # A fragrant and elegant wine, known for its floral notes and smooth finish.
]


class Features(BaseModel):
    features: List[float]


def load_model(file_path):
    return joblib.load(file_path)


model = load_model("model.pkl")


@app.post("/predict")
def predict(features: Features):
    # Get the numerical prediction
    prediction_index = model.predict([features.features])[0]
    # Map the numerical prediction to the label
    prediction_label = LABELS[prediction_index]
    return {"prediction": prediction_label}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9000)
