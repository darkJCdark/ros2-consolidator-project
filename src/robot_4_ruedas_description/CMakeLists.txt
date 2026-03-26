cmake_minimum_required(VERSION 3.8)
project(robot_4_ruedas_description)

find_package(ament_cmake REQUIRED)

install(
  DIRECTORY launch urdf rviz
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
