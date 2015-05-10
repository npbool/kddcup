from sklearn.datasets import *
from sklearn.ensemble import *
from sklearn.metrics import roc_curve  
from sklearn.metrics import auc 
import numpy

X_train, y_train, X_test, y_test = load_svmlight_files(("./fea/train_1","./fea/train_2"))

y_test = numpy.array(y_test)
print y_test.shape

clsier = RandomForestClassifier(n_estimators = 50, min_samples_leaf=10, verbose=1)
clsier.fit(X_train, y_train)
y_prob = numpy.array(clsier.predict_proba(X_test))
y_pred = y_prob[:,1]
print "SHAPE"
print y_pred.shape

fpr, tpr, thresholds = roc_curve(y_test, y_pred, pos_label=1)  
print auc(fpr, tpr)

print clsier.score(X_test, y_test)

