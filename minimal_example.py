import importlib
import elate

importlib.reload(elate)
from elate import ELATE,gen

import numpy as np
import pandas as pd
Y, D, Z, X = gen(n=4000, beta_d=1.0, beta_z=1.0)


model = ELATE(Y, D, Z, X,2)
res = model.fit(bootstrap=50)

print(res.summary())

