import problems as prb
import algorithms as alg

# comparisons to run: 0 = random agent on Cliff Jumper
compsToRun = [0]

def runRandom(env, agent, episodes):
    """
    Play `episodes` full episodes and return the mean reward and mean steps.
    env      : a problem instance (CliffJumper or CoinCatcher)
    agent    : any agent with a getMove(problem) method
    episodes : number of episodes to play
    """
    totalReward = 0
    totalSteps = 0

    for _ in range(episodes):
        env.reset()
        done = False

        while not done:
            action = agent.getMove(env)
            _, reward, _, done = env.step(action)
            totalReward += reward
            totalSteps += 1

    # averages over all episodes
    return totalReward / episodes, totalSteps / episodes

if 0 in compsToRun:
    agent = alg.RandomAgent()
    meanReward, meanSteps = runRandom(prb.CliffJumper(seed=0), agent, 20)
    print(f"{agent} on Cliff Jumper")
    print(f"Mean reward per episode: {meanReward:.2f}")
    print(f"Mean steps per episode: {meanSteps:.2f}")

if 1 in compsToRun:
    agent = alg.RandomAgent()
    meanReward, meanSteps = runRandom(prb.CoinCatcher(seed=0), agent, 20)
    print(f"{agent} on Coin Catcher")
    print(f"Mean reward per episode: {meanReward:.2f}")
    print(f"Mean steps per episode: {meanSteps:.2f}")