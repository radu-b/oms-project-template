# Description

This is a template that can be used as a starting point for Python-based experimental reports. I've used this during my classes at OMS CS.

The basic pattern is to first run experiments, save the resulting data and only then plot the results. This template helps enforce that pattern.

Any experiment running code should go in `src/experiments.py`. There, use `run_experiment(name, callback)` and pass a name for your experiment and a callback for the actual experiment code. The callback should just return a dictionary with all the results of the experiment. Of course, the code can be split in more files, these should be just the entry points.

Do this for all the experiments, and `run_experiment` will handle serialization of the result in the `/data` folder. It will also re-run only experiments that don't have output data, so that you don't have to keep commening and uncommenting code. Just call all `run_experiment` for all experiments in a row, and delete any data you want to re-generate before running the script.

Similarly, the plotting code should go in `src/plots.py`. It's best if you use an IDE that allows you to run comment cells (`#%%` delimited), as you can run the code both as a script (to generate all your plots) or step by step (to tweak any plotting parameters). To get the experiment data, just call `experiment_data(name)` and it will handle deserialization.

## Installing prerequites

The code is compatible with Python 3 and requires `matplotlib` and `numpy`.

The report uses Pandoc and generates a PDF file using LaTeX. This is great a way to get a "paper"-like report while still using the simple markdown syntax.

To generate the report you need the following system packages:

- `texlive-full` (or you can use this gist https://gist.github.com/briandk/924d101f28dbf309758206fa3eff32b4 for a lighter install)
- `pandoc`
- `pandoc-citeproc`
- `make`

These should be added according to your system, for instance in Ubuntu run `sudo apt-get install pandoc`.

# Important

Usually the projects in OMS CS require that this file (`README.md`) contains instructions for reproducing the experiements. So please replace the contents of this files with appropriate explanations. They could be something like the ones below, just add any extra requirements and instructions.

## Running the project

Running this project requires Python 3.6 and the latest version of the following libraries:

- matplotlib
- numpy

The project runs in two stages:

- running the experiments to generate data
- running the analysis to create the plots

To run the experiments, start the `experiments.py` script from the `src` folder (your working directory needs to be `src`).

Each experiment, when run, creates it's own data file in the `data` folder. To re-run some experiments, first delete the corresponding file (otherwise the experiment will be skipped), and then, restart `experiments.py`.

In order to generate the plots, run the `plots.py` script from the `src` folder.

This can be done only after the required experiment data has been saved. The plots are saved in the `plots` folder, where they overwrite previous plots (they don't cache previous results, unlike the experiments).
