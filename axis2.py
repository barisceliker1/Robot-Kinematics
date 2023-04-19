import numpy as np
from numpy.linalg import inv
import math
import matplotlib.pyplot as plt
import time
beta = 0.01
tol = 0.1
lamb = 40
iterations = 10000
#x 
mg = []
ii = []

def axis2(d1,d2,l1,l2,ex,ey):
    def fk(l1,l2,d1,d2):
        dr1,dr2 = np.radians(d1), np.radians(d2)
        li = float(l1)
        dr1 = float(dr1)
        dr2 = float(dr2)
        li2=float(l2)
        x = float(((li*np.cos(dr1))+(li2*np.cos(dr1+dr2))))
        y = round(((li*np.sin(dr1))+(li2*np.sin(dr1+dr2))))
        return x,y;


    def jacobian(l1,l2,d1,d2): 
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

    def error(x,y,ex,ey):
        errorx = float(ex - x); errory = float(ey - y)
        magnitude = float(math.sqrt(math.pow(errorx, 2) + math.pow(errory, 2)))
        return errorx , errory, magnitude;
   


    for i in range(iterations):
        x, y = (fk(l1,l2,d1,d2))
        
        errx,erry,mag = error(x,y,ex,ey)
        if( mag > tol):
            mg.append(mag);
            ii.append(i);
            delx = float(beta * errx)
            dely = float(beta * erry)
            df = np.matrix([[delx],[dely]])
            J = jacobian(l1,l2,d1,d2)
            deld = np.matmul(J,df)
            d1 = d1 + np.degrees(deld[0,0])
            d2 = d2 + np.degrees(deld[1,0])
        else:
            print (" You have reached your destination")
            break
    else:
        print ("You have reached the end of your iterations")
    

    plt.plot(ii,mg)
    plt.xlabel('Iterations')
    plt.ylabel('Magnitude of error')
    plt.show()
