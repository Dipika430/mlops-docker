import pickle

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

print("Model loaded successfully!")

# Dummy prediction
print("Prediction:", model.predict([[5]]))