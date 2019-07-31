from dotenv import load_dotenv
import os
from instabot import Bot
from os import listdir


def get_images_from_directory(image_dir):
    image_extension = ('.jpg', '.jpeg', '.tiff', '.tif', '.png')
    return [os.path.join(image_dir, image) for image in
            listdir(image_dir) if image.endswith(image_extension)]


if __name__ == '__main__':
    load_dotenv()
    username = os.getenv('INSTAGRAM_LOGIN')
    password = os.getenv('INSTAGRAM_PASSWORD')
    image_dir = os.getenv('IMAGE_DIR')
    instagram_dir = os.getenv('INSTAGRAM_DIR')

    if not os.path.exists(instagram_dir):
        os.makedirs(instagram_dir)

    bot = Bot(base_path=instagram_dir)
    bot.login(username=username, password=password)
    images = get_images_from_directory(image_dir=image_dir)
    try:
        for image in images:
            bot.upload_photo(image, caption='')
            if bot.api.last_response.status_code != 200:
                print(bot.api.last_response)
    except Exception as error:
        print(str(error))

    bot.logout()