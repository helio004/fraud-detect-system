import os
import pandas as pd
from catboost import CatBoostClassifier
from core.models import ResponseModel


class ModelLoader:
    def __init__(self, model_path):
        self.model = self.read_model(model_path)

    def read_model(self, model_path):
        try:
            model_artifact_path = os.path.join(model_path, "fraud_model.cbm")
            model = CatBoostClassifier()
            model.load_model(model_artifact_path)
            return model
        except Exception as e:
            print("error: ", e)
            return None

    def predict_is_fraud(self, features):
        features = pd.DataFrame([features.dict()])
        fraud_pred = self.model.predict(features)

        return ResponseModel(
            is_fraud=True if fraud_pred == 1 else False,
            probability=round(self.model.predict_proba(features)[:, 1][0], 4)
        )
