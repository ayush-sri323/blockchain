# blockchain-be

Prerequisite:
1.Install mysql 8.0.28 with user `root` and password as `password`
2. mysql> create database be_blockchain;


Steps
1. python3 -m .venv
2. source .venv/bin/activate
3. pip3 install -r requirements.txt 
4. ./manage.py makemigrations
5. ./manage.py migrate
6. ./manage.py createsuperuser 
7. ./manage.py runserver
