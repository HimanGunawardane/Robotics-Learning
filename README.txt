# GR1 RobotSim

Created by:
John Sargant
Aldo Setiawan
Ngoc Kim Nguyen
Bamunu Arachchi Pathirannehalage Himan Sanvidu Gunawardane
Omar Fakhra

gatea url: https://gitea.cdirmit.co/2025S2_Projects/RoboSim


**Project Description**

This project was created by RMIT as a group capstone project. 
It is a controlable humanoid robot sim. Due to project complications 
this project only allows you to make the robot wave and do a simple 
movement, to test if the connection to the robot is working.
The ROS2 script has however been built in a way to make it easy 
to control other joints the robot.


**Project Requirments**

--ROS2 requiremnts--

It is recomended that this project is run on a 
device running Ubuntu Linux 24.04. This is the recomended 
enviroment to run both ROS2 and Nvidia Isaac 5.0.0. 
Windows can be used but you may run into issues.


ROS 2 Jazzy Jalisco or ROS 2 Humble Hawksbill and their Requirments
are needed to run the ROS2 scripts in this project.
They can be fount here: https://www.ros.org/blog/getting-started/$0

It is also recomended you learn how to use ROS2 if you do not already know how.
tutorials can be found here: https://docs.ros.org/en/jazzy/Tutorials.html$0




--Isaac requiremnts--

Nvidia Isaac 5.0.0 is more hardware intensive than ROS2, so it has minimum hardware requiremnts. Those are as follows:
. CPU: Intel Core i7 (7th Generation)/AMD Ryzen 5
. Cores: 4
. RAM: 32GB
. Storage: 50GB SSD
. GPU: GeForce RTX 4080
. VRAM: 16GB
. OS: Ubuntu 22.04/24.04 or Windows 10/11(Ubuntu is prefered when connecting to ROS)


Ideal hardware requiremntsare are as follows:
. CPU: Intel Core i9, X-series or higher/AMD Ryzen 9, Threadripper or higher
. Cores: 16
. RAM: 64GB
. Storage: 1TB SSD
. RTX PRO 6000 Blackwell
. VRAM: 48GB
. OS: Ubuntu 22.04/24.04 or Windows 10/11(Ubuntu is prefered when connecting to ROS)


Isaac sim 5.0.0 can be downloaded from here: https://docs.isaacsim.omniverse.nvidia.com/5.1.0/installation/index.html$0


**How to Run the Project**

 

1. Setup and Execution 
    . Download Project Files 
    . Final_wave_model.usd (Isaac Sim Scene file) 
    . Trajectory_controller ROS 2 package 

2. Open Isaac Sim 
    . Launch Isaac Sim 5.0.0. 
    . Load the file Final_wave_model.usd from the project directory. 
    . Confirm that the ROS 2 Bridge extensions are all enabled. (Window -> Extensions -> Search ROS 2 -> toggle/enable all) 

3. Prepare ROS 2 Environment  
    . Open a terminal on Ubuntu 
    . Source ROS 2 Jazzy: source /opt/ros/jazzy/setup.bash 
    . Navigate to the trajectory_controller package directory. 

4. Build and Source the Package(run the follwing commands while in the package's directory)
    . colcon build  
    . Source install/local_setup.bash 

5. Run the Controller Package and Node(run the follwing command) 

    . ros2 run trajectory_controller trajectory_controller_node 

6. Execute the demonstration 

    . Ensure Isaac Sim is unpaused 

    . In the ROS 2 terminal, press w to trigger the wave motion 

    . The simulated GR-1 should lift its left arm and perform a wave 


*Notes* 

    . The ROS 2 script is designed to be easily extened to other joints and motions beyond the wave gesture. 

    . If communication fails, verify that the ROS 2 Bridge is active and that the correct topics (/gr1joint_command, /gr1/joint_state) are visible. 

    . Running both Isaac Sim and ROS 2 on the same machine reduces latency and connection errors. 
