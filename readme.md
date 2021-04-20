# Poketch! Pokedex and more
Simple Pokedex utility written in Django.

## How to install?
The easiest way to use Poketch is to run it in a Docker container.

To install Poketch in Docker container:
1. Clone this repository with `git clone https://github.com/deru303/poketch`
2. Edit the *poketch/settings.py* file and type your server IP address in ALLOWED_HOSTS array.
3. Run `docker-compose up` and wait until containers are ready.
4. Run `docker exec -it poketch_web_1 /bin/bash`. This will connect you to the Django container shell.
5. In Django container shell, run `python manage.py makemigrations && python manage.py migrate`.
6. Use phpmyadmin *(localhost:6050)* and import *poketch_db.sql* from https://github.com/deru303/pokemon-databases
7. Restart your containers `docker-compose down && docker-compose up -d`. Everything should be working now!

## How to use?
Just type localhost:6050 in your browser URL bar.

## How to backup my Pokemon data?
You can use phpmyadmin and export database file.
To open phpmyadmin, type localhost:5050 in your browser URL bar.