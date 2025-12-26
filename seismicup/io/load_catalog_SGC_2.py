import pandas as pd
import os
import re

def crear_catalogo_SGC_2(path_catalogo, file_excel):
  df_temp_1 =pd.read_excel(os.path.join(path_catalogo, file_excel),
                        decimal=',',
                         skiprows=13,
                        engine='calamine')

  df_temp_1['Fecha-Hora UTC'] = df_temp_1.loc[:,'FECHA - HORA UTC']
  departamento = []
  municipio = []

  for row in df_temp_1.loc[:, 'REGION']:
    mun_dep = re.split(', | - ', row)
    if len(mun_dep) == 1:
      departamento.append(mun_dep[0])
      municipio.append(np.nan)
    elif len(mun_dep) == 2:
      #print(mun_dep)
      departamento.append(mun_dep[1])
      municipio.append(mun_dep[0])
    elif len(mun_dep) == 3:
      #print(mun_dep)
      departamento.append(mun_dep[1])
      municipio.append(mun_dep[0])
    #print(mun_dep)

  df_temp_1['Departamento'] = departamento
  df_temp_1['Departamento'] = df_temp_1['Departamento'].str.upper()
  df_temp_1['Municipio'] = municipio
  df_temp_1['Municipio'] = df_temp_1['Municipio'].str.upper()

  print('')
  print(df_temp_1['Departamento'].unique())
  print('')
  print(df_temp_1['Municipio'].unique())
  print('')
  print(df_temp_1.columns)

  df_concat = df_temp_1.copy()
  df_concat = df_concat.loc[:,['FECHA - HORA UTC',
                              'LATITUD (°)', #
                              'LONGITUD (°)', # grados
                              'PROF. (Km)',
                              'MAGNITUD',
                              'TIPO MAGNITUD',
                              'ERROR LATITUD (Km)',
                              'ERROR LONGITUD (Km)',
                              'ERROR PROFUNDIDAD (Km)',
                              'FASES',
                              'RMS (Seg)',
                              'GAP (°)', # grados
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
