# Birthday Wish

This is a simple Django application which will send email to the customer on their birthday

## Overview

On customer birthday the system will automatically send email to customer email. 
`Django Rest Framework` is used for building api. With api customer info will be store on database and
a schedule will be created on customer birthday to send him/her a birthday wish. 

`CELERY` is used for handling schedule/asynchronous job using `redis` as message broker. 

## Prerequisites

To get started with this application, you will need to have the following
technologies installed on your local machine:

- [python3.9](https://www.python.org/downloads/release/python-390/) (Mandatory)
- [redis](https://redis.io/) (Mandatory)
- [postgresql](https://www.postgresql.org/) (Not Mandatory)
- [Docker](https://www.docker.com/) (Not Mandatory)
- [Docker Compose](https://docs.docker.com/compose/) (Not Mandatory)


## Installation

#### Cloning the project

```
https://github.com/aninda052/birthday_wish.git
cd birthday_wish
```

#### creating `.env` file

Create a `.env` file for your environment variable.

```
 touch .env
```

You can find the details of all the variables in `.env.example` file.
For running the project just copy billow dummy information and past it to your .env file and save it.

```
DEBUG=True
SECRET_KEY=xy+y*vn5(^^&qp-q5zx@-^@o+v%sw)$y9)o1zskb4y*0khdnaa

CELERY_BROKER_URL=redis://localhost:6379
CELERY_RESULT_BACKEND=redis://localhost:6379

DATABASE=sqlite
```

### Running The project 

You can run the project in 2 ways

- ####  Using `runserver`  command

<pre>

# create a virtual environment using <a href="https://virtualenv.pypa.io/en/latest/installation.html">virtualenv</a>
virtualenv -p python3 venv

# Activate virtual environment
source venv/bin/activate

# Install all required python packages
pip install -r requirements.txt

# generate database migration files
python manage.py makemigrations

# migrate new changes on database
python manage.py migrate --no-input

# create initial superuser
DJANGO_SUPERUSER_PASSWORD=admin DJANGO_SUPERUSER_USERNAME=admin DJANGO_SUPERUSER_EMAIL=admin@email.com python manage.py createsuperuser --noinput

# run user server at port 8000
python manage.py runserver 8000

</pre>


- #### Using `docker-compose`

To run the project using `docker-compose`; `docker` and `docker-compose` must be installed on your system. 
For installation instructions refer to the Docker [docs](https://docs.docker.com/compose/install/).

After you installing `docker` and `docker-compose` properly, run -

```
docker-compose up --build
```

If everything went well, go to `http://127.0.0.1:8000` and you'll find the project up and running.

## Api

To add a customer use billow end point with `POST` request -

```
http://localhost:8000/api/add-customer/
```
Note: `Django REST framework` provide [self describing APIs](https://www.django-rest-framework.org/topics/documenting-your-api/#self-describing-apis).
So you can just hit the above endpoint from your browser and get the documentation.

##### Request Body

```
{
    "email" : "customer_email@email.com",
    "date_of_birth": "YYYY-MM-DD",
    "first_name": "customer_first_name",
    "last_name": "customer_last_name"
}
```
