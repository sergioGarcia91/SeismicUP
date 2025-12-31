import matplotlib.pyplot as plt
import numpy as np

def GutenbergRichter_scatter_plot(N_count,
                                magnitudes,
                                ax_h,
                                mc=None,
                                magnitud_maxima=10):
  if mc is None:
    mc = 0

  color_ = []

  for i in range(len(magnitudes)):
    color_.append('k')
  color_ = np.array(color_)
  color_[(magnitudes >= mc) & (magnitudes <= magnitud_maxima)] = 'b'

  if mc > 0:
    ax_h.scatter(magnitudes, 
                np.log10(N_count),
                c=color_,
                s=5, 
                label=f'Mc={mc}')
    ax_h.legend()
    
  else:
    ax_h.scatter(magnitudes, 
                np.log10(N_count),
                c=color_,
                s=5)  

  if magnitud_maxima == 10:
    max_lim_x = magnitudes[N_count == 0][0]
    ax_h.set_xlim(left=magnitudes.min()-0.5, right=max_lim_x+0.5)
  else:
    ax_h.set_xlim(left=magnitudes.min()-0.5, right=magnitudes.max()+0.5)
                                    
  ax_h.set_ylabel('$Log_{10}(N$)')
  ax_h.set_xlabel('Magnitud')
  ax_h.grid(ls='--', c='gray', alpha=0.7)
  ax_h.set_title('Gutenberg-Richter Plot')
  #ax_h.set_xlim(left=magnitudes.min()-0.5, right=magnitudes.max()+0.5)
