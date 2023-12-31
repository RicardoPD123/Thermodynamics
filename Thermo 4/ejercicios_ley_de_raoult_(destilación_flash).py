# -*- coding: utf-8 -*-
"""Ejercicios Ley de Raoult (Destilación Flash)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15PPoDzAeShr_OHm3OhmGDQkStbYfwija

# Presentación
Alumno: Ricardo Arath Díaz Parra

Matrícula: 202121428

Materia: Fisicoquímica IV

En el siguiente cuaderno se presentan los problemas propuestos resueltos en el lenguaje de programación llamado **python** dicho lenguaje ha tenido un gran impacto en las áreas de la ingeniería en los últimos años y funciona como una forma poderosa y sencilla de realizar modelos y programas de importancia para cientificos e ingenieros
\
\
***¿Cómo leer el código?***

Las primeras celdas están destinadas a crear las funciones necesarias que se utilizarán a lo largo de la resolución de los ejercicios, dichas funciones solo se necesitarán escribirse una vez para posteriormente solo utilizarlas (llamarlas) y trabajar de una forma más óptima

De igual manera, dentro de las celdas de código se encontrará texto que inicia con un **"#"**, esto indicará una explicación de lo que se está realizando en la línea o en la celda
\
\
***Estructura***

En la parte superior izquierda, al lado de **"+ Código"** del lado izquierdo se encuentra este ícono: ![image.png](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACIAAAAbCAYAAAAZMl2nAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAAEnQAABJ0Ad5mH3gAAAD+SURBVEhL7dZBCkRQHAbwb+YaysZWVm4gcQJyC1tScg4bOYeFnMRCYWOhSEkzQ29q5oVmmmbG4v02/F9v8S3e5zldbnAAZ/L8OxaExoLQdoOUZYk8z8n0XZv1LYoCQRBgmibYtg1JkhCGIZqmITtepygKZFkm07rNIGmaIo7j5V3TNJimCcdxUNf1svYOy7KgqiqZ1m0GadsWvu9jGAZ4ngeO45AkCbquIzteJ4oiBEEg0zr2ZaUdJsjuGZlb0/f9f89IlmWIomh513UdhmGw1vwUaw3t+K15vGvurXFdF1VVLWvv+Kg1h7l9Z/P/yDiO4HmerHwPqy+NBXkGXAFWdcFGERDOIgAAAABJRU5ErkJggg==), al presionar dicho ícono desplegará el índice para una navegación más cómoda
"""

# Importando las librerias a utilizar
import numpy as np # Funciones matemáticas
import matplotlib.pyplot as plt # Gráficos

# Creamos la función que utilizaremos para calcular la temperatura de rocío para cualquier tipo de mezcla
def Trocio(a,b,c,y,P):
  Ti=b/(a-np.log(P))-c # Temperaturas de cada componente
  Tsup=1/np.sum(y/Ti) # Temperatura supuesta
  err=1
  while err>=0.000001:
    Pi=np.exp(a-b/(Tsup+c)) # Presiones de cada componente (i)
    Pksat=P*np.sum(y/(Pi/Pi[0]))  # Presión del componente k
    Tn=b[0]/(a[0]-np.log(Pksat))-c[0] # Temperatura nueva (calculada con el componente k)
    err=np.abs(Tn-Tsup)
    Tsup=Tn
  print(f'La temperatura de rocío es: {Tsup}°C')

# Temperatura de burbuja para cualquier tipo de mezcla
def Tburbuja(a,b,c,x,P):
  Ti=b/(a-np.log(P))-c
  Tsup=sum(x*Ti)
  err=1
  while err>=0.000001:
    Pi=np.exp(a-b/(Tsup+c))
    alphai=Pi/Pi[0]
    P2n=P/np.sum(alphai*x)
    Tn=b[0]/(a[0]-np.log(P2n))-c[0]
    err=np.abs(Tn-Tsup)
    Tsup=Tn
  print(f'La temperatura de burbuja es: {Tsup}°C')

