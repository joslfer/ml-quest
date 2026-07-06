import numpy as np 


def sigmoide(z):
    return 1/(1+np.exp(-z))

def coste(x,y,a,b):
    p = sigmoide(a*x+b)
    #c = [ (-(y[i]*np.log(p[i])+ (1-y[i])*np.log(1-p[i]))) for i in range(len(x))] 

    #for i in range(len(x)):
        #c = c + (-(y[i]*np.log(p[i])+ (1-y[i])*np.log(1-p[i])))
    return -np.mean(y*np.log(p)+(1-y)*np.log(1-p))
