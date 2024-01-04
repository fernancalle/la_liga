# La Liga Match Predictor API Documentation

## Overview
This document details the La Liga Match Predictor API, a FastAPI application designed to predict the outcome of football matches in the Spanish La Liga. The API allows users to input any home and away team combination to predict match outcomes.

## API Endpoint Details

### POST `/predict_match`
This endpoint predicts the outcome of a La Liga match based on the specified home and away teams. It accepts JSON data containing the names of the home and away teams.

#### Request Model
- `HomeTeam`: String (name of the home team)
- `AwayTeam`: String (name of the away team)

#### Response
- JSON object containing the `HomeTeam`, `AwayTeam`, and predicted outcome.

## How to Test the API

### Using `curl`

To test the API with `curl`, execute the following command:

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/predict_match' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "HomeTeam": "<home_team_name>",
  "AwayTeam": "<away_team_name>"
}'
```

_Replace <home_team_name> and <away_team_name> with the names of the teams involved in the match._

### Example:

``` bash
curl -X 'POST' \
  'http://127.0.0.1:8000/predict_match' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "HomeTeam": "Real Madrid",
  "AwayTeam": "Barcelona"
}'
```

### Using Swagger UI

1. Open your web browser and navigate to http://127.0.0.1:8000/docs.
2. Locate the /predict_match endpoint.
3. Use the Swagger UI to send a POST request with the HomeTeam and AwayTeam details.
4. View the API's JSON response containing the prediction.

### Test Cases and Results

Examples of matches that can be tested:

- Real Madrid vs Barcelona
- Sevilla vs Atletico Madrid
- Villarreal vs Valencia

### Code Details
The main.py file for the FastAPI application includes the endpoint /predict_match, which uses a trained machine learning model to predict the outcome of La Liga matches based on the HomeTeam and AwayTeam.
