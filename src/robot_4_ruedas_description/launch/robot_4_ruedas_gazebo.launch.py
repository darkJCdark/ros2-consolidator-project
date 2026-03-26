from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
from ament_index_python.packages import PackageNotFoundError
import os


def generate_launch_description():
    pkg_share = get_package_share_directory('robot_4_ruedas_description')
    urdf_path = os.path.join(pkg_share, 'urdf', 'robot_4_ruedas.urdf')

    with open(urdf_path, 'r', encoding='utf-8') as infp:
        robot_desc = infp.read()

    try:
        gazebo = IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')
            )
        )
        spawn = Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            output='screen',
            arguments=['-entity', 'robot_4_ruedas', '-topic', 'robot_description', '-x', '0', '-y', '0', '-z', '0.3'],
        )
    except PackageNotFoundError:
        gazebo = IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(get_package_share_directory('ros_gz_sim'), 'launch', 'gz_sim.launch.py')
            ),
            launch_arguments={'gz_args': '-r empty.sdf'}.items(),
        )
        spawn = Node(
            package='ros_gz_sim',
            executable='create',
            output='screen',
            arguments=['-name', 'robot_4_ruedas', '-topic', 'robot_description', '-x', '0', '-y', '0', '-z', '0.3'],
        )

    rsp = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': robot_desc, 'use_sim_time': True}],
    )

    return LaunchDescription([
        gazebo,
        rsp,
        spawn,
    ])
