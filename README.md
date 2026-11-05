## Cryo Coupe: Cliff Jumper

A Tesla Roadster jummps off a cliff, it dodges obsacles with help of cold-gas thrusters. Our goal is to demonstrate how Q-Learning compares against hand written baselines. 

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
This file will provide a brief demonstration of your project.

#### Submission Requirements:
- **Progress Report:** Demonstrate *random agents* attempting to solve each problem.  
- **Final Report:** Demonstrate *each algorithm* attempting to solve at least one problem.  

#### Guidelines for Demonstrations:
Keep the demonstrations concise but meaningful to highlight key behaviors. Some agent types (e.g., random agents) may struggle or fail to solve a problem. Some problems may take a long time to complete (e.g., a full game of chess). In such cases, you should cut off the demonstration after a representative sample of the agent's behavior and problem mechanics has been shown. 

### 4. `problems.py`  
This file will contain the implementation of the problems you are solving with your AI algorithms.  
- Ensure that the problems are clearly defined and modular, so the algorithms can be easily tested on each.  
- For the **progress report**, this file should be fully implemented and require no major edits afterward.

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