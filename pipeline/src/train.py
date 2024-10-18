import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.utils.class_weight import compute_class_weight

from catboost import CatBoostClassifier


def train_model():
    dataset = pd.read_csv("/tmp/train_set.csv")
    X = dataset.drop('is_fraud', axis=1)
    y = dataset['is_fraud']

    categorical_features = [
        col for col in X.columns if X[col].dtype == 'object']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)

    classes = np.unique(y_train)
    weights = compute_class_weight(
        class_weight='balanced', classes=classes, y=y_train)
    class_weights = dict(zip(classes, weights))

    params = {
        'iterations': 1000,
        'learning_rate': 0.1,
        'depth': 6,
        'eval_metric': 'AUC',
        'random_seed': 42,
        'verbose': 100,
        'loss_function': 'Logloss',
        'cat_features': categorical_features,
        'class_weights': class_weights
    }

    clf = CatBoostClassifier(**params)
    clf.fit(X_train, y_train, eval_set=(X_test, y_test), verbose=False)

    clf.save_model("model/fraud_model.cbm")
