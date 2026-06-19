import numpy as np
from scipy.spatial import cKDTree
from scipy import stats

def correlacion_integral_xy(x_km, y_km, radio_en_km):
    """C(r) = 2*N_pairs(R<r) / [N*(N-1)]  con distancias euclídeas en km."""
    P = np.c_[x_km, y_km].astype(float)
    N = len(P)
    tree = cKDTree(P)
    C = []
    for r in radio_en_km:
        # cuenta vecinos de cada punto dentro de r (incluye el propio → restamos 1)
        neigh = tree.query_ball_point(P, r)
        total_dir = sum(len(lst) - 1 for lst in neigh)   # pares dirigidos (i→j)
        C.append(total_dir / (N*(N-1)))                  # equivale a 2*N_pairs/[N(N-1)]
    return np.asarray(C)

def correlacion_integral_xyz(x_km, y_km, z_km, radio_en_km):
    P = np.c_[x_km, y_km, z_km].astype(float)
    N = len(P)

    if N < 2:
        raise ValueError("Se necesitan al menos 2 puntos")

    tree = cKDTree(P)
    C = []

    for r in radio_en_km:
        total_dir = tree.count_neighbors(tree, r) - N
        C.append(total_dir / (N * (N - 1)))

    return np.asarray(C)
