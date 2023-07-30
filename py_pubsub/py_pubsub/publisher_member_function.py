
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rclpy
from rclpy.node import Node

from std_msgs.msg import String
import time


import serial

class MinimalPublisher(Node):
    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(String, 'topic', 10)
       
       
        self.serial_port = serial.Serial('/dev/ttyUSB4', 9600)
       
        timer_period = 0.25  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0
        '''
        while rclpy.ok():
            humidity_data = self.serial_port.readline().decode('utf-8').strip()
            if humidity_data == "Leak":
                  print("Leak")
        
'''
    def timer_callback(self):
        #self.i = 0
        msg = String()
        humidity_data = String()
        if rclpy.ok():
        	humidity_data = self.serial_port.readline().decode('utf-8').strip()
        msg.data = humidity_data
        self.publisher_.publish(msg)
        '''
        if (humidity_data == 'Leak'):
        	if (self.i == 0):
        		#print("Leak\n")
        		self.get_logger().info('Publishing: "%s"' % msg.data)
        		self.i = 1
        elif (humidity_data == 'No Leak'):
        	if (self.i == 1):
        		self.get_logger().info('Publishing: "%s"' % msg.data)
        		self.i = 0
 '''
        #self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
       

def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
