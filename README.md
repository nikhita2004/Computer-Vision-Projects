# Computer-Vision-Projects

**1. Hand Gesture-Based Screen Mode Switcher with OpenCV and MediaPipe**(mode_change.py)

This project uses OpenCV and MediaPipe to toggle between light and dark modes on a Windows system through simple hand gestures, providing an intuitive, hands-free interface to change screen modes.

**Features**

Hand Gesture Detection: Utilizes MediaPipe's hand-tracking model to detect and interpret gestures based on the positions of finger landmarks.
Toggle Light/Dark Mode: Switches Windows system mode between light and dark themes, depending on hand gestures. 
When the thumb is above the index finger, it triggers light mode; otherwise, it switches to dark mode.

**How It Works**

The program captures hand landmarks through the webcam and detects gestures based on the thumb and index finger's relative positions.
If the thumb is positioned above the index finger, Windows light mode is activated.
If the thumb is positioned below the index finger, Windows dark mode is activated.
This is achieved by modifying a Windows registry setting that controls the system's theme.


**2.Hand Gesture-Based Screenshot Capture**(screenshot.py)

This project uses OpenCV and MediaPipe to capture screenshots with a simple open-palm gesture. It provides an intuitive way to take screenshots without needing to press any buttons, enhancing the user experience during presentations, gaming, or other activities where hands-free operation is beneficial.

**Features**

Hand Gesture Detection: Utilizes MediaPipe's hand-tracking model to detect hand gestures in real-time using a webcam.
Screenshot Capture: Takes a screenshot whenever an open palm gesture is detected, making it easy to capture moments without interrupting workflow.

**How It Works**

The program captures frames from the webcam and processes them to detect hand landmarks.
An open palm gesture is detected when the base of the index finger is above the bases of the other fingers.
When the open palm gesture is recognized, a screenshot is taken and saved with a timestamp.
