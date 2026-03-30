# 🏦 Bank Churn Prediction

## 📌 Overview

This project focuses on predicting whether a bank customer will **leave (churn)** or **stay** using machine learning techniques. Customer churn prediction helps businesses take proactive actions to retain customers and reduce revenue loss.

---

## 🎯 Problem Statement

Customer churn is a major challenge in the banking sector. The goal of this project is to build a model that can accurately predict whether a customer is likely to leave the bank based on their historical data.

---

## 📊 Dataset

* The dataset contains **10,000 customer records** with multiple features. ([bankchurn.vercel.app][1])
* Target variable: **Exited (1 = churn, 0 = stay)**
* Key features include:

  * Credit Score
  * Geography
  * Gender
  * Age
  * Tenure
  * Balance
  * Number of Products
  * Has Credit Card
  * Is Active Member
  * Estimated Salary

---

## ⚙️ Project Workflow

### 1. Data Preprocessing

* Removed unnecessary columns (CustomerId, Surname, etc.)
* Handled missing values and duplicates
* Encoded categorical variables
* Feature scaling

### 2. Exploratory Data Analysis (EDA)

* Visualized data distribution
* Checked correlations between features
* Identified class imbalance in churn data

### 3. Model Building

Implemented and compared multiple machine learning models:

* Logistic Regression
* Decision Tree
* Random Forest
* K-Nearest Neighbors
* Support Vector Machine
* (Optional) Deep Learning / ANN

### 4. Model Evaluation

* Accuracy Score
* Confusion Matrix
* Precision, Recall, F1-score
* ROC-AUC Curve

---

## 📈 Key Insights

* Customer churn is typically **imbalanced (~20% churn rate)** ([galajainam.com][2])
* Age, balance, and activity status strongly influence churn
* Active members are less likely to leave
* Customers with low engagement are at higher risk

---

## 🛠️ Tech Stack

* Python 🐍
* Pandas & NumPy
* Matplotlib & Seaborn
* Scikit-learn
* (Optional) TensorFlow / Keras

---

## 🚀 How to Run

```bash
# Clone the repository
git clone https://github.com/your-username/Bank-Churn-Prediction.git

# Navigate to project folder
cd Bank-Churn-Pr

# Install dependencies
pip install -r requirements.txt

# Run notebook / script
jupyter notebook
```



---

## 📌 Future Improvements

* Hyperparameter tuning
* Deployment using Flask / Streamlit
* Real-time prediction API
* Feature engineering improvements

---

## 🤝 Contributing

Feel free to fork this repository and contribute by improving models, adding features, or optimizing performance.

---

## 📬 Contact

* LinkedIn: https://linkedin.com/in/neeraj-ch7
* GitHub: https://github.com/neeraj-ch7

---

## ⭐ If you like this project

Give it a star ⭐ on GitHub!

[1]: https://bankchurn.vercel.app/?utm_source=chatgpt.com "Bank Churn Prediction Model"
[2]: https://www.galajainam.com/projects/customer-churn/index.html?utm_source=chatgpt.com "Customer Churn Prediction | Jainam Gala"
