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

'''Selected Parameters'''
RefCity = 0
PreInfected = 0
EndTime = 30 #Days

'''Tourism'''
#Rate at which people visit
α = []
for i in range(0,len(N)):
    dlon = (long[i] - long[RefCity])*np.pi/180
    dlat = (lat[i] - lat[RefCity])*np.pi/180
    a = (np.sin(dlat/2))**2 + np.cos(lat[RefCity]*np.pi/180) * np.cos(lat[i]*np.pi/180) * (np.sin(dlon/2))**2
    c = 2 * np.arctan2( np.sqrt(a), np.sqrt(1-a) )
    R = 6373 #Radius of Earth
    d = R * c
    if i == RefCity:
        α.append(1)
    else:
        α.append(1/d)
#Number of Infected in other Cities
ICity = []
for i in range(0,len(N)):
    ICity.append(PreInfected)
#Number of Infected visiting the Reference City
Sum = 0
for i in range(0,len(N)):
    Sum += α[i]*ICity[i]/N[i]
#Creates arrays
S = np.arange(0,EndTime)
I = np.arange(0,EndTime)
R = np.arange(0,EndTime)
V = np.arange(0,EndTime)
#Fills arrays over time
for t in range(0,EndTime):
    S[0] = N[RefCity]
    I[0] = ICity[RefCity]
    R[0] = 0
    V[0] = 0
    dS = (1-p)*N[RefCity]*μ-μ*S[t]-β*S[t]*(I[t]/N[RefCity] + Sum)
    dI = β*S[t]*(I[t]/N[RefCity]) - γ*(I[t]/N[RefCity]) - μ*I[t]
    dR = γ*(I[t]/N[RefCity])-μ*γ
    dV = p*μ - μ*V[t]
    S[t] += dS
    I[t] += dI
    R[t] += dR
    V[t] += dV
