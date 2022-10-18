import numpy as np
import matplotlib.pyplot as plt

class VelSzamok():

    def __init__(self, n_rows, n_cols):
        self.n_rows=n_rows
        self.n_cols=n_cols
        self.value=np.random.random((self.n_rows, self.n_cols))
    def plot_column_averages(self, show=True):
        averages =self.value.mean(axis=0)
        plt.plot(averages)
        if show:
            plt.show()


a1=VelSzamok(5,2)
a2=VelSzamok(6,3)
#print(a1.value)
#print(a2.value)
print(VelSzamok.plot_column_averages(a1))

