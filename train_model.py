import pickle
from sklearn.linear_model import LinearRegression

# Train simple model
X = [[1],[2],[3],[4]]
y = [2,4,6,8]

model = LinearRegression()
model.fit(X, y)

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ model.pkl created successfully!")