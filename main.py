import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import ItoProcess.main
import ItoProcess.constant as c

process1 = ItoProcess(drift=c.drift1, vol=c.vol)
path1 = process1.simulate_path()
plt.plot(path1)
plt.show()

process2 = ItoProcess(drift=c.drift2, vol=c.vol)
path2 = process2.simulate_path()
plt.plot(path2)
plt.show()