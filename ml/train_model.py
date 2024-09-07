import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from joblib import dump


data = pd.DataFrame({
    'time_slot': ['morning', 'afternoon', 'evening'],
    'on_time_delivery': [0.8, 0.9, 0.7],
    'user_preference': [0.6, 0.7, 0.5]
})


data['time_slot'] = data['time_slot'].map({'morning': 0, 'afternoon': 1, 'evening': 2})


X = data[['time_slot', 'user_preference']]
y = data['on_time_delivery']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)


dump(model, 'delivery_model.joblib')
print("Model trained and saved.")
