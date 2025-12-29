import pandas as pd
import numpy as np

np.random.seed(14)

num_samples = 500

# Generate features
age = np.random.randint(18, 90, num_samples)

heart_rate = np.random.normal(75, 15, num_samples).astype(int)
heart_rate = np.clip(heart_rate, 40, 140)

activity_level = np.random.randint(0, 8, num_samples)

cholesterol = np.random.normal(210, 40, num_samples).astype(int)
cholesterol = np.clip(cholesterol, 120, 350)

diabetes = np.random.choice([0, 1], size=num_samples, p=[0.82, 0.18])

# Compute risk level using realistic rules
risk = []
for i in range(num_samples):
    hr = heart_rate[i]
    act = activity_level[i]
    ag = age[i]
    chol = cholesterol[i]
    dia = diabetes[i]

    high_risk = (
        hr < 50 or
        hr > 100 or
        ag > 60 or
        chol > 240 or
        dia == 1 or
        act < 2
    )

    # Add small noise (10%)
    if np.random.rand() < 0.10:
        high_risk = not high_risk

    risk.append(1 if high_risk else 0)

# Build DataFrame
df = pd.DataFrame({
    "heart_rate": heart_rate,
    "activity_level": activity_level,
    "age": age,
    "cholesterol": cholesterol,
    "diabetes": diabetes,
    "risk_level": risk
})

# Save to CSV
df.to_csv("health_data_v1.csv", index=False)

print("health data csv generated with 500 rows.")
print(df.head())
