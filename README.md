## **Health Monitoring System with ML Risk Prediction and AI‑Generated Advice**

This project builds a machine learning model using a Random Forest classifier to predict a person's health risk level based on key health indicators. It also integrates the OpenAI API to generate personalized health advice based on the model’s predicted risk level together with the patient’s health indicators.

**Features**

- Trains a Random Forest ML model on health data
- Predicts health risk using the trained model
- Generates personalized health advice using OpenAI (GPT-4o)
- Evaluates the model using test dataset (accuracy, classification report and confusion matrix)
- Illustrates how the model predicts risk and produces advice for a new patient input outside the train/test split

**Requirements**

- Dependencies:
    - pandas
    - scikit-learn
    - python-dotenv
    - numpy
    - openai
    - ipykernel

  To install the dependencies: pip install -r requirements.txt

- .env file contains the OpenAI API key (OPENAI_API_KEY).

**How It Works**

- Loads health data from health_data_v1.csv (Synthetic dataset generated using generate-synthetic-health-data.py script).
- Uses the following features for prediction:
    - heart_rate
    - activity_level
    - age
    - cholesterol
    - diabetes
- Trains a Random Forest model to classify risk_level (low/high).
- Provides two main functions:
    - predict_health_risk(...) → returns "low" or "high"
    - generate_health_advice(...) → returns AI‑generated advice
- Evaluates the model using test data.
- Check the health monitoring system for a new patient input. 

**Notes**

- This project is for educational purposes and not medical diagnosis.  