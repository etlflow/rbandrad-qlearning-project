## Cryo Coupe: Cliff Jumper
A Tesla Roadster jumps off a cliff, it dodges obsacles with help of cold-gas thrusters. Our goal is to demonstrate how Q-Learning compares against hand written baselines. 

---

## Repository Structure
The repository includes the following files:

### 1. `problems.py`  
Starts with a `makeRow()` function that creates new rows, with randomly assigned obstacles. The `CliffJumper` class, encapsulates; 
    - `reset()` which helps start a new episode with the car in the center column. It helps reset the game, and return to a starting state. 
    - `_state()` encodes what the agents sees, which starts with its own column in addition to the next row. 
    - `step()` allows the agent to take one step,, with actions that allow it to thrust left right, and coast.
    - `getLegalMoves()` Defines the moves that are considered legal for the agent. 
    - `showState` Draws the state in a window and waits a few milliseconds. 

### 2. `algorithms.py`
Contains `RandomAgent` class that contains the `getMove()` funtion that allows the random agent to get all the legal moves the agent is allowed to make. The final report will contain `NearestOpen`, which will try to pick the nearest open reachable cell,  `CenterSeeking` which attempts to stay safe, and then drift to the center column, and lastly `QAgent` the learning algorithm, that will use a q-table to record past states. 

### 3. `comparisons.py`  
This file will contain the code for performing comparisons between your selected algorithms. This portion has not yet been built. 

### 3. `demo.py`  
The demonstration script lets us run the project to see the starting state (screen). For each step in the range of steps allowed, the agent has to pick a legal move, the `step()` function returns state, reward, crashed, or done. It displays the final state then closes the demo window.

---

## Setup Instructions

### Step 1: Prepare Python Environment
These instructions will setup the evaluation environment we will use to evaluate your project. Use this environment (without addition or modification) to make sure your code will run the same on our machines.
- Download and install [Anaconda](https://www.anaconda.com/download)
- Open Terminal (or Anaconda prompt in Windows)
- `conda create --name evalenv python=3.9`
- `conda activate evalenv`
- `pip install --upgrade pip`
- `pip install -r requirements.txt`

### Step 1.1: Activate Python Environment
- Open Terminal (or Anaconda prompt in Windows)
- `conda activate evalenv`
  
### Step 2: Run demo.py
- Open project directory: `cd <your_directory>`
- `python demo.py`