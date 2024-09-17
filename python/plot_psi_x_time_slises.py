import numpy as np
from matplotlib import cm
from matplotlib import pyplot as plt
import time
import os
import gc

with open("dir_paths.txt", "r") as f:
    basedir = f.readline().split("\n")[0]
    inner_electron_dir_path = f.readline().split("\n")[0]
    external_electron_dir_path = f.readline().split("\n")[0]

x = np.load(inner_electron_dir_path + "/RSSFM1D/src/arrays_saved/x.npy")
y = np.load(external_electron_dir_path + "/RSSFM1D/src/arrays_saved/x.npy")
t = np.load(basedir + "/arrays_saved/time_evol/t.npy")

X, Y = np.meshgrid(x, y, indexing="ij")

if not os.path.exists(basedir + "/imgs/time_evol/psi_x"):
    os.makedirs(basedir + "/imgs/time_evol/psi_x")

fig, axs = plt.subplots(ncols=1, nrows=1, figsize=(8, 8), layout="constrained")

for i in range(len(t)):
    ts = time.time()
    psi = np.load(basedir + f"/arrays_saved/time_evol/psi_x/psi_t_{i}.npy")
    axs.set(
        aspect="equal",
        title=f"step={i} of {len(t)}; t = {t[i]:.{5}f} a.u.",
    )
    b = axs.pcolormesh(
        X,
        Y,
        np.abs(psi) ** 2,
        cmap=cm.jet,
        shading="auto",
        vmax=1e-5,
    )
    cb = plt.colorbar(b, ax=axs)
    fig.savefig(basedir + f"/imgs/time_evol/psi_x/psi_t_{i}.png")
    axs.clear()
    cb.remove()
    gc.collect()
    print(f"step {i} of {len(t)}; time of step = {(time.time()-ts):.{5}f}")
