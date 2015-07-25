#!/usr/bin/env python
# -*- coding: utf-8 -*-

import scipy.stats as st

print '''
31. Suponer que el 0,15% de las antenas de los nuevos teléfonos móviles de una empresa están defectuosos. 
Si se escogen 2000 antenas al azar, calcular las siguientes probabilidades:

a) Ninguna de las antenas esté defectuosa 
b) Tres o más antenas estén defectuosas

Utilizar la aproximación binomial a Poisson y compararla con el resultado exacto.
'''
print '''
Binomial:
Bi(n,p) = Bi(2000, 0.0015)

n = 2000
p = 0.0015

Poisson:
p(λ), λ = n * p

a) x: número de antenas defectuosas:
P(x = 0)
k = 0
'''

n = 2000
p = 0.0015
k = 0

p_k = st.binom.pmf(k, n, p)
p_k_p = st.poisson.pmf(k, n * p)

print '''
P(x = 0)_bin(n,p) = %s
P(x = 0)_poisson(n*p) = %s
''' % (p_k, p_k_p)