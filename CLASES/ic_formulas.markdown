# ESTIMAR INTERVALO DE CONFIANZA #

INGREDIENTES:

- Una muestra.
- Nivel de confianza o significación (𝛂).
- Distribución de la que proviene la muestra o su tamaño.

## PARA LA MEDIA

## $$IC(\mu) = \bar{x} \pm Z_{\alpha /2} \frac{S_1}{\sqrt{n}}$$

## PARA LA PROPORCIÓN

## $$ IC(p) = \hat{p} \pm Z_{\alpha/2} \sqrt{ \frac{ \hat{p} (1-\hat{p}) }{n}} $$

## PARA LA VARIANZA

##  $$IC(\sigma) = \frac{(n-1)S_1^2}{\chi^2_{(n-1\ ;\ \alpha/2)}}$$
##  $$IC(\sigma) = \frac{(n-1)S_1^2}{\chi^2_{(n-1\ ;\ 1-\alpha/2)}}$$


__Nota:__ Esto se aplica siempre que la población provenga de una distribución normal o la muestra tenga un tamaño mayor que 30, que gracias el TCL podemos suponer normalidad. De no ser el caso, aplicamos la distribución _t-student_, con n-1 grados de libertad.