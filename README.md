# 🤖 Robot Móvil de Cuatro Ruedas en ROS2

## 📌 Descripción del Proyecto

Este proyecto consiste en el diseño, modelado y simulación de un robot móvil de cuatro ruedas utilizando **ROS2** y **Gazebo**. El robot está compuesto por un chasis principal y cuatro ruedas, permitiendo su visualización y simulación en un entorno físico virtual.

El sistema integra la descripción del robot mediante archivos URDF, la simulación en Gazebo y la visualización en RViz.

---

## 🎯 Objetivo del Proyecto

El objetivo principal es desarrollar un modelo funcional de robot móvil de cuatro ruedas, como evolución de modelos más simples, permitiendo:

- Representar su estructura mediante URDF.
- Incorporar propiedades físicas como colisiones e inercias.
- Simular su comportamiento en Gazebo.
- Automatizar su ejecución mediante archivos de lanzamiento.

---

## ⚙️ Requisitos Técnicos

### 🔹 Modelado URDF

El robot ha sido modelado utilizando el archivo: urdf/robot_4_ruedas.urdf

Este archivo define:

- Un enlace principal (`base_link`) que representa el chasis.
- Cuatro ruedas:
  - `left_wheel`
  - `right_wheel`
  - `front_left_wheel`
  - `front_right_wheel`
- Uniones (`joint`) de tipo `revolute`, que permiten la rotación de las ruedas.

---

### 🔹 Propiedades Físicas

El modelo incluye propiedades físicas necesarias para la simulación:

- **Colisiones (`collision`)**:  
  Permiten que el robot interactúe con el entorno en Gazebo.

- **Inercia (`inertial`)**:  
  Se han definido valores de masa e inercia para el chasis y las ruedas.

Estas propiedades permiten que el robot tenga una interacción más realista con el entorno de simulación.

---

### 🔹 Simulación en Gazebo

El robot se integra en Gazebo mediante un archivo de lanzamiento que:

- Inicia el entorno de simulación.
- Carga el modelo del robot.
- Inserta el robot en la escena.

En la simulación se puede observar la estructura del robot y su interacción básica con el entorno.

---

### 🔹 Archivo de Lanzamiento (.launch.py)

El archivo principal de ejecución es: launch/robot_4_ruedas_gazebo.launch.py

Este archivo se encarga de:

- Incluir el entorno de Gazebo.
- Leer el archivo URDF del robot.
- Publicar el modelo mediante `robot_state_publisher`.
- Insertar el robot en la simulación mediante un nodo de spawn.

El archivo contempla compatibilidad con:

- `gazebo_ros`
- `ros_gz_sim`

---

## 📂 Estructura del Repositorio

El proyecto está organizado de la siguiente manera:

src/
└── robot_4_ruedas_description/
├── launch/
│   └── robot_4_ruedas_gazebo.launch.py
├── urdf/
│   └── robot_4_ruedas.urdf
├── rviz/
│   └── robot_4_ruedas.rviz
├── CMakeLists.txt
└── package.xml

### Archivos importantes

- **URDF del robot**: `urdf/robot_4_ruedas.urdf`
- **Archivo de lanzamiento**: `launch/robot_4_ruedas_gazebo.launch.py`
- **Configuración de RViz**: `rviz/robot_4_ruedas.rviz`

---

## ▶️ Instrucciones de Uso

### 🔧 Compilación

Desde la raíz del workspace:

colcon build --packages-select robot_4_ruedas_description

Luego:

source install/setup.bash

---

### 🚀 Ejecución

Para lanzar la simulación:

ros2 launch robot_4_ruedas_description robot_4_ruedas_gazebo.launch.py


Alternativamente, se puede utilizar el script:

bash run.bash

---

### 👀 Resultado esperado

Al ejecutar el proyecto se debe observar:

* El entorno de Gazebo abierto.
* El robot de cuatro ruedas cargado en la escena.
* El modelo visible y posicionado sobre el plano.

---

## 📊 Resultados

El proyecto permite:

* Visualizar el robot en RViz.
* Cargar el modelo en Gazebo.
* Integrar correctamente la descripción del robot con el entorno de simulación.

---

## 🧠 Conclusiones

* La definición de **colisiones** es importante para la interacción en Gazebo.
* Las **inercias** permiten representar propiedades físicas del robot.
* El uso de **URDF** facilita la descripción estructural del robot.
* El archivo de lanzamiento permite ejecutar todo el sistema de forma integrada.
* La combinación de ROS2 y Gazebo permite validar modelos robóticos en simulación.

---

## 👥 Integrantes

Trabajo desarrollado en grupo.

---

## 📅 Detalles de Entrega

* Formato: repositorio con estructura ROS2.
* Ejecución: mediante archivo launch.
* Evaluación: basada en la correcta visualización del robot en Gazebo y revisión del código.