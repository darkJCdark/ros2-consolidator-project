# 🤖 Four-Wheeled Mobile Robot in ROS2

## 📌 Project Description

This project involves the design, modeling, and simulation of a four-wheeled mobile robot using **ROS2** and **Gazebo**. The robot consists of a main chassis and four wheels, allowing its visualization and simulation in a virtual physical environment.

The system integrates the robot description through URDF files, simulation in Gazebo, and visualization in RViz.

---

## 🎯 Project Objective

The main objective is to develop a functional model of a four-wheeled mobile robot, as an evolution of simpler models, enabling:

- Representation of its structure through URDF.  
- Incorporation of physical properties such as collisions and inertias.  
- Simulation of its behavior in Gazebo.  
- Automation of execution through launch files.  

---

## ⚙️ Technical Requirements

### 🔹 URDF Modeling

The robot has been modeled using the file: `urdf/robot_4_ruedas.urdf`

This file defines:

- A main link (`base_link`) representing the chassis.  
- Four wheels:  
  - `left_wheel`  
  - `right_wheel`  
  - `front_left_wheel`  
  - `front_right_wheel`  
- `revolute` joints that allow wheel rotation.  

---

### 🔹 Physical Properties

The model includes physical properties required for simulation:

- **Collisions (`collision`)**:  
  Allow the robot to interact with the environment in Gazebo.  

- **Inertia (`inertial`)**:  
  Mass and inertia values have been defined for the chassis and wheels.  

These properties enable the robot to have a more realistic interaction with the simulation environment.  

---

### 🔹 Simulation in Gazebo

The robot is integrated into Gazebo through a launch file that:

- Starts the simulation environment.  
- Loads the robot model.  
- Inserts the robot into the scene.  

In the simulation, the robot’s structure and its basic interaction with the environment can be observed.  

---

### 🔹 Launch File (.launch.py)

The main execution file is: `launch/robot_4_ruedas_gazebo.launch.py`

This file is responsible for:

- Including the Gazebo environment.  
- Reading the robot’s URDF file.  
- Publishing the model via `robot_state_publisher`.  
- Inserting the robot into the simulation using a spawn node.  

The file supports compatibility with:

- `gazebo_ros`  
- `ros_gz_sim`  

---

## 📂 Repository Structure

The project is organized as follows:

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

### Key Files

- **Robot URDF**: `urdf/robot_4_ruedas.urdf`  
- **Launch File**: `launch/robot_4_ruedas_gazebo.launch.py`  
- **RViz Configuration**: `rviz/robot_4_ruedas.rviz`  

---

## ▶️ Usage Instructions

### 🔧 Compilation

From the workspace root:

```
colcon build --packages-select robot_4_ruedas_description
```

Then:

```
source install/setup.bash
```

---

### 🚀 Execution

To launch the simulation:

```
ros2 launch robot_4_ruedas_description robot_4_ruedas_gazebo.launch.py
```

Alternatively, you can use the script:

```
bash run.bash
```

---

### 👀 Expected Result

When running the project, you should see:

- The Gazebo environment opened.  
- The four-wheeled robot loaded into the scene.  
- The model visible and positioned on the plane.  

---

## 📊 Results

The project enables:

- Visualization of the robot in RViz.  
- Loading the model in Gazebo.  
- Proper integration of the robot description with the simulation environment.  

---

## 🧠 Conclusions

- Defining **collisions** is crucial for interaction in Gazebo.  
- **Inertias** allow representation of the robot’s physical properties.  
- Using **URDF** simplifies the structural description of the robot.  
- The launch file enables integrated execution of the entire system.  
- Combining ROS2 and Gazebo validates robotic models in simulation.  

---

## 👥 Team Members

Project developed collaboratively in a group.  

---

## 📅 Delivery Details

- **Format**: ROS2 repository structure.  
- **Execution**: via launch file.  
- **Evaluation**: based on correct visualization of the robot in Gazebo and code review.  
