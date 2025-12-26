import numpy as np

def mc_menor_pendiente(magnitudes,
                       valores_N,
                       magnitud_minima = 0,
                       magnitud_maxima = 10,
                       texto = True):
  magnitudes = np.asarray(magnitudes, dtype=float)
  filtro_magnitudes = (magnitudes >= magnitud_minima) & (magnitudes <= magnitud_maxima)
  magnitudes = magnitudes[filtro_magnitudes]


  valores_N = np.asarray(valores_N, dtype=float)
  valores_N = valores_N[filtro_magnitudes]

  filtro_0 = valores_N > 0
  magnitudes = magnitudes[filtro_0]
  valores_N = valores_N[filtro_0]

  dy = np.diff(valores_N)
  dx =np.diff(magnitudes)

  slope = dy / dx # pendiente
  # np.diff ... out[i] = a[i+1] - a[i]

  if texto:
    print(f'magnitudes: {magnitudes}')
    print(f'dNdx: {slope}')
  Mc = magnitudes[np.argmin(slope)]
  print(f'Mc: {Mc}')
  # np.argmin ... Returns the indices of the minimum values along an axis ... the first occurrence is returned

  return Mc
