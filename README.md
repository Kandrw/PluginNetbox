 



# Расширение функциональности Netbox

## Цель кейса:
    С помощью plugin и/или доработки основного кода Netbox необходимо
    добавить функциональность хранения и отображение в Netbox информации о
    кабельном хозяйстве оптической сети.



### Задание 1. 
    Добавить в систему сущности - сплайс-пластина, муфта (со
    схемой разварки), в сущность кабель - добавить понятие модуль, волокно.
    Примерное ТЗ на эту функциональность можно прочитать тут:
    https://web.archive.org/web/20240417191117/https://plugin-
    ideas.netbox.dev/ideas/PLUGINS-I-35 Схему разварки муфт — реализовать в
    графическом виде.
### Задание 2. 
    Добавить возможность к сущности кабель —
    добавить/загрузить трассу его прохождения в формате GeoJSON и
    отображать в GUI карту с размещенными на ней кабелями/муфтами/колодцами.
### Задание 3.
    Добавить отдельную сущность оптическая трасса — которая
    собирается из разных волокон разных кабелей, на промежуточных кроссах
    выполняются кроссировки.





Запуск через docker-compose

    Build: ./run.sh -c
    Start: ./run.sh -r
    Stop: ./run.sh -d

Запуск через виртуальные окружения

    Установка компонентов

        sudo apt update
        sudo apt install -y python3 python3-venv python3-pip git
        sudo apt install redis-server
        sudo systemctl start redis-server
        python3 -m venv venv
        source venv/bin/activate
        cd netbox
        pip install -r requirements.txt
        cp netbox/netbox/configuration_example.py netbox/netbox/configuration.py

        python netbox/generate_secret_key.py
            Добавить ключ в SECRET_KEY в файле netbox/netbox/configuration.py

        sudo -u postgres psql
        CREATE DATABASE netbox;
        CREATE USER netbox_user WITH PASSWORD '12345678';
        GRANT ALL PRIVILEGES ON DATABASE netbox TO netbox_user;
        \q

        python3 netbox/manage.py createsuperuser
        python3 netbox/manage.py migrate
    Запуск

        python3 netbox/manage.py runserver



