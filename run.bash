#!/bin/bash
colcon build --packages-select robot_4_ruedas_description
source install/setup.bash
ros2 launch robot_4_ruedas_description robot_4_ruedas_gazebo.launch.py