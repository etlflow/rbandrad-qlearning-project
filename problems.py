"""
This file will contain your the code for your problems.
"""

import numpy as np
import cv2


def makeRow(rng, obstacleProb, twoObstacleProb=0.5, width=5):
    """
    Build one new row of obstacles.
    rng             : numpy Generator, e.g. np.random.default_rng(seed)
    obstacleProb    : probability the row contains ANY obstacles
    twoObstacleProb : given a non-empty row, probability it has 2 obstacles (else 1)
    width           : number of columns (5)
    Returns an int array of length `width`: 1 = obstacle, 0 = open.
    """
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


class CliffJumper:
    """
    Cryo Coupe: Cliff Jumper.
    A car falls down a cliff and uses cold-air thrusters to dodge obstacles.
    Actions: 0 = thrust left, 1 = thrust right, 2 = coast.
    """

    def __init__(
        self,
        obstacleProb=0.5,
        twoObstacleProb=0.5,
        seed=42,
        width=5,
        height=5,
        maxSteps=500,
    ):
        # game settings (stored so reset/step can use them later)
        self.obstacleProb = obstacleProb
        self.twoObstacleProb = twoObstacleProb
        self.width = width
        self.height = height
        self.maxSteps = maxSteps

        # rewards and costs
        # on a successful step
        self.surviveReward = 1

        # on a crash
        self.crashReward = -10

        # movment of left/right only; coasting is free
        self.thrustCost = 0.2

        # random number generator
        self.rng = np.random.default_rng(seed)

        # sizes the Q-agent will need
        self.numActions = 3
        self.numStates = self.width * (2**self.width)

        # state variables
        self.grid = None
        self.carCol = None
        self.stepCount = None
        self.reset()

    def reset(self):
        """
        Start a new episode: fresh random rows, car in the center column.
        Only the game is reset. Returns the starting state.
        """
        # build `height` random rows, then stack them into a 2D array
        rows = [
            makeRow(self.rng, self.obstacleProb, self.twoObstacleProb, self.width)
            for _ in range(self.height)
        ]

        # defines the grid as a 2d numpy array
        self.grid = np.array(rows)

        # car starts in the center column
        self.carCol = self.width // 2

        # no steps taken yet
        self.stepCount = 0

        return self._state()

    def _state(self):
        """
        Encode what the agent sees: its column plus the next row.
        Returns an int.
        """
        # the agent sees only the next row
        nextRow = self.grid[0]

        # read the 0/1 cells as a binary number, leftmost cell = highest bit
        rowBits = 0
        for cell in nextRow:
            # shift the running total left by one bit, then add this cell
            rowBits = rowBits * 2 + cell

        # car column picks the block of 2**width states, rowBits picks inside it
        return int(self.carCol * (2**self.width) + rowBits)

    def step(self, action):
        """
        Advance one step.
        action: 0 = thrust left, 1 = thrust right, 2 = coast.
        Returns (state, reward, crashed, done).
        """
        # column change for each action: left = -1, right = +1, coast = 0
        move = [-1, 1, 0][action]

        # True when the action is left or right
        thrusted = action < 2

        # thrust first
        self.carCol = self.carCol + move
        crashed = False

        # wall check: off the screen on either side is a crash
        if self.carCol < 0 or self.carCol >= self.width:
            crashed = True
        else:
            # the row arriving at the car is the next row
            arrivingRow = self.grid[0]

            # collision check: is there an obstacle where the car is?
            if arrivingRow[self.carCol] == 1:
                crashed = True

            # scroll: drop row 0, append a new random row at the end
            newRow = makeRow(
                self.rng, self.obstacleProb, self.twoObstacleProb, self.width
            )
            self.grid = np.vstack((self.grid[1:], newRow))

        self.stepCount += 1

        # reward
        if crashed:
            print("CRASH!")
            reward = self.crashReward
        else:
            reward = self.surviveReward
            if thrusted:
                reward = reward - self.thrustCost

        # episode ends on a crash or when the step limit is reached
        done = crashed or self.stepCount >= self.maxSteps

        return self._state(), reward, crashed, done

    def getLegalMoves(self):
        """
        Actions that keep the car on the screen.
        Returns a list drawn from [0, 1, 2].
        """
        # coasting is always allowed
        moves = [2]

        # thrusting left needs a column to the left of the car
        if self.carCol > 0:
            moves.append(0)

        # thrusting right needs a column to the right of the car
        if self.carCol < self.width - 1:
            moves.append(1)

        return moves