# 🫀 Heart Disease Prediction App

This is a machine learning web application built with **Streamlit App** that predicts the likelihood of heart disease in a patient based on user input features.

## 🚀 Features
- Loads a trained ML model (`Random Forest`)
- Scales user input using a saved `StandardScaler`
- Predicts heart disease likelihood
- User-friendly Streamlit interface

## 🧰 Tech Stack
- Python
- Streamlit
- Scikit-learn
- NumPy
- Pandas
- Matplotlib / Seaborn

## 📁 Project Structure
```
heart_disease_predictor/
│
├── heart_disease_app.py        # Streamlit web app
├── heart_disease_model.pkl     # Trained ML model
├── scaler.pkl                  # Fitted scaler for preprocessing
├── requirements.txt            # Python dependencies
└── README.md                   # Project overview and usage guide
```

## 📝 Setup Instructions

1. **Clone or download this repo**
2. **Install dependencies**:
```bash
pip install -r requirements.txt
```

3. **Run the Streamlit app**:
```bash
streamlit run heart_disease_app.py
```

4. **Interact with the app**: Input values and view predictions in your browser.

## 📌 Notes
- Ensure that the `heart_disease_model.pkl` and `scaler.pkl` are in the same directory as the app.
- Model was trained on features including age, sex, chest pain type, cholesterol, etc.

## ✨ Example Prediction
Input: `Male, Age: 58, Cholesterol: 230, ...`  
Output: ✅ *Unlikely to have heart disease*

---

### Author
Built with ❤️ using Streamlit and Scikit-learn.