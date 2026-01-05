import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score
import seaborn as sns
import matplotlib.pyplot as plt

# 1. PAGE CONFIGURATION
st.set_page_config(page_title="AI NIDS Dashboard", layout="wide")

st.title("AI-Powered Network Intrusion Detection System")
st.markdown("""
### Project Overview
This system uses the **Random Forest Algorithm** to analyze network traffic.
* **Benign:** Safe, normal traffic.
* **Malicious:** Potential cyberattacks (DDoS, Port Scan, etc.).
""")

# 2. DATA LOADING (Simulated Dataset)
@st.cache_data
def load_data():
    np.random.seed(42)
    n_samples = 5000
    data = {
        'Destination_Port': np.random.randint(1, 65535, n_samples),
        'Flow_Duration': np.random.randint(100, 100000, n_samples),
        'Total_Fwd_Packets': np.random.randint(1, 100, n_samples),
        'Packet_Length_Mean': np.random.randint(20, 1500, n_samples),
        'Active_Mean': np.random.randint(0, 1000, n_samples),
        'Label': np.random.choice([0, 1], size=n_samples, p=[0.8, 0.2])
    }
    return pd.DataFrame(data)

df = load_data()

# 3. SIDEBAR - MODEL TRAINING
st.sidebar.header("Settings")
if st.sidebar.button("Train Model Now"):
    X = df.drop('Label', axis=1)
    y = df['Label']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Save model and test data to session state
    st.session_state['model'] = model
    st.session_state['test_data'] = (X_test, y_test)
    st.sidebar.success("Model Trained Successfully!")

# 4. DASHBOARD VISUALS
if 'model' in st.session_state:
    model = st.session_state['model']
    X_test, y_test = st.session_state['test_data']
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)

    st.subheader("1. Model Performance")
    m1, m2, m3 = st.columns(3)
    m1.metric("Accuracy", f"{acc*100:.2f}%")
    m2.metric("Total Samples", len(df))
    m3.metric("Detected Threats", np.sum(y_pred))

    st.write("### Confusion Matrix")
    cm = confusion_matrix(y_test, y_pred)
    fig, ax = plt.subplots(figsize=(5, 3))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Reds', xticklabels=['Safe', 'Attack'], yticklabels=['Safe', 'Attack'], ax=ax)
    st.pyplot(fig)
else:
    st.warning("Please click 'Train Model Now' in the sidebar to begin.")

# 5. LIVE ATTACK SIMULATOR
st.divider()
st.subheader("2. Live Traffic Simulator (Test the AI)")
st.write("Enter network packet details below to see if the AI flags it as an attack.")

c1, c2, c3, c4, c5 = st.columns(5)
p_port = c1.number_input("Dest Port", 0, 65535, 80)
p_dur = c2.number_input("Duration (ms)", 0, 100000, 500)
p_pkts = c3.number_input("Total Packets", 0, 500, 10)
p_len = c4.number_input("Packet Len Mean", 0, 1500, 64)
p_active = c5.number_input("Active Mean", 0, 1000, 0)

if st.button("Analyze Packet"):
    if 'model' in st.session_state:
        # Match the exact feature names used during training
        input_data = pd.DataFrame([[p_port, p_dur, p_pkts, p_len, p_active]], 
                                  columns=['Destination_Port', 'Flow_Duration', 'Total_Fwd_Packets', 'Packet_Length_Mean', 'Active_Mean'])

        prediction = st.session_state['model'].predict(input_data)

        if prediction[0] == 1:
            st.error("🚨 ALERT: Malicious Traffic Detected!")
        else:
            st.success("✅ Normal Traffic: Packet is safe.")
    else:
        st.error("You must train the model before testing packets.")
