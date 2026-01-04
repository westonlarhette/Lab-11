#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  1 17:39:17 2024

@author: westonlarhette
"""

""" Lab 11: Brownian Motion """

#1.1 Generatinga and plotting trajectories

num_steps = 1000

# Random Walk trajectory
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng()

# =============================================================================
x_step1 = rng.random(num_steps) > 0.5
y_step1 = rng.random(num_steps) > 0.5
x_step1 = 2*x_step1 - 1
y_step1 = 2*y_step1 - 1
x_position1 = np.cumsum(x_step1)
y_position1 = np.cumsum(y_step1)


x_step2 = rng.random(num_steps) > 0.5
y_step2 = rng.random(num_steps) > 0.5
x_step2 = 2*x_step2 - 1
y_step2 = 2*y_step2 - 1
x_position2 = np.cumsum(x_step2)
y_position2 = np.cumsum(y_step2)


x_step3 = rng.random(num_steps) > 0.5
y_step3 = rng.random(num_steps) > 0.5
x_step3 = 2*x_step3 - 1
y_step3 = 2*y_step3 - 1
x_position3 = np.cumsum(x_step3)
y_position3 = np.cumsum(y_step3)


x_step4 = rng.random(num_steps) > 0.5
y_step4 = rng.random(num_steps) > 0.5
x_step4 = 2*x_step4 - 1
y_step4 = 2*y_step4 - 1
x_position4 = np.cumsum(x_step4)
y_position4 = np.cumsum(y_step4)


plt.figure()

plt.subplot(2,2,1)
plt.plot(x_position1,y_position1)
plt.xlim([-20,20])
plt.ylim([-20,20])
# Labeling plots
plt.xlabel('X position') 
plt.ylabel('Y position')
plt.title('2D Random Walk #1')

plt.subplot(2,2,2)
plt.plot(x_position2,y_position2)
plt.xlim([-20,20])
plt.ylim([-20,20])
# Labeling plots
plt.xlabel('X position') 
plt.ylabel('Y position')
plt.title('2D Random Walk #2')

plt.subplot(2,2,3)
plt.plot(x_position3,y_position3)
plt.xlim([-20,20])
plt.ylim([-20,20])
# Labeling plots
plt.xlabel('X position') 
plt.ylabel('Y position')
plt.title('2D Random Walk #3')

plt.subplot(2,2,4)
plt.plot(x_position4,y_position4)
plt.xlim([-20,20])
plt.ylim([-20,20])
# Labeling plots
plt.xlabel('X position') 
plt.ylabel('Y position')
plt.title('2D Random Walk #4')

plt.tight_layout()
plt.show()

# =============================================================================

#1.2 Plotting the displacement distribution
num_walks = 100
rng = np.random.default_rng()
x = np.zeros(num_steps)
y = np.zeros(num_steps)
x_final = np.zeros(num_walks)
y_final = np.zeros(num_walks)
displacement = np.zeros(num_walks)
for i in range(num_walks):
    x_step = rng.random(num_steps) > 0.5
    y_step = rng.random(num_steps) > 0.5
    x_step = 2*x_step - 1
    y_step = 2*y_step - 1
    x = np.cumsum(x_step)
    y = np.cumsum(y_step)    
    x_final[i] = x[-1]
    y_final[i] = y[-1]
    displacement[i] = np.sqrt(x[-1]**2 + y[-1]**2)
    
# Increase number of walks to 1000
num_walks = 1000
rng = np.random.default_rng()
x = np.zeros(num_steps)
y = np.zeros(num_steps)
x_final = np.zeros(num_walks)
y_final = np.zeros(num_walks)
displacement = np.zeros(num_walks)
for i in range(num_walks):
    x_step = rng.random(num_steps) > 0.5
    y_step = rng.random(num_steps) > 0.5
    x_step = 2*x_step - 1
    y_step = 2*y_step - 1
    x = np.cumsum(x_step)
    y = np.cumsum(y_step)    
    x_final[i] = x[-1]
    y_final[i] = y[-1]
    displacement[i] = np.sqrt(x[-1]**2 + y[-1]**2)
    
# Make scatter plot
plt.figure()
plt.scatter(x_final,y_final)
plt.xlabel('Final X-position Displacement')
plt.ylabel('Final Y-position displacement')
plt.title('Scatter Plot of Displacement Values (1000 random walks, 1000 steps per walk)')

# Make histogram of displacement values
plt.figure()
plt.hist(displacement,bins=20)
plt.xlabel('Total Displacement of Random Walk (1000 steps)')
plt.ylabel('Frequency')
plt.title('Histogram of Random Walk Displacement Values')

# Make a histogram of displacement-squared
plt.figure()
d = displacement**2
plt.hist(d,bins=15)
plt.xlabel('Displacement Values Squared')
plt.title('Histogram of Squared Displacement Values')

# Use semilog and loglog axes
plt.figure()
plt.subplot(2,1,1)
plt.semilogy(displacement)
plt.title('Semilog-Y graph of Displacement Values')
plt.subplot(2,1,2)
plt.loglog(displacement)
plt.title('Loglog Graph of Displacement Values')

plt.tight_layout()
plt.show()

## Commentary:
## Plotting the displacement-squared values certainly looks like an
## exponential decay function. Plotting the displacement with semilogy
## or loglog makes the graph look, relatively, like a straight line
## (with some oscillation of course since we are plotting random data
## and not a clean mathematical expression), but largely taking the
## log of the data linearizes it, suggesting that the data
## has some kind of an exponential or power-law relationships

# Find average value of squared-displacement
avg_squaredisplacement = np.mean(d) # For different trials, this number is around 2000

# Repeat the same for a 4000-step walk
num_steps = 4000
num_walks = 1000
rng = np.random.default_rng()
x = np.zeros(num_steps)
y = np.zeros(num_steps)
x_final = np.zeros(num_walks)
y_final = np.zeros(num_walks)
displacement = np.zeros(num_walks)
for i in range(num_walks):
    x_step = rng.random(num_steps) > 0.5
    y_step = rng.random(num_steps) > 0.5
    x_step = 2*x_step - 1
    y_step = 2*y_step - 1
    x = np.cumsum(x_step)
    y = np.cumsum(y_step)    
    x_final[i] = x[-1]
    y_final[i] = y[-1]
    displacement[i] = np.sqrt(x[-1]**2 + y[-1]**2)

d = displacement**2

avg_squaredisplacement = np.mean(d)
# This quantity is roughly 8000 for multiple tests

## My conclusion is that the mean-squared displacement of random walk
## is proportional to the number of steps in a given walk, an interesting
## emergent statistical phenomena that I wouldn't have expected until
## running through it. I suspect that the relationship is as follows:
## mean-square displacement = 2*num_steps

