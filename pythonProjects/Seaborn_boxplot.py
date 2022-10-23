import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math

eff = [3, 6, 4, 5, 2]
data = [1, 3, 5, 7, 9]
s = []

for i in range(len(eff)):
    for j in range(eff[i]):
        s.append(data[i])

print(round(np.percentile(s, 61), 4))

x = [[1]*3 + [3]*6 + [5]*4 + [7]*5 + [9]*2]
df = pd.DataFrame(x)
df.T.boxplot(vert=False, grid=False)
plt.subplots_adjust(left=0.01)
plt.xlabel('Superficie en dizaine de ha')
plt.title('Boite à moustache de la distribution')
plt.xticks(s)
plt.show()
