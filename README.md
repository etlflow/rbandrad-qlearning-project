# Cryo Coupe: Cliff Jumper and Coin Catcher
This project compares tabular Q-learning against approximate (feature-based) Q-learning on two simple, scalable games. The first game, Cliff Jumper, has a Cryo Coupe jumping off a cliff and dodging obstacles with the help of cold-gas thrusters. The second game, Coin Catcher, has a paddle sliding along the bottom of the screen to catch falling coins.

Cliff Jumper is displayed on a 5x5 screen. The car has 3 actions (thrust left, thrust right, coast) and 160 states (the car's column plus the next row).

Coin Catcher is displayed on a 3 column screen. The paddle has 3 actions (move left, move right, stay) and 192 states (the paddle's column plus the next 2 rows).

## Repository Structure
The repository includes the following files:

### 1. `problems.py`  
Starts with a `makeRow()` function that creates new rows with randomly assigned obstacles (or coins). It contains two classes, `CliffJumper` and `CoinCatcher`, which share the same methods:
- `reset()` starts a new episode with the car (or paddle) in the center column. It resets the game and returns the starting state.
- `_state()` encodes what the agent sees: its own column plus the visible rows.
- `step()` lets the agent take one step. It returns the state, reward, crashed and done.
- `getLegalMoves()` returns the moves that keep the agent on the screen.
- `showState()` draws the state in a window and waits a few milliseconds.

The games differ in how an episode ends. In Cliff Jumper an episode ends on a crash or at the step limit. In Coin Catcher nothing ends the episode early, only the step limit, and a missed coin just costs reward.

### 2. `algorithms.py`
Contains the `RandomAgent` class. Its `getMove()` asks the problem for the legal moves and picks one at random, so it works on both games. The final report will also contain `QAgent`, the tabular learning algorithm that stores a value for each state-action pair, and `ApproxQAgent`, which learns weights for hand-written features instead of a table.

### 3. `comparisons.py`  
This file holds the code for comparing the agents. Right now it runs the random agent on each game over 20 episodes and prints the mean reward and mean steps per episode. The list `compsToRun` selects which comparisons to run. The comparisons between `QAgent` and `ApproxQAgent` have not yet been built.

### 4. `demo.py`  
The demonstration script lets us run the project to see each game. A random agent plays Cliff Jumper and then Coin Catcher. For each step in the range of steps allowed (at most 100), the agent picks a legal move and the `step()` function returns the state, reward, crashed and done. Each game ends when the episode is over or the steps run out, then the demo window closes.

## Setup Instructions

### Step 1: Prepare Python Environment
These instructions will setup the evaluation environment we will use to evaluate your project. Use this environment (without addition or modification) to make sure your code will run the same on our machines.
- Download and install [Anaconda](https://www.anaconda.com/download)
- Open Terminal (or Anaconda prompt in Windows)
- `conda create --name evalenv python=3.9`
- `conda activate evalenv`
- `pip install --upgrade pip`
- `pip install -r requirements.txt`

### Step 2: Activate Python Environment
- Open Terminal (or Anaconda prompt in Windows)
- `conda activate evalenv`
  
### Step 3: Run demo.py
- Open project directory: `cd <your_directory>`
- `python demo.py`

## Repository
https://github.com/etlflow/rbandrad-qlearning-project
