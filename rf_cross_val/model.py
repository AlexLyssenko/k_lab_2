import joblib
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier


def train_and_save():
    data = load_iris()
    X, y = data.data, data.target

    model_for_cv = RandomForestClassifier(random_state=42)

    cv_scores = cross_val_score(model_for_cv, X, y, cv=5)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    joblib.dump(model, "iris_model.pkl")


if __name__ == "__main__":
    train_and_save()
