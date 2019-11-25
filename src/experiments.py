from common import *


def experiment_1():
    # Set the random seed, so the experiment can be reproduced
    np.random.seed(10)

    x = np.random.rand(100)
    y = np.random.rand(100)

    # Return a map with all recorded data
    return {"x": x, "y": y}


def experiment_2():
    np.random.seed(10)

    start = timer()

    x = np.linspace(0, 2 * np.pi, 50)
    y = np.sin(x)

    end = timer()

    return {"x": x, "y": y, "time": end - start}


if __name__ == "__main__":

    run_experiment("experiment_1", experiment_1)
    run_experiment("experiment_2", experiment_2, force=True)

    # Same for the other experiments, only the ones that don't already have a result in `/data` will be re-run.

    # If you do want to re-run an experiment, manually delete the corresponding .npz file from `/data`. The default is like that to prevent accidental re-runs. If you need to keep re-running an experiment in order to fix bugs, set the third parameter force=True.
