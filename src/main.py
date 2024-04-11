import random
import numpy as np

from environment import CatchEnv

def run_environment():
    """!
    Run the environment with a random agent.
    Make sure to adapt this to train your own implementation.
    """
    env = CatchEnv()
    number_of_episodes = 1

    for ep in range(number_of_episodes):
        env.reset()

        state, reward, terminal = env.step(random.randint(0,2))
        # You probably want to use these values to train your agent :)

        while not terminal:
            state, reward, terminal = env.step(random.randint(0,2))
            print("Reward obtained by the agent: {}".format(reward))
            state = np.squeeze(state)

        print("End of the episode")


if __name__ == "__main__":
    run_environment()
