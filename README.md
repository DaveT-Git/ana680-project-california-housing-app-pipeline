# California Housing Price Predictor App

Flask web application that predicts median house values (in $100,000 units) for California census block groups using a linear regression model trained on the classic California Housing dataset from scikit-learn (1990 census data).

## Important Disclaimer

**This project is for educational and demonstration purposes only.**

The model is a simple linear regression baseline using five features (median income, average rooms, house age, latitude, longitude). It achieves modest performance (test R² ≈ 0.617, RMSE ≈ 0.712) but is **not** intended for real estate valuation, investment decisions, lending, or any financial/professional use.

- Predictions are approximations based on historical census data and do **not** reflect current market conditions, property-specific features, or economic factors.
- Housing prices are highly location-dependent and volatile — always consult licensed real estate professionals, appraisers, or official sources.
- The app demonstrates machine learning deployment (Flask + Docker + CI/CD + Heroku + AWS EC2) and is **not** production-grade or certified.

## Features Used
- MedInc: Median income in the block group (in tens of thousands of dollars)  
- HouseAge: Median house age in the block group (in years)  
- AveRooms: Average number of rooms per household  
- Latitude: Latitude of the block group  
- Longitude: Longitude of the block group  

## Model
- Linear Regression with StandardScaler in a scikit-learn Pipeline  
- Test performance: RMSE ≈ 0.712, R² ≈ 0.617  
- Deployed via Docker container (Gunicorn production server)  

Run locally:  
`python app.py`  
Open: http://127.0.0.1:5000

## Live Deployments
**Heroku (auto-deployed via GitHub Actions):**  
https://ca-housing-app-djt84-f1fd66680ef6.herokuapp.com/

**AWS EC2 (manual Docker Compose + Nginx proxy):**  
http://54.167.189.220 (t3.micro instance, may be stopped for cost control)

**Docker Hub Image:**  
https://hub.docker.com/r/djt84/ca-housing-app

## Detailed Documentation
For full project narrative, CI/CD pipeline details, troubleshooting notes, visualizations (including California geography with house value clusters), final directory structure diagram, and step-by-step deployment walkthroughs, see:  
→ [Detailed Project README](./README-detailed.md)  
(or `/docs/README-detailed.md` if moved to a docs folder)

### Screenshots

#### 1. Main Input Form
<img width="450" alt="California Housing Predictor Form" src="https://github.com/user-attachments/assets/...replace-with-your-screenshot-id..." />

Enter values for the five features and get a predicted median house value.

#### 2. Prediction Result Example
<img width="450" alt="Prediction Output" src="https://github.com/user-attachments/assets/...replace-with-your-screenshot-id..." />

Displayed in both scaled units and approximate dollars after submission.
