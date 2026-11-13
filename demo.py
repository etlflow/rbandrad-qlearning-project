"""
This file runs a short demonstration of the project.
A random agent plays each game in turn, Cliff Jumper and then Coin Catcher.
Each game is shown for a limited number of steps, or until the episode ends.
"""

import problems as prb
import algorithms as alg
import cv2

# settings for the demo
demoSteps = 100
frameMs = 300

# one instance of each game, and one random agent that plays both
games = [
    prb.CliffJumper(seed=42),
    prb.CoinCatcher(seed=42),
]
agent = alg.RandomAgent()

for env in games:
    print(f"{agent} playing {type(env).__name__}")

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
