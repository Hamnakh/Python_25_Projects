# Bulk File Renamer

A simple and user-friendly application to rename multiple files in a directory at once.

## Features

- Select any folder on your computer
- Add prefix and suffix to file names
- Set starting number for sequential renaming
- Preserves file extensions
- User-friendly GUI interface

## Requirements

- Python 3.x
- tkinter (usually comes with Python installation)

## How to Use

1. Run the `bulk_renamer.py` script
2. Click "Browse" to select the folder containing files you want to rename
3. Enter the desired prefix (optional)
4. Enter the desired suffix (optional)
5. Set the starting number for sequential renaming
6. Click "Rename Files" to start the renaming process

## Example

If you have files named:
- image1.jpg
- image2.jpg
- image3.jpg

And you set:
- Prefix: "vacation_"
- Suffix: "_2024"
- Start Number: 1

The files will be renamed to:
- vacation_1_2024.jpg
- vacation_2_2024.jpg
- vacation_3_2024.jpg

## Note

- The application will preserve the original file extensions
- Files are renamed in alphabetical order
- Make sure you have write permissions for the selected folder 