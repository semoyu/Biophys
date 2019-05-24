import numpy as np
import matplotlib.pyplot as plt

N = np.loadtxt('C:/Users/semoyu/Desktop/CenPop2010_OR.txt', skiprows=1, delimiter=",", usecols=(2))
lat = np.loadtxt('C:/Users/semoyu/Desktop/CenPop2010_OR.txt', skiprows=1, delimiter=",", usecols=(5))
long = np.loadtxt('C:/Users/semoyu/Desktop/CenPop2010_OR.txt', skiprows=1, delimiter=",", usecols=(6))

μ = (11.8 / 1000)/365
def SIRV(β, γ, p, RefCity, RCPreInfected, PreInfected, Prevaccinated, EndTime):
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
    Sum = 0
    for i in range(0,len(N)):
        if i == RefCity:
            ICity.append(RCPreInfected*N[i])
        else:
            ICity.append(PreInfected*N[i])
        Sum += α[i]*ICity[i]/N[i]

    S = np.arange(0,EndTime)
    I = np.arange(0,EndTime)
    R = np.arange(0,EndTime)
    V = np.arange(0,EndTime)
    PS = []
    for t in range(0,EndTime-1):
        I[0] = ICity[RefCity]
        R[0] = 0
        V[0] = Prevaccinated*N[RefCity]
        S[0] = N[RefCity] - ICity[RefCity] - R[0] - V[0]
        dS = (1-p)*μ*N[RefCity]-μ*S[t]-β*S[t]*(I[t]/N[RefCity] + Sum)
        dI = β*S[t]*(I[t]/N[RefCity] + Sum) - γ*I[t] - μ*I[t] - I[t]*0.0066
        dR = γ*I[t]-μ*R[t]
        dV = p*μ*N[RefCity] - μ*V[t]
        S[t+1] = S[t] + dS
        I[t+1] = I[t] + dI
        R[t+1] = R[t] + dR
        V[t+1] = V[t] + dV
    EndPop = S[EndTime-1]+I[EndTime-1]+R[EndTime-1]+V[EndTime-1]
    return EndPop
    # plt.plot(np.arange(0,EndTime), V ,'--',label='Vaccinated')
    # plt.plot(np.arange(0,EndTime), S+I+R+V ,label='Pre-Vacc')
    # plt.plot([], [], ' ', label='Vaccinated %1.2f' %p)
    # plt.plot([], [], ' ', label='Percent Saved %1.2f' %(((EndPop-571680)/N[RefCity])*100))
    # plt.legend(loc ='best')
    # plt.xlabel('Time (Days)')
    # plt.ylabel('Population')
    # plt.title('City: %i' %RefCity)

def Fred(β, γ, p, RefCity, RCPreInfected, PreInfected, Prevaccinated, EndTime):
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
    Sum = 0
    for i in range(0,len(N)):
        if i == RefCity:
            ICity.append(RCPreInfected*N[i])
        else:
            ICity.append(RCPreInfected*N[i])
        Sum += α[i]*ICity[i]/N[i]

    S = np.arange(0,EndTime)
    I = np.arange(0,EndTime)
    R = np.arange(0,EndTime)
    V = np.arange(0,EndTime)

    for t in range(0,EndTime-1):
        I[0] = ICity[RefCity]
        R[0] = 0
        V[0] = Prevaccinated*N[RefCity]
        S[0] = N[RefCity] - ICity[RefCity] - R[0] - V[0]
        dS = (1-p)*μ*N[RefCity]-μ*S[t]-β*S[t]*(I[t]/N[RefCity] + Sum)
        dI = β*S[t]*(I[t]/N[RefCity] + Sum) - γ*I[t] - μ*I[t] - I[t]*0.0066
        dR = γ*I[t]-μ*R[t]
        dV = p*μ*N[RefCity] - μ*V[t]
        S[t+1] = S[t] + dS
        I[t+1] = I[t] + dI
        R[t+1] = R[t] + dR
        V[t+1] = V[t] + dV
    EndPop = S[EndTime-1]+I[EndTime-1]+R[EndTime-1]+V[EndTime-1]
    plt.plot(np.arange(0,EndTime), S+I+R+V ,label='Non Pre-Vacc')
    plt.legend(loc= 'best') #Non pre-vacc

'''SIRV(β, γ, p, RefCity, RCPreInfected Percent, PreInfected Percent, Prevaccinated Percent, EndTime)'''
PS1 = []
PS2 = []
# plt.ion()
for p in range(0,101,1):
    # plt.cla()
    # Fred(.5,1/100,p/100,0,.12,.12,0,3650)
    PS1.append(((SIRV(.5,1/100,p/100,0,.12,.12,0,3650)-571680)/N[0])*100)
    PS2.append(((SIRV(.5,1/100,p/100,0,.12,.12,.8,3650)-571680)/N[0])*100)
    # plt.ylim(550000,960000)
    # plt.pause(1e-9)
# plt.ioff()
plt.figure()
plt.plot(np.arange(0,101,1),PS1, label = 'Non Prevacc')
plt.plot(np.arange(0,101,1),PS2, label = 'Prevacc')
plt.xlabel('Percent of Newborns Vaccinated')
plt.ylabel('Percent of Population Alive Due to Vaccination')
plt.legend(loc = 'best')
plt.show()
