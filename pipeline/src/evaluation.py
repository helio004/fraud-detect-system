import os
import json

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, roc_curve, f1_score
from catboost import CatBoostClassifier


def evaluate_model():
    dataset = pd.read_csv("/tmp/eval_set.csv")
    X = dataset.drop('is_fraud', axis=1)
    y = dataset['is_fraud'].astype(int)

    clf = CatBoostClassifier()
    clf.load_model("model/fraud_model.cbm")

    pred_prob = clf.predict_proba(X)[:, 1]
    pred = clf.predict(X)

    auc = roc_auc_score(y, pred_prob)
    print(f'AUC score: {auc}')

    path = "model/metrics/"
    if not os.path.exists(path):
        os.makedirs(path)

    fpr, tpr, _ = roc_curve(y, pred_prob)

    plt.figure()
    plt.plot(fpr, tpr, label='ROC Curve')

    plt.text(0.5, 0.5,
             f"F1 Score: {f1_score(y, pred):.2f}\nROC AUC Score: {roc_auc_score(y, pred_prob):.2f}",
             fontsize=10, ha='center', va='center', bbox=dict(boxstyle='round,pad=0.3', edgecolor='black', facecolor='lightgray'))

    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic (ROC) Curve')
    plt.legend(loc='lower right')

    plt.savefig(os.path.join(path, 'roc_curve.png'))
    plt.close()
