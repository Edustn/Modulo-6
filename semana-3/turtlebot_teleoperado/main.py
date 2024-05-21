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
        
        # Criação do servidor para o serviço de parada de emergência
        self.stop_robot_srv = self.create_service(Empty, 'stop_robot', self.stop_robot_callback)

    def send_cmd_vel(self, linear_vel, angular_vel):
        self.twist_msg.linear.x = linear_vel
        self.twist_msg.angular.z = angular_vel
        self.publisher_.publish(self.twist_msg)
        print("Linear Vel: {}, Angular Vel: {}".format(linear_vel, angular_vel))
    
    # Callback do servidor de parada de emergência
    def stop_robot_callback(self, request, response):
        print("Serviço de parada de emergência acionado para desligamento de toda a conexão")
        self.send_cmd_vel(0.0, 0.0)  # Para o robô
        return response

    def stop_robot(self):
        if not self.stop_robot_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().error('Serviço de parada de emergência não disponível')
            return
        request = Empty.Request()
        future = self.stop_robot_client.call_async(request)
        rclpy.spin_until_future_complete(self, future)
        if future.result() is not None:
            self.get_logger().info('Robô parado com sucesso.')
            self.destroy_node()  # Destruir o nó antes de sair
            rclpy.shutdown()
            sys.exit()

        else:
            self.get_logger().error('Falha ao parar o robô.')

def get_key():
    tty.setraw(sys.stdin.fileno())
    select.select([sys.stdin], [], [], 0)
    key = sys.stdin.read(1)
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

def main(args=None):
    rclpy.init(args=args)
    node = TeleopTurtle()


    print("Para movimentar o robô utilize as teclas A,W,S,D")
    print("Em caso de uma parada de emergência tecle S")
    print("Em caso que necessite que o robô fique inoperante e encerre o sistema, tecle F")

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
            print("Parada completa acionada")
            node.stop_robot()
        

    node.send_cmd_vel(0.0, 0.0)
  
if __name__ == '__main__':
    settings = termios.tcgetattr(sys.stdin)
    main()
