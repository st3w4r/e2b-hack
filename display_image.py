import requests
from PIL import Image
from io import BytesIO

def display_image_from_url(screenshot_url):
    # Fetch the image from the URL
    response = requests.get(screenshot_url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Open the image using PIL
        image = Image.open(BytesIO(response.content))
        
        # Display the image
        image.show()
    else:
        print("Failed to retrieve image. Status code:", response.status_code)

if __name__ == "__main__":
    # Example usage
    screenshot_url = 'https://example.com/path/to/your/image.png'
    display_image_from_url(screenshot_url)