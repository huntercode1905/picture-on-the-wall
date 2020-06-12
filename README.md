# Picture on the Wall

A stock photo website built with Django and the CSS Framework Bootstrap

Check out the site here: https://picture-on-the-wall.herokuapp.com/home/

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development. 

### Installing

A step by step series of examples that tell you how to get a development env running. Download the picture-on-the-wall folder then:

Installing Django and 3rd party packages

```
cd picture-on-the-wall
pipenv install django
pipenv shell
pip install Pillow
pip install whitenoise
```

Run the project on your local machine

```
python manage.py migrate
python manage.py runserver
```

## Built With

* [Django](https://www.djangoproject.com/) - The Web framework used
* [Pillow](https://pillow.readthedocs.io/en/stable/) - The Python Imaging Library
* [Bootstrap](https://getbootstrap.com/) - The CSS framework used

