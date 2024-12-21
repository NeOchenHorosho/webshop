# WEBSHOP

Мощнейший open-source инструмент на основе которого можно построить практически любой веб-магазин.
 Отличительной чертой данного проекта является невероятная адаптируемость и возможность для расширения и изменения функционала без необходимости прохождения сложного и дорогого процесса рефакторинга
## Инструкция по установке и запуску  
Скачиваете проект, устанваливаете необходимые библиотеки (см. requirements.txt), через терминал запускаете сервер следующей командой: "py manage.py runserver"  
Далее, переходите по следующему адресу: http://127.0.0.1:8000/admin  
По умолчанию для ознакомления установлены superuser с именем frog и паролем 1111 и прочие элементы базы базы данных.  
В данном окне администрации вы можете управлять пользователями, корзинами, продуктами и заказами.  
## Архитектура
Данный бек-энд составляющая данного сайта основывается на следующих django-приложениях:    
**CART**  
Содержит в себе модели Cart, CartItem  
**ORDERS**  
Содержит в себе модели Order, OrderItem  
**PRODUCT**  
Содержит в себе модель Product  
**USERS**  
Содержит в себе модели CustomUser (он наследуется от AbdstractUser и я вставил бесполезное поле Balance вместо ключевого слова pass, потому что я не знал, как себя в таком случае поведёт django)  

## Технологии
- Backend:
  - Python 3.x
  - Django
- Frontend:
  - HTML5, CSS3
  - Новейший Bootstrap 5
- База данных:
  - SQLite
- Дополнительно:
  - Git для контроля версий
## Примечания
Очень красивая и удобная панель администрирования