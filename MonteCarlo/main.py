import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import ItoProcess.main
import MonteCarlo.constant as c

def MonteCarloGraph(Ito_process: ItoProcess, nb_simulation=c.BASE_NB_POINT_MC) -> pd.DataFrame:
  # Takes into argument an Ito process and returns a dataframe with nb_simulation of the trajectory of the process
  storage = [Ito_process.simulate_path() for _ in range(nb_simulation)]
  return pd.DataFrame(data=storage)
  