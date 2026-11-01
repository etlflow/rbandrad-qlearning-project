'''
This file will contain your the code for your problems. 
'''

import numpy as np
import cv2

def makeRow(rng, obstacleProb, twoObstacleProb=0.5, width=5):
  '''
  Build one new row of obstacles.
  rng             : numpy Generator, e.g. np.random.default_rng(seed)
  obstacleProb    : probability the row contains ANY obstacles
  twoObstacleProb : given a non-empty row, probability it has 2 obstacles (else 1)
  width           : number of columns (5)
  Returns an int array of length `width`: 1 = obstacle, 0 = open.
  '''
  # start with every cell open (0)
  row = np.zeros(width, dtype=int)

  # coin flip: does this row have any obstacles at all?
  if rng.random() < obstacleProb:

    # how many obstacles in this row? 1 or 2
    obstacleCount = 2 if rng.random() < twoObstacleProb else 1

    # pick which columns hold obstacles (no repeats)
    obstacleCols = rng.choice(width, size=obstacleCount, replace=False)

    # mark the chosen columns as obstacles
    row[obstacleCols] = 1

  return row