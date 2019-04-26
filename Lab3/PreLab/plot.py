import numpy as np
import pylab
import matplotlib.pyplot as plt

# y = [(((1.5 / (Req + 1)) * (1.5 / (Req + 1))) * Req) for Req in np.arange(0.01, 100, 0.01)]
# x = [Req for Req in np.arange(0.01, 100, 0.01)]

y = [3.411, 3.415, 3.410, 3.123, 1.931, 1.152, 0.506, 0.036, 0.002]
x = [100, 250, 500, 3000, 10000, 20000, 50000, 150000, 250000]

fig, ax = plt.subplots()
ax.set_xscale('symlog', basex=10)

ax.plot(x, y)

# plt.show()

# plt.savefig('part3.pgf')

Req = 0.01
print(((1.5 / (Req + 1)) * (1.5 / (Req + 1))) * Req)
Req = 1
print(((1.5 / (Req + 1)) * (1.5 / (Req + 1))) * Req)
