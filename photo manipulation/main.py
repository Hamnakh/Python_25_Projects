from PIL import Image, ImageEnhance, ImageFilter
import numpy as np
import os

class PhotoManipulator:
    def __init__(self, image_path):
        self.image = Image.open(image_path)
        self.original_image = self.image.copy()
        
    def adjust_brightness(self, factor):
        """Adjust the brightness of the image.
        factor > 1 increases brightness
        factor < 1 decreases brightness"""
        enhancer = ImageEnhance.Brightness(self.image)
        self.image = enhancer.enhance(factor)
        return self
        
    def adjust_contrast(self, factor):
        """Adjust the contrast of the image.
        factor > 1 increases contrast
        factor < 1 decreases contrast"""
        enhancer = ImageEnhance.Contrast(self.image)
        self.image = enhancer.enhance(factor)
        return self
        
    def apply_blur(self, radius=2):
        """Apply Gaussian blur to the image"""
        self.image = self.image.filter(ImageFilter.GaussianBlur(radius))
        return self
        
    def apply_sharpness(self, factor):
        """Adjust the sharpness of the image.
        factor > 1 increases sharpness
        factor < 1 decreases sharpness"""
        enhancer = ImageEnhance.Sharpness(self.image)
        self.image = enhancer.enhance(factor)
        return self
        
    def reset(self):
        """Reset the image to its original state"""
        self.image = self.original_image.copy()
        return self
        
    def save(self, output_path):
        """Save the modified image"""
        self.image.save(output_path)
        
    def show(self):
        """Display the image"""
        self.image.show()

def main():
    # Example usage
    try:
        # Create output directory if it doesn't exist
        if not os.path.exists('outputs'):
            os.makedirs('outputs')
            
        # Example: Load an image and apply various effects
        manipulator = PhotoManipulator('input.jpg')
        
        # Apply effects
        manipulator.adjust_brightness(1.5)  # Increase brightness
        manipulator.adjust_contrast(1.2)    # Increase contrast
        manipulator.apply_blur(2)           # Apply blur
        manipulator.save('outputs/modified.jpg')
        
        # Reset and apply different effects
        manipulator.reset()
        manipulator.adjust_brightness(0.8)  # Decrease brightness
        manipulator.adjust_contrast(0.9)    # Decrease contrast
        manipulator.apply_sharpness(2)      # Increase sharpness
        manipulator.save('outputs/modified2.jpg')
        
        print("Image processing completed successfully!")
        
    except FileNotFoundError:
        print("Error: Input image not found. Please make sure 'input.jpg' exists in the current directory.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
