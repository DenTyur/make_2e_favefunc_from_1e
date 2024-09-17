import datetime
import multiprocessing as mp
import os
import time

import numpy as np
from numba import njit, prange

with open("dir_paths.txt", "r") as f:
    basedir = f.readline().split("\n")[0]
    inner_electron_dir_path = f.readline().split("\n")[0]
    external_electron_dir_path = f.readline().split("\n")[0]

if not os.path.exists(basedir + "/arrays_saved/time_evol/psi_x"):
    os.makedirs(basedir + "/arrays_saved/time_evol/psi_x")

procs = 4

psi_t_dir_path = basedir + "/arrays_saved/time_evol/psi_x"
psi_inner_t_dir_path = (
    inner_electron_dir_path + "/RSSFM1D/src/arrays_saved/time_evol/psi_x"
)
psi_external_t_dir_path = (
    external_electron_dir_path + "/RSSFM1D/src/arrays_saved/time_evol/psi_x"
)
t_inner = np.load(inner_electron_dir_path +
                  "/RSSFM1D/src/arrays_saved/time_evol/t.npy")
t_external = np.load(
    external_electron_dir_path + "/RSSFM1D/src/arrays_saved/time_evol/t.npy"
)

if np.allclose(t_inner, t_external, atol=1e-5):
    Nt = len(t_inner)
    np.save(basedir + "/arrays_saved/time_evol/t.npy", t_inner)
else:
    print("Error: t_inner =! t_external")
    exit()

# ======== ФУНКЦИИ ИНТЕГРИРОВАНИЯ ==========================


@njit(parallel=True)
def combine_x(psi_x_t_inner, psi_x_t_external, N):
    """
    Объединение невзаимодействующих электронов
    в координатном пространстве
    """
    psi_x1x2 = np.zeros((N, N), dtype=np.complex_)
    for i0 in prange(N):
        for i1 in prange(N):
            psi_x1x2[i0, i1] = (
                psi_x_t_inner[i0] * psi_x_t_external[i1]
                + psi_x_t_external[i0] * psi_x_t_inner[i1]
            ) / np.sqrt(2)
    return psi_x1x2


# ======= Временной цикл==========================


def time_cycle(it1, it2):
    for i in range(it1, it2):
        """
        Прогонка по всем временным шагам
        """
        psi_x_t_inner = np.load(psi_inner_t_dir_path + f"/psi_t_{i}.npy")
        psi_x_t_external = np.load(psi_external_t_dir_path + f"/psi_t_{i}.npy")
        psi_x1x2 = combine_x(
            psi_x_t_inner, psi_x_t_external, len(psi_x_t_inner))
        np.save(
            basedir + f"/arrays_saved/time_evol/psi_x/psi_t_{i}.npy",
            psi_x1x2,
        )


def processesed(tsteps):
    """
    Распараллеливание временного цикла
    """
    cores = procs
    it1 = 0
    it2 = 0
    step = tsteps // cores

    processes = []

    for proc in range(cores):
        it2 = it1 + step
        if it2 > Nt:
            it2 = Nt
        p = mp.Process(target=time_cycle, args=(it1, it2))
        processes.append(p)
        p.start()
        print("proc start", proc, it1, it2)
        it1 = it2

    for p in processes:
        p.join()


# ================================================
#                 RUN
# ================================================


time_start = time.time()  # отсечка цикла
print("Nt=", Nt)
processesed(Nt + 1)
print(f"TIME_CYCLE = {datetime.timedelta(seconds=time.time()-time_start)}")
