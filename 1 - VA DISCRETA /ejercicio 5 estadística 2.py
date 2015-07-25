#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ejercicio 5 estadística 2

import numpy as np

# DATOS:
print "ESTADISTICA 2: \n- TEMA 1: \n -- EJERCIO 5\n"
horas = range(1,9)
ni = [20, 38, 53, 45, 40, 13, 5, 36]
pago = [3, 6, 9, 12, 14, 16, 18, 20]
fi = map(lambda x: float(x)/sum(ni), ni)

# esperanza de los pagos:
# ∑pago*fi

esp_pago = sum(np.multiply(fi,pago))
v_pago = sum(np.multiply(fi,np.multiply(pago,pago))) - esp_pago ** 2
dt_pago = np.sqrt(v_pago)

print "Esperanza de pago =", esp_pago
print "Varianza de pago =", v_pago
print "Desviacion tipica =", dt_pago

# Que pago se espera si el coche lleva estacionado
# dos o mas horas

horas = range(2,9)
ni = [38, 53, 45, 40, 13, 5, 36]
pago = [6, 9, 12, 14, 16, 18, 20]
fi = map(lambda x: float(x)/sum(ni), ni)

# esperanza de los pagos:
# ∑pago*fi

esp_pago = sum(np.multiply(fi,pago))
v_pago = sum(np.multiply(fi,np.multiply(pago,pago))) - esp_pago ** 2
dt_pago = np.sqrt(v_pago)

print "\nSI EL COCHE LLEVA DOS HORAS O MAS\n"
print "Esperanza de pago =", esp_pago
print "Varianza de pago =", v_pago
print "Desviacion tipica =", dt_pago