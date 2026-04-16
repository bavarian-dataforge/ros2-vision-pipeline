import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
import cv2
import numpy as np

class ViewerNode(Node):
    def __init__(self):
        super().__init__('viewer_node')
        self.sub = self.create_subscription(
            Image, '/yolo/detection',
            self.callback, 10)
        self.count = 0
        self.get_logger().info("Viewer gestartet!")

    def callback(self, msg):
        frame = np.frombuffer(msg.data, dtype=np.uint8)
        frame = frame.reshape((msg.height, msg.width, 3))
        cv2.imwrite('/tmp/yolo_frame.jpg', frame)
        self.count += 1
        if self.count % 10 == 0:
            self.get_logger().info(f"Frame {self.count} gespeichert!")

def main():
    rclpy.init()
    node = ViewerNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
