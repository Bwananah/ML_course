# -*- coding: utf-8 -*-
"""a function used to compute the loss."""

import numpy as np




def compute_loss(y, tx, w):
    """Calculate the loss using either MSE or MAE.

    Args:
        y: shape=(N, )
        tx: shape=(N,2)
        w: shape=(2,). The vector of model parameters.

    Returns:
        the value of the loss (a scalar), corresponding to the input parameters w.
    """
    e = y - tx@w
    n = y.shape[0]
    
    return e.T@e/(2*n)