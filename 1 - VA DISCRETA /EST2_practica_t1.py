#!/usr/bin/env python
# -*- coding: utf-8 -*-

import scipy.stats as st


print '''
20. El **numero de maquinas reparadas** por un tecnico en un dia de trabajo sigue una **distribucion de Poisson de media 3**, calcular la probabilidad de que:

a. un dia cualquiera repare al menos 5.
b. un dia repare 5 sabiendo que ya ha reparado mas de 2 
c. en una semana (5 dias) repare entre 12 y 16 maquinas
'''

# Numero de maquinas reparadas por día
# λ = 3 (maquinas por día)
lambda_a = 3
# p(3)

print "# APARTADO A:\n## TENEMOS QUE CALCULAR:"
print "P(X ≥ 5) = 1 - P(X ≤ 4)"
print "\nBuscamos en Tablas: "
print "P(X ≥ 5) =", 1 - st.poisson.cdf(4, lambda_a)

print "\n# APARTADOS B: \n## TENEMOS QUE HALLAR:\n"
print ">>> P(X = 5 | X > 2) \n= P(X > 2 | X = 5 ) * P(X = 5) / P(X > 2)"
print "P(X > 2 | X = 5 ) = 1"
print "P(X = 5) =", st.poisson.pmf(5, lambda_a)
print "P(X > 2) = 1 - P(X ≤ 2) =", 1 - st.poisson.cdf(2, lambda_a)
print "P(X = 5 | X > 2) =", st.poisson.pmf(5, lambda_a) / (1 - st.poisson.cdf(2, lambda_a))

print """\n# APARTADO C: \n## TENEMOS QUE HALLAR:\n
En 5 días repare entre 12 y 16 maquinas:

Esto se traduce en: λ = 3 · 5 = 15
:
"""
a = 11
b = 16
lambda_c = 15
p_a = st.poisson.cdf(a, lambda_c)
p_b = st.poisson.cdf(b, lambda_c)
print "P(12 ≤ x ≤ 16) = P(x ≤ 16) - P(x ≤ 11) =", p_b - p_a