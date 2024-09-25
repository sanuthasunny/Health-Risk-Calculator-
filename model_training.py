import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle

# Load dataset
data = pd.read_csv('framingham_heart_study.csv')

# Preprocess data
data.dropna(inplace=True)

# Define features and target
X = data[['age', 'gender', 'sysBP', 'diaBP', 'BMI', 'cholesterol', 'diabetes', 'smoker']]
y = data['heart_disease']

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train RandomForest model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save the model
with open('health_risk_model.pkl', 'wb') as f:
    pickle.dump(model, f)
