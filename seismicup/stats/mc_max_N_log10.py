import numpy as np

def mc_maximo_N_log10(magnitudes,
                      valores_N,
                      correcion_m = 0.2,
                      magnitud_minima = 0,
                      magnitud_maxima = 10,
                      redondeo_N = 1):
  magnitudes = np.asarray(magnitudes, dtype=float)
  filtro_magnitudes = (magnitudes >= magnitud_minima) & (magnitudes <= magnitud_maxima)
  magnitudes = magnitudes[filtro_magnitudes]
  magnitudes = magnitudes[::-1]

  valores_N = np.asarray(valores_N, dtype=float)
  valores_N = np.log10(valores_N)
  valores_N = np.round(valores_N, redondeo_N)
  valores_N = valores_N[filtro_magnitudes]
  valores_N = valores_N[::-1]


  Mc = magnitudes[np.argmax(valores_N)] + correcion_m
  print(f'Mc: {Mc}')
  return Mc
