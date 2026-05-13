# ROS 2 Vision Pipeline with YOLO

Real-time object detection pipeline built with ROS 2 Jazzy and YOLOv8.
Developed as part of a personal AI-robotics learning journey by Florian Englmeier.

## Demo
Live object detection via USB webcam — person, chair, book and more detected in real-time.

## System Requirements
- Ubuntu 24.04 LTS
- ROS 2 Jazzy
- Python 3.12
- USB Webcam

## Installation

### 1. ROS 2 Jazzy
sudo apt install ros-jazzy-desktop
echo "source /opt/ros/jazzy/setup.bash" >> ~/.bashrc

### 2. Dependencies
sudo apt install -y ros-jazzy-cv-bridge python3-opencv
sudo pip3 install ultralytics --break-system-packages

### 3. Build
cd ~/ros2_dev/ros2_ws
colcon build
source install/setup.bash

## Usage

Open three terminals. In each one first run:
source /opt/ros/jazzy/setup.bash
source ~/ros2_dev/ros2_ws/install/setup.bash

Terminal 1 - Camera Node:
ros2 run vision_pipeline camera_node

Terminal 2 - YOLO Node:
ros2 run vision_pipeline yolo_node

Terminal 3 - Live Viewer:
python3 ~/ros2_dev/week1/live_viewer.py

## Architecture
USB Webcam → camera_node → /camera/image_raw → yolo_node → /yolo/detection → viewer

## Author
Florian Englmeier
M.Eng. Electronic & Mechatronic Systems
GitHub: bavarian-dataforge
