import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
import numpy as np
from ultralytics import YOLO

class YoloNode(Node):
    def __init__(self):
        super().__init__('yolo_node')
        self.model = YOLO("yolov8n.pt")
        self.sub = self.create_subscription(
            Image, '/camera/image_raw',
            self.callback, 1)
        self.pub = self.create_publisher(
            Image, '/yolo/detection', 10)
        self.get_logger().info("YOLO Node gestartet!")

    def callback(self, msg):
        frame = np.frombuffer(msg.data, dtype=np.uint8)
        frame = frame.reshape((msg.height, msg.width, 3))
        results = self.model(frame, verbose=False)
        annotated = results[0].plot()
        out = Image()
        out.header = msg.header
        out.height, out.width = annotated.shape[:2]
        out.encoding = "bgr8"
        out.is_bigendian = False
        out.step = annotated.shape[1] * 3
        out.data = annotated.tobytes()
        self.pub.publish(out)
        self.get_logger().info("Erkannt!", throttle_duration_sec=2.0)

def main():
    rclpy.init()
    node = YoloNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
