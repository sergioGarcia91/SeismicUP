import numpy as np
from scipy.spatial import cKDTree
from scipy import stats

def estimar_Dc(r_km, C, idx_range=None):
    """Pendiente de log10 C vs log10 r en el tramo idx_range (tu “escala inercial”)."""
    m = (C > 0) & (C < 1)
    xr, yr = np.log10(r_km[m]), np.log10(C[m])
    if idx_range is None:
        # elige por defecto el tramo intermedio
        q1, q3 = np.quantile(xr, [0.25, 0.75])
        sel = (xr >= q1) & (xr <= q3)
    else:
        sel = np.zeros_like(xr, bool)
        sel[idx_range[0]:idx_range[1]] = True
    slope, intercept, *_ = stats.linregress(xr[sel], yr[sel])
    return slope, intercept, (xr, yr, sel)   # slope = Dc
