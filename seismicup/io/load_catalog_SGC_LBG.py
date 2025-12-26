import pandas as pd
import os
import re

def crear_catalogo_SGC_LBG(path_catalogo, file_excel):
  df_temp_1 =pd.read_excel(os.path.join(path_catalogo, file_excel),
                        decimal=',',
                        engine='calamine')

  df_temp_1['Fecha-Hora UTC'] = df_temp_1.loc[:,'Fecha  (UTC)'] + ' ' + df_temp_1.loc[:,'Hora  (UTC)']
  df_temp_1['Departamento'] = np.nan
  df_temp_1['Municipio'] = np.nan
  df_temp_1['FASES'] = np.nan

  print('')
  print(df_temp_1['Departamento'].unique())
  print('')
  print(df_temp_1['Municipio'].unique())
  print('')
  print(df_temp_1.columns)

  df_concat = df_temp_1.copy()
  df_concat = df_concat.loc[:,['Fecha-Hora UTC',
                              'Latitud(°)', #
                              'Longitud(°)', # grados
                              'Profundidad(Km)',
                              'Magnitud',
                              'Tipo Magnitud',
                              'Error  Latitud(Km)',
                              'Error  Longitud(Km)',
                              'Error  Profundidad(Km)',
                              'FASES',
                              'Rms(Seg)',
                              'Gap(°)', # grados
                              'Departamento',
                              'Municipio',]
                              ]
  print('Eventos: ', len(df_concat))

  del df_temp_1

  df_concat.reset_index(drop=True, inplace=True)
  df_concat.columns = ['Fecha-Hora UTC',
                        'Latitud', # grados
                        'Longitud', # grados
                        'Profundidad [km]',
                        'Magnitud',
                        'Tipo Magnitud',
                        'Error Latitud [km]',
                        'Error Longitud [km]',
                        'Error Profundidad [km]',
                        'Numero de Fases',
                        'RMS [seg]',
                        'Gap', # grados
                        'Departamento',
                        'Municipio',
                        ]

  return df_concat
