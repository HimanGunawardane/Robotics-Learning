# File: trajectory_controller_node.py
#
# chat GPT was used to convert this file from a trajectory controller to a joint controller
# that mostly involved rewriting some the logic and changing some names

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
import time
import math


class JointStateController(Node):

    def __init__(self):
        super().__init__('joint_state_controller_node')

        # Publisher for Isaac Sim ArticulationControllerBridge
        self.joint_pub = self.create_publisher(JointState, '/gr1/joint_command', 10)

        #names of joints that will be moved on sim robot
        self.joint_names = [
            'left_shoulder_pitch_joint',
            'left_elbow_pitch_joint',
            'left_shoulder_yaw_joint',
            'left_wrist_yaw_joint'
        ]

        #current positions of those joints in radians
        self.current_positions = [0.0, 0.0, 0.0, 0.0]
        
        #sends the joint positions to isaac
    def send_joint_state(self, target_positions):
        msg = JointState()
        msg.name = self.joint_names
        msg.position = target_positions
        msg.velocity = [0.0] * len(target_positions)
        msg.effort = [0.0] * len(target_positions)
        msg.header.stamp = self.get_clock().now().to_msg()

        self.joint_pub.publish(msg)
        self.get_logger().info(f"Sent joint state: {target_positions}")
        self.current_positions = target_positions

    #used to test that the connection is working 
    def movement_test(self):
        # Move all joints forward by 0.5 radians
        new_positions = [p + 0.5 for p in self.current_positions]
        self.send_joint_state(new_positions)
        time.sleep(2.0)

        # Move all joints back
        new_positions = [p - 0.5 for p in self.current_positions]
        self.send_joint_state(new_positions)
        time.sleep(2.0)

    def movement_wave(self):
        # Raise arm by 90 degrees (in radians) and rotates wrist
        new_positions = [
            self.current_positions[0] + math.radians(-80),
            self.current_positions[1] + math.radians(-110),
            self.current_positions[2], self.current_positions[3] + math.radians(-90),
        ]
        self.send_joint_state(new_positions)
        time.sleep(2.0)

        # Wave motion rolls the arm left and right
        for i in range(5):
            delta = math.radians(30 if i % 2 == 0 else -60)
            wave_positions = new_positions.copy()
            wave_positions[2] += delta
            self.send_joint_state(wave_positions)
            time.sleep(1.5)

        # Reset arm position
        reset_positions = [0.0, 0.0, 0.0, 0.0]
        self.send_joint_state(reset_positions)
        time.sleep(2.0)


def main(args=None):
    rclpy.init(args=args)
    node = JointStateController()


    #control menu
    while True:
        action = input("What would you like to do? |t = test|w = wave|q = quit|")
        if action == 't':
            node.movement_test()
        elif action == 'w':
            node.movement_wave()
        elif action == 'q':
            break
        else:
            print("Invalid input.")

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

