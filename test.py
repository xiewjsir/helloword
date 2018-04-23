#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#this a test

import numpy as np
from numpy.linalg import eigvals

def run_experiment(niter=100):
    k = 100
    results = []
    for _ in range(niter):
        mat = np.random.randn(k,k)
        max_eigenvalue = np.abs(eigvals(mat).max())
        results.append(max_eigenvalue)
    return results

some_results = run_experiment()
print('Larget one we saw:%s'%np.max(some_results))