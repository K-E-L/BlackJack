from sklearn import svm
import numpy as np
from numpy import genfromtxt

from sklearn.metrics import accuracy_score

class LearningModel:
    # trains the model on init
    def __init__(self):
        self.name = 'SVC'
        
        self.data = genfromtxt('shoeDataTrainR.csv', delimiter=',')
        self.X, self.y = np.split(self.data, [-1], axis=1)
        # self.clf = svm.SVC()
        self.clf = svm.SVR()
        self.clf.fit(self.X, self.y)


    def predict(self, pX):
        # # max 1.5?
        # min -.5?
        # print(self.clf.predict([pX])[0])
        # if self.clf.predict([pX])[0] > 1:
        #     print(self.clf.predict([pX])[0])
        #     val = input()
        return self.clf.predict([pX])[0]



    def test(self):
        test_data = genfromtxt('shoeData.csv', delimiter=',')
        self.testX, self.testy = np.split(test_data, [-1], axis=1)

        y_pred = genfromtxt('modelPredict.csv', delimiter=',')
        self.predX, self.predy = np.split(y_pred, [-1], axis=1)

        self.testX = list(self.testX)
        self.testy = list(self.testy)
        self.predX = list(self.predX)
        self.predy = list(self.predy)

        for i in range(0,len(self.testX)):
            if self.testX[i].all() != self.predX[i].all():
                print("test:", self.testX[i])
                print("pred:", self.predX[i])
                print("i: ", i)
                break
                # del self.testX[i]

        print("accuracy:")
        print(accuracy_score(self.testy[:i], self.predy[:i]))
