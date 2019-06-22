import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn import svm


df = pd.read_csv(r'.\data\UCI_Credit_Card_OHE.csv')

def_data = df.drop(columns='def_pay')
def_target = df['def_pay']

clf_linear = svm.SVC(kernel='linear')
scores_linear = cross_val_score(clf_linear, def_data, def_target, cv=10, scoring='accuracy')
print(scores_linear)
print('The mean accuracy of linear SVM: ')
print(scores_linear.mean())

clf_poly = svm.SVC(kernel='poly')
scores_poly = cross_val_score(clf_linear, def_data, def_target, cv=10, scoring='accuracy')
print(scores_poly)
print('The mean accuracy of poly SVM: ')
print(scores_poly.mean())
print('done')
