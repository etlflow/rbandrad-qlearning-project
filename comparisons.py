"""
This file will contain code for performing your comparisons. It should perform (or have a setting that lets us perform) ***ALL*** your comparisons when run.
We recommend adding the ability to run a subset of the comparisons for testing purposes (as illustrated below).
"""

import problems as prb
import algorithms as alg

# comparisons to run: 0 = random agent on Cliff Jumper
compsToRun = [0]

if 0 in compsToRun:
    episodes = 20
    totalReward = 0
    totalSteps = 0

    env = prb.CliffJumper(seed=0)
    agent = alg.RandomAgent()

    for _ in range(episodes):
        env.reset()
        done = False

        while not done:
            action = agent.getMove(env)
            _, reward, _, done = env.step(action)
            totalReward += reward
            totalSteps += 1

    print(f"{agent} over {episodes} episodes")
    print(f"Mean reward per episode: {totalReward / episodes:.2f}")
    print(f"Mean steps per episode: {totalSteps / episodes:.2f}")
