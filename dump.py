import matplotlib.pyplot as plt
import numpy as np
import random
import math 
class Polynomial:
    def __init__(self, coef_co=[]):
        self.coef_co = coef_co

    def __str__(self):
        strings = []
        strings.append("Coefficients of the polynomial are:")
        temp = " ".join([str(x) for x in self.coef_co])
        strings.append(str(temp))
        return "\n".join(strings)

    # Evaluating the polynomial at a point and using getitem to hget the value
    def __getitem__(self, item):
        return sum([(item ** i) * self.coef_co[i] for i in range(len(self.coef_co))])

    # Defining addition of Polynom,ials properly
    def __add__(self, other):
        size = max(len(self.coef_co), len(other.coef_co))
        sum = [0 for i in range(size)]
        for i in range(0, len(self.coef_co), 1):
            sum[i] = self.coef_co[i]
        for i in range(len(other.coef_co)):
            sum[i] += other.coef_co[i]
        self.coef_co = sum
        return self

    # defining Subtraction properly
    def __sub__(self, other):
        size = max(len(self.coef_co), len(other.coef_co))
        sum = [0 for i in range(size)]
        for i in range(0, len(self.coef_co), 1):
            sum[i] = self.coef_co[i]
        for i in range(len(other.coef_co)):
            sum[i] -= other.coef_co[i]
        self.coef_co = sum
        return self

    # Defining constant multiplication
    def __rmul__(self, other):
        vector = self.coef_co
        for i in range(len(vector)):
            self.coef_co[i] = other * self.coef_co[i]
        return self

    # defining multiplication of two ploynomials
    def __mul__(self, other):
        r1 = len(self.coef_co)
        r2 = len(other.coef_co)
        prod = [0] * (r1 + r2 - 1)
        for i in range(r1):
            for j in range(r2):
                prod[i + j] += self.coef_co[i] * other.coef_co[j]
        self.coef_co = prod
        return self

    def derivative(self):  # derivative method
        derivative_coef = []
        for i in range(1, len(self.coef_co)):
            # The derivative formula of the polynomial [x^n becomes x^(n-1)]
            derivative_coef.append((i) * self.coef_co[i])
        self.coef_co = derivative_coef
        return self

    def get_coef(self):
        coef=[]
        for i in self.coef_co:
            coef.append(i)
        return coef    
    def area(self, a, b):  # area method
        self.a = a
        self.b = b
        # intilalizing the coef of the co-efficients with a zero to compensate for the constant in integration
        Integration_coef = [0]
        for i in range(len(self.coef_co)):
            # integration formula of a polynomial [x^n becomes  x^n/n+1]
            Integration_coef.append(self.coef_co[i] / (i + 1))
        p = Polynomial(Integration_coef)  # Creating a polynomial with the co-efficients
        return "Area in the interval " + str([self.a, self.b]) + " is: " + str((p[self.b] - p[self.a]))

    def get_power(self,degree):
          p=Polynomial(self.coef_co)
          q=Polynomial([1])
          for i in range(degree):
              q*=p
          return q   



    def Aberth(self,array):
        
        self.array=array 
        p=Polynomial([1])
        for i in self.array:
            p=p*Polynomial([-i,1])

        
        coef=p.get_coef()
        degree=len(coef)-1
        p1=Polynomial(coef)
        dp=p1.derivative()
       
        roots=[]    
        x=(abs(coef[0])/abs(coef[-1]))**(1/degree)
        
        for i in range (degree):
            root=complex(x*np.cos((2*np.pi/degree)*i +np.pi/(2*degree)),
                                             x*np.sin((2*np.pi/degree)*i +np.pi/(2*degree))) 
            roots.append(root)   

        print(roots)

       
        
        iteration=0
        while iteration<10:    
            for i in range(degree):
                  ratio = p[roots[i]]/dp[roots[i]]
                  #print("ratio",ratio)
                  offset = ratio / (1 - (ratio * sum(1/(roots[i] - j) 
                                          for j in roots if j != roots[i])))
                  #print("Offest",offset)                        
                  roots[i]-=offset
            iteration+=1
            print(iteration,roots)     
            
        print(roots)  
                                

q=Polynomial()
q.Aberth([1,0,-1])   
