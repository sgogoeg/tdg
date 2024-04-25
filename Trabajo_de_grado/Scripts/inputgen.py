import numpy as np

num_samples = 100

startcoup = -2
stopcoup =  1
basecoup = 10 

couplings = np.logspace(startcoup, stopcoup, num_samples, base=basecoup)

startmass = 0
stopmass =  3
basemass = 10 

masses = np.logspace(startmass, stopmass, num_samples, base=basemass)

input = []

for i in masses:

    mass = i*np.ones(couplings.shape)
    inputtemp = np.column_stack((mass, couplings))

    input.append(inputtemp)

input = np.vstack(input)

# Save to CSV
np.savetxt("inputW65.csv", input, delimiter=",")