# California Housing Price Predictor – Detailed Documentation

This document provides in-depth context, visualizations, directory structure, and deployment notes for the project.

## Dataset & Model Overview
The model uses the California Housing dataset (scikit-learn / 1990 census block groups, 20,640 samples). After EDA, correlation analysis, outlier clipping (1%/99% on MedInc and AveRooms), and feature selection, five features were chosen to balance performance and simplicity:

- **MedInc** — strongest predictor (corr ~0.69)  
- **AveRooms**, **HouseAge** — moderate positive influence  
- **Latitude** & **Longitude** — kept separate to capture multiple high-value clusters (Bay Area + Los Angeles areas)

**Performance (test set):**  
MSE: 0.5068 | RMSE: 0.7119 | R²: 0.6167  

While not state-of-the-art (tree-based models reach R² > 0.80), it serves as a clean, fast baseline for deployment-focused learning.

## Importance of Location in California Housing
Location is one of the most critical drivers of house prices in California due to coastal access, job centers, schools, and topography. The scatterplot below shows median house values by geographic coordinates:

![California House Values by Location](images/ca-geography-house-values.png)

**Key observations:**
- High-value clusters appear in the **San Francisco Bay Area** (top-left, around lat 37–38, lon -122) and **Los Angeles / Orange County** regions (bottom-right, around lat 33–34, lon -118).
- Lower values dominate inland and northern rural areas.
- This geographic pattern justifies keeping **Latitude** and **Longitude** as separate features rather than a single distance metric — a distance-to-SF feature would undervalue LA proximity.

## Final Project Directory Structure
```
CA-housing-app/ 
├── app.py 
├── ANA680_Final_Project.ipynb
├── ca_housing_pipeline.pkl 
├── requirements.txt 
├── Dockerfile 
├── .dockerignore 
├── .python-version 
├── nginx.conf 
├── docker-compose.yml 
├── .github/ 
│   └── workflows/ 
│       └── deploy-to-heroku.yml 
├── tests/ 
│   └── test_app.py 
├── templates/ 
│   └── index.html 
├── assets/ 
│   ├── ca-geography-house-values.png 
│   ├── app_blank.png 
│   └── app_filled_in.png 
├── README.md 
└── README-detailed.md
```
## Deployment Summary
- **Local**: `python app.py` → http://127.0.0.1:5000  
- **Heroku**: Auto-deployed via GitHub Actions on push to main  
- **AWS EC2**: t3.micro instance, Docker Compose with app + Nginx proxy  
  - Public URL (when running): http://54.167.189.220  
  - Security Group: ports 80 (HTTP), 22 (SSH) open  
  - Auto-start via systemd service

Step-by-step narrative




## Acknowledgments
Built as part of an academic MLOps/DevOps course focusing on reproducible pipelines, containerization, and multi-cloud deployment.


