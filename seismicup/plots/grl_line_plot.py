import matplotlib.pyplot as plt
import numpy as np

def GutenbergRichter_line_plot(b_value,
                               a_value,
                               ax_h,
                               magnitud_minima=0,
                               magnitud_maxima=10):
  
  x_data = np.array([magnitud_minima, magnitud_maxima])
  y_data = a_value - b_value * x_data
  a = np.round(a_value, 3)
  b = np.round(b_value, 3)
  ax_h.plot(x_data,
            y_data,
            ls='--',
            c='r',
            label=f'$Log_{10}(N$) = {a}-{b}m')
  
  ax_h.legend()
