<img width="1901" height="920" alt="image" src="https://github.com/user-attachments/assets/784e920a-38c1-4bff-848a-40313cb5f2ad" />
<img width="1899" height="924" alt="image" src="https://github.com/user-attachments/assets/6a8f05b4-a515-4bc2-b94d-30cdf95de2de" />

Веб-сайт для кальян-бара, разработанный на Django. Сайт включает в себя главную страницу, меню, новости, информацию о локациях и отзывы клиентов.

# 🚀 Функциональность
- Главная страница - Приветственная страница с краткой информацией о баре и последними новостями
- Меню - Страница с категориями и позициями меню
- Новости - Лента новостей заведения
- Локации - Информация о адресах, телефонах и часах работы
- Отзывы - Страница с отзывами клиентов и формой для добавления нового отзыва

# 🛠 Технологии
- Backend: Django 4.2+
- Frontend: HTML5, CSS3
- База данных: SQLite (по умолчанию)
- Стили: Встроенный CSS с темной темой и бронзовыми акцентами

# 📦 Установка и запуск
```
pip install django
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

# 📝 Модели данных
- MenuCategory - Категории меню
- MenuItem - Позиции меню
- News - Новости заведения
- Location - Локации баров
- Review - Отзывы клиентов
