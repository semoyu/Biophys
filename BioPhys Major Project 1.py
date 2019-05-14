import numpy as np
import matplotlib.pyplot as plt

# Comm 1
β =
γ =
α = #1/r
μ =
p =

N =
S =
I =
V = #are there those vaccinated before the diease starts

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
