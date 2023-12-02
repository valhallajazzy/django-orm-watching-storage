# Пульт охраны банка

Это внутренний репозиторий для сотрудников банка "Сияние". Если вы попали в этот репозиторий
случайно, то вы не сможете его запустить, т.к. у вас нет доступа к БД, но можете свободно
использовать код верстки или посмотреть как реализованы запросы к БД.

Пульт охраны - это сайт, который можно подключить к удаленной базе данных с визитами и карточками
пропуска сотрудников нашего банка.

## Установка и запуск

* Скачайте код
* Установите зависимости в корневой директории проекта и активируйте их
```console
$ poetry install
$ poetry shell
```
* Создайте файл .env в корневой директории проекта и задайте переменные окружения

![Screenshot](https://github.com/valhallajazzy/django-orm-watching-storage/blob/main/Pictures/env_path.png)
![Screenshot](https://github.com/valhallajazzy/django-orm-watching-storage/blob/main/Pictures/values_environ.png)

Подробнее о переменных окружения:

SECRET_KEY - Секретный ключ Django используется для обеспечения криптографической подписи. Этот ключ в основном используется для подписи файлов cookie сеанса. Если бы у кого-то был этот ключ, он смог бы изменить файлы cookie, отправленные приложением.

ALLOWED_HOSTS - Список строк, представляющих имена хостов/доменов, которые может обслуживать этот сайт Django.

DB_ENGINE - Используемая база данных. Вы можете использовать серверную часть базы данных, которая не поставляется с Django, указав ENGINEполный путь (т. е mypackage.backends.whatever. ).

DB_HOST - Какой хост использовать при подключении к базе данных. Пустая строка означает локальный хост. Не используется с SQLite.

DB_PORT - Порт, который будет использоваться при подключении к базе данных. Пустая строка означает порт по умолчанию. Не используется с SQLite.

DB_NAME - Имя базы данных, которую нужно использовать. Для SQLite это полный путь к файлу базы данных. При указании пути всегда используйте косую черту, даже в Windows (например, C:/homes/user/mysite/sqlite3.db).

DB_USER - Имя пользователя, которое будет использоваться при подключении к базе данных. Не используется с SQLite.

DB_PASSWORD - Пароль, который будет использоваться при подключении к базе данных. Не используется с SQLite.

DEBUG - Логическое значение, которое включает/выключает режим отладки. Если ваше приложение выдает исключение, когда DEBUG имеет значение True, Django отобразит подробную обратную трассировку, включая множество метаданных о вашей среде, например все определенные на данный момент настройки Django (из settings.py).

* Из корневой папки проекта запустите сервер командой
```console
$ python manage.py runserver
```
