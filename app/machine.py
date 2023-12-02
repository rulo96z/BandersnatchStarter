from pandas import DataFrame
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import joblib
import datetime

class Machine:
    """
    A machine learning model using Random Forest Classifier.

    This class provides functionality to train a Random Forest Classifier on input data,
    make predictions, save and load the model, and retrieve information about the model.

    Attributes:
    - name (str): Name of the machine learning model.
    - model (Pipeline): Trained Random Forest Classifier model.

    Methods:
    - __init__(self, df: DataFrame): Initialize the Machine with a DataFrame.
    - __call__(self, pred_basis: DataFrame): Make predictions using the trained model.
    - save(self, filepath: str): Save the Machine instance to a file using joblib.
    - open(filepath: str) -> Machine: Load a Machine instance from a file using joblib.
    - info(self) -> str: Get information about the Machine instance.
    """

    def __init__(self, df: DataFrame):
        """
        Initialize the Machine with a DataFrame.
        """
        self.name = "Random Forest Classifier"
        target = df["Rarity"]
        features = df[['Level', 'Health', 'Energy', 'Sanity']]
        self.model = Pipeline([
            ("scaler", StandardScaler()),
            ("clf", RandomForestClassifier(n_estimators=300,
                                           criterion='gini',
                                           min_samples_leaf=1,
                                           min_samples_split=2))
        ])
        self.model.fit(features, target)

    def __call__(self, pred_basis: DataFrame):
        """
        Make predictions using the trained model.
        """
        prediction = self.model.predict(pred_basis)
        confidence = self.model.predict_proba(pred_basis).max()
        return *prediction, confidence

    def save(self, filepath):
        """
        Save the Machine instance to a file using joblib.
        """
        joblib.dump(self, filepath)

    @staticmethod
    def open(filepath):
        """
        Load a Machine instance from a file using joblib.
        """
        return joblib.load(filepath)

    def info(self):
        """
        Get information about the Machine instance.
        """
        return f"Base Model: {self.name} <br /> Timestamp: {datetime.datetime.now():%Y-%m-%d %l:%M:%S %p}"
