import requests
from bs4 import BeautifulSoup

def get_github_profile_image():
    github_input = input("Enter GitHub profile URL or username (e.g., https://github.com/username or just username): ").strip()

    # Automatically build full URL if only username is given
    if not github_input.startswith("http"):
        github_url = f"https://github.com/{github_input}"
    else:
        github_url = github_input

    try:
        response = requests.get(github_url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        profile_image = soup.find('img', {'class': 'avatar-user'})

        if profile_image:
            image_url = profile_image.get('src')
            print(f"\n✅ Profile Image URL: {image_url}")
        else:
            print("⚠️ Profile image not found. Please check the username or URL.")

    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    print("GitHub Profile Image Scraper")
    print("---------------------------")
    get_github_profile_image()
