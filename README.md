# 🛡️ Gun Detection Security System 🚨

Welcome to the Gun Detection Security System repository! This project is a comprehensive security system that uses advanced computer vision techniques to detect guns and faces in real-time from a webcam feed, with features for image and video capture upon detection, along with detailed reporting of detection events.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
  - [Requirements](#requirements)
  - [Installation Steps](#installation-steps)
  - [Troubleshooting](#troubleshooting)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction
In today's world, security is of utmost importance, and the Gun Detection Security System aims to enhance security measures by providing a reliable and efficient solution for detecting firearms in various environments. This system leverages the power of computer vision to detect guns and faces in real-time, enabling prompt action and intervention in critical situations.

<p align="center">
  <img src="https://github.com/Rishit-katiyar/Gun-Detection-Security-System/assets/167756997/2604e55a-e186-42e8-834e-94af4036ac63" alt="gun_20240428191108">
</p>

## Features
🔍 Real-time gun detection from webcam feed  
👤 Face detection for additional context  
📸 Image capture upon gun detection  
🎥 Video recording when a gun is detected  
📊 Detailed reporting of detection events  

## Installation

### Requirements
Before installing the Gun Detection Security System, ensure that you have the following prerequisites:
- Python 3.x installed on your system
- Git installed for cloning the repository
- OpenCV library for computer vision tasks
- NumPy library for numerical operations

### Installation Steps
Follow these steps to set up the Gun Detection Security System on your local machine:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Rishit-katiyar/Gun-Detection-Security-System.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd Gun-Detection-Security-System
   ```

3. **Install the required Python packages** using pip:
   ```bash
   pip install -r requirements.txt
   ```

4. **Download the cascade classifier file** for gun detection and place it in the project directory.

5. **Optionally, customize the system settings** in the code according to your preferences.

### Troubleshooting
If you encounter any issues during the installation process, try the following troubleshooting steps:

- **Ensure Python and pip are properly installed**:
  Check if Python and pip are installed and added to your system's PATH. You can verify their versions by running:
  ```bash
  python --version
  pip --version
  ```

- **Update pip and setuptools**:
  Ensure that pip and setuptools are up-to-date by running:
  ```bash
  pip install --upgrade pip setuptools
  ```

- **Check for OpenCV installation**:
  If you encounter errors related to OpenCV installation, try reinstalling it using pip:
  ```bash
  pip install opencv-python-headless
  ```

## Usage
To use the Gun Detection Security System, follow these steps:

1. **Run the `advanced_system_code.py` script**:
   ```bash
   python advanced_system_code.py
   ```

2. The system will start detecting guns and faces from the webcam feed in real-time.

3. Upon detecting a gun, the system will save an image of the detection event in the `gun_detection_images` folder.

4. If configured, the system will also record a video clip of the detection event.

5. Review the detailed reporting of detection events in the console.

## Contributing
Contributions are welcome! If you have any ideas, suggestions, or improvements for the Gun Detection Security System, feel free to open an issue or submit a pull request. Let's work together to make security systems better and more effective.

## License
This project is licensed under the GNU General Public License v3.0 (GNU GPLv3). See the [LICENSE](LICENSE) file for details.
