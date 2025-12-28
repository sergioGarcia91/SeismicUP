import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def histograma_GRL_noise_plot(df,
                    columna,
                    ax_h,
                    step_,
                    dist_min,
                    y_log = True):

  p10 = np.round(df[columna].quantile(q=0.1), 3)
  p25 = np.round(df[columna].quantile(q=0.25), 3) # q1
  p50 = np.round(df[columna].quantile(q=0.5), 3) # q2
  p75 = np.round(df[columna].quantile(q=0.75), 3) # q3
  p90 = np.round(df[columna].quantile(q=0.9), 3)
  mean_ = np.round(df[columna].mean(), 3)
  std_ = np.round(df[columna].std(), 3)

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
  ax_h.axvline(x=p10, label=f'P10: {p10}', c='k', ls='--')
  ax_h.axvline(x=p25, label=f'Q1: {p25}', c='b', ls='--')
  ax_h.axvline(x=p50, label=f'Q2: {p50}', c='r', ls='--')
  ax_h.axvline(x=p75, label=f'Q3: {p75}', c='b', ls='--')
  ax_h.axvline(x=p90, label=f'P90: {p90}', c='k', ls='--')

  ax_h.set_xlim(left=xlim_h[0], right=xlim_h[1])
  ax_h.grid(ls='--', c='gray', alpha=0.7)
  ax_h.legend()
  ax_h.set_title(f'{columna} [Mean:{mean_} - std:{std_}]')

  if y_log:
    ax_h.set_yscale('log')
