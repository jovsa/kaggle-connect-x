def agent(observation, configuration):
    # source: https://www.kaggle.com/ajeffries/connectx-getting-started
    from random import choice

    return choice(
        [c for c in range(configuration.columns) if observation.board[c] == 0]
    )
