import numpy as np
from sklearn import metrics
import sys
# print(gt,pred,topN)

def get_auc(gt,pred,topN):
    pred=open(pred,'r').readlines()
    # print(len(pred))
    # print(pred[0])
    pred=[float(i) for i in list(pred)]
    pred=np.array(pred)
    gt=open(gt,'r').read()
    # print(gt[1194])
    gt=[int(i) for i in list(gt)]
    gt=np.array(gt)
    # print(len(gt))

    fpr, tpr, thresholds = metrics.roc_curve(gt, pred)
    print("AUC: {}".format(metrics.auc(fpr, tpr)))
    # with open("auc_{}.txt".format(topN),'w') as fw:
    #     fw.write(metrics.auc(fpr, tpr))
if __name__=='__main__':
    pred,gt,topN=sys.argv[1:]
    get_auc(gt,pred,topN)
    # fr=open('gt.txt','r').read()
    # print(len(fr))
    # print(len(fr))