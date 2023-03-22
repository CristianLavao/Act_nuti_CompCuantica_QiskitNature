# Act_nuti_CompCuantica_QiskitNature

# Importación de geometría molecular:
## el primer paso para realizar cálculos de estructura electrónica con Qiskit Nature es importar la geometría molecular del sistema de interés. Esto se puede hacer usando una variedad de formatos de archivo, como PDB, XYZ o MOL2.
![image](https://user-images.githubusercontent.com/22063158/226792219-5161a4b2-c773-4fef-be61-8b3e4e8ff137.png)

# Generación del segundo hamiltoniano cuantificado: 
## una vez importada la geometría molecular, Qiskit Nature utiliza una biblioteca interna para generar el segundo hamiltoniano cuantificado para el sistema. Esta es una representación matemática de la estructura electrónica de la molécula y describe el comportamiento de los electrones en términos de sus funciones de onda.
![image](https://user-images.githubusercontent.com/22063158/226792290-3748ba1e-befe-4ca3-8a5b-d7d885843ba8.png)

# Asignación del hamiltoniano a qubits: 
## el segundo hamiltoniano cuantificado se asigna luego a qubits mediante un algoritmo llamado transformación de Jordan-Wigner. Este proceso implica mapear los operadores fermiónicos en el hamiltoniano a los operadores de Pauli en qubits.
![image](https://user-images.githubusercontent.com/22063158/226792384-38dabcab-05e3-4edb-86db-34b51260a7ec.png)

# Construcción del circuito ansatz: 
## Qiskit Nature proporciona una variedad de circuitos ansatz preconstruidos que se pueden usar para cálculos de estructuras electrónicas, o los usuarios pueden construir los suyos propios. Estos circuitos generalmente se construyen utilizando puertas parametrizadas, como rotaciones y puertas entrelazadas, que están optimizadas para minimizar la energía del sistema.
![image](https://user-images.githubusercontent.com/22063158/226792440-96bf0c24-2aa4-4f9d-a6bb-8a41c23860e7.png)

# Ejecución del algoritmo variacional:
## el circuito ansatz se usa luego junto con un algoritmo variacional, como el solucionador propio cuántico variacional (VQE), para encontrar la energía del estado fundamental del sistema. Esto implica ejecutar el circuito en una computadora cuántica o un simulador cuántico y optimizar los parámetros del circuito para encontrar la energía mínima.

# Extracción de resultados: 
## una vez que se encuentra la energía mínima, Qiskit Nature proporciona herramientas para extraer información adicional sobre el sistema, como la estructura electrónica, las longitudes de enlace y los ángulos de enlace.









