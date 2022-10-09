# -*- coding: utf-8 -*-
"""implement a polynomial basis function."""

import numpy as np


def build_poly(x, degree):
    """polynomial basis functions for input data x, for j=0 up to j=degree."""
    n = x.shape[0]
    res = np.zeros((n, degree+1))
    
    for i in range(n):
        for j in range(degree+1):
            res[i, j] = x[i]**j
            
    return res