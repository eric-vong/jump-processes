# GLOBAL VARIABLES

BASE_START_POINT = 0
BASE_START_TIME = 0
BASE_END_POINT = None
BASE_END_TIME = 365
BASE_NB_POINT = 1000

def drift1(time, value):
  return 0

def drift2(time, value):
  return time

def vol(time, value):
  return 1
  