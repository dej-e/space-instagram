#Космический Инстаграм

Скрипты для загрузки изображений из SpaceX и Hubble, с последующей публикацией в Instagram 


#Как установить

Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть есть конфликт с Python2) для установки зависимостей:

pip install -r requirements.txt

Для работы скрипта необходимо зарегистрироваться в Instagram.
 
Если у вас нет аккаута в Instagram, создайте его.

После клонирования проекта создайте в корень файл .env с таким содержимым:

IMAGES_DIR=images
HUBBLE_COLLECTION=spacecraft 
INSTAGRAM_DIR=instagram
INSTAGRAM_LOGIN=_your instagram username_
INSTAGRAM_PASSWORD=_your instagram password_

Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков dvmn.org.