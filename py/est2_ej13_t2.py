#!/usr/bin/env python
# -*- coding: utf-8 -*-

import scipy.stats as st

enunciado = '''El precio de las acciones de un banco al 
final de cada jornada de comercializacion del ano pasado 
se rigio por una distribucion normal. 

El precio medio fue de 42€ por accion y 
la desviacion tipica de 2,25€ por accion

a) ¿Que porcentaje de jornadas el precio 
estuvo por encima de los 45€?

b) ¿Que porcentaje de jornadas el precio 
oscilo entre 38 y 40 €?

c) ¿Cual fue el nivel del precio de las acciones 
para el que el 15% de las jornadas se mantuvo mas alto?'''

# --------------------
# enunciado
# --------------------

print enunciado
print '''
x: precio de la accion. ~ N(µ,σ)
E(x) = 42
V(x) = 2.25
'''
# --------------------
# apartado a
# --------------------

print''' 
APARTADO A:
===========

x: numero de jornadas en el que el precio es mayor que 45 ~ N(42, 2.25)
P(x>45) = 1 - P(x ≤ 45)
'''
k = 45
mu = 42
sigma = 2.25
p_a =  1 - st.norm.cdf(k, mu, sigma)
print "P(x>45) = ", p_a

# --------------------
# APARTADO B:
# --------------------

print'''
APARTADO B:
===========

b) ¿Que porcentaje de jornadas el precio oscilo 
entre 38 y 40 €?

P(38 ≤ x ≤ 40) = P(x ≤ 40) - (1 - P(x ≤ 38))

'''
a = 38
b = 40

p_b = st.norm.cdf(b, mu, sigma) - st.norm.cdf(a, mu, sigma)

print "P(38 ≤ x ≤ 40) =", p_b


# --------------------
# APARTADO C:
# --------------------
print '''
c) ¿Cual fue el nivel del precio de las acciones 
para el que el 15% de las jornadas
se mantuvo mas alto?

P(x ≥ k) = 0,15
1 - P(x ≤ k) = 0,15
Como la normal es una distribucion simétrica:
P(x ≥ k) = 0,15 >>> P(x ≤ k) = 0,85
'''
print "P(x ≤ k) = 0,85 >>> k =", st.norm.ppf(0.85, mu, sigma)
print '''
Para buscar en tablas:
Tipificamos:
z_0 = (38 - mu) / sigma
z_1 = (40 - mu) / sigma
'''

z_0 = (38 - mu) / sigma
z_1 = (40 - mu) / sigma
print z_0, "≤ x ≤", z_1, 0.9625 - 0.8133