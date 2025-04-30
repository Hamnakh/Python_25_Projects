# GitHub Profile Image Scraper

A simple Python web scraping tool that extracts profile image URLs from GitHub user profiles.

## Features

- Takes a GitHub profile URL as input
- Extracts and displays the profile image URL
- Handles errors gracefully
- Works with public GitHub profiles

## Prerequisites

- Python 3.x
- pip (Python package installer)

## Installation

1. Clone or download this repository
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the script:
   ```bash
   python github_profile_scraper.py
   ```

2. When prompted, enter a GitHub profile URL in the format:
   ```
   https://github.com/username
   ```

3. The program will output the direct URL to the profile image

## Example

```
GitHub Profile Image Scraper
---------------------------
Enter GitHub profile URL (e.g., https://github.com/username): https://github.com/octocat

Profile Image URL: https://avatars.githubusercontent.com/u/583231?v=4
```

## Dependencies

- requests==2.31.0
- beautifulsoup4==4.12.2

## Notes

- This tool only works with public GitHub profiles
- The profile image URL can be used to view or download the image
- Make sure to enter the complete GitHub profile URL

## Error Handling

The program handles various error cases:
- Invalid URLs
- Network connectivity issues
- Non-existent profiles
- Private profiles

## License

This project is open source and available for personal and educational use. 