import pandas as pd
import os
import re

def crear_catalogo_SGC_1(path_catalogo, file_excel):
  df_temp_1 =pd.read_excel(os.path.join(path_catalogo, file_excel),
                         decimal=',',
                         engine='calamine')

  df_temp_1['Fecha-Hora UTC'] = df_temp_1.loc[:,'FECHA'] + ' ' + df_temp_1.loc[:,'HORA_UTC']
  df_temp_1['Departamento'] = df_temp_1.loc[:,'DEPARTAMENTO'].str.upper()
  df_temp_1['Municipio'] = df_temp_1.loc[:,'MUNICIPIO'].str.upper().str.replace('_',' ')

  print('')
  print(df_temp_1['Departamento'].unique())
  print('')
  print(df_temp_1['Municipio'].unique())
  print('')
  print(df_temp_1.columns)

  df_ml = df_temp_1[df_temp_1['MAGNITUD Ml'].notnull()].copy()
  df_ml['Magnitud'] = df_ml['MAGNITUD Ml']
  df_ml['Tipo Magnitud'] = 'Ml'
  df_ml = df_ml.loc[:,['Fecha-Hora UTC',
                      'LATITUD (grados)', #
                      'LONGITUD (grados)', # grados
                      'PROFUNDIDAD (Km)',
                      'Magnitud',
                      'Tipo Magnitud',
                      'ERROR LATITUD (Km)',
                      'ERROR LONGITUD (Km)',
                      'ERROR PROFUNDIDAD (Km)',
                      '# FASES',
                      'RMS (Seg)',
                      'GAP (grados)', # grados
                      'Departamento',
                      'Municipio',]
                      ]
  print('Eventos Ml: ', len(df_ml))

  df_mw = df_temp_1[df_temp_1['MAGNITUD Mw'].notnull()].copy()
  df_mw['Magnitud'] = df_mw['MAGNITUD Mw']
  df_mw['Tipo Magnitud'] = 'Mw'
  df_mw = df_mw.loc[:,['Fecha-Hora UTC',
                      'LATITUD (grados)', #
                      'LONGITUD (grados)', # grados
                      'PROFUNDIDAD (Km)',
                      'Magnitud',
                      'Tipo Magnitud',
                      'ERROR LATITUD (Km)',
                      'ERROR LONGITUD (Km)',
                      'ERROR PROFUNDIDAD (Km)',
                      '# FASES',
                      'RMS (Seg)',
                      'GAP (grados)', # grados
                      'Departamento',
                      'Municipio',]
                      ]
  print('Eventos Mw: ', len(df_mw))

  df_concat = pd.concat([df_ml, df_mw], ignore_index=True)
  print('Eventos totales: ', len(df_concat))
  print(df_concat.info())

  del df_temp_1
  del df_ml
  del df_mw

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
