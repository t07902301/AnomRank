import numpy as np
from sklearn import metrics
import sys
def get_auc(gt,pred,topN):
    pred=open(pred,'r').readlines()
    pred=[float(i) for i in list(pred)]
    pred=np.array(pred)
    gt=open(gt,'r').read()
    gt=[int(i) for i in list(gt)]
    gt=np.array(gt)
    fpr, tpr, thresholds = metrics.roc_curve(gt, pred)
    print("AUC: {}".format(metrics.auc(fpr, tpr)))
if __name__=='__main__':
    pred,gt,topN=sys.argv[1:]
    get_auc(gt,pred,topN)