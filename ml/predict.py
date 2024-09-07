from joblib import load
import numpy as np
import os

# Define the correct path to the model file dynamically to avoid file not found errors
model_path = os.path.join(os.path.dirname(__file__), 'ml', 'delivery_model.joblib')

# Try to load the model and handle errors gracefully
try:
    model = load(model_path)
except FileNotFoundError:
    print(f"Error: Model file not found at {model_path}. Please check the path and try again.")
    # Handle the error appropriately, for example, by returning a default value or exiting
    model = None  # Set to None to prevent further usage if not found

def predict_best_time_slot(preferences):
    # Check if the model is loaded correctly
    if model is None:
        print("Model not loaded. Unable to predict best time slot.")
        return "Model error"  # Return an error message or handle accordingly

    # Define mapping and available time slots
    preference_map = {'morning': 0, 'afternoon': 1, 'evening': 2}
    time_slots = ['morning', 'afternoon', 'evening']
    predictions = {}

    # Predict the preference scores for each time slot
    for slot in time_slots:
        slot_code = preference_map.get(slot)
        user_pref = preferences.get(slot, 0)  # Default to 0 if not specified
        
        # Predict the score using the loaded model and handle any potential errors
        try:
            prediction = model.predict([[slot_code, user_pref]])
            predictions[slot] = prediction[0]  # Add the prediction to the dictionary
        except Exception as e:
            print(f"Error during prediction for {slot}: {e}")
            predictions[slot] = -1  # Assign a negative value in case of an error

    # Determine the best time slot based on the highest predicted score
    best_slot = max(predictions, key=predictions.get)
    return best_slot
