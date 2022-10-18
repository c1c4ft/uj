import numpy as np
from scipy.stats import norm

class Option:
    def __init__(self, right:str, pos:int, strike:float, expiry:str):
        #call v put
        self.right=right
        #long v short
        self.pos=pos
        #kötési árf
        self.strike=strike
        #lejárat
        self.expiry=expiry
        #valatilitás
        self.vola=np.nan
    def initVola(self):
        self.vola=1
    def calcPrice(self, S: float, timeToExp: float, vola: float, rate=0):
        if not np.isnan(vola):
            IV = vola
        else:
            IV = self.vola if not np.isnan(self.vola) else self.initVola
        if np.isnan(IV):
            print("Vola is not set!")
            return np.nan
        t = timeToExp
        if t > 0:
            d1 = (np.log(S / self.strike) + (rate + IV ** 2 / 2) * t) / (IV * np.sqrt(t))
            d2 = d1 - IV * np.sqrt(t)
            if self.right == 'C':
                return (S * norm.cdf(d1) - norm.cdf(d2) * self.strike * np.exp(-rate * t)) * self.pos
            else:
                return (norm.cdf(-d2) * self.strike * np.exp(-rate * t) - S * norm.cdf(-d1)) * self.pos
        elif t == 0:
            return self.payoff(S)
        else:
            print("expired!")
            return np.nan
    def payoff(self,spot:float):
        if self.right=="c":
            return max(spot-self.strike, 0)*self.pos
        elif self.right=="p":
            return max(self.strike-spot, 0)*self.pos
        else:
            print("Wrong option type")
            return None




opt=Option("c",1, 100, "20221215")
print(Option.payoff(opt, 120))
print(Option.calcPrice(opt, 110,0.5, 0.3,0.04))








