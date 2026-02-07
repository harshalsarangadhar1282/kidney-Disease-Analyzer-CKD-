import streamlit as st
import numpy as np

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Chronic Kidney Disease Prediction",
    layout="wide",
    page_icon="🩺"
)

# ---------------- CSS ----------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #f4f7fb, #ffffff);
}
h1, h2, h3 {
    color: #0d47a1;
}
.section {
    background: #ffffff;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.15);
    margin-bottom: 20px;
}
.label {
    font-weight: 700;
    margin-top: 10px;
    color: #263238;
}
.result-good {
    background: #e8f5e9;
    padding: 20px;
    border-radius: 15px;
    font-size: 18px;
    color: #2e7d32;
    font-weight: bold;
}
.result-bad {
    background: #ffebee;
    padding: 20px;
    border-radius: 15px;
    font-size: 18px;
    color: #c62828;
    font-weight: bold;
}
footer {
    text-align:center;
    color:#555;
}
</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown("<h1 style='text-align:center;'>🩺 Chronic Kidney Disease Prediction System</h1>", unsafe_allow_html=True)
st.markdown("---")

# ---------------- INPUT SECTION ----------------
st.subheader("🔍 Patient Medical Details")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.markdown("### 🧑 Basic Information")
    st.markdown("<div class='label'>Age (years)</div>", unsafe_allow_html=True)
    age = st.slider("", 1, 100, 45)

    st.markdown("<div class='label'>Blood Pressure (mmHg)</div>", unsafe_allow_html=True)
    bp = st.slider("", 50, 180, 80)

    st.markdown("<div class='label'>Specific Gravity</div>", unsafe_allow_html=True)
    sg = st.selectbox("", [1.005, 1.010, 1.015, 1.020, 1.025])

    st.markdown("<div class='label'>Albumin</div>", unsafe_allow_html=True)
    al = st.slider("", 0, 5, 1)

    st.markdown("<div class='label'>Sugar</div>", unsafe_allow_html=True)
    su = st.slider("", 0, 5, 0)
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.markdown("### 🧪 Urine Test Results")
    st.markdown("<div class='label'>Red Blood Cells</div>", unsafe_allow_html=True)
    rbc = st.selectbox("", ["normal", "abnormal"])

    st.markdown("<div class='label'>Pus Cell</div>", unsafe_allow_html=True)
    pc = st.selectbox("", ["normal", "abnormal"])

    st.markdown("<div class='label'>Pus Cell Clumps</div>", unsafe_allow_html=True)
    pcc = st.selectbox("", ["present", "notpresent"])

    st.markdown("<div class='label'>Bacteria</div>", unsafe_allow_html=True)
    ba = st.selectbox("", ["present", "notpresent"])

    st.markdown("<div class='label'>Blood Glucose Random (mg/dl)</div>", unsafe_allow_html=True)
    bgr = st.slider("", 70, 500, 120)
    st.markdown("</div>", unsafe_allow_html=True)

with col3:
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.markdown("### 🧬 Blood Test Results")
    st.markdown("<div class='label'>Blood Urea (mg/dl)</div>", unsafe_allow_html=True)
    bu = st.slider("", 10, 200, 40)

    st.markdown("<div class='label'>Serum Creatinine (mg/dl)</div>", unsafe_allow_html=True)
    sc = st.slider("", 0.4, 15.0, 1.2)

    st.markdown("<div class='label'>Sodium (mEq/L)</div>", unsafe_allow_html=True)
    sod = st.slider("", 110, 160, 135)

    st.markdown("<div class='label'>Potassium (mEq/L)</div>", unsafe_allow_html=True)
    pot = st.slider("", 2.0, 7.0, 4.5)

    st.markdown("<div class='label'>Haemoglobin (g/dl)</div>", unsafe_allow_html=True)
    hemo = st.slider("", 3.0, 17.0, 12.0)
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")

st.markdown("<div class='section'>", unsafe_allow_html=True)
st.subheader("❤️ Medical History")
col4, col5, col6 = st.columns(3)

with col4:
    st.markdown("<div class='label'>Hypertension</div>", unsafe_allow_html=True)
    htn = st.selectbox("", ["yes", "no"])

    st.markdown("<div class='label'>Diabetes Mellitus</div>", unsafe_allow_html=True)
    dm = st.selectbox("", ["yes", "no"])

with col5:
    st.markdown("<div class='label'>Coronary Artery Disease</div>", unsafe_allow_html=True)
    cad = st.selectbox("", ["yes", "no"])

    st.markdown("<div class='label'>Appetite</div>", unsafe_allow_html=True)
    appet = st.selectbox("", ["good", "poor"])

with col6:
    st.markdown("<div class='label'>Pedal Edema</div>", unsafe_allow_html=True)
    pe = st.selectbox("", ["yes", "no"])

    st.markdown("<div class='label'>Anemia</div>", unsafe_allow_html=True)
    ane = st.selectbox("", ["yes", "no"])
st.markdown("</div>", unsafe_allow_html=True)

# ---------------- RULE-BASED PREDICTION ----------------
risk_score = 0
if sc > 1.5: risk_score += 2
if bu > 50: risk_score += 1
if hemo < 11: risk_score += 1
if bp > 140: risk_score += 1
if dm == "yes": risk_score += 1
if htn == "yes": risk_score += 1
if ane == "yes": risk_score += 1

# ---------------- RESULT ----------------
st.markdown("---")
st.subheader("📊 Prediction Result")

if st.button("🔍 Predict CKD"):
    if risk_score >= 4:
        st.markdown("<div class='result-bad'>❌ High Risk of Chronic Kidney Disease<br>⚠️ Consult a nephrologist immediately.</div>", unsafe_allow_html=True)
    else:
        st.markdown("<div class='result-good'>✅ Low Risk of Chronic Kidney Disease<br>👍 Patient condition appears normal.</div>", unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown("<footer><b>CKD Classification Project | Machine Learning & Streamlit</b></footer>", unsafe_allow_html=True)
