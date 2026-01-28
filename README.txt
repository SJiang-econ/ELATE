# ELATE

**ELATE** is a Python package for estimating Encouraged-LATE, a novel causal parameter defined in the paper "The Encouraged LATE: Point Identified Treatment Effects Without Instrument Exclusion" written by Jinyoung Choi, Shuo Jiang and Arthur Lewbel

This is the version 1.0 package which provides:
- Two-step semiparametric estimation of the coefficients: \beta_{d1}: Encouraged-LATE; \beta_z: the direct effect of IV
- Bootstrap standard errors
- t-statistics
- p-values

---
Below we illustrate the usage of this package with our minimal example:

#import the packages
from elate import ELATE,gen
import numpy as np
import pandas as pd

#data generation
Y, D, Z, X = gen(n=4000, beta_d=1.0, beta_z=1.0)

# feed data and the degree of polynomial in the first step sieve estimation (set to 2 in the example)
model = ELATE(Y, D, Z, X, 2)

#choose the number of bootstrap draws for standard error estimation (set to 50 in the example)
res = model.fit(bootstrap=50)

#report the result
print(res.summary())