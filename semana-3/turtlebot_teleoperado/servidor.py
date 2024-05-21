import rclpy
from rclpy.node import Node
from std_srvs.srv import Empty
import os
import signal

class StopRobotService(Node):
    def __init__(self):
        super().__init__('stop_robot_service')
        self.srv = self.create_service(Empty, 'stop_robot', self.stop_robot_callback)

    def stop_robot_callback(self, request, response):
        self.get_logger().info('Stopping the robot and killing the process...')
<<<<<<< HEAD
=======
        
>>>>>>> refs/remotes/origin/main
        
        # Matando o processo de operação
        os.kill(os.getpid(), signal.SIGINT)
        return response

def main(args=None):
    rclpy.init(args=args)
    node = StopRobotService()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
