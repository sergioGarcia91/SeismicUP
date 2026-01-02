import numpy as np
from scipy import stats # regresion lineal
import pandas as pd

def get_GutenbergRichter_values_boosted_2(magnitudes,
                                          percentage_data= 0.8,
                                          magnitud_minima= 0,
                                          magnitud_maxima= 10,
                                          steps_= 0.1,
                                          n_resamples= 1000,
                                          replace_=True,
                                          correcion_m = 0.2):
  if percentage_data < 0.4:
    percentage_data = 0.4
    print('percentage_data modificado a 0.4')
  elif percentage_data > 1.0:
    percentage_data = 1.0
    print('percentage_data modificado a 1.0')

  total_data = len(magnitudes)
  n_data = int(total_data * percentage_data)

  magnitudes_array = np.asarray(magnitudes, dtype=float)
  filtro_magnitudes = (magnitudes_array >= magnitud_minima) & (magnitudes_array <= magnitud_maxima)
  magnitudes_array = magnitudes_array[filtro_magnitudes]

  magnitudes_bins = np.arange(start=magnitud_minima,
                              stop=magnitud_maxima+steps_,
                              step=steps_)

  b_value = []
  a_value = []
  mc_value = []

  for i in range(n_resamples):
    muestra_magnitudes = np.random.choice(magnitudes_array, size=n_data, replace=replace_)
    N = []
    for magnitud in magnitudes_bins:
      sumar_cantidad = (muestra_magnitudes >= magnitud).sum()
      N.append(sumar_cantidad)
    N = np.array(N)
    m = magnitudes_bins.copy()

    N_MC = []
    for i in range(len(magnitudes_bins)-1):
      sumar_cantidad = (magnitudes_bins[i] < magnitudes_array) & (magnitudes_array <= magnitudes_bins[i+1])
      sumar_cantidad = sumar_cantidad.sum()
      N_MC.append(sumar_cantidad)
    N_MC = np.array(N_MC)
    Mc = magnitudes_bins[np.argmax(N_MC)] + correcion_m
                  
    filtro_0 = N >= 1
    N = N[filtro_0]
    log10_N = np.log10(N)
    m = m[filtro_0]

    filtro_mc = m >= Mc
    magnitudes_aux = m[filtro_mc]
    N_aux = log10_N[filtro_mc]

    resultado = stats.linregress(x=magnitudes_aux,
                                 y=N_aux)

    mc_value.append(Mc)
    b_value.append(-1*resultado.slope)
    a_value.append(resultado.intercept)

  mc_value = np.array(mc_value)
  b_value = np.array(b_value)
  a_value = np.array(a_value)

  dict_values = {
      'b_values': b_value,
      'a_values': a_value,
      'mc_values': mc_value,
      'mc_mean': mc_value.mean(),
      'mc_std': mc_value.std(),
      'b_mean': b_value.mean(),
      'b_std': b_value.std(),
      'a_mean': a_value.mean(),
      'a_std': a_value.std()}

  return dict_values
