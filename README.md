# 🤖 Robot Móvil de Cuatro Ruedas en ROS2

## 📌 Descripción del Proyecto

Este proyecto consiste en el diseño, modelado y simulación de un robot móvil de cuatro ruedas utilizando **ROS2** y **Gazebo**. El robot está compuesto por un chasis principal y cuatro ruedas, permitiendo su desplazamiento en un entorno simulado con comportamiento físico realista.

El sistema integra la descripción del robot mediante archivos URDF, la simulación en Gazebo y la visualización en RViz.

---

## 🎯 Objetivo del Proyecto

El objetivo principal es desarrollar un modelo funcional de robot móvil de cuatro ruedas, como evolución de modelos más simples, permitiendo:

* Representar su estructura mediante URDF.
* Definir propiedades físicas realistas (colisiones e inercias).
* Simular su comportamiento en Gazebo.
* Automatizar su ejecución mediante archivos de lanzamiento.

---

## ⚙️ Requisitos Técnicos

### 🔹 Modelado URDF

El robot ha sido modelado utilizando un archivo URDF ubicado en:

```
urdf/robot_4_ruedas.urdf
```

Este archivo define:

* Un enlace principal (`base_link`) que representa el chasis.
* Cuatro ruedas:

  * `left_wheel`
  * `right_wheel`
  * `front_left_wheel`
  * `front_right_wheel`
* Las uniones (`joint`) de tipo `revolute`, permitiendo la rotación de las ruedas.

---

### 🔹 Propiedades Físicas

Se han definido correctamente las propiedades físicas necesarias para la simulación:

* **Colisiones (`collision`)**:
  Permiten que el robot interactúe físicamente con el entorno en Gazebo.

* **Inercia (`inertial`)**:
  Se han asignado masa y matrices de inercia al chasis y a cada rueda, lo cual es fundamental para un comportamiento dinámico realista.

Estas propiedades aseguran que el robot:

* No atraviese el suelo.
* Responda correctamente a la gravedad y fuerzas físicas.

---

### 🔹 Simulación en Gazebo

El robot es simulado en Gazebo mediante un archivo de lanzamiento que:

* Inicia el entorno de simulación.
* Carga el modelo del robot.
* Inserta el robot en la escena.

Durante la simulación se puede observar:

* La estructura completa del robot.
* La interacción con el entorno físico.

---

### 🔹 Archivo de Lanzamiento (.launch.py)

El archivo principal de ejecución es:

```
launch/robot_4_ruedas_gazebo.launch.py
```

Este archivo realiza:

* Inclusión del entorno de Gazebo.
* Lectura del archivo URDF.
* Publicación del robot mediante `robot_state_publisher`.
* Inserción del robot en Gazebo usando un nodo de spawn.

También contempla compatibilidad con:

* `gazebo_ros`
* `ros_gz_sim`

---

## 📂 Estructura del Repositorio

El proyecto está organizado de la siguiente manera:

```
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
```

Archivos importantes:

* **URDF del robot**: `urdf/robot_4_ruedas.urdf`
* **Archivo de lanzamiento**: `launch/robot_4_ruedas_gazebo.launch.py`
* **Configuración de RViz**: `rviz/robot_4_ruedas.rviz`

---

## ▶️ Instrucciones de Uso

### 🔧 Compilación

Desde la raíz del workspace:

```bash
colcon build --packages-select robot_4_ruedas_description
```

Luego:

```bash
source install/setup.bash
```

---

### 🚀 Ejecución

Para lanzar la simulación:

```bash
ros2 launch robot_4_ruedas_description robot_4_ruedas_gazebo.launch.py
```

Alternativamente, se puede להשתמש el script:

```bash
bash run.bash
```

---

### 👀 Resultado esperado

Al ejecutar el proyecto se debe observar:

* El entorno de Gazebo abierto.
* El robot de cuatro ruedas correctamente cargado.
* El robot posicionado sobre el plano y listo para simulación.

---

## 📊 Resultados

El robot fue correctamente modelado y simulado, logrando:

* Representación visual en RViz.
* Integración funcional con Gazebo.
* Definición adecuada de propiedades físicas.

---

## 🧠 Conclusiones

* La correcta definición de **colisiones** es fundamental para evitar errores en la simulación.
* Las **inercias** permiten un comportamiento físico más realista.
* El uso de archivos de lanzamiento simplifica la ejecución del sistema completo.
* La integración entre URDF, Gazebo y ROS2 permite desarrollar simulaciones robóticas completas de manera modular.

---

## 👥 Integrantes

Trabajo desarrollado en grupo.

---

## 📅 Detalles de Entrega

* Formato: repositorio con estructura ROS2.
* Ejecución: mediante archivo launch.
* Evaluación: basada en la correcta visualización y funcionamiento del robot en Gazebo.

---
