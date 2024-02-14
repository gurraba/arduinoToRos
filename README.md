# arduinoToRos

## Purpose
This repository contains code and to send data over serial between arduino and ROS. It is very bare bones, but it might help get you started.
I am very new to ROS and had the same issue many hobbyists and students have: How do I communicate between ros2 and an arduino without using microros?
If you're as stuck as I was, this  might be of help.

## Prerequisites
- Ros2 iron irwini
- PySerial installed
- Ubuntu 22.04 LTS (might work on windows idk)
- 
## Getting Started
Build your own package named com topic and replace the files with the files in the repo. 
The publisher and subscriber node are called "talker" and "listener", respectively.
* ros2 run com_topic talker
* ..--..             listener

1. **Clone the Repository**: Clone this repository to your local machine using the following command:
   ```bash
   git clone https://github.com/your-username/arduinoToRos.git
