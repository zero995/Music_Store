# Music_Store
this is a little REST API with admin page for admin a Online Music Store

This project was developed using Fedora 29 and Python 3.7

requirements python-virtualenv

run this commands for start
git clone https://github.com/zero995/Music_Store.git

cd Music_Store

python3 -m venv venv

. venv/bin/activate

pip install -r reqs.txt


python manage.py makemigrations

python migrate

create a super user for django

python manage.py createsuperuser

test app

python manage.py test

for email configuration you need edit
Music_Store/api/settings.py
at the end you can put your smtp configurations by defuault is configurated for gmail


for make a scheduled task for low stock


add this line at the end of 

crontab -e

0 0 0,6 ? * MON * [path of installation]/venv/bin/python [path of installation]/manage.py refill_warn



endpoints:

api/register/   method POST params  email, name this endpoint is used for register a new user and deliver an api key by mail
api/list/   method GET params  genere(optional) you can filter the albums list by genere if the genere param is missing show all albums
/admin you can add artists. albums, and generes using web interface
