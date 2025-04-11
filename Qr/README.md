
# QR Code Generator and Decoder

This is a simple Python application that allows you to generate QR codes from text data and decode information from existing QR code images.

## Features

- Generate QR codes from text input
- Decode information from QR code images
- Simple command-line interface
- Error handling for invalid inputs

## Requirements

- Python 3.6 or higher
- Required Python packages (install using `pip install -r requirements.txt`):
  - qrcode
  - Pillow
  - pyzbar

## Installation

1. Clone this repository or download the files
2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

Run the program using:
```
python qr_code_app.py
```

The program will present you with a menu where you can:
1. Generate a new QR code
2. Decode an existing QR code
3. Exit the program

### Generating QR Codes
- Choose option 1
- Enter the text you want to encode
- Specify a filename for the QR code image (optional)

### Decoding QR Codes
- Choose option 2
- Enter the path to the QR code image file
- The program will display the decoded information

## Note

For decoding QR codes, make sure you have the `zbar` library installed on your system:
- Windows: Download and install from [zbar releases](https://github.com/NaturalHistoryMuseum/ZBar/releases)
- Linux: `sudo apt-get install libzbar0`
- macOS: `brew install zbar` 