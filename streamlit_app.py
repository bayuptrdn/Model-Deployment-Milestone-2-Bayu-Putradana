import streamlit as st
import eda
import prediction

# ===== Sidebar Navigation =====
with st.sidebar:
    st.title("Weather Prediction App")
    st.markdown("---")

    page = st.radio("Pilih Halaman:", ("EDA", "Model Demo"))

    st.markdown("---")
    st.subheader("About Application")
    st.write("""
    This application provides an **Exploratory Data Analysis (EDA)** 
    and a **weather prediction demo** using the **XGBoost** model 
    based on historical weather data **across Australia**.
    """)

# ===== Page Routing =====
if page == "EDA":
    eda.run()  # Panggil fungsi run() dari eda.py
else:
    prediction.run()  # Panggil fungsi run() dari prediction.py
