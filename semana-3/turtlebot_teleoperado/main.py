import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_srvs.srv import Empty
import sys, select, termios, tty

class TeleopTurtle(Node):
    def __init__(self):
        super().__init__('turtlebot3_teleop')
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
        self.twist_msg = Twist()
        self.stop_robot_client = self.create_client(Empty, 'stop_robot')

    def send_cmd_vel(self, linear_vel, angular_vel):
        self.twist_msg.linear.x = linear_vel
        self.twist_msg.angular.z = angular_vel
        self.publisher_.publish(self.twist_msg)
        print("Linear Vel: {}, Angular Vel: {}".format(linear_vel, angular_vel))

    def call_stop_robot_service(self):
        while not self.stop_robot_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service not available, waiting again...')
        req = Empty.Request()
        future = self.stop_robot_client.call_async(req)
        rclpy.spin_until_future_complete(self, future)
        if future.result() is not None:
            self.get_logger().info('Service call succeeded')
        else:
            self.get_logger().error('Service call failed')

def get_key():
    tty.setraw(sys.stdin.fileno())
    select.select([sys.stdin], [], [], 0)
    key = sys.stdin.read(1)
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

def main(args=None):
    rclpy.init(args=args)
    node = TeleopTurtle()

    try:
        while True:
            key = get_key()
            if key == '\x03':
                break
            elif key == 'w':
                node.send_cmd_vel(0.2, 0.0) 
            elif key == 'x':
                node.send_cmd_vel(-0.2, 0.0)
            elif key == 'd':
                node.send_cmd_vel(0.0, -0.5) 
            elif key == 'a':
                node.send_cmd_vel(0.0, 0.5)  
            elif key == 's':
                print("Botão de segurança acionado")
                node.send_cmd_vel(0.0, 0.0)
            elif key == 'f':
                print("Parando o robô e matando o processo")
                node.call_stop_robot_service()
                break

        node.send_cmd_vel(0.0, 0.0)
    finally:
        rclpy.shutdown()

if __name__ == '__main__':
    settings = termios.tcgetattr(sys.stdin)
    main()
