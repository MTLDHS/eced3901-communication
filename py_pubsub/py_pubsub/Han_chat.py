import rclpy
from rclpy.node import Node
from std_msgs.msg import String
#from geometry_msgs.msg import Twist
import serial

class HumidityListener(Node):
    def __init__(self):
        super().__init__('humidity_listener')
        #self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
        self.serial_port = serial.Serial('/dev/ttyUSB4', 9600)

    def listen(self):
        while rclpy.ok():
            humidity_data = self.serial_port.readline().decode('utf-8').strip()
            if humidity_data == "Too humid!":
            	print("Leak")
                #self.send_stop_command()
'''
    def send_stop_command(self):
        msg = Twist()  # 创建一个新的Twist消息
        msg.linear.x = 0.0
        msg.angular.z = 0.0
        self.publisher_.publish(msg)
'''
def main(args=None):
    rclpy.init(args=args)
    humidity_listener = HumidityListener()
    rclpy.spin(humidity_listener)
    humidity_listener.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
