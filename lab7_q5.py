import numpy as np
from numpy import cos, sin, pi, exp
import matplotlib.pyplot as plt 

def Newton_system(F, J, x, eps):
  
    F_value = F(x)
    F_norm = np.linalg.norm(F_value, ord=2)  # l2 norm of vector
    norm_values=[]
    counter=[]
    iteration_counter = 0
    while abs(F_norm) > eps:
        delta = np.linalg.solve(J(x), -F_value)
        x = x + delta
        F_value = F(x)
        F_norm = np.linalg.norm(F_value, ord=2)
        norm_values.append(F_norm)
        iteration_counter += 1
        counter.append(iteration_counter)
    print("The solution vector is:",x)    
    fig,ax=plt.subplots()
    ax.plot(counter,norm_values,"r--",label="Convergence of Newton-Raphson")
    ax.set_xlabel("No of iterations")
    ax.set_ylabel("Norm Values")
    ax.set_title("Plot of Norm values of f with respect to no of iterations",fontsize=10)
    ax.grid()
    ax.legend()
    
    plt.show()
 
def F(x):
        return np.array(
            [3*x[0]-cos(x[1]*x[2])-3/2,
                4*x[0]**2 -625*x[1]**2 + 2*x[2]-1, 20*x[2]+exp(-x[0]*x[1]) +9 ])

def J(x):
        return np.array(
            [[3,x[2]*sin(x[1]*x[2]),x[1]*sin(x[1]*x[2])],
             [8*x[0],-1250*x[1],2],[-x[1]*exp(-x[1]*x[0]),-x[0]*exp(-x[1]*x[0]),20]])

Newton_system(F, J, x=np.array([1,2,3]), eps=0.000001)

