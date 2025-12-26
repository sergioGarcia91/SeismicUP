import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
 
def histograma_plot(df, columna, ax_h, step_, dist_min, y_log = True):
  p10 = np.round(df[columna].quantile(q=0.1), 2)
  p25 = np.round(df[columna].quantile(q=0.25), 2) # q1
  p50 = np.round(df[columna].quantile(q=0.5), 2) # q2
  p75 = np.round(df[columna].quantile(q=0.75), 2) # q3
  p90 = np.round(df[columna].quantile(q=0.9), 2)

  step_ = step_
  dist_min = dist_min # valor minimo del histograma
  dist_max = step_ * (1 + int(df[columna].max() // step_) )
  bins_h = np.arange(start=dist_min, stop=dist_max+step_, step=step_)
  xlim_h = [dist_min-step_, bins_h.max()+step_]


  sns.histplot(data = df,
              x = columna,
              bins = bins_h,
              ax= ax_h,
              legend= False)
  # quantiles
  ax_h.axvline(x=p10, label=f'P10: {p10} km', c='k', ls='--')
  ax_h.axvline(x=p25, label=f'Q1: {p25} km', c='b', ls='--')
  ax_h.axvline(x=p50, label=f'Q2: {p50} km', c='r', ls='--')
  ax_h.axvline(x=p75, label=f'Q3: {p75} km', c='b', ls='--')
  ax_h.axvline(x=p90, label=f'P90: {p90} km', c='k', ls='--')

  ax_h.set_xlim(left=xlim_h[0], right=xlim_h[1])
  ax_h.grid(ls='--', c='gray', alpha=0.7)
  ax_h.legend()
  if y_log:
    ax_h.set_yscale('log')
