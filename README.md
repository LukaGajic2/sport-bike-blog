# SPORT BIKE BLOG

## Table of Contents

## Technologies Used

### Main Languages Used:

-HTML5
-CSS3
-Python
-Django

### Libraries, Frameworks and Programs:

-CodeAnywhere - IDE to create my html files & styling sheet before pushing the project to Github.
-GitHub - to store my repository.
-Django
-Bootstrap
-Font Awesome - to add icons to the social links in the footer element.
-Am I Responsive? - to ensure the project looked good across all devices.

### Installed Packages

- 'django' gunicorn
- dj_database_url psycopg2
- dj3-cloudinary-storage
- django-summernote [(link)](https://summernote.org/)
- django-allauth [(link)](https://django-allauth.readthedocs.io/en/latest/)
- django-crispy-forms[(link)](https://django-crispy-forms.readthedocs.io/en/latest/index.html)

## Deployment:
Sport Bike Blog site was deployed to Heroku following next steps:

- Install Django & Gunicorn:
```pip3 install 'django' gunicorn```
- Install Django database & psycopg:
```pip3 install dj_database_url psycopg2```
- Install Cloudinary:
```pip3 install dj3-cloudinary-storage```
- Creating the requirements.txt file with the following command:
```pip3 freeze --local > requirements.txt```
- a django project was created using:
```django-admin startproject sportbike .```
- the blog app was then created with:
```python3 manage.py startapp blog```
- which was then added to the settings.py file within our project directory.
- the changes were then migrated using:
```python3 manage.py migrate```
- navigated to [Heroku](www.heroku.com) & created a new app called sport-bike-blog.
- added the Heroku Postgres database to the Resources tab.
- navigated to the Settings Tab, to add the following key/value pairs to the configvars:

1. key: SECRET_KEY | value: randomkey
2. key: PORT | value: 8000
3. key: CLOUDINARY_URL | value: API environment variable
4. key: DATABASE_URL | value: value supplied by Heroku

- added the DATABASE_URL, SECRET_KEY & CLOUDINARY_URL to the env.py file
- added the DATABASE_URL, SECRET_KEY & CLOUDINARY_URL to the settings.py file
- add an import os statement for the env.py file.
- added Heroku to the ALLOWED_HOSTS in settings.py
- created the Procfile
- pushed the project to Github
- connected my github account to Heroku through the Deploy tab
- connected my github project repository, and then clicked on the "Deploy" button
