import numpy as np
from scipy import stats

def mc_estabilidad_b(magnitudes,
                     valores_N,
                     magnitud_minima = 0,
                     magnitud_maxima = 10,
                     N_min = 1,
                     ventana_estabilidad = 5,
                     redondeo_ = 3,
                     min_mc_top3 = True,
                     texto = True):
  magnitudes = np.asarray(magnitudes, dtype=float)
  magnitudes = np.round(magnitudes, redondeo_)
  filtro_magnitudes = (magnitudes >= magnitud_minima) & (magnitudes <= magnitud_maxima)
  magnitudes = magnitudes[filtro_magnitudes]

  log10_N = np.asarray(valores_N, dtype=float)
  log10_N = log10_N[filtro_magnitudes]
  filtro_0 = valores_N >= N_min
  log10_N = log10_N[filtro_0]
  magnitudes = magnitudes[filtro_0]
  log10_N = np.log10(log10_N)

  b_list = []
  a_list = []
  m_min = []
  for i in magnitudes[:-1]:
    filtro_ = magnitudes >= i
    magnitudes_aux = magnitudes[filtro_]
    N_aux = log10_N[filtro_]

    resultado = stats.linregress(x=magnitudes_aux,
                                 y=N_aux)
    b_list.append(resultado.slope)
    a_list.append(resultado.intercept)
    m_min.append(i)

  b_list = np.array(b_list)
  a_list = np.array(a_list)
  m_min = np.array(m_min)
  std_b = []
  mean_b = []
  m_min_std = []

  if texto:
      print(f'Ventana de estabilidad: {ventana_estabilidad}')
  for i in range(len(b_list)-ventana_estabilidad):
    std_b.append(np.round(np.std(b_list[i:i+ventana_estabilidad]), redondeo_))
    mean_b.append(np.round(np.mean(b_list[i:i+ventana_estabilidad]), redondeo_))
    m_min_std.append(m_min[i])
    if texto:
      print(f'M min: {m_min[i]} --> promedio de b: {mean_b[i]} -- std: {std_b[i]}')

  std_b = np.array(std_b)
  mean_b = np.array(mean_b)
  m_min_std = np.array(m_min_std)

  index_sort = np.argsort(std_b)
  mc_sort = m_min_std[index_sort]
  std_b_sort = std_b[index_sort]
  mean_b_sort = mean_b[index_sort]

  if min_mc_top3:
    mc = mc_sort[:3].min()
  else:
    mc = mc_sort[0]

  print(f'mc: {mc}')

  diccionario_b = {'m': m_min,
                   'b': b_list,
                   'a': a_list,
                   'std-b': std_b,
                   'm-std': m_min_std,
                   'mc-sort': mc_sort,
                   'std-b-sort': std_b_sort,
                   'mean-b-sortp': mean_b_sort,
                   'mc': mc}

  #print(std_b)

  return diccionario_b
