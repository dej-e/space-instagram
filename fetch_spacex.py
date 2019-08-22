from dotenv import load_dotenv
import requests
import os

def get_spacex_images(url):
    response = requests.get(url)
    if response.ok:
        return response.json()['links']['flickr_images']
    return None

def fetch_spacex_last_launch(spacex_api_url, image_dir):
    image_links = get_spacex_images(url=spacex_api_url)
    os.makedirs(image_dir, exist_ok=True)

    for image_number, image_url in enumerate(image_links):
        ext = image_url.split('.')[-1]
        response = requests.get(image_url)
        response.raise_for_status()
        image_filename = f'image{image_number}.{ext}'
        images_path = os.path.join(image_dir,image_filename)
        with open(images_path, 'wb') as file:
            file.write(response.content)


if __name__ == '__main__':
    load_dotenv()
    spacex_api_url = 'https://api.spacexdata.com/v3/launches/latest'
    image_dir = os.getenv('IMAGE_DIR')
    try:
        fetch_spacex_last_launch(spacex_api_url, image_dir=image_dir)
    except requests.exceptions.HTTPError as error:
        print(error)
        exit(2)
