from sklearn import svm
import numpy as np
from numpy import genfromtxt

class LearningModel:
    # trains the model on init
    def __init__(self):
        self.name = 'SVC'
        
        data = genfromtxt('shoeDataTrain.csv', delimiter=',')
        self.X, self.y = np.split(data, [-1], axis=1)
        self.clf = svm.SVC()
        # self.clf = svm.SVR()
        self.clf.fit(self.X, self.y)

    def predict(self, pX):
        # # max 1.5?
        # print(self.clf.predict([pX])[0])
        # if self.clf.predict([pX])[0] < 0:
        #     val = input()
        return self.clf.predict([pX])[0]
