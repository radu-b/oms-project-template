# You can use the cell delimiter (#%%) to run your code block by block in editors that support them, such as PyCharm or Visual Studio Code, via Jupyter. This works great when plotting, as you often need to tweak things and retry the same code. In order for local imports to work, you might have to adjust the root folder for Jupyter (to ${workspaceFolder}/src).

#%%
from common import *

#%% Plot experiment 1

e1_data = np.load(experiment_file("experiment_1"))
e1_x = e1_data["x"]
e1_y = e1_data["y"]

plt.figure(figsize=(10, 7))
plt.title("First experiment")
plt.xlabel("X")
plt.ylabel("Y")

plt.scatter(e1_x, e1_y)

plt.tight_layout()
plt.savefig(plot_file("experiment_1"))
plt.show()

#%% Print a sample markdown table (paste output in report.md)

print("First table")
print()
print_row("Iteration", "Input X", "Output Y")
print("|-----|-----:|-----:|")

for i in range(1, 4):
    print_row(i, f"{e1_x[i]:.2f}", f"{e1_y[i]:.2f}")

#%% Plot experiment 2

e2_data = np.load(experiment_file("experiment_2"))
e2_x = e2_data["x"]
e2_y = e2_data["y"]
e2_time = e2_data["time"]

print("Second experiment duration", e2_time)

plt.figure(figsize=(5, 5))
plt.title("Second experiment")
plt.xlabel("X")
plt.ylabel("Y")

plt.plot(e2_x, e2_y)

plt.tight_layout()
plt.savefig(plot_file("experiment_2"))
plt.show()


# %%
