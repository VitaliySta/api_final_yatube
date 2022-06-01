### API для Yatube  
#### Описание: API социальной сети для публикации постов.  
#### Основные технологии  
Python 3.7    
Django 2.2.16   
#### Запуск проекта в dev-режиме:
 - Клонируйте проект с помощью git clone или скачайте ZIP-архив.  
 - Установите и активируйте виртуальное окружение    
``` python -m venv venv ```  
 - Установите зависимости из файла requirements.txt    
``` pip install -r requirements.txt ```  
 - Сделайте миграции    
``` python manage.py makemigrations ```
 ``` python manage.py migrate ```  
 - В папке с файлом manage.py выполните команду:    
``` python manage.py runserver ```  
### В проекте есть следующие эндпоинты:
 - /api/v1/posts/ - посты
 - /api/v1/posts/{post_id}/comments/ - комментарии
 - /api/v1/groups/ - группы
 - /api/v1/follow/ - подписчики


 **Аутентификация в проекте настроена по JWT-токену**
 
**Автор** 
Стацюк В.Н.
