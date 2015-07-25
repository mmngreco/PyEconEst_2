#!/usr/bin/env
# -*- coding:utf-8 -*-
from __future__ import division

import numpy as np
import scipy.stats as st

enunciado = '''
1. Una empresa tiene que presentar una
oferta para una obra publica.

Estima que los materiales necesarios
costaran 25000€, cada dia de trabajo
supone un coste laboral de 800€ y
el plazo de ejecucion tiene que ser
10 dias porque cada dia de retraso
supondra una penalizacion de 1000€.

Analizando obras similares ha calculado
que la variable aleatoria que mide el
numero de dias de ejecucion tiene la
siguiente distribucion

dias = [8,9,10,11,12]
probabilidad = [0.1,0.2,0.4,0.2,0.1]


\ta) ¿Cual es la probabilidad de que 
\t   el numero de dias de ejecucion 
\t   este entre 9 y 11 dias?

\tb) Si una obra ya lleva 9 dias de
\t   ejecucion ¿cual es la probabilidad 
\t   de que dure al menos 1 dia mas?

\tc) ¿Cual es el coste medio de la obra?

\td) ¿Cual es la desviacion 
\t   tipica del coste de la obra?
'''
print enunciado

print '\na)\n'

dias = [8, 9, 10, 11, 12]
probabilidad = [0.1, 0.2, 0.4, 0.2, 0.1]

