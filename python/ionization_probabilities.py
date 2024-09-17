import os
import time
import matplotlib
import numpy as np
from matplotlib import pyplot as plt

with open("dir_paths.txt", "r") as f:
    basedir = f.readline().split("\n")[0]
    inner_electron_dir_path = f.readline().split("\n")[0]
    external_electron_dir_path = f.readline().split("\n")[0]

if not os.path.exists(basedir + "/arrays_saved/ionization_probabilities"):
    os.makedirs(basedir + "/arrays_saved/ionization_probabilities")
if not os.path.exists(basedir + "/imgs/ionization_probabilities"):
    os.makedirs(basedir + "/imgs/ionization_probabilities")

t = np.load(basedir + "/arrays_saved/time_evol/t.npy")

x0 = np.load(inner_electron_dir_path + "/RSSFM1D/src/arrays_saved/x.npy")
x1 = np.load(external_electron_dir_path + "/RSSFM1D/src/arrays_saved/x.npy")

dx0 = x0[1] - x0[0]
dx1 = x1[1] - x1[0]

surface_indexes = np.array([325, 350, 400, 500, 600, 700])
np.save(
    basedir + "/arrays_saved/ionization_probabilities/surface_indexes.npy",
    surface_indexes,
)
ionization_probabilities = np.zeros(
    (
        len(surface_indexes),
        len(t),
    )
)

for i in range(len(t)):
    ts = time.time()
    psi = np.load(basedir + f"/arrays_saved/time_evol/psi_x/psi_t_{i}.npy")

    for surf_number, surf_ind in enumerate(surface_indexes):
        ionization_probabilities[surf_number, i] = (
            np.sum(np.abs(psi[surf_ind:, surf_ind:])
                   ** 2, axis=(0, 1)) * dx0 * dx1
        )
    print(f"step = {i} of {len(t)}; time of step = {(time.time()-ts):.{5}f}")

np.save(
    basedir + "/arrays_saved/ionization_probabilities/ionization_probabilities.npy",
    ionization_probabilities,
)

# выставляем большой шрифт на картинках по умолчанию
font = {"size": 20}
matplotlib.rc("font", **font)

fig, ax = plt.subplots(1, 1, figsize=(10, 10), layout="constrained")
for surf_number, surf_ind in enumerate(surface_indexes):
    ax.plot(
        t,
        ionization_probabilities[surf_number, :],
        label=f"x>{x0[surf_ind]}",
    )
ax.grid()
ax.legend(fontsize=20)
ax.set(xlabel=r"t[a.u.]", ylabel="W")
fig.savefig(
    basedir + "/imgs/ionization_probabilities/ionization_probabilities.png")
