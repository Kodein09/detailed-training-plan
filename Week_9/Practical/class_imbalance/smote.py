# import numpy as np
# import matplotlib.pyplot as plt
#
# from sklearn.datasets import make_classification
# from sklearn.neighbors import NearestNeighbors
# from sklearn.model_selection import train_test_split
#
#
#
# X, y = make_classification(
#     n_samples=100,
#     n_features=2,
#     n_informative=2,
#     n_redundant=0,
#     weights=[0.9, 0.1],
#     shuffle=True,
#     random_state=42
# )
#
# def smote_and_plot(X, y):
#     print(f"X:\n{X} LENGTH: {len(X)}\n"
#           f"y:\n{y} LENGTH: {len(y)}\n")
#     minority_mask = (y == 1)
#     print(f"Minority mask:\n{minority_mask}")
#     X_minority = X[minority_mask]
#     print(f"X_Minority:\n{X_minority} Length: {len(X_minority)}")
#
#     nn = NearestNeighbors(n_neighbors=3)
#     nn.fit(X_minority)
#     distances, indices = nn.kneighbors(X_minority)
#     print(f"\nDistances:\n{distances}\n"
#           f"\nIndices:\n{indices}\n")
#
#     synthetic_points = []
#     for i in range(len(X_minority)):
#         current_point = X_minority[i]
#         print(f"Current point on iter [{i}] : {X_minority[i]}")
#
#         nn_idx = np.random.choice(indices[i][1:])
#         random_neighbor = X_minority[nn_idx]
#
#         diff = random_neighbor - current_point
#         new_point = current_point + np.random.rand() * diff
#         synthetic_points.append(new_point)
#         print(synthetic_points)
#
#     synthetic_points = np.array(synthetic_points)
#
#
#
# smote_and_plot(X, y)


# import numpy as np
# import matplotlib.pyplot as plt
#
# from sklearn.neighbors import NearestNeighbors
#
#
# np.random.seed(42)
#
# majority = np.random.rand(50, 2) + 1
# minority = np.random.rand(10, 2)
#
# print(f"Majority class:\n{majority}\n"
#       f"\nMinority class:\n{minority}\n")
#
# sample_idx = np.random.randint(0, len(minority))
# sample = minority[sample_idx]
# print(f"Sample index: {sample_idx}\n"
#       f"Sample: {sample}")
#
# #Neighbors quantity
# k = 6
#
# #NearestNeighbors for finding k nearest neighbours
# neighbors = NearestNeighbors(n_neighbors=k).fit(minority)
# print(f"KNN: {neighbors}\n")
# distances, indices = neighbors.kneighbors([sample])
# print(f"Distances: {distances}\n"
#       f"Indices: {indices}\n")
#
# plt.figure(figsize=(12, 10))
# plt.scatter(majority[:, 0], majority[:, 1], label="Majority class", alpha=0.6)
# plt.scatter(minority[:, 0], minority[:, 1], label="Minority class", alpha=0.6)
# plt.scatter(sample[0], sample[1], label="Selected Sample", c='red', edgecolor='black', s=100)
# plt.scatter(minority[indices][0][:, 0], minority[indices][0][:, 1], label="KNN", c='green', edgecolor='black')
#
# plt.title("KNN for Selected Sample")
# plt.legend()
# # plt.show()
#
#
# def create_synthetic_points(sample, neighbors, n_synthetic):
#     synthetic_points = []
#     for _ in range(n_synthetic):
#         neighbor = neighbors[np.random.randint(0, len(neighbors))]
#
#         fraction = np.random.rand()
#
#         synthetic_point = sample + (neighbor - sample) * fraction
#         synthetic_points.append(synthetic_point)
#
#     synthetic_points = np.array(synthetic_points)
#
#     plt.figure(figsize=(12, 10))
#     plt.scatter(majority[:, 0], majority[:, 1], label="Majority class", alpha=0.6)
#     plt.scatter(minority[:, 0], minority[:, 1], label="Minority class", alpha=0.6)
#     plt.scatter(sample[0], sample[1], label="selected Sample", c='red', edgecolor='black')
#     plt.scatter(synthetic_points[:, 0], synthetic_points[:, 1],
#                 label="Synthetic Generated Points", c='green', edgecolor='black')
#     plt.title("KNN with Synthetic Generated Points or SMOTE")
#     plt.legend()
#     # plt.show()
#
#     return synthetic_points
#
# neighbors = minority[indices][0][1:]
# print(f"Neighbors = minority[indices][0][1:]:\n{neighbors}\n")
#
# print(f"Result from created synthetic points:\n{create_synthetic_points(sample, neighbors, 10)}")



import numpy as np
import matplotlib.pyplot as plt

from sklearn.neighbors import NearestNeighbors


np.random.seed(42)

majority_class = np.random.rand(50, 2) + 1
minority_class = np.random.rand(10, 2)

neighbors = NearestNeighbors(n_neighbors=6)

def smote_and_plot(neighbors, n_synthetic_points: int):
    sample_idx = np.random.randint(0, len(minority_class))
    sample = minority_class[sample_idx]

    synthetic_points = []
    for _ in range(len(neighbors)):
        rand_neighbor = neighbors[np.random.randint(0, len(neighbors))]
        fraction = np.random.randn()
        synthetic_point = sample + (sample - neighbors) * fraction
        synthetic_points.append(synthetic_point)
    synthetic_points = np.array(synthetic_points)

    plt.figure(figsize=(12, 10))
    plt.scatter(majority_class[:, 0], majority_class[:, 1], label="Majority class", alpha=0.6, color='RoyalBlue')
    plt.scatter(minority_class[:, 0], minority_class[:, 1], label="Minority class", alpha=0.6, color='maroon', s=50)

    plt.scatter(synthetic_points[:, 0], synthetic_points[:, 1],
                label="Synthetic points", alpha=0.6, color='orange', s=100)
    plt.legend()
    plt.show()

    return synthetic_points

print(smote_and_plot(neighbors, 10))