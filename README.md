# 🫀 Heart Disease Prediction using Machine Learning

## 📌 Overview
This project develops a machine learning model to predict the likelihood of heart disease based on clinical features, including age, blood pressure, cholesterol levels, and other relevant factors. The goal is to assist in early detection and support medical decision-making through data-driven insights

## 🚀 Features
- Exploratory Data Analysis
- Data Preprocessing: Feature scaling, feature engineering
- Model Selection: Evaluation of multiple ML classifiers (e.g., Random Forest, XGBoost)
- Performance Metrics: Accuracy, precision, recall, F1-score, ROC-AUC curve
- Deployment: Interactive web interface using Streamlit

## 🛠️ Installation

1. **Clone the repository**

```bash
git clone https://github.com/auspicie/Heart-Disease_Prediction-ML.git
cd heart-disease-prediction

2. **Install dependencies**
pip install -r requirements.txt
```bash

## 💻 Usage
**Run the Streamlit app**:
streamlit run heart_disease_app.py


**Interact with the app**: Input values and view predictions in your browser.
## ✨ Example Prediction
Input: `Male, Age: 58, Cholesterol: 230, ...`  
Output: ✅ *Unlikely to have heart disease*

---

## 📊 Dataset
Source: [https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset]

Clinical Features: Age, cholesterol, blood pressure, chest pain type, smoking history, etc.

## 🤝 Contributing

Contributions are welcome! Feel free to:
Open an issue
Submit a pull request

## 📄 License
This project is licensed under the MIT License.

## 📌 Notes
- Ensure that the `heart_disease_model.pkl` and `scaler.pkl` are in the same directory as the app.

### Author: Samsudeen Bankole
Built with ❤️ using Streamlit and Scikit-learn.