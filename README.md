[README.md](https://github.com/user-attachments/files/33744866/README.md)
[![Open in MATLAB Online](https://www.mathworks.com/images/responsive/global/open-in-matlab-online.svg)](https://matlab.mathworks.com/open/github/v1?repo=l23212242-alt/MSFP2)

# Práctica 2: Modelado y control del sistema cardiovascular mediante el modelo Windkessel

## Información del estudiante

Javier Vazquez Gomez [23212242]; l23212242@tectijuana.edu.mx

Modelado de Sistemas Fisiológicos

Ingeniería Biomédica

## Docente

Dr. Paul Antonio Valle Trujillo; paul.valle@tectijuana.edu.mx

Departamento de Ingeniería Eléctrica y Electrónica, Tecnológico Nacional de México/IT Tijuana, Blvd. Alberto Limón Padilla s/n, Tijuana, C.P. 22454, B.C., México.

## Descripción de la asignatura

El modelizado de sistemas fisiológicos es una herramienta importante en Ingeniería Biomédica, permite comprender el funcionamiento del cuerpo humano, así como diseñar y evaluar terapias y dispositivos médicos; se define como el proceso de formular modelos matemáticos o computacionales que representan el comportamiento y la interacción de los sistemas biológicos y fisiológicos. Esta asignatura pretende aportar al perfil del Ingeniero Biomédico la capacidad de realizar investigación científica en el área de Biología de Sistemas con la finalidad de dirigir y participar en equipos de trabajo interdisciplinarios en contextos nacionales e internacionales, así como de proporcionar soluciones informáticas para resolver problemas en el campo de la Ingeniería Biomédica con ética profesional; lo anterior al proporcionar al estudiante bases sólidas para modelizar sistemas y diseñar controladores para la solución de problemas en las áreas de atención médica y del sector industrial médico. La construcción de analogías entre circuitos eléctricos y sistemas fisiológicos para la formulación de modelos matemáticos y el diseño de controladores mediante la experimentación in silico brindan herramientas de gran aplicación en el quehacer profesional del Ingeniero Biomédico.

La asignatura de Modelado de Sistemas Fisiológicos forma parte del plan de estudios de la carrera en Ingeniería Biomédica con la siguiente competencia general del curso: Utiliza las propiedades de los circuitos RLC para describir la dinámica de sistemas fisiológicos, obtener modelos matemáticos y aplicar el control clásico, esto con el objetivo de integrar los principios de la Ingeniería de Control, la Electrónica Analógica y las Ciencias de la Computación con la Anatomía y Fisiología del cuerpo humano para proporcionar descripciones cuantitativas y cualitativas de sistemas fisiológicos complejos con el objetivo de modelizar, analizar, controlar, ilustrar y predecir su dinámica tanto en el corto como en el largo plazo.

## Objetivos

1. Identificar las variables y los parámetros del modelo Windkessel de cuatro elementos.
2. Determinar el modelo de ecuaciones integro-diferenciales y el sistema de ecuaciones diferenciales ordinarias.
3. Calcular la función de transferencia para los casos normotenso, hipotenso e hipertenso.
4. Analizar los polos, la estabilidad y el error en estado estacionario de los modelos.
5. Simular las respuestas del sistema en MATLAB/Simulink y Python utilizando una señal de entrada común.
6. Sintonizar los controladores PID de los casos hipotenso e hipertenso tomando como referencia la respuesta normotensa.
7. Comparar las respuestas en lazo abierto y lazo cerrado y representar los resultados mediante gráficas.
8. Relacionar el circuito equivalente con las estructuras cardiovasculares mediante un diagrama biológico.

## Descripción detallada del sistema

En esta práctica se utiliza el modelo Windkessel de cuatro elementos para representar de manera simplificada el comportamiento del sistema cardiovascular mediante una analogía eléctrica. La impedancia característica **Z** representa la oposición al flujo en la región arterial proximal; la inertancia **L**, los efectos de inercia de la sangre; la resistencia periférica **R**, la oposición al flujo en los vasos periféricos; y la distensibilidad **C**, la capacidad de las arterias para almacenar volumen ante variaciones de presión.

Se consideran tres condiciones cardiovasculares: hipotenso, normotenso e hipertenso. En las simulaciones realizadas se utilizaron los siguientes parámetros:

| Parámetro | Hipotenso | Normotenso | Hipertenso |
|---|---:|---:|---:|
| Z | 0.010 | 0.010 | 0.010 |
| L | 0.001 | 0.001 | 0.001 |
| R | 1.000 | 1.000 | 1.000 |
| C | 3.500 | 1.500 | 1.000 |

En estos tres conjuntos de parámetros, **Z, L y R permanecen constantes**, mientras que **C cambia según la condición**. El valor mayor de C corresponde al caso hipotenso y el menor al hipertenso, de acuerdo con el planteamiento utilizado en esta práctica.

La presión arterial de entrada se representa mediante **Pa(t)** y la presión de salida mediante **Pp(t)**. A partir de las relaciones del circuito equivalente y la transformada de Laplace, se obtiene la función de transferencia:

$$
G(s)=\frac{P_p(s)}{P_a(s)}=\frac{LRs+RZ}{CLRZs^2+L(Z+R)s+RZ}
$$

Se calculan los polos de cada modelo para estudiar su estabilidad. También se desarrolla el modelo de ecuaciones diferenciales ordinarias utilizando el flujo asociado a la inertancia y la presión de salida como variables de estado.

Las simulaciones se realizan durante **15 segundos**. Primero se obtiene la respuesta normotensa; posteriormente, esta respuesta se utiliza como entrada de los modelos hipotenso e hipertenso en la implementación numérica. En Simulink se representan las tres condiciones y se incorporan controladores PID independientes para los casos hipotenso e hipertenso, utilizando como referencia la respuesta del individuo normotenso. Las ganancias se ajustan mediante la herramienta PID Tuner.

En Python se implementan las funciones de transferencia, se calculan los polos y se comparan las respuestas de los modelos sin controlador y con controlador. Las gráficas permiten observar las diferencias entre las señales de las tres condiciones y evaluar el seguimiento de la referencia normotensa.

**Palabras clave:** Modelo Windkessel; Sistema cardiovascular; Función de transferencia; Controlador PID; Estabilidad; Simulaciones numéricas.

## Lista de archivos incluidos en el repositorio

1. Cuaderno computacional de MATLAB y su versión exportada [.mlx y .pdf].
2. Modelo de Simulink [.slx].
3. Código desarrollado en Python [.py].
4. Señal de entrada utilizada en las simulaciones [.xlsx].
5. Análisis matemático: ecuaciones, función de transferencia, polos, estabilidad y error en estado estacionario [.pdf].
6. Figuras de las simulaciones de los casos normotenso, hipotenso e hipertenso en MATLAB y Python [.pdf].
7. Capturas de los parámetros y las respuestas de los controladores PID para los casos hipotenso e hipertenso [.png].
8. Diagrama biológico del sistema cardiovascular y su relación con el modelo Windkessel [.jpeg].

## Referencias

[1] P. A. Valle, *Syllabus para Modelado de Sistemas Fisiológicos*, Tecnológico Nacional de México / Instituto Tecnológico de Tijuana, Tijuana, B.C., México, 2026. Permalink: https://biomath.xyz/course/

[2] M. C. Khoo, *Physiological Control Systems: Analysis, Simulation, and Estimation*, 2nd ed. IEEE Press, 2018.

[3] N. S. Nise, *Control Systems Engineering*, 8th ed. John Wiley & Sons, 2020.
