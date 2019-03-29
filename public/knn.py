from __future__ import print_function
import numpy as np
from sklearn import neighbors, datasets
from sklearn.model_selection import train_test_split  # for splitting data
from sklearn.metrics import accuracy_score  # for evaluating results
import tkinter
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2
from mlxtend.data import loadlocal_mnist
import pickle

x, y = loadlocal_mnist(
    images_path='/namtr/python/python3/mnist/t10k-images.idx3-ubyte',
    labels_path='/namtr/python/python3/mnist/t10k-labels.idx1-ubyte')

data_test = x
target_test = y
img = cv2.imread('/namtr/Digits-Recognition-nodeJs-version-/public/image.png', 0)
img = 255-img
hor = np.zeros((20,4))
ver = np.zeros((4,28))
img = np.hstack((img,hor))
img = np.hstack((hor,img))
img = np.vstack((ver,img))
img = np.vstack((img,ver))


# print('Labels:', np.unique(target_train))
# # data_train, data_test, target_train, target_test = train_test_split(
# #     data, target, test_size=1000)
# # print('Train size:', data_train.shape[0], ', test size:', data_test.shape[0])

# model = neighbors.KNeighborsClassifier(n_neighbors=7, p=2, weights='distance')
# model.fit(data_train, target_train)

model = pickle.load(open('KNN_model.sav','rb'))
# filename = 'KNN_model.sav'
# pickle.dump(model,open(filename, 'wb'))

# target_pred = model.predict(img.reshape((1,784)))
target_pred = model.predict(data_test)
print("Accuracy of 7NN: %.2f %%" %
      (100*accuracy_score(target_test, target_pred)))

# plt.axis('off')
# plt.imshow(img,cmap=plt.cm.gray_r, interpolation='nearest')
# plt.title('Prediction:%i ' % target_pred)

diff_indices = [i for i in range(1000) if target_pred[i] != target_test[i]]
print(len(diff_indices))
print(diff_indices)
for i in range(10):
    plt.subplot(2, 5, i+1)
    plt.axis('off')
    plt.imshow(data_test[diff_indices[i]].reshape((28, 28)),
               cmap=plt.cm.gray_r, interpolation='nearest')
    plt.title('Prediction:%i ' % target_pred[diff_indices[i]])

plt.show()
