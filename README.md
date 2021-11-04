# Приложение "Tractor"

Приложение "Tractor" - это доска объявлений для владельцев грузового транспорта и спецтехники. Любой человек может 
зарегистрироваться в приложении и выставлять объявления аренды своей техники, а так же просматривать и подавать заявки 
на объявления других пользователей. 

Преимущества данного приложения в его простате. Например:
1) Если техника занята, то вы видите это и не тратите время на звонки.
2) Вы можете заранее подавать заявки предложив свою цену оплаты, таким образом заранее подготовив исполнителя.
3) Если Вам необходимо нескольколько видов техники, вы можете посмотреть список пользователей с имеющейся у них 
техникой и найти одного человека для этого, а так же предложив свою цену можете хорошо сэкономить.
4) Если вы владелец техники, то вы можете заранее договориться с заказчиками с помощью полученных заявок, таким образом 
составить расписание работ на перед.

**Для того чтобы запустить проект Вам необходимо выполнить следующие действия :**

*Установка зависимостей*
1) sudo apt-get install libjpeg-dev zlib1g-dev - для работы с картинками
2) virtualenv/venv - виртуальное окружение

*Запускаем виртуальное окружение*
3) . venv/bin/activate

*Устанавливаем Django*

4) pip install Django==3.2

*Устанавливаем необходимые библиотеки*

5) pip install Pillow - для работы с картинками
6) pip install django-crispy-forms - для работы с формами
7) pip install crispy-bootstrap5 - для работы с фреймворком bootstrap5
8) pip install python-form - для работы с формами

*Либо устанавливаем все с помощью файла requirements.txt*

9) pip install -r requirements.txt

*Применяем миграции*

10) python manage.py migrate

*Скачиваем фикстуры*

11) python manage.py loaddata fixtures/dump.json
12) python manage.py loaddata fixtures/auth_dump.json

*Запускаем проект*

13) python manage.py runserver

**Пароли пользователей: Ss123456**