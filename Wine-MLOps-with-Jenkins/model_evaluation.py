import joblib
from sklearn.metrics import accuracy_score, classification_report


def load_model(file_path):
    return joblib.load(file_path)


def load_preprocessed_data(file_path):
    return joblib.load(file_path)


def evaluate_model(model, X_test, y_test):
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    report = classification_report(y_test, predictions)
    return accuracy, report


if __name__ == "__main__":
    X_train, X_test, y_train, y_test = load_preprocessed_data("preprocessed_data.pkl")

    model = load_model("model.pkl")
    accuracy, report = evaluate_model(model, X_test, y_test)
    print(f"Model Accuracy: {accuracy}")
    print(f"Classification Report:\n{report}")
