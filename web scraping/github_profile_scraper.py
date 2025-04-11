import requests
from bs4 import BeautifulSoup

def get_github_profile_image():
    # Ask for GitHub profile URL
    github_url = input("Enter GitHub profile URL (e.g., https://github.com/username): ")
    
    try:
        # Send GET request to the GitHub profile
        response = requests.get(github_url)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find the profile image
        # The profile image is usually in an img tag with class 'avatar'
        profile_image = soup.find('img', {'class': 'avatar'})
        
        if profile_image:
            # Get the src attribute which contains the image URL
            image_url = profile_image.get('src')
            print(f"\nProfile Image URL: {image_url}")
        else:
            print("Profile image not found. Please check the URL and try again.")
            
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    print("GitHub Profile Image Scraper")
    print("---------------------------")
    get_github_profile_image() 