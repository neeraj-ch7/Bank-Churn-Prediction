import pickle

model_path = r"C:\Users\ASUS\Desktop\model.pkl"
try:
    with open(model_path, "rb") as f:
        model = pickle.load(f)
    print("Model type:", type(model))
    if hasattr(model, "predict"):
        print("Model has predict method.")
    if hasattr(model, "feature_names_in_"):
        print("Expected features:", model.feature_names_in_)
    if hasattr(model, "n_features_in_"):
        print("Number of expected features:", model.n_features_in_)
except Exception as e:
    print("Error loading model:", str(e))
