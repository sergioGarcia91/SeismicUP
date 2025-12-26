import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
 
def time_magnitud_plot(df,
                       filtro_datos,
                       columna_eje_x_tiempo,
                       comlumna_eje_y,
                       ax_s,
                       label_s='Earthquakes'):
  x_min = df[columna_eje_x_tiempo].min()
  x_max = df[columna_eje_x_tiempo].max()
  y_min = int(df[comlumna_eje_y].min())
  y_max = int(df[comlumna_eje_y].max())+1

  df = df[filtro_datos].copy()
  df.reset_index(drop=True, inplace=True)

  p10 = df[comlumna_eje_y].quantile(q=0.1).round(2)
  p25 = df[comlumna_eje_y].quantile(q=0.25).round(2) # q1
  p50 = df[comlumna_eje_y].quantile(q=0.5).round(2) # q2
  p75 = df[comlumna_eje_y].quantile(q=0.75).round(2) # q3
  p90 = df[comlumna_eje_y].quantile(q=0.9).round(2)

  ax_s.scatter(df[columna_eje_x_tiempo],
               df[comlumna_eje_y],
               s=1,
               label=label_s,
               alpha=0.8)
  ax_s.set_xlim(x_min, x_max)
  #left, right = ax_s.get_xlim()
  left, right = 0, 1 # son valores entre 0 y 1

  # quantiles
  ax_s.axhline(y=p10, xmin=left, xmax=right, label=f'P10: {p10}', c='k', ls='--')
  ax_s.axhline(y=p25, xmin=left, xmax=right, label=f'Q1: {p25}', c='b', ls='--')
  ax_s.axhline(y=p50, xmin=left, xmax=right, label=f'Q2: {p50}', c='r', ls='--')
  ax_s.axhline(y=p75, xmin=left, xmax=right, label=f'Q3: {p75}', c='b', ls='--')
  ax_s.axhline(y=p90, xmin=left, xmax=right, label=f'P90: {p90}', c='k', ls='--')


  ax_s.set_yticks(np.arange(0, 8, 0.5))
  ax_s.set_ylim(y_min, y_max)
  ax_s.grid(ls='--', c='gray', alpha=0.7)
