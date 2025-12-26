import numpy as np

def obtener_N_LGR(magnitudes_array,
                  magnitud_minima=0,
                  magnitud_maxima=10,
                  steps_=0.1,
                  texto=True):
  magnitudes_array = np.asarray(magnitudes_array, dtype=float)
  filtro_magnitudes = (magnitudes_array >= magnitud_minima) & (magnitudes_array <= magnitud_maxima)
  magnitudes_array = magnitudes_array[filtro_magnitudes]

  magnitudes_bins = np.arange(start=magnitud_minima,
                              stop=magnitud_maxima+steps_,
                              step=steps_)
  N = []

  for magnitud in magnitudes_bins:
     sumar_cantidad = (magnitudes_array >= magnitud).sum()
     N.append(sumar_cantidad)
     if texto:
      print(f'M: {magnitud} --> N: {sumar_cantidad}')
  N = np.array(N)
  diccionario_N = {'m': magnitudes_bins,
                   'N': N}

  return diccionario_N
