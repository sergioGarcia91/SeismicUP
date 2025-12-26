import matplotlib.pyplot as plt
import os
 
def save_plot(path_save_figuras, file_name, formato= 'png', dpi_=300):
  file_ = file_name + '.' + formato
  file_to_save = os.path.join(path_save_figuras, file_)
  plt.savefig(file_to_save,
              format=formato,
              dpi=dpi_,
              bbox_inches = 'tight',
              pad_inches=0.25)
