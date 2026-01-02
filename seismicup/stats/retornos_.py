import numpy as np

def periodo_retorno(a_value,
                    b_value,
                    magnitud_minima,
                    magnitud_maxima,
                    steps_,
                    periodo_years,
                    retorno_years=[1, 10, 50, 100],
                    texto=True):

  magnitudes_bins = np.arange(start=magnitud_minima,
                              stop=magnitud_maxima+steps_,
                              step=steps_)

  # Number of events per year
  T_enYears = periodo_years
  print('Años de estudio (T): ', T_enYears)

  # number of events per year a_1
  #a_1 = a_value / np.log10(T_enYears)
  a_1 = a_value - np.log10(T_enYears)
  print('Eventos por año ($a_{1}$): ', 10**a_1)

  N_calculado = []
  P_1year_calculado = []
  P_all_time = []
  theta_years_calculado = []
  theta_days_calculado = []
  theta_months_calculado = []
  m_lista = []
  P_retornos_ = []

  for m in magnitudes_bins:
    # Cumulative frequency of events per year or seismicity index
    # is calculated for m
    N1_45 = 10**(a_1-(b_value*m))

    # Probability of an event with ml >= m occurring in 1 year
    P_45_1year = 1-np.exp((-1*N1_45*1))
    N_ = 10**(a_value - (b_value*m))
    P_all_years = 1-np.exp((-1*N_*T_enYears))
    retornos_ = {'Years': [],
                 'value': [],
                 'm': []}
    retornos_['m'].append(m)
    
    for retorno_year in retorno_years:
      retornos_['Years'].append(retorno_year)
      retornos_['value'].append(1-np.exp((-1*N_*retorno_year)))
    
    # Return period
    theta_years = 1/N1_45 # years
    theta_days = theta_years * 365
    theta_months = theta_days / 30

    m_lista.append(m)
    N_calculado.append(N1_45)
    P_1year_calculado.append(P_45_1year)
    P_all_time.append(P_all_years)
    P_retornos_.append(retornos_)
    theta_years_calculado.append(theta_years)
    theta_days_calculado.append(theta_days)
    theta_months_calculado.append(theta_months)

    if texto:
      print(f'Frecuencia acumulada N_1({m}): ', N1_45)
      print(f'Probabilidad que ocurra un evento de ml >= {m} en 1 año: ', P_45_1year)
      print('Retorno cada: ', theta_years, ' años')
      print('Retorno cada: ', theta_days, ' días')
      print('Retorno cada: ', theta_months, ' meses')
      print('\n')
  dict_periodo_retorno = {
      'm': m_lista,
      'N': N_calculado,
      'P_1year': P_1year_calculado,
      'P_all_time': P_all_time,
      'P_retornos': P_retornos_,
      'theta_years': theta_years_calculado,
      'theta_days': theta_days_calculado,
      'theta_months': theta_months_calculado
  }

  return dict_periodo_retorno
