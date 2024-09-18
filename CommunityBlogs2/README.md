# CommunityBlogs

## Description

## Preparation

```bash
  
    # create venv
    conda create --name web python=3 -y
    conda activate web
    
    # install packages
    sudo apt install -y mongodb
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
