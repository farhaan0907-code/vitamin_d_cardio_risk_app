import pandas as pd
import random

num_samples = 400
data = []

for _ in range(num_samples):

    age = random.randint(40, 60)  # perimenopausal
    bmi = random.randint(18, 35)
    bp = random.randint(100, 170)
    cholesterol = random.randint(150, 300)
    activity = random.randint(1, 3)   # 1=Low 2=Moderate 3=High
    smoking = random.randint(0, 1)    # 0=No 1=Yes
    diabetes = random.randint(0, 1)   # 0=No 1=Yes
    vitd_risk = random.randint(0, 2)  # 0=Low 1=Moderate 2=High

    risk_score = 0

    # Age risk
    if age > 50:
        risk_score += 1

    # BMI risk
    if bmi > 30:
        risk_score += 2
    elif bmi > 25:
        risk_score += 1

    # BP risk
    if bp > 140:
        risk_score += 2
    elif bp > 120:
        risk_score += 1

    # Cholesterol risk
    if cholesterol > 240:
        risk_score += 2
    elif cholesterol > 200:
        risk_score += 1

    # Activity protective
    if activity == 1:
        risk_score += 1

    # Smoking
    if smoking == 1:
        risk_score += 2

    # Diabetes
    if diabetes == 1:
        risk_score += 2

    # Vitamin D linkage
    if vitd_risk == 2:
        risk_score += 2
    elif vitd_risk == 1:
        risk_score += 1

    # Assign label
    if risk_score <= 3:
        label = 0
    elif risk_score <= 6:
        label = 1
    else:
        label = 2

    data.append([
        age, bmi, bp, cholesterol,
        activity, smoking, diabetes,
        vitd_risk, label
    ])

columns = [
    "Age", "BMI", "BP", "Cholesterol",
    "Activity", "Smoking", "Diabetes",
    "VitD_Risk", "Cardio_Label"
]

df = pd.DataFrame(data, columns=columns)

df.to_csv("cardio_data.csv", index=False)

print("Cardio dataset generated!")
print(df["Cardio_Label"].value_counts())