#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 18:59:00 2024

@author: westonlarhette
"""

""" Lab 11: Rare Events"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import factorial as fact

# 2.1 The Poisson Distribution
#A:
lambda_value = 8
l = np.arange(0,100,1)
probs = (np.exp(-lambda_value)*lambda_value**l)/fact(l)
plt.plot(l,probs)
plt.xlabel('l: Number of heads')
plt.ylabel('Probability of getting l heads in 100 flips')

#B:
N1 = 1000
M1 = np.zeros(N1)
for i in range(N1):
    rng = np.random.default_rng()
    M1[i] = sum(rng.random(100) < 0.08)


# Plot histogram of M - frequency of M heads in N (1000) trials
plt.figure()
plt.subplot(2,1,1)
plt.hist(M1,bins=25)
plt.xlabel('Bins: number of heads in a trial')
plt.ylabel('Frequency of a given number of heads')
plt.title('Unfair coin flip Histogram (N = 1000)')
plt.plot(l,probs*N1)

# Repeating the process for N = 100,000 trials
N2 = 100000
M2 = np.zeros(N2)
for i in range(N2):
     rng = np.random.default_rng()
     M2[i] = sum(rng.random(100) < 0.08)
     
plt.subplot(2,1,2) 
plt.hist(M2,bins=25)
plt.xlabel('Bins: number of heads in a trial')
plt.ylabel('Frequency of a given number of heads')
plt.title('Unfair coin flip Histogram (N = 100,000)')
plt.plot(l,probs*N2)
plt.tight_layout()

## Commentary:
## The most probable values in both plots are around 6-9 heads
## Each plot looks similar but they share a similarity of
## every graph having zero frequency for certain numbers of heads,
## as if every trial does not have any number of heads for those
## specific values that are absent from the graphs
## Weirdly, in the N = 100,000 plot, the most probable value for the Poisson 
## distribution coincides with the area of the coinflip graph where there is 
## zero frequency. Very strange. There is a big gap right where the highest
## frequency number of heads should be.

# 2.2 Waiting Times
# Count intervals between heads for unfair coin flip
#

# =============================================================================
trial1 = rng.random(100) < 0.08
indices1 = np.nonzero(trial1)
wait_times1 = np.diff(indices1)
wait_times1 = wait_times1.flatten()

trial2 = rng.random(100) < 0.08
indices2 = np.nonzero(trial2)
wait_times2 = np.diff(indices2)
wait_times2 = wait_times2.flatten()

trial3 = rng.random(100) < 0.08
indices3 = np.nonzero(trial3)
wait_times3 = np.diff(indices3)
wait_times3 = wait_times3.flatten()

trial4 = rng.random(100) < 0.08
indices4 = np.nonzero(trial4)
wait_times4 = np.diff(indices4)
wait_times4 = wait_times4.flatten()

trial5 = rng.random(100) < 0.08
indices5 = np.nonzero(trial5)
wait_times5 = np.diff(indices5)
wait_times5 = wait_times5.flatten()

trial6 = rng.random(100) < 0.08
indices6 = np.nonzero(trial6)
wait_times6 = np.diff(indices6)
wait_times6 = wait_times6.flatten()

trial7 = rng.random(100) < 0.08
indices7 = np.nonzero(trial7)
wait_times7 = np.diff(indices7)
wait_times7 = wait_times7.flatten()

trial8 = rng.random(100) < 0.08
indices8 = np.nonzero(trial8)
wait_times8 = np.diff(indices8)
wait_times8 = wait_times8.flatten()

trial9 = rng.random(100) < 0.08
indices9 = np.nonzero(trial9)
wait_times9 = np.diff(indices9)
wait_times9 = wait_times9.flatten()

trial10 = rng.random(100) < 0.08
indices10 = np.nonzero(trial10)
wait_times10 = np.diff(indices10)
wait_times10 = wait_times10.flatten()

trial11 = rng.random(100) < 0.08
indices11 = np.nonzero(trial11)
wait_times11 = np.diff(indices11)
wait_times11 = wait_times11.flatten()

trial12 = rng.random(100) < 0.08
indices12 = np.nonzero(trial12)
wait_times12 = np.diff(indices12)
wait_times12 = wait_times12.flatten()


wait_times_total = np.concatenate((wait_times1,wait_times2,wait_times3,wait_times4,wait_times5,wait_times6,wait_times7,wait_times8,wait_times9,wait_times10,wait_times11,wait_times12))

plt.figure()
plt.hist(wait_times_total, color='blue', bins=12)
plt.xlabel('Value of time interval between flips that result in heads')
plt.ylabel('Frequency of intervals')
plt.title('Histogram of Unfair Coinflip & Time Intervals between flips giving heads')

plt.tight_layout()
plt.show()
# =============================================================================
    

## Commentary:
# Before graphing the wait times distribution, I thought that the distribution would unevenly lean to the right,
# with a higher frequency of medium-long waiting times in between coin flips that result in heads
# since there is a lower probability of getting heads than tails for this unfair coin.
# But the histogram gave me the exact opposite: the graph leans towards the left, with a higher frequency of relatively
# shorter wait times, with the highest frequency wait times being between 0 and 5 seconds.
# 
    
# Repeat for 1000 coin flips
trial1000 = rng.random(1000) < 0.08
indices1000 = np.nonzero(trial1000)
wait_times1000 = np.diff(indices1000)
wait_times1000 = wait_times1000.flatten()

plt.figure()
plt.subplot(3,1,1)
plt.hist(wait_times1000,bins=12)
plt.xlabel('Value of Time Intervals between flips giving heads')
plt.ylabel('Frequency')
plt.title('Histogram of 1000 Unfair Coin Flips & Time Intervals between flips giving heads')

# Find average waiting time between heads:
avg_time_1000 = np.mean(wait_times1000)

# Plot semilog and loglog plots:
# Semilog:
plt.subplot(3,1,2)
plt.semilogy(wait_times1000)
plt.title('Semilog histogram (N = 1000)')

# Loglog:
plt.subplot(3,1,3)
plt.loglog(wait_times1000)
plt.title('Loglog Histogram (N = 1000')

plt.tight_layout()

## Commentary:
# The semilog plot looks like an oscilating distribution - a sine or cosine
# Loglog does not look like any clear distribution pattern that I am familiar with


# Repeat of 100,000 coin flips
trial100000 = rng.random(100000) < 0.08
indices100000 = np.nonzero(trial100000)
wait_times100000 = np.diff(indices100000)
wait_times100000 = wait_times100000.flatten()
# Average time between heads (N = 100000)
avg_time100000 = np.mean(wait_times100000)

plt.figure()
plt.subplot(3,1,1)
plt.hist(wait_times100000,bins=12)
plt.xlabel('Value of Time Intervals between flips giving heads')
plt.ylabel('Frequency')
plt.title('Histogram of 100000 Unfair Coin Flips & Time Intervals between flips giving heads')

# Plot semilog and loglog plots:
# Semilog:
plt.subplot(3,1,2)
plt.semilogy(wait_times100000)
plt.title('Semilog histogram (N = 100000)')

# Loglog:
plt.subplot(3,1,3)
plt.loglog(wait_times100000)
plt.title('Loglog Histogram (N = 100000')

plt.tight_layout()

## Commentary:
# The patterns for what these distributions look like (N = 100,000) are similar to those 
# for the N = 1000 case, i.e. semilog looks like it is oscillating, and the same is true here,
# only for the semilog plot, the oscilation is much more condensed since the x-range
# now goes from 0 to 10^4 and the vertical range only goes from 0 to 10^2








