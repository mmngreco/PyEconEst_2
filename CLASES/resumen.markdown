# QUÉ HEMOS VISTO:

## Tomar una muestra de tamaño _n_.

### Muestreo __con reposición__: 
La característica principal de este tipo de muestreo es que las observaciones pueden _repetirse_, por tanto, cada observación tiene una probabilidad distinta de resultar elegida.

* __En Excel__:
    1. Datos Necesarios: 
        * Tabla de datos
        * Tamaño de la Población (N): `=Contar()`
        * Tamaño de la Muestra (n)
        * Observaciones Numeradas (1-N): `rellenar > series > columnas y límite`
    2. Sortear al azar con repeticiones: `=ALEATORIO()`.
    3. Corregir la amplitud (a = N-1): `=ALEATORIO()* a`.
    4. Desplazar el rango del aleatorio: `=_ALEATORIO() * a_ + 1`
    5. Transformar en valores discretos: `=REDONDEAR( _aleatorio * a + 1_ ; 0)` Ó `=REDONDEAR.MAS(_aleatorio * N_ ; 0)`. Esta última función es la forma más correcta de hacerlo, ya que cogería valores entre 0-1 = 1, 1-2=2, ..., N-1-N=N.
    6. Numeramos las columnas (variables) de la tabla de datos, en nuestra tabla de la muestra.
    7. Seleccionar la muestra: `=BUSCARV(_valor_ ; _tabla_; _columna_ ; 0)`.
        - __valor:__ fijando columnas
        - __tabla:__ fijando todo
        - __columna:__ fijando filas
    8. Comprobar las referencias a celdas, deben ser absolutas (fijas) de algún modo, ya sea fila, columna o todo.
    9. Arrastrar 

### Muestreo __sin reposición__: 

Las observaciones son unicas, y cada una de ellas tiene, por tanto, la misma probabilidad.

__En Excel__:

1. Datos Necesarios:
    - Tamaño de la Población.
    - Tamaño de la __Muestra__ o __Fracción de Muestreo__. 
2. Calculamos la fracción de muestreo: $fm = \frac{n}{N}$.
3. Asignamos a cada observación de la población un valor aleatorio: `=ALEATORIO()`.
4. Creamos una variable Binomial para el sorteo: `=SI( ALEATORIO < fm; 1; 0)`.
5. Seleccionar la muestra: __Tabla Dinámica__.
    1. Seleccionar toda la tabla, nombres incluidos.
    2. Insertar > tabla dinámica
    3. Organizar las variables según nuestras necesidades:
        -   __Filtro:__ Variable = {1,0}
        -   __Columna:__ Valores de una variable que queremos poner como Etiquetas de Columnas.
        -   __Fila:__ Valores de una variable que queremos poner como Etiqueta de Fila. En general será el nº de observación.
        -   __Valores__: Serán los valores que queremos que contenga la tabla para dichas filas y columnas, dado el filtro.
            -   Valores tiene la opción de cambiar el estadistico de resúmen __'Total'__, por el que nos sea de mejor conveniencia: promedio, varianza, etc...