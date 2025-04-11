# Photo Manipulation Project

This project allows you to manipulate images by adjusting brightness, contrast, applying blur effects, and more using Python.

## Requirements
- Python 3.x
- Pillow (PIL)
- numpy

## Installation
1. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage
1. Place your input image in the project directory and name it `input.jpg`
2. Run the script:
```bash
python main.py
```
3. The modified images will be saved in the `outputs` directory

## Features
- Adjust brightness
- Adjust contrast
- Apply blur effects
- Adjust sharpness
- Reset to original image
- Save modified images

## Example
```python
# Create a PhotoManipulator instance
manipulator = PhotoManipulator('input.jpg')

# Increase brightness
manipulator.adjust_brightness(1.5)

# Increase contrast
manipulator.adjust_contrast(1.2)

# Apply blur
manipulator.apply_blur(2)

# Save the modified image
manipulator.save('outputs/modified.jpg')
```

## Notes
- Brightness factor > 1 increases brightness, < 1 decreases brightness
- Contrast factor > 1 increases contrast, < 1 decreases contrast
- Blur radius determines the intensity of the blur effect
- Sharpness factor > 1 increases sharpness, < 1 decreases sharpness 