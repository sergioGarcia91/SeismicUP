import numpy as np
from scipy import stats # regresion lineal

def get_GutenbergRichter_values(N_count,
                                magnitudes,
                                mc=None,
                                magnitud_maxima=10):
  if mc is None:
    mc = 0
  
  N_count_ = N_count[N_count > 0]
  magnitudes_ = magnitudes[N_count > 0]

  filtro_ = (magnitudes_ >= mc) & (magnitudes_ <= magnitud_maxima)

  magnitudes_ = magnitudes_[filtro_]
  N_count_ = N_count_[filtro_]

  resultado = stats.linregress(x=magnitudes_,
                               y=np.log10(N_count_))
  
  b_value = -1*resultado.slope
  a_value = resultado.intercept

  return b_value, a_value
