from kaggle_environments import make
import agents
import utils
from datetime import datetime

if __name__ == "__main__":
    # initialize
    env = make("connectx", debug=True)
    env.reset()

    #get agent
    my_agent = agents.random_agent.agent
    env.run([my_agent, "random"])

    # # sample env.render
    # print(env.render(mode="ansi", width=500, height=450))

    # Play as first position against random agent.
    trainer = env.train([None, "random"])

    observation = trainer.reset()

    while not env.done:
        my_action = my_agent(observation, env.configuration)
        print("My Action", my_action)
        observation, reward, done, info = trainer.step(my_action)
        # env.render(mode="ipython", width=100, height=90, header=False, controls=False)
    print(env.render())

    # Compare agent against baselines
    utils.compare_against_baseline(my_agent)

    time_stamp = datetime.utcnow().strftime("%y_%m_%d__%f")
    # utils.write_agent_to_file(my_agent, f"submission_{time_stamp}.py")
