# CommunityBlogs

## Description


## Preparation

```bash
  
    # create venv (if needed)
    conda create --name web python=3 -y
    conda activate web
    
    # install packages
    pip3 install -r requirements.txt
    
    # prepare django app
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
    python manage_insert_sample_posts.py
    

```

## Run the app

```bash
    python manage.py runserver
```


## Django Tech Introduction

`django-admin` create a dir containing some django project base files.
The entry is `./manage.py` and we use `python manage.py ...` to control the django operations.

Django is be default associated with a SQL database. To start the django web correctly,
we need first migrate our data models into this SQL database. (p.s the database is set with `./project/settings.py`)

The router of the whole django app is defined in `./project/urls.py`. 
Some urls directly leads to a **View** (A function: request -> rendered page):

```python
    # in ./project/urls.py
    path("register/", user_views.register, name="register"),

```
Some urls are grouped in sub-app. The views are included from developer created sub-app folder:

```python
    
    # in ./project/urls.py
    path('sub_app_name/', include('sub_app.urls')),
    
    # in ./sub_app/urls.py, there are sub-url accessed by, for example, sub_app_name/home
    path('', views.home, name="sub-app-home"),
    path('about', views.about, name="sub-app-about"),

```

A **View** is a function take request as input and output a rendered page. Often we use `django.shortcuts.render` to
render a HTML, and we control the HTML using Django Template Language(DTL), i.e. the `{% %}`.`

The benefits of Django is that it contains useful pre-implemented views (eg. admin.site.urls), 
pre-implemented components(eg. UserCreationForm), and easy to implement data models (using `django.db.models.xxxField`)
And it handles some typical data based interactions for you (eg. user registration/login)