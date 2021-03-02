import random
import matplotlib.pyplot as plt
import numpy as np
def estimatePi(INTERVAL):
          
          pi=[]
          circle_points = 0
          square_points = 0
          
          for i in range(INTERVAL):
              
              rand_x = random.uniform(-1, 1) # uniformly choosing the x-cordinate
              
              rand_y = random.uniform(-1, 1) # uniformly choosing the y-coordinate
              
              # checking whether it lies inside the circle or the square 
              origin_dist = rand_x ** 2 + rand_y ** 2
              if origin_dist <= 1:
                  circle_points += 1
              square_points += 1
              pi.append(4 * circle_points / square_points)
          
          fig,ax=plt.subplots(1)
          plt.grid(True, which='both')
          p=[i for i in range(INTERVAL)]
          ax.plot(p,pi,label="Monte_carlo method")
          plt.axhline(y=np.pi,color='r',label="value of math.pi")
          plt.ylim([3.10,3.2])
          ax.legend()
          plt.show()
estimatePi(2000000)          