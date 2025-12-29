## **Health Risk Prediction using ML and AI-generated advice**

This project builds a machine‑learning model using a Random Forest classifier to predict a person's health risk level based on key health indicators. It also integrates the OpenAI API to generate personalized health advice based on the model’s prediction.

**Features**
- Trains a Random Forest model on health data
- Predicts health risk using the trained model
- Generates personalized health advice using OpenAI
- Evaluates the model using test dataset (accuracy, classification report and confusion matrix)
- Evaluates model performance on an unseen patient data outside the train/test split

**Requirements**

Dependencies:
- pandas
- scikit-learn
- python-dotenv
- openai
- ipykernel

.env file contains the OpenAI API key (OPENAI_API_KEY).

**How It Works**
1. Loads health data from health_data_v1.csv (Synthetic dataset generated using generate-synthetic-health-data.py script).

2. Uses the following features for prediction:
    - heart_rate
    - activity_level
    - age
    - cholesterol
    - diabetes

3. Trains a Random Forest model to classify risk_level (low/high).

4. Provides two main functions:
    - predict_health_risk(...) → returns "low" or "high"
    - generate_health_advice(...) → returns AI‑generated advice

5. Evaluates the model.

**Notes**
- This project is for educational purposes and not medical diagnosis.  