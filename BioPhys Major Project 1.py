import numpy as np
import matplotlib.pyplot as plt

# α ratio of people interacting with other communities: should be from 0.0-1.0: define as 1/r where r is distance from two communities
# β risk of getting infected: if 1.0 100% of contractoin needs to be between 0.0-1.0
# γ rate of recovery of infected person
# μ death and birth rate
# N population from data

#Ross' computer
# N = np.loadtxt('/Users/ross/Desktop/Code/PH591/CenPop2010_OR.txt', skiprows=1, delimiter=",", usecols=(2))
# lat = np.loadtxt('/Users/ross/Desktop/Code/PH591/CenPop2010_OR.txt', skiprows=1, delimiter=",", usecols=(5))
# long = np.loadtxt('/Users/ross/Desktop/Code/PH591/CenPop2010_OR.txt', skiprows=1, delimiter=",", usecols=(6))

#Cameron's computer
N = np.loadtxt('/Users/ross/Desktop/Code/PH591/CenPop2010_OR.txt', skiprows=1, delimiter=",", usecols=(2))
lat = np.loadtxt('/Users/ross/Desktop/Code/PH591/CenPop2010_OR.txt', skiprows=1, delimiter=",", usecols=(5))
long = np.loadtxt('/Users/ross/Desktop/Code/PH591/CenPop2010_OR.txt', skiprows=1, delimiter=",", usecols=(6))

#Comm 1
β = .9 #measels
γ = (1/7) #recovery rate of measels
α = .5 #1/r
μ = (3.425*(10**-5)) #births per person per day
p = .5



S1[0] = N[0] #S1[time index] = N[community index] 
I = 1
V = 10 #are there those vaccinated before the diease starts
End = 1000

dS = (1-p)*N*μ-μ*S-β*S*(I/N + α*I/N)
dI = β*S*(I/N) - γ*(I/N)
dR = γ*(I/N)-μ*γ
dV = p*μ - μ*V

S = N
I = 0
R = 0
V = 0
for t in range(0,End):
    S += dS
    I += dI
    R += dR
    V += dV
