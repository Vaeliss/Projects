import matplotlib.pyplot as plt
import math
from random import choice

class CasualStock:

    def __init__(self,points):
        self.points = points
        self.y = [choice([i for i in range(1,101)])]

    def fill_y(self):
        for i in range(self.points-1):
            self.y.append((1.0 + choice([i/1000 for i in range(-25,+26)]))*self.y[-1])
'''
stocks_perf = []
for i in range(500):
    cs = CasualStock(3650)
    cs.fill_y()
    stocks_perf.append(cs.y[-1]*100/cs.y[0]-100)

tenYearsPerf = sum(stocks_perf)/500
print('Causal500, 10 year performance: '+str(tenYearsPerf))

'''

cs  = CasualStock(3650)
cs.fill_y()
fig,ax = plt.subplots(figsize=(9,15))

ax.set_title('Random stock',fontsize=20)
ax.set_xlabel('time',fontsize=14)
ax.set_ylabel('price',fontsize=14)
ax.plot(range(cs.points),cs.y,c='blue',linewidth=3)

plt.show()
