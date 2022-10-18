import numpy as np
from scipy.stats import norm

from options import Option

opt=Option("c",1, 100, "20221215")

K=100
expiry="20221215"
C=Option("c",1,K,expiry)
P=Option("c",-1,K,expiry)

S=124.35
t=0.23
vola=0.45

print(C.calcPrice(S,t,vola)+P.calcPrice(S,t,vola)-S+K)

