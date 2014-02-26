def readtxt(text,**kwarg):
   import cStringIO
   import numpy as np
   return np.loadtxt(cStringIO.StringIO(text),**kwarg)
