import pandas as pd
from sklearn.model_selection import train_test_split


def preprocess_data():
    df = pd.read_csv("/app/data/fraud_data (2).csv")
    dataset = df.drop(['trans_date_trans_time', 'merchant',
                      'dob', 'trans_num', 'job'], axis=1)

    dataset = dataset[dataset['is_fraud'].isin(['0', '1'])]
    dataset['is_fraud'] = dataset['is_fraud'].astype(int)

    train_set, eval_set = train_test_split(dataset, test_size=0.05)

    train_set.to_csv("/tmp/train_set.csv", index=False)
    eval_set.to_csv("/tmp/eval_set.csv", index=False)
