import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
 
def plot_corte(df,
               columna_x,
               columna_y,
               filtro_datos,
               ax_s,
               label_s,
               invert_yaxis=True):
  x_min = df[columna_x].min()
  x_max = df[columna_x].max()
  y_min = df[columna_y].min()
  y_max = df[columna_y].max()

  df = df[filtro_datos].copy()
  df.reset_index(drop=True, inplace=True)

  ax_s.scatter(df[columna_x],
               df[columna_y],
               s=1,
               label=label_s,
               alpha=0.8)
  ax_s.set_xlim(x_min, x_max)

  ax_s.set_xlim(x_min, x_max)
  ax_s.set_ylim(y_min, y_max)
  ax_s.grid(ls='--', c='gray', alpha=0.7)
  ax_s.set_xlabel(columna_x)
  ax_s.set_ylabel(columna_y)

  if invert_yaxis:
    ax_s.invert_yaxis()
