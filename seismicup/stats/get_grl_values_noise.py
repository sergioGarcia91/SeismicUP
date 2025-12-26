import numpy as np
from scipy import stats # regresion lineal

def get_GutenbergRichter_values_noised(N_count,
                                       magnitudes,
                                       noise=0.1,
                                       n_resamples= 1000,
                                       mc=None,
                                       magnitud_maxima=10):
  if mc is None:
    mc = 0
  
  N_count_ = N_count[N_count > 0]
  magnitudes_ = magnitudes[N_count > 0]

  filtro_ = (magnitudes_ >= mc) & (magnitudes_ <= magnitud_maxima)

  magnitudes_ = magnitudes_[filtro_]
  N_count_ = N_count_[filtro_]

  b_value = []
  a_value = []
  for i in range(n_resamples):
    noise_m = 1 + np.random.normal(loc=0.0, scale=noise, size=len(N_count_)) 
    N_count_aux = N_count_ * noise_m
    resultado = stats.linregress(x=magnitudes_,
                                 y=np.log10(N_count_aux))
    
    b_value.append(-1*resultado.slope)
    a_value.append(resultado.intercept)

  b_value = np.array(b_value)
  a_value = np.array(a_value)

  dict_values = {
      'b_values': b_value,
      'a_values': a_value,
      'b_mean': b_value.mean(),
      'b_std': b_value.std(),
      'a_mean': a_value.mean(),
      'a_std': a_value.std()} 

  return dict_values
