import streamlit as st
import numpy as np
import joblib

# ---------------- LOAD MODELS ----------------
vitd_model = joblib.load("vitamin_d_model.pkl")
cardio_model = joblib.load("cardio_model.pkl")

st.title("Integrated Vitamin D & Cardiovascular Risk Assessment")

# ---------------- STEP 1 ----------------
st.markdown("### Step 1: Vitamin D Risk Assessment")

sun_duration = st.selectbox("Sun Exposure Duration",
                             ["<10 min", "10–20 min", "20–30 min", ">30 min"])

sun_time = st.selectbox("Sun Exposure Time",
                        ["Before 10 AM", "10AM–3PM", "After 3PM"])

clothing = st.selectbox("Clothing Pattern",
                        ["Fully Covered", "Partial", "Arms/Face Exposed"])

sunscreen = st.selectbox("Sunscreen Use",
                         ["Daily", "Occasionally", "Never"])

milk = st.selectbox("Milk Intake",
                    ["Rarely", "3–4/week", "Daily"])

egg = st.selectbox("Egg Intake",
                   ["Never", "1–2/week", "≥3/week"])

fish = st.selectbox("Fish Intake",
                    ["Never", "Monthly", "Weekly"])

activity_vitd = st.selectbox("Physical Activity",
                             ["Sedentary", "Occasional", "Regular"])

bmi_category = st.selectbox("BMI Category",
                            ["≥25", "18.5–24.9", "<18.5"])


def encode(value, options):
    return options.index(value) + 1


# -------- SESSION STORAGE --------
if "vitd_prediction" not in st.session_state:
    st.session_state.vitd_prediction = None


# -------- VITAMIN D BUTTON --------
if st.button("Predict Vitamin D Risk"):

    vitd_input = np.array([[
        encode(sun_duration, ["<10 min", "10–20 min", "20–30 min", ">30 min"]),
        encode(sun_time, ["Before 10 AM", "10AM–3PM", "After 3PM"]),
        encode(clothing, ["Fully Covered", "Partial", "Arms/Face Exposed"]),
        encode(sunscreen, ["Daily", "Occasionally", "Never"]),
        encode(milk, ["Rarely", "3–4/week", "Daily"]),
        encode(egg, ["Never", "1–2/week", "≥3/week"]),
        encode(fish, ["Never", "Monthly", "Weekly"]),
        encode(activity_vitd, ["Sedentary", "Occasional", "Regular"]),
        encode(bmi_category, ["≥25", "18.5–24.9", "<18.5"])
    ]])

    st.session_state.vitd_prediction = vitd_model.predict(vitd_input)[0]


# -------- SHOW VITAMIN D RESULT --------
if st.session_state.vitd_prediction is not None:

    st.markdown("## Vitamin D Result")

    if st.session_state.vitd_prediction == 0:
        st.success("🟢 Low Vitamin D Risk")
    elif st.session_state.vitd_prediction == 1:
        st.warning("🟡 Moderate Vitamin D Risk")
    else:
        st.error("🔴 High Vitamin D Risk")

    # ---------------- STEP 2 ----------------
    st.markdown("---")
    st.markdown("### Step 2: Cardiovascular Risk Assessment")

    age = st.number_input("Age", min_value=40, max_value=60)
    bmi = st.number_input("BMI", min_value=15.0, max_value=40.0)
    bp = st.number_input("Systolic Blood Pressure", min_value=90, max_value=200)
    cholesterol = st.number_input("Cholesterol (mg/dL)", min_value=100, max_value=400)
    activity_cardio = st.selectbox("Physical Activity Level",
                                    ["Low", "Moderate", "High"])
    smoking = st.selectbox("Smoking Status", ["No", "Yes"])
    diabetes = st.selectbox("Diabetes", ["No", "Yes"])

    if st.button("Predict Cardiovascular Risk"):

        cardio_input = np.array([[
            age,
            bmi,
            bp,
            cholesterol,
            ["Low", "Moderate", "High"].index(activity_cardio) + 1,
            ["No", "Yes"].index(smoking),
            ["No", "Yes"].index(diabetes),
            st.session_state.vitd_prediction
        ]])

        cardio_prediction = cardio_model.predict(cardio_input)[0]

        st.markdown("## Final Cardiovascular Risk Result")

        if cardio_prediction == 0:
            st.success("🟢 Low Cardiovascular Risk")
        elif cardio_prediction == 1:
            st.warning("🟡 Moderate Cardiovascular Risk")
        else:
            st.error("🔴 High Cardiovascular Risk")


st.markdown("---")
st.caption("Academic Research Project – Vitamin D & Cardiovascular Risk Analysis")