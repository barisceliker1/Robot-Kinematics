import numpy as np
from numpy.linalg import inv
import math

def jacobian(l1,l2,d1,d2):
    lamb = 40
    t1,t2=np.radians(d1),np.radians(d2)
    l1 = float(l1)
    l2=float(l2)
    x1 = float(-l1*np.sin(t1)-l2*np.sin(t1+t2)); x2 = float(-l2*np.sin(t1+t2))
    y1 = float(l1*np.cos(t1)+l2*np.cos(t1+t2)); y2 = float(l2*np.cos(t1+t2))
    J = np.matrix([[x1,x2],[y1,y2]])
    Jt = J.transpose()
    # transpose of matrix
    I = np.identity(2)
    JI =np.matmul(J,Jt); lambI= lamb*lamb*I    
    JJI = np.add(JI,lambI)
    # JI + lambı matrix
    JJJI = inv(JJI)
    IJ = np.matmul(Jt,JJJI)
    return IJ;
    

