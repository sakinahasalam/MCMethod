import numpy as np
#from scipy.integrate import quad
import time
import matplotlib.pyplot as plt

def func(x):
    return np.power(x,2)/2 + np.log(np.power(x,2))

# Initialize
a = -2
b = 2
errorlist =[]
timelist =[]
Nlist = range[100,100000,100]
realans = 0.2118

# General integration method
#interresult = quad(func,a,b)
#print(interresult[0])

# computer cannot integrate by using general integration method
# due to the complexity of the equation which MonteCarlo Method become
# handy equation with boundary problem like in func(x)

# IMPORTANT SAMPLIN = MORE POINT AT IMPORTANT POINT OBTAINED DURING SAMPLING
# WEAKNESS IMPORTANT SAMPLING =  CANNOT KNOW EXACT GRAPH
# OVERCOME BY USING  =  STRITIFIED SAMPLING (BY PARTITIONING THE GRAPH)
# BY STRITIFIED - SMALLER SAMPLING HIGHER ACCURACY

# Monte Carlo Method allow you to do the crate sampling
# allow to do different sampling method

# Monte Carlo Method - EG ICING MODEL

for N in Nlist:

    starttime = time.time()
    numChoice = np.random.choice([-1,1, N]) *np.random.normal(0,0.6,N)
    # np.random.choice = choose from -1 to 1 from range N list
    # np.random.normal =  draw normal sample from Gaussian distribution
    result = func(numChoice)

    #Integrate
    Integrate = ((b-a)/N)*sum(result)
    print(Integrate)
    errorlist.append(abs(realans-Integrate))
    timelist.append(time.time() - starttime)

print('MC Answer: \n' , Integrate)
print('Error: \n', errorlist)
print('Time: \n', timelist)

plt.subplot(211)
plt.xscale('log')
plt.plot(Nlist,Errorlist)
plt.subplot(212)
plt.xscale('log')
plt.plot(timelist,Errorlist)
plt.show()


#changing sample distribution will get different result due to the randomness
