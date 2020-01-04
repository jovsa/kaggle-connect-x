# file contains util functions

import inspect
from kaggle_environments import evaluate
import os


def mean_reward(rewards):
    return sum(r[0] for r in rewards) / sum(r[0] + r[1] for r in rewards)


def compare_against_baseline(agent, baselines=["random", "negamax"], num_episodes=10):
    for baseline in baselines:
        print(
            f"current agent vs {baseline} agent:",
            mean_reward(evaluate("connectx", [agent, baseline], num_episodes)),
        )


def write_agent_to_file(function, file):
    submission_folder = "submissions"
    if not os.path.exists(submission_folder):
        os.makedirs(submission_folder)

    full_path = os.path.join(submission_folder, file)
    with open(full_path, "a" if os.path.exists(full_path) else "w") as f:
        f.write(inspect.getsource(function))
        print(function, "written to", full_path)
