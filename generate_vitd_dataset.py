import pandas as pd
import random

# Number of samples
num_samples = 300

data = []

for _ in range(num_samples):

    # Randomly generate encoded responses
    sun_duration = random.randint(1, 4)
    sun_time = random.randint(1, 3)
    clothing = random.randint(1, 3)
    sunscreen = random.randint(1, 3)
    milk = random.randint(1, 3)
    egg = random.randint(1, 3)
    fish = random.randint(1, 3)
    activity = random.randint(1, 3)
    bmi = random.randint(1, 3)

    # Calculate Risk Score Based on Your Scoring Rules
    
    risk_score = 0

    # Sun Duration
    if sun_duration == 1:
        risk_score += 2
    elif sun_duration == 2:
        risk_score += 1

    # Sun Time
    if sun_time == 3:
        risk_score += 1

    # Clothing
    if clothing == 1:
        risk_score += 2
    elif clothing == 2:
        risk_score += 1

    # Sunscreen
    if sunscreen == 1:
        risk_score += 1

    # Milk
    if milk == 1:
        risk_score += 2
    elif milk == 2:
        risk_score += 1

    # Egg
    if egg == 1:
        risk_score += 2
    elif egg == 2:
        risk_score += 1

    # Fish
    if fish == 1:
        risk_score += 2
    elif fish == 2:
        risk_score += 1

    # Activity
    if activity == 1:
        risk_score += 1

    # BMI
    if bmi == 1:
        risk_score += 1

    # Assign Risk Label
    if risk_score <= 3:
        label = 0  # Low
    elif risk_score <= 6:
        label = 1  # Moderate
    else:
        label = 2  # High

    data.append([
        sun_duration, sun_time, clothing, sunscreen,
        milk, egg, fish, activity, bmi, label
    ])

# Create DataFrame
columns = [
    "Sun_Duration", "Sun_Time", "Clothing", "Sunscreen",
    "Milk", "Egg", "Fish", "Activity", "BMI",
    "VitD_Label"
]

df = pd.DataFrame(data, columns=columns)

# Save CSV
df.to_csv("vitamin_d_data.csv", index=False)

print("Dataset generated successfully!")
print("Shape:", df.shape)