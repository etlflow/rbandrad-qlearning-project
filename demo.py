import problems as prb
import algorithms as alg
import cv2

"""
This file will contain the code needed to run a demonstration of your project. 

For the progress report, it should contain code that shows a brief demonstration of random agents attempting to solve each problem. 

For the final report, it should contain code that shows a brief demonstration of each algorithm attempting to solve each problem. 

In both cases, to make sure we can grade these all in time, please ensure that each demonstration is just long enough to show some
meaningful behavior. If your problem is chess playing, for example, you might show 5 moves from each player, where one player uses one 
algorithm and one player uses another. If your problem is snake, you might show game long enough for the player to eat two apples or die
(whichever comes first).
"""

# settings for the demo
demoSteps = 100
frameMs = 300

# a game with a fixed seed so the demo is repeatable, and a random agent
env = prb.CliffJumper(seed=42)
agent = alg.RandomAgent()

# show the starting screen
env.showState(frameMs)

for step in range(demoSteps):
    # agent picks one of the legal moves
    action = agent.getMove(env)

    # step() returns (state, reward, crashed, done) in that order
    state, reward, crashed, done = env.step(action)

    print(f"step {step + 1}: action {action}, reward {reward}")
    env.showState(frameMs)

    # stop when the episode is over
    if done:
        break

# hold the final frame, then close the window
cv2.waitKey(2000)
cv2.destroyAllWindows()
