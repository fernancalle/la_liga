<p align="center">
  <img src="https://github.com/fernancalle/portfolio/blob/main/assets/img/laligalogo.png?raw=true" width="200" height="200" alt="La Liga Logo">
</p>

# La Liga Football Matches Analysis

## Project Overview
This project focuses on analyzing football matches from the Spanish La Liga for the seasons 2022-2023 and 2023-2024. The data, sourced from Football-Data.co.uk, is stored in a SQLite database. The primary goal is to predict the outcomes of football matches, with a special focus on determining whether Real Madrid will win, using a simple yet effective model based on specific match statistics.

## Project Steps
1. **Data Extraction and Loading**: The data from Football-Data.co.uk is extracted and loaded into a SQLite database for easy querying and analysis.
2. **Data Analysis and Prediction**: Using Python and various libraries, the data is analyzed to predict match outcomes, particularly focusing on Real Madrid's performance.
3. **Modeling and Prediction**: A simple machine learning model is applied to predict Real Madrid's chances of winning, leveraging select match statistics.

## Code Structure
- `create_db.py`: Handles database connections and operations.
- `etl.py`: Contains the code for extracting, transforming, and loading data.
- `prediction.ipynb`: A Jupyter notebook detailing the analysis and prediction process.
- `main.py`: The FastAPI application for deploying the machine learning model as an API.

## Local Setup
### Installation
- **Python 3.8+** and the following packages:
  - pandas
  - sqlite3
  - scikit-learn
  - matplotlib
  - seaborn
  - fastapi
  - uvicorn
- **SQLite**: For database management.

### Running the Project
1. Set up the SQLite database using `db.py`.
2. Run the ETL process with `etl.py`.
3. Open `prediction.ipynb` in a Jupyter environment to view and run the analysis and prediction code.
4. Start the FastAPI server using `uvicorn main:app --reload` to launch the API.

## Data
The data includes match details such as dates, teams, scores, and various match statistics. It's sourced during the project's ETL process.

## Real Madrid Win Predictor API

### Overview

The API uses a simple trained machine learning model to predict the outcome of Real Madrid matches in La Liga. The prediction is based on the opposing team and other key match details.

### API Endpoint

- **Endpoint**: `/predict_madrid_win`
- **Method**: POST
- **Input**: JSON object with `HomeTeam` and `AwayTeam` information.
- **Output**: JSON object with the prediction result (`Win` or `Lose`).

### Using Swagger UI

Swagger UI provides an interactive way to test the API:

1. **Start the API Server**: Ensure that the FastAPI server is running.

   ```bash
   uvicorn main:app --reload

2. Access Swagger UI: Navigate to http://127.0.0.1:8000/docs in your web browser.

3. Test the Endpoint: Use the Swagger UI to send a request to the /predict_madrid_win endpoint and view the response.

### Model and Encoder Files

The RandomForestClassifier model, a simple yet effective predictive tool, is saved in a file named model.pkl.
The LabelEncoder for team names is saved in a file named encoder.pkl.
These files are used by main.py to make predictions in the API.

_This revision clarifies that the model is simple and specifically tailored to predict Real Madrid's winning likelihood based on selected match criteria._
