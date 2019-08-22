from dotenv import load_dotenv
from urllib.parse import urlparse, urljoin
import requests
import os


def download_file(url, filename):
    image_dir = os.getenv('IMAGE_DIR')
    os.makedirs(image_dir, exist_ok=True)

    response = requests.get(url, verify=False)
    response.raise_for_status()
    save_path = os.path.join(image_dir, filename)
    with open(save_path, 'wb') as file:
        file.write(response.content)


def fetch_image_from_hubble(image_id):
    hubble_image_url = 'http://hubblesite.org/api/v3/image/{}'.format(image_id)
    response = requests.get(url=hubble_image_url)
    response.raise_for_status()
    image_link = response.json()['image_files'][-1]['file_url']

    file_ext = get_file_extension(image_link)
    image_filename = '.'.join([str(image_id), file_ext])
    parsed_url = urlparse(image_link)
    if not parsed_url.scheme:
        image_url = urljoin('http://', image_link)
    else:
        image_url = image_link

    download_file(url=image_url, filename=image_filename)


def fetch_images_from_hubble_collection(collection_name):
    hubble_collection_url = 'http://hubblesite.org/api/v3/images' \
        .format(collection_name)
    payload = {
        'collection_name': collection_name,
        'page': 'all'
    }

    response = requests.get(url=hubble_collection_url,
                            params=payload, verify=False)
    response.raise_for_status()
    image_links = response.json()

    for image_link in image_links:
        image_id = image_link['id']
        fetch_image_from_hubble(image_id=image_id)


def get_file_extension(filename):
    return filename.split('.')[-1]


if __name__ == '__main__':
    load_dotenv()
    collection_name = os.getenv('HUBBLE_COLLECTION')
    try:
        fetch_images_from_hubble_collection(collection_name=collection_name)
    except requests.exceptions.HTTPError as error:
        print(error)
        exit(2)
