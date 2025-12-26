import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.font_manager as fm
import urllib.request

Font_url_ = "!wget https://github.com/justrajdeep/fonts/raw/master/Times%20New%20Roman.ttf"

def get_TimesNewRoman_font():
  urllib.request.urlretrieve(Font_url_, 'Times New Roman.ttf')
  font_path = "Times New Roman.ttf"

  # Añadir la fuente al administrador de fuentes de Matplotlib
  font_prop = fm.FontProperties(fname=font_path)
  fm.fontManager.addfont(font_path)
  
  # Nombre de la fuente para usar en rcParams
  font_name = font_prop.get_name()
  font_name
  
  plt.rcParams['font.family'] = font_name  
