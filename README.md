## BriteCore django app

### Technologies

* Python 3.4
* Django
* Django REST Framework
* PostgreSQL
* AWS Elasticbeanstalk


### Installation guide

* Prepare database

```bash
docker run --name postgres -e POSTGRES_PASSWORD=manager -p 5432:5432 -d postgres:9.6.
psql -h localhost -U postgres -c "create user britecore with password 'britecore'"
psql -h localhost -U postgres -c "create database britecore with owner britecore"
```

* Prepare virtual environment

```bash
virtualenv venv -p 3.4
source venv/bin/activate
pip3 install -r requirements.txt
```

* Run 

```bash
python manage.py migrate --noinput
python manage.py collectstatic --noinput
python manage.py runserver 127.0.0.1 8000
```

### Running tests

```bash
python manage.py test
```