# Presión de rocío para cualquier tipo de mezcla
def Procio(a,b,c,y,T):
  Psat=np.exp(a-b/(T+c))
  Procio=1/sum(y/Psat)
  x=(y*Procio)/Psat
  print(f'La presión de rocío es de {Procio} kPa con unas composiciones de {x} respectivamente')

# Presión de burbuja para cualquier tipo de mezcla
def Pburbuja(a,b,c,x,T):
  Psat=np.exp(a-b/(T+c))
  Pburbuja=sum(x*Psat)
  y=(x*Psat)/Pburbuja
  print(f'La presión de burbuja es de {Pburbuja} kPa con unas composiciones de {y} respectivamente')

# Diagrama Pxy
def Pxy(a,b,c,T):
  Psat=np.exp(a-b/(T+c))
  x=np.arange(0,1.01,0.01)
  P=Psat[1]+(Psat[0]-Psat[1])*x
  y=x*Psat[0]/P
  plt.plot(x,P,y,P,linewidth=2)
  plt.xlabel('$x_1y_1$')
  plt.ylabel('P')
  plt.title('Diagrama Pxy')
  plt.grid()
  plt.xticks(np.arange(0, 1.1, 0.1))
  plt.yticks(np.arange(Psat[1], Psat[0]+1, 5))
  plt.legend(['linea de burbuja','línea de rocío'])
  plt.show()

# Diagrama Txy
def Txy(a,b,c,P):
  Tsat=b/(a-np.log(P))-c
  T=np.linspace(Tsat[0],Tsat[1],11)
  Psat1=np.exp(a[0]-b[0]/(T+c[0]))
  Psat2=np.exp(a[1]-b[1]/(T+c[1]))
  x=(P-Psat2)/(Psat1-Psat2)
  y=x*Psat1/P
  plt.plot(x,T,y,T,linewidth=2)
  plt.xlabel('$x_1y_1$')
  plt.ylabel('T')
  plt.title('Diagrama Txy')
  plt.grid()
  plt.legend(['linea de burbuja','linea de rocio'])
  plt.xticks(np.arange(0, 1.1, 0.1))
  plt.yticks(np.arange(T[0], T[-1]+1, 2.5))
  plt.show()

import numpy as np

z=np.array([0.4,0.6])
P=110
a=np.array([14.0572,14.7513])
b=np.array([2914.23,3331.7])
c=np.array([232.148,227.6])
Trocio(a,b,c,z,P)
Tburbuja(a,b,c,z,P)

"""# Ejercicio 1
El sistema n-butanol(1)/n-pentanol(2)/n-hexanol(3), se apega bastante a la ley de Raoult, y se ha determinado que a $T=70°C$:

$P_1^{sat}=798.62\thinspace kPa\\P_2^{sat}=283.95\thinspace kPa\\P_3^{sat}=105.4\thinspace kPa$

Para una mezcla de composición global $z_1=0.4,z_2=0.35,z_3=0.25$. Determine la presión donde comenzará a evaporarse si la mezcla original está en fase líquida y se somete a un proceso de expansión manteniendo $T=70°C$
"""

# Definiendo las presiones de saturación de cada componente dado y las composiciones globales
Ps=np.array([798.62,283.95,105.4])
x=np.array([0.4,0.35,0.25])

# Calculando la presión de burbuja
Pbu=sum(x*Ps)
y=(x*Ps)/Pbu
print(f'La presión de burbuja es de {Pbu} kPa con unas composiciones de {y} respectivamente')

"""# Ejercicio 2
Una mezcla formada por acetona(1)/acetonitrilo(2) con una composición global $z_1=0.42$ y $z_2=0.58$ se encuentra a $T=70°C$. Determine el intervalo de presión en kPa en donde la mezcla exista en equilibrio líquido-vapor.
"""

# Definimos constantes de los componentes, composiciones globales y temperatura
z=np.array([0.42,0.58])
T=70
a=np.array([14.3145,14.8950])
b=np.array([2756.22,3413.10])
c=np.array([228.060,250.523])

# Calculando el intervalo de equilibrio en la mezcla
Pb=Pburbuja(a,b,c,z,T)
Pr=Procio(a,b,c,z,T)

"""Ya que el intervalo de equilibrio en una mezcla se encuentra dentro del ojal, se tiene que calcular la presión de rocío y burbuja

Por lo tanto para el sistema acetona/acetonitrilo con las condiciones dadas, el intervalo de equilibrio L-V es de 223.5541 Kpa a 256.1075 kPa

# Ejercicio 3
Una mezcla formada por cloroformo(1)/tetracloruro de carbono(2) se encuentra a $T=75°C$ y $P=110\thinspace kPa$. Determine el intervalo del componente 1 donde la mezcla puede existir en equilibrio líquido-vapor.
"""

# Definiendo constantes de los componentes de la mezcla
a=np.array([13.7324,14.0572])
b=np.array([2548.74,2914.23])
c=np.array([218.552,232.148])

"""# Ejercicio 4
Suponiendo que la ley de Raoult es válida realice los cálculos siguientes para el sistema benceno(1)/tolueno(2):
"""

# Definiendo las constantes de los componentes de la mezcla
a=np.array([13.7819,13.9320])
b=np.array([2726.81,3056.96])
c=np.array([217.572,217.625])

"""## Inciso a)
Se conoce $x_1=0.33$ y $T=100°C$, encuentre $y_1$ y $P$
"""

x=np.array([0.33,1-0.33])
T=100
Pburbuja(a,b,c,x,T)

"""## Inciso b)
Se conoce $y_1=0.33$ y $T=100°C$, encuentre $x_1$ y $P$
"""

y=np.array([0.33,1-0.33])
T=100
Procio(a,b,c,y,T)

"""## Inciso c)
Se conoce $x_1=0.33$ y $P=120\thinspace kPa$, encuentre $y_1$ y $T$
"""

x=np.array([0.33,1-0.33])
P=120
Tburbuja(a,b,c,x,P)

"""## Inciso d)
Se conoce $y_1=0.33$ y $P=120\thinspace kPa$, encuentre $x_1$ y $T$
"""

y=np.array([0.33,1-0.33])
P=120
Trocio(a,b,c,y,P)

"""## Inciso e)
Se conoce $T=105°C$ y $P=120\thinspace kPa$, encuentre $x_1$ y $y_1$
"""



"""## Inciso f)
Para el inciso e), si la fracción mol global del benceno es $z_1=0.33$, ¿Cuál es la fracción molar de vapor en el sistema de dos fases?

## Inciso g)
¿Por qué es probable que la ley de Raoult sea un excelente modelo de ELV para este sistema, en las condiciones establecidas (o calculadas)?

# Ejercicio 5
Suponiendo que la ley de Raoult es válida prepare un diagrama P-x-y para una tempertaura de $T=90°C$, y un diagrama T-x-y para una presión de $P=90\thinspace kPa$ para los sistemas siguientes:
"""

# Definiendo temperatura y presión para los diagramas
P=90
T=90

"""## Inciso a)
Benceno(1)/etilbenceno(2)
"""

# Definiendo constantes de los componentes de la mezcla
a=np.array([13.7819,13.9726])
b=np.array([2726.81,3259.93])
c=np.array([217.572,212.300])

# Haciendo el diagrama Txy
Txy(a,b,c,P)

# Haciendo el diagrama Pxy
Pxy(a,b,c,T)

"""## Inciso b)
1-clorobutano(1)/clorobenceno(2)
"""

# Definiendo constantes de los componentes de la mezcla
a=np.array([13.7965,13.8635])
b=np.array([2723.73,3174.78])
c=np.array([218.265,211.700])

# Haciendo el diagrama Txy
Txy(a,b,c,P)

# Haciendo el diagrama Pxy
Pxy(a,b,c,P)

