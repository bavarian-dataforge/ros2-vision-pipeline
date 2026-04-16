import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
import cv2

class CameraNode(Node):
    def __init__(self):
        super().__init__('camera_node')
        self.cap = cv2.VideoCapture(1)
        self.pub = self.create_publisher(Image, '/camera/image_raw', 10)
        self.timer = self.create_timer(0.1, self.callback)
        self.get_logger().info("Kamera Node gestartet!")

    def callback(self):
        ret, frame = self.cap.read()
        if not ret:
            self.get_logger().warn("Kein Bild!")
            return
        msg = Image()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = "camera"
        msg.height, msg.width = frame.shape[:2]
        msg.encoding = "bgr8"
        msg.is_bigendian = False
        msg.step = frame.shape[1] * 3
        msg.data = frame.tobytes()
        self.pub.publish(msg)
        self.get_logger().info("Bild gesendet!", throttle_duration_sec=2.0)

    def destroy_node(self):
        self.cap.release()
        super().destroy_node()

def main():
    rclpy.init()
    node = CameraNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
