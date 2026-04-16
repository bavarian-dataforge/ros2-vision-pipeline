from setuptools import find_packages, setup

package_name = 'vision_pipeline'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='parallels',
    maintainer_email='parallels@todo.todo',
    description='Vision Pipeline',
    license='MIT',
    entry_points={
        'console_scripts': [
            'camera_node = vision_pipeline.camera_node:main',
            'yolo_node = vision_pipeline.yolo_node:main',
            'viewer_node = vision_pipeline.viewer_node:main',
        ],
    },
)
