import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import pickle

# 1. Create Synthetic Bank Customer Data
np.random.seed(42)
n_samples = 1000

# Generating random features
credit_score = np.random.randint(300, 850, n_samples)
geography = np.random.choice(['France', 'Spain', 'Germany'], n_samples)
gender = np.random.choice(['Male', 'Female'], n_samples)
age = np.random.randint(18, 92, n_samples)
tenure = np.random.randint(0, 11, n_samples)
balance = np.random.uniform(0, 250000, n_samples)
# Many users have 0 balance, let's simulate that
balance[np.random.rand(n_samples) < 0.3] = 0
num_products = np.random.choice([1, 2, 3, 4], n_samples, p=[0.5, 0.4, 0.08, 0.02])
has_crcard = np.random.choice([0, 1], n_samples)
is_active = np.random.choice([0, 1], n_samples)
estimated_salary = np.random.uniform(10000, 200000, n_samples)

# Generate target (Churn: 1 = Left, 0 = Stayed) based on some simplistic logic
churn_prob = (
    (age > 50) * 0.3 + 
    (balance > 100000) * -0.1 + 
    (is_active == 0) * 0.2 + 
    (geography == 'Germany') * 0.15 + 
    (num_products >= 3) * 0.3
)
churn_prob = np.clip(churn_prob + np.random.uniform(-0.1, 0.1, n_samples), 0, 1)
churn = (churn_prob > 0.4).astype(int)

# Create DataFrame
df = pd.DataFrame({
    'CreditScore': credit_score,
    'Geography': geography,
    'Gender': gender,
    'Age': age,
    'Tenure': tenure,
    'Balance': balance,
    'NumOfProducts': num_products,
    'HasCrCard': has_crcard,
    'IsActiveMember': is_active,
    'EstimatedSalary': estimated_salary,
    'Churn': churn
})

# 2. Prepare Data for Model Pipeline
X = df.drop('Churn', axis=1)
y = df['Churn']

# Define categorical & numerical columns
categorical_cols = ['Geography', 'Gender']
numerical_cols = ['CreditScore', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'HasCrCard', 'IsActiveMember', 'EstimatedSalary']

# Preprocessing steps
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numerical_cols),
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_cols)
    ]
)

# Create the pipeline with RandomForest
model_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier(n_estimators=100, random_state=42))
])

# Train Model
print("Training the 10-feature Random Forest model...")
model_pipeline.fit(X, y)

# 3. Save the model to Desktop
out_path = r"C:\Users\ASUS\Desktop\test_model.pkl"
with open(out_path, 'wb') as f:
    pickle.dump(model_pipeline, f)

print(f"Model successfully saved to: {out_path}")
