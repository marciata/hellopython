import numpy as np
from sklearn.datasets import load_iris
from sklearn import tree


# dataset de tipos de flor de iris
iris = load_iris()

# separando um subconjunto dos dados para testar os dados treinados
test_idx = [0, 50, 100]

# training data
train_target = np.delete(iris.target, test_idx)
train_data = np.delete(iris.data, test_idx, axis = 0)

# testing data
test_target = iris.target[test_idx]
test_data = iris.data[test_idx]

# label do conjunto de caracteristicas disponíveis no dataset
# ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
print(iris.feature_names)
# label dos tipos de flores disponíveis
# ['setosa' 'versicolor' 'virginica']
print(iris.target_names)
# valores das características da primeira flor
print(iris.data[0])

# utilizando o algoritmo de arvore de decisao - facil de ler e entender
clf = tree.DecisionTreeClassifier()
clf.fit(train_data, train_target)

print('Dados de teste (0 = setosa, 1 - versicolor, 2 - virginica)')
print(test_target)

print('Dados previstos pelo algoritmo')
print(clf.predict(test_data))
