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


from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import RFE


# RFE (Recursive Feature Elimination)
def recursive_feature_elimination(dataset, model: LogisticRegression()):
    X, y = train_test_split(dataset, test_size=0.22, random_state=0)