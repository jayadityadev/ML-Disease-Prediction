# ⚕️ AI-Powered Disease Prediction System

This is an open-source Streamlit-based web app that predicts the likelihood of various diseases using Machine Learning (ML) models. It takes user inputs and provides a risk assessment based on trained models.

## ✨ Features

- 🔍 **Multi-Disease Prediction**: Supports Diabetes, Heart Disease, Lung Cancer, Parkinson's, and Thyroid disorders.
- 🤖 **Machine Learning Models**:
  - 🟢 Diabetes → Random Forest
  - ❤️ Heart Disease → Logistic Regression
  - 🫁 Lung Cancer → Logistic Regression
  - 🧠 Parkinson's → Support Vector Classifier (SVC)
  - 🦋 Thyroid → Logistic Regression
- 🖥 **User-Friendly UI**: Built with Streamlit.
- 📊 **Risk Level Assessment**: Displays a probability score for disease likelihood.
- 🔓 **Open Source**: Licensed under the MIT License.

## 📂 Project Structure

```
Disease_Prediction_Project/  
│── 📁 data/                     # CSV datasets for training models  
│── 📁 frontend/                  # Streamlit frontend files  
│   ├── 📄 app.py                 # Main Streamlit application  
│   ├── 🎨 styles.css             # CSS for UI styling  
│── 📁 models/                    # Trained ML models (saved as .sav files)  
│── 📁 notebooks/                 # Jupyter notebooks for model training  
│   ├── 📜 Diabetes_Training.ipynb  
│   ├── 📜 Heart_Disease_Training.ipynb  
│   ├── 📜 Lung_Cancer_Training.ipynb  
│   ├── 📜 Parkinsons_Training.ipynb  
│   ├── 📜 Thyroid_Training.ipynb  
│── 📁 utils/                     # Helper functions  
│   ├── 🛠 predict.py              # Disease prediction logic  
│   ├── 🧮 risk_assessment.py      # Risk evaluation functions  
│── 📄 .gitignore  
│── 📖 README.md  
│── 📝 LICENSE                     # Open-source MIT License  
```

## 🚀 How to Run

### 1️⃣ Create a Virtual Environment

It's recommended to use a virtual environment to manage dependencies. Run:

```bash
# Create a virtual environment  
python -m venv .venv  

# Activate the virtual environment  
# 🖥 Windows  
.venv\Scripts\activate  

# 🐧 macOS/Linux  
source .venv/bin/activate  
```

### 2️⃣ Install Dependencies

Run the following command to install the required Python libraries:

```bash
pip install -r requirements.txt
```
(If requirements.txt is missing, manually install Streamlit, Scikit-Learn, Pandas, NumPy, etc.)

### 3️⃣ Run the Application

```bash
streamlit run frontend/app.py
```
This will launch the disease prediction system in your browser.

## 🧠 How It Works

1. **User Inputs**: The app collects health parameters.
2. **Model Prediction**: The trained ML model processes inputs and predicts risk.
3. **Risk Level Display**: The result includes risk level (e.g., Low, Medium, High) with a probability score.

## 🔖 Notes

- ⚠️ Personalized health suggestions are NOT implemented yet.
- 🏥 ML models are pre-trained and saved in the models/ directory.
- 📊 Training datasets are available in the data/ directory.

## 🚀 Future Improvements

- ✅ Implement personalized health suggestions.
- ✅ Improve UI/UX for better user experience.
- ✅ Expand the dataset for higher accuracy.
- ✅ Deploy on cloud platforms for public access.

## 🤝 Contributing

This is an open-source project, and contributions are welcome!
To contribute:

1. Fork the repository.
2. Create a new branch for your changes.
3. Submit a pull request with a clear description.

## 📜 License

This project is licensed under the MIT License. See the LICENSE file for details.