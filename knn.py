import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import seaborn as sns
sns.set()

breast_cancer = load_breast_cancer()
X = pd.DataFrame(breast_cancer.data, columns=breast_cancer.feature_names)
X = X[['mean area', 'mean compactness']]
y = pd.Categorical.from_codes(breast_cancer.target, breast_cancer.target_names)
y = pd.get_dummies(y, drop_first=True)

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

knn = KNeighborsClassifier(n_neighbors=3, metric='euclidean')
knn.fit(X_train, y_train)

y_pred = knn.predict(X_test)

features = np.array([['maligant', 'benign'] for predicted in y_pred])
print(features[:, y_pred])
print(y_pred)
print(features[y_pred])
fig, axs = plt.subplots(1, 2)
axs[0].scatter(
    x=X_test['mean area'],
    y=X_test['mean compactness'],
    c=y_test['benign'],
    cmap='coolwarm',
    alpha=0.7,
)
axs[0].set_title('Ground truth')
axs[1].scatter(
    X_test['mean area'],
    X_test['mean compactness'],
    c=y_pred,
    cmap='coolwarm',
    alpha=0.7,
)
axs[1].set_title('Predicted values')

for ax in axs.flat:
    ax.set(xlabel='Mean Area of tumor', ylabel='Mean Compactness of tumor')
plt.show()
conf = confusion_matrix(y_test, y_pred)
print(conf)
print(classification_report(y_test, y_pred))