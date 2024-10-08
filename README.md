Описание проекта
Проект на фреймворке Django 4.2, база данных — PostgreSQL. Сайт предназначен для продажи мебели, с возможностью регистрации и входа в учетную запись. Реализован каталог товаров с различными фильтрами: по категориям, по возрастанию/убыванию цены, товары по акции. Также имеется корзина покупателя, в которой можно изменять количество товаров и видеть общую стоимость. Из корзины можно перейти к форме для оформления заказа (в форме есть поля для реквизитов, способа оплаты, контактных данных и т.д.). История заказов доступна в профиле пользователя. Также реализована удобная админ-панель для отслеживания заказов и редактирования товаров.
Для запуска проекта:
1) Создайте виртуальное окружение для установки зависимостей python версии 3.12.1: "python -m venv venv"
2) Активируйте виртуальное окружение: "venv\Scripts\activate" (для Windows) или же source "venv/bin/activate" (для macOS/Linux)
3) Установите зависимости проекта, указанные в файле requirements.txt: "pip install -r requirements.txt"
4) Создайте базу данных в PostgreSQL (или используйте другую конфигурацию базы данных, если необходимо).
   Обновите настройки базы данных в файле settings.py:
  "DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}"
5) Используйте следующие команды для загрузки фикстур:
"python manage.py loaddata fixtures/goods/categories.json"
"python manage.py loaddata fixtures/goods/products.json"
6) Миграции: python manage.py migrate
7) Создайте суперпользователя для доступа к админ-панели: "python manage.py createsuperuser"
8) Запустите сервер разработки Django: "python manage.py runserver"
