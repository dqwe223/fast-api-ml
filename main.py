from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

model = joblib.load("iris_model.pkl")

# Define the input data format using Pydantic's BaseModel
class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# Mapping of numeric predictions to iris species names
species_mapping = {0: "Setosa", 1: "Versicolour", 2: "Virginica"}

@app.get('/')
def home():
    return {'text': 'Iris Flower Species Prediction aaaaaaa'}

# Create JSON output
@app.post("/predict")
def predict(data: IrisInput):
    # Convert input data to a NumPy array
    input_data = np.array([[data.sepal_length, data.sepal_width, data.petal_length, data.petal_width]])

    # Make the prediction
    prediction = model.predict(input_data)

    # Map the numeric prediction to the corresponding species name
    predicted_species = species_mapping[int(prediction[0])]

    return {"prediction": predicted_species}

