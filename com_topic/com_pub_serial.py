import rclpy
from rclpy.node import Node
import serial
from std_msgs.msg import String


class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(String, 'topic', 1)
        timer_period = 0 # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0
        self.serial_port = serial.Serial(port='/dev/ttyACM0', baudrate=9600)  # Adjust this to match your Arduino's serial port
   

    def timer_callback(self):
        msg = String()
        msg.data = str(self.serial_port.readline())
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1


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
