#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ESTADISTICA 2
## DISTRIBUCIÓN BINOMIAL
### EJERCICIO 7

import math

# Probabilidad de dar positivo en un control de alcolemia
# es del 10%, se realizan 100 pruebas.

n = 100
p = 0.10
q = 1 - p

# probabilidad de obtener 20 positivos o mas.

def prob(n,p,k):
	a = math.factorial(n)
	b = math.factorial(k)
	c = math.factorial(n - k)
	d = p ** k
	e = (1 - p) ** (n - k)
	return a / (b * c) * d * e

k = range(21,n+1)
prob_ac = [prob(n,p,e) for e in k]

k_c = range(0,10+1)
prob_ac_c = [prob(n,p,e) for e in k_c]

print "P(X ≥ 21) =", sum(prob_ac)
print "P(X ≤ 10) =", sum(prob_ac_c)