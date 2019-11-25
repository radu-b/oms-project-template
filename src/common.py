import os

import matplotlib

# Stops the plots from popping up when running the script from thge command line
# matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
from timeit import default_timer as timer

# Uses the LaTeX font (Latin Modern Roman) also in plots. This requires
# that you have a valid LaTeX installation and also may require that
# you have the corresponding font files in TTF format on your system.
plt.rcParams["font.family"] = ["Latin Modern Roman"]
plt.rcParams["text.usetex"] = True


def plot_file(name):
    """ Gets the standard file for saving a plot """

    # Maybe the script is run from src, maybe from the project root
    if os.path.exists("plots"):
        return f"plots/{name}.pdf"
    elif os.path.exists("../plots"):
        return f"../plots/{name}.pdf"
    else:
        print("Please run from the `src` folder.")


def experiment_exists(name):
    return os.path.exists(experiment_file(name))


def experiment_file(name):
    """ Gets the standard path for an experiment output data file"""

    # Maybe the script is run from src, maybe from the project root
    if os.path.exists("data"):
        return f"data/{name}.npz"
    elif os.path.exists("../data"):
        return f"../data/{name}.npz"
    else:
        print("Please run from the `src` folder.")


def run_experiment(name: str, experiment: callable, force: bool = False):
    """ Runs an experiment, only if its output file does not already exist. To re-run an experiment, you'll have to manually remove the corresponding file in `/data`.

    Args:
        name: the name of the experiment
        experiment: a function/lambda that actually performs the experiment and returns a dict with the results
        force: forces a re-run even if the experiment output exists
    """

    if not force and experiment_exists(name):
        print("Skipping", name)
        return

    print("Running", name)

    data = experiment()

    # Use numpy to save the data
    np.savez_compressed(experiment_file(name), **data)


def print_row(*args):
    """Prints the input items in the markdown table row format"""

    print("|", " | ".join(str(a) for a in args), "|")
