# Cryo Coupe: Cliff Jumper
A Cryo Coupe jumps off a cliff, it dodges obstacles with help of cold-gas thrusters. Our goal is to demonstrate how Q-Learning compares against hand written baselines. The game will be displayed on a 5x5 screen, the car will have 3 actions (thrust left, thrust right, coast), with 
160 states (the car's column plus the next row).

## Repository Structure
The repository includes the following files:

### 1. `problems.py`  
Starts with a `makeRow()` function that creates new rows, with randomly assigned obstacles. The `CliffJumper` class, encapsulates; 
- `reset()` which helps start a new episode with the car in the center column. It helps reset the game, and return to a starting state. 
- `_state()` encodes what the agents sees, which starts with its own column in addition to the next row. 
- `step()` allows the agent to take one step, with actions that allow it to thrust left right, and coast. It returns state, reward, crashed and done.
- `getLegalMoves()` Defines the moves that are considered legal. 
- `showState` Draws the state in a window and waits a few milliseconds. 

### 2. `algorithms.py`
Contains `RandomAgent` class that contains the `getMove()` asks the problem for the legal moves and picks one at random. The final report will contain `NearestOpen`, which will try to pick the nearest open reachable cell,  `CenterSeeking` which attempts to stay safe, and then drift to the center column, and lastly `QAgent` the learning algorithm, that will use a q-table that would store state-action pairs which amount to (160 states × 3 actions) 480 values, and the agent updates it from experience.

### 3. `comparisons.py`  
This file holds the code for comparing the agents. Right now it runs only the random agent on Cliff Jumper over a few episodes and prints its mean reward and mean steps per episode. The comparisons between `QAgent`, the baselines and `RandomAgent` have not yet been built.

### 4. `demo.py`  
The demonstration script lets us run the project to see the starting state (screen). For each step in the range of steps allowed, the agent has to pick a legal move, the `step()` function returns state, reward, crashed and done. It displays the final state then closes the demo window.

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