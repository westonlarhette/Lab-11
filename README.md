# Lab-11
Loyola Marymount University: PHYS1200

1 BROWNIAN MOTION: 

In the Brownian Motion portion of the lab, we focused on modeling the Brownian motion and diffusion of liquid or gas molecules with a computational 2-dimensional random walk process.
We compared the trajectories of different random walks based on varying lists made by random number generation. Despite these graphs of random walks being uniquely different each time, we attempted to find a common similarity by doing an analysis of the displacement of each trial.
We simulated 100 separate random walks with a 'for' loop, each walk containing 1000 steps and then simulated 1000 separate walks and plotted the end x and y points in a scatter plot. There was a general clustering towards some kind of center within the graph with some data outliers being away from the cluster which is to be expected. We used histograms to plot the total displacement and the square of the displacement. The displacement histogram was generally clustered towards the left end of the graph, only slightly looking like some sort of power law or exponential relation. The square-displacement histogram very clearly looked like an exponential decay. To test this interpretation, we took the semilog and loglog of the data and graphed it for these unique axes. The purpose of these axes is to linearize  exponential behavior of a function or dataset and thus if data is truly modeling an exponential function, we expect to see the semilog and loglog graphs plot a rather linear line. This is indeed what I say when I used these axes, only with what looks like very clustered oscillation up and down. Despite this, what would be considered the general "amplitude" of this oscillation was constant and within a certain range of y-values, the graph essentially looked like a linear function. This was evidence that the displacement squared and thus the displacement does follow some sort of exponential decay in terms of the frequency of each displacement. This means that the most frequent displacements were statistically the shorter ones and that the frequency of displacements exponentially decays as the displacement increases.

We then found the mean-square displacement for 1000 step walks and 4000 step walks. For the 1000 step walks, I would get values of mean-square displacement that would generally center around 2000. For the 4000 step walks, they would center around 8000. This led me to the conclusion that the square-displacement is proportional to the number of steps in a given walk and more so that it is linearly proportional by a factor of two. This is certainly an interesting emergent statistical phenomena that I would never have expected until I ran through the code.



2 RARE EVENTS

In the Rare Events portion of the lab we modeled an unflair coin flip that has a probability of landing on heads of only 8%. We modeled this with random number generation in the same way we previously modeled a fair coin flip (probability = 0.5 instead of 0.08) and then compared what we got to the actual Poisson distribution that is the mathematical description of this kind of statistical behavior.

We counted the number of heads for each trial, M, and then plotted a histogram of this quantity and found that the frequency of getting a certain number of heads in a trial of 100 coin flips was very closely modeled by the Poisson distribution, with the exception that I had big missing gaps of zero frequency for certain M that could not be explained.

The most probable outcomes modeled by the Poisson distribution for this particular unfair coin were between 6-9 heads per 100 flios.

We then modeled the distribution waiting times for each trial between flips that would result in heads using a time series called a Poisson process, where 1 coin flip occurs per second. Before graphing this distribution, because heads is a rare outcome, I thought that the distribution would unevenly lean to the right, with a higher frequency of medium-long waiting times in between coin flips that result in heads. But the histogram gave me the exact opposite: the graph leans towards the left, with a higher frequency of relatively shorter wait times, with the highest frequency wait times being between 0 and 5 seconds. I suspect this occurs because each waiting time between heads is memoryless since each flip is independent of the previous one but I cannot understand how this would give rise to more frequent shorter wait times.

The histogram of these time intervals for 1000 coin flips looked somewhat like an exponential decay, so again to test that assumption, I took the semilog and loglog of this data and once again it generally resembled a linear graph, thus presenting evidence that the frequency of time intervals is an exponential decay and that the most frequent time intervals were the shorter ones.
The average waiting times between heads was about 12.3 seconds.
