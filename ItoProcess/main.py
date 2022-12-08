import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import ItoProcess.constant as c

class ItoProcess():
  """
  Create an Ito Process
  """
  def __init__(self, drift, vol,
               start_point=c.BASE_START_POINT, start_time=c.BASE_START_TIME, 
               end_point=c.BASE_END_POINT, end_time=c.BASE_END_TIME,
               nb_point=c.BASE_NB_POINT):
    """
    drift: func, drift of the Ito Process
    Volatility: func, volatility of the Ito Process

    start_point: Optionnal, float, taken as 0 otherwise
    start_time: Optionnal, float, taken as 0 otherwise
    end_point: Optionnal, float, end point is not fixed by default
    end_time: Optionnal, float, end time is fixed as 365 by default

    nb_point: Optionnal, integer, number of points to simulate
    """
    self.current_value = start_point
    self.end_point = end_point
    self.start_time = start_time
    self.end_time = end_time
    self.nb_point = nb_point
    self.step = (end_time - start_time)/nb_point

    self.drift = drift
    self.vol = vol

  def simulate_brownian_increment(self):
    self.dW = np.random.normal(loc=0, scale=self.step, size=self.nb_point)

  def simulate_next_iteration(self, iteration):
    # We have dX = drift(t, X_t) dt + vol(t, X_t) dW_t
    # X_(t+1) = X_t + dX
    time = (iteration + 1) * self.step
    is_last_iteration = time == self.end_time
    if is_last_iteration and self.end_point:
      self.current_value = self.end_point
    else:
      variation = self.drift(time=self.step, value=self.current_value) * self.step + self.vol(time=self.step, value=self.current_value) * self.dW[iteration]
      future_value = self.current_value + variation
      self.current_value = future_value
    return self.current_value

  def simulate_path(self):
    self.simulate_brownian_increment()
    values = [self.simulate_next_iteration(iteration=iteration) for iteration in range(self.nb_point)]
    self.current_value = 0
    return values
    