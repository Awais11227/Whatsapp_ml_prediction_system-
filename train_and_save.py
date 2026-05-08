import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

# Load dataset
df = pd.read_csv("Churn_Modelling.csv")

# Drop unnecessary columns
df.drop(['RowNumber', 'CustomerId', 'Surname'], axis=1, inplace=True)

# One-hot encoding
df = pd.get_dummies(df, columns=['Geography', 'Gender'], drop_first=True)

# Features and target
X = df.drop('Exited', axis=1)
y = df['Exited']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# Scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Model
model = LogisticRegression(max_iter=200)
model.fit(X_train_scaled, y_train)

# Accuracy
accuracy = model.score(X_test_scaled, y_test)
print("Model Accuracy:", accuracy)

# Save model + scaler
joblib.dump(model, "artifacts/model.pkl")
joblib.dump(scaler, "artifacts/scaler.pkl")

# Save feature order (VERY IMPORTANT for WhatsApp input)
joblib.dump(list(X.columns), "artifacts/features.pkl")

print("Model, scaler, and features saved successfully.")