## **Health Data Generator** 
This script creates a synthetic dataset of 500 patients with realistic health features. Each feature is generated within medically reasonable ranges and a risk_level is assigned based on basic health‑risk rules.

**Features**
- heart_rate — resting heart rate (40–140).
    - Low (<50) or high (>100) increases risk.
- activity_level — weekly activity sessions (0–7).
    - Low activity (<2) increases risk.
- age — patient age (18–90).
    - Older age (>60) increases risk.
- cholesterol — cholesterol level (120–350 mg/dL).
    - High cholesterol (>240) increases risk.
- diabetes — 0 = no, 1 = yes.
    - Diabetes increases risk.

**Risk Calculation**
A patient is labeled high risk (1) if any of these are true:

- heart_rate < 50
- heart_rate > 100
- age > 60
- cholesterol > 240
- diabetes == 1
- activity_level < 2

To mimic real-world imperfect medical data a small amount (10%) of randomness is added.

**Output**
The script saves a file named health_data_v1.csv with 500 rows of clean, ready‑to‑use data.