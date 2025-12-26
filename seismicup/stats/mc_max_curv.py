import numpy as np

def mc_maxima_curvatura(magnitudes_array,
                        steps_=0.1,
                        correcion_m = 0.2,
                        magnitud_minima = 0,
                        magnitud_maxima = 10,
                        texto = True):
  magnitudes = np.asarray(magnitudes_array, dtype=float)
  magnitudes_bins = np.arange(start=magnitud_minima,
                              stop=magnitud_maxima+steps_,
                              step=steps_)
  N = []

  for i in range(len(magnitudes_bins)-1):
    sumar_cantidad = (magnitudes_bins[i] < magnitudes_array) & (magnitudes_array <= magnitudes_bins[i+1])
    sumar_cantidad = sumar_cantidad.sum()
    N.append(sumar_cantidad)
    if texto:
      print(f'{magnitudes_bins[i]} < m <= {magnitudes_bins[i+1]} --> N: {sumar_cantidad}')
  N = np.array(N)

  Mc = magnitudes_bins[np.argmax(N)] + correcion_m
  print(f'Mc: {Mc}')
  return Mc
