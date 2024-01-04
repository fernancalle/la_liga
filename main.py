from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import joblib

# Initialize FastAPI app
app = FastAPI()

# Load the trained model and label encoder
model = joblib.load('/Users/fernandocalle/Desktop/portfolio/la_liga/real_madrid_model.pkl')
encoder = joblib.load('/Users/fernandocalle/Desktop/portfolio/la_liga/team_name_encoder.pkl')

class MatchInfo(BaseModel):
    HomeTeam: str
    AwayTeam: str

@app.post("/predict_madrid_win")
def predict_madrid_win(match_info: MatchInfo):
    # Preprocess the input data
    home_team_encoded = encoder.transform([match_info.HomeTeam])[0]
    away_team_encoded = encoder.transform([match_info.AwayTeam])[0]
    input_data = np.array([[home_team_encoded, away_team_encoded]])

    # Make a prediction
    prediction = model.predict(input_data)
    return {"prediction": "Win" if prediction[0] == 1 else "Lose"}

