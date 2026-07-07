import numpy as np 
import matplotlib.pyplot as plt

def sigmoide(z):
    return 1/(1+np.exp(-z))

def coste(x,y,a,b):
    p = sigmoide(a*x+b)
    p = np.clip(p, 1e-10, 1 - 1e-10)
    #c = [ (-(y[i]*np.log(p[i])+ (1-y[i])*np.log(1-p[i]))) for i in range(len(x))] 

    #for i in range(len(x)):
        #c = c + (-(y[i]*np.log(p[i])+ (1-y[i])*np.log(1-p[i])))
    return -np.mean(y*np.log(p)+(1-y)*np.log(1-p))



def entrenar(x,y, alpha, n):
    N = len(x)
    a = 0 
    b = 0 
    a_record = []
    b_record = [] 
    L = []
    for paso in range(n):
        a_record.append(a)
        b_record.append(b)
        L.append(coste(x,y,a,b))
        grad_a = (1/N)*np.sum(x*(sigmoide(a*x+b)-y))
        grad_b = (1/N)*np.sum(sigmoide(a*x+b)-y)
        a = a - alpha*grad_a
        b = b - alpha*grad_b
    return a, b, a_record, b_record, L



if __name__ == "__main__":
    a_real = 2
    b_real = -5

    x = np.random.uniform(0, 10, 1000)
    z = a_real * x + b_real
    p = sigmoide(z)
    y = np.random.binomial(1, p)

    a, b, a_record, b_record, L = entrenar(x, y, 0.01, 100000)

    plt.plot(L)
    plt.xlabel("Paso")
    plt.ylabel("L")
    plt.grid()
    plt.title("Coste en cada iteración")

    a_vals = np.linspace(-7, 7, 1000)
    b_vals = np.linspace(-7, 7, 1000)
    A, B = np.meshgrid(a_vals, b_vals)

    J = np.zeros([len(a_vals), len(b_vals)])
    for i in range(len(a_vals)):
        for j in range(len(b_vals)):
            J[i, j] = coste(x, y, A[i, j], B[i, j])

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.plot_surface(A, B, J, alpha=0.5)
    ax.plot(a_record, b_record, L, color="orange", linewidth=2, zorder=5)
    ax.set_xlabel("$a$")
    ax.set_ylabel("$b$")
    ax.set_zlabel("$Coste$")

    plt.show()