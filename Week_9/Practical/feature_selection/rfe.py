# import matplotlib.pyplot as plt
#
# from sklearn.pipeline import Pipeline
# from sklearn.datasets import load_digits
# from sklearn.feature_selection import RFE
# from sklearn.preprocessing import MinMaxScaler
# from sklearn.linear_model import LogisticRegression

# digits = load_digits()
# X = digits.images.reshape((len(digits.images), -1))
# y = digits.target
#
# pipe = Pipeline([
#     ('scaler', MinMaxScaler()),
#     ('rfe', RFE(estimator=LogisticRegression(), n_features_to_select=1, step=1))
# ])
#
# pipe.fit(X, y)
# ranking = pipe.named_steps['rfe'].ranking_.reshape(digits.images[0].shape)
#
# plt.matshow(ranking, cmap=plt.cm.Blues)
#
# for i in range(ranking.shape[0]):
#     for j in range(ranking.shape[1]):
#         plt.text(j, i, str(ranking[i, j]), ha='center', va='center', color='black')
#
# plt.colorbar()
# plt.title("Ranking of pixels with RFE\n(Logistic Regression)")
# plt.show()


import numpy as np
import pandas as pd
from sklearn.feature_selection import RFE, RFECV
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, StratifiedKFold


# RFE (Recursive Feature Elimination)
def recursive_feature_elimination(df: pd.DataFrame, target_column: str, model = None) -> object:
    if model is None:
        model = LogisticRegression()
    X = df.drop(columns=[target_column])
    X = X.select_dtypes(include=np.number)
    print(f"X:\n{X}\n")
    y = df[target_column]
    print(f"y:\n{y}\n")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=0)
    print(f"X_train:\n{X_train}\n"
          f"X_test:\n{X_test}\n"
          f"y_train:\n{y_train}\n"
          f"y_test:\n{y_test}\n")
    rfe_selector = RFE(estimator=model, n_features_to_select=2, step=1)
    print(f"--- RFE_Selector ---\n{rfe_selector}")
    rfe_selector.fit(X_train, y_train)
    return list(X.columns[rfe_selector.support_])

choco_dataset = pd.DataFrame({
    'Chocolate': ['KitKat', 'Snickers', 'Twix', 'Mars', 'Bounty', 'Albeni'],
    'Price_$': [3, 2, 2, 1, 2, 1],
    'Weight_g': [45, 50, 50, 40, 45, 40],
    'Cacao_%': [30, 40, 20, 40, 10, 20],
    'Is_Tasty': [1, 1, 0, 1, 0, 0]
})
print(recursive_feature_elimination(choco_dataset, 'Is_Tasty'))


def recursive_feature_elimination_cross_validation(df: pd.DataFrame, target_column: str, model = None) -> object:
    if model is None:
        model = LogisticRegression()

    X = df.select_dtypes(include=np.number).drop(columns=target_column, errors='ignore')
    y = df[target_column]
    cv_strategy = StratifiedKFold(n_splits=2, shuffle=True, random_state=0)
    rfecv_selector = RFECV(estimator=model, step=1, cv=cv_strategy, scoring='accuracy')
    rfecv_selector.fit(X, y)
    return list(X.columns[rfecv_selector.support_])
print(recursive_feature_elimination_cross_validation(choco_dataset, 'Is_Tasty'))

# def recursive_feature_elimination_cross_validation(df: pd.DataFrame, target_column: str, model = None) -> object:
#     if model is None:
#         model = LogisticRegression()
#     X = df.select_dtypes(include=np.number)
#     X = X.drop(columns=[target_column], errors='ignore')
#     y = df[target_column]
#     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=0)
#     rfecv_selector = RFECV(estimator=model, step=1, cv=2, scoring='accuracy')
#     rfecv_selector.fit(X_train, y_train)
#     return list(X.columns[rfecv_selector.support_])
#
# print(recursive_feature_elimination_cross_validation(choco_dataset, 'Is_Tasty'))