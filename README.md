# Airport-API-Service
Api service for tracking flights written on DRF

# Installing using GitHub
Install PostgresSQL and create db

git clone https://github.com/vshvanska/airport-api-service
cd cinema_API
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
create .env file, inside:
- set DB_HOST=<your db hostname>
- set DB_NAME=<your db name>
- set DB_USER=<your db username>
- set DB_PASSWORD=<your db user password>
- set SECRET_KEY=<your secret key>

python manage.py migrate
python manage.py runserver

# Run with docker
Docker should be installed

docker-compose build
docker-compose up

# Getting access
create user via /api/user/register/
get access token via /api/user/token/