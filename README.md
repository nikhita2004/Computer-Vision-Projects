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
