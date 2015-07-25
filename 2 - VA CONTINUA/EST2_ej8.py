#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ESTADISTICA 2
## DISTRIBUCIÓN BINOMIAL
### EJERCICIO 8

import math

# Probabilidad de dar positivo en un control de alcolemia
# es del 10%, se realizan 100 pruebas.



n_x = 4
p_x = 0.50
n_y = 2000.
p_y = None

# probabilidad de obtener 20 positivos o mas.

def prob(n,p,k):
	a = math.factorial(n)
	b = math.factorial(k)
	c = math.factorial(n - k)
	d = p ** k
	e = (1 - p) ** (n - k)
	return a / (b * c) * d * e


k_x = 0
prob_ac_x = prob(n_x,p_x,k_x)

x = 2
k_c = range(x,x)
prob_ac_c = [prob(n,p,e) for e in k_c]

print "P(X ≥ 1) =", 1 - prob_ac_x
print "P(X ≤ 10) =", sum(prob_ac_c)