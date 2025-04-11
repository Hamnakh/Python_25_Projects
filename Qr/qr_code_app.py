import qrcode
from PIL import Image
from pyzbar.pyzbar import decode
import os

def generate_qr_code(data, filename="qr_code.png"):
    """Generate a QR code from the given data and save it as an image."""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    qr_image = qr.make_image(fill_color="black", back_color="white")
    qr_image.save(filename)
    print(f"QR code has been generated and saved as {filename}")

def decode_qr_code(image_path):
    """Decode a QR code from an image file."""
    try:
        image = Image.open(image_path)
        decoded_objects = decode(image)
        
        if not decoded_objects:
            print("No QR code found in the image.")
            return
        
        for obj in decoded_objects:
            print(f"Decoded data: {obj.data.decode('utf-8')}")
    except Exception as e:
        print(f"Error decoding QR code: {str(e)}")

def main():
    while True:
        print("\nQR Code Generator and Decoder")
        print("1. Generate QR Code")
        print("2. Decode QR Code")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ")
        
        if choice == "1":
            data = input("Enter the data to encode in QR code: ")
            filename = input("Enter the filename to save the QR code (default: qr_code.png): ")
            if not filename:
                filename = "qr_code.png"
            if not filename.endswith('.png'):
                filename += '.png'
            generate_qr_code(data, filename)
            
        elif choice == "2":
            image_path = input("Enter the path to the QR code image: ")
            if os.path.exists(image_path):
                decode_qr_code(image_path)
            else:
                print("File not found. Please check the path and try again.")
                
        elif choice == "3":
            print("Thank you for using the QR Code Generator and Decoder!")
            break
            
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main() 