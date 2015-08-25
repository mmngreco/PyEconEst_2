# CLASE 1: QUÉ HEMOS VISTO:

## Tomar una muestra de tamaño __n__.
- Muestreo __con reposición__: Las observaciones pueden repetirse, por tanto cada observación tiene una probabilidad distinta de resultar elegida.
    + __En Excel__:
        1. Sortear al azar con repeticiones: `=ALEATORIO()`.
        2. Corregir la amplitud (a = N-1): `=ALEATORIO()* a`.
        3. Transformar en valores discretos: `=REDONDEAR( ; 0)`.
        4. Seleccionar la muestra: `=BUSCARV(_valor_ ; _tabla_; _columna_)`.
- Muestreo __sin reposición__: Las observaciones son unicas (misma probabilidad).
    + __En Excel__:
        1. Calculamos la fracción de muestreo: $fm = \frac{n}{N}$.
        2. Asignamos a cada observación de la población un valor aleatorio: `=ALEATORIO()`.
        3. Creamos una variable Binomial para el sorteo: `=SI( ALEATORIO < fm; 1; 0)`.
        4. Seleccionar la muestra: __Tabla Dinámica__.