# Smart Parking System with OpenCV

This project implements a Smart Parking System using OpenCV, designed to detect available parking spaces in images or video streams.

![Alt Text](https://im3.ezgif.com/tmp/ezgif-3-a5ae0b51f6.gif)

## Project Overview

The system consists of three Python files:

- `rectanglepoints.py`: Obtains accurate coordinates for the initial parking space.
- `label_cars.py`: Labels all cars within the image or video.
- `main.py`: Contains the complete Smart Parking System implementation.

## Usage

1. **Obtaining Initial Coordinates:**
   - Run `rectanglepoints.py` to acquire precise coordinates for the initial parking space. This step is crucial for accurate parking space detection.

2. **Labeling Cars:**
   - Utilize `label_cars.py` to label cars present in the image or video. This aids in the detection process.

3. **System Implementation:**
   - Execute `main.py` to initiate the complete Smart Parking System. This integrates coordinate acquisition and car labeling for parking space detection.

## Accuracy Considerations

For optimal accuracy:
- Maintain a stable camera position without movement for improved detection precision.
- Adequate lighting conditions can significantly enhance detection accuracy.

## Requirements

- cvzone
- OpenCV
- numpy
- pickle 

## Contribution

Feel free to contribute, provide feedback, or suggest enhancements to improve the system's accuracy and efficiency.

<!-- Additional instructions, troubleshooting, or usage examples can be added here -->
