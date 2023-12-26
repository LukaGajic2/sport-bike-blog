# SPORT BIKE BLOG

"Sport Bike Blog is your ultimate destination for the latest news, reviews, and insights into the exhilarating world of sport bikes. Whether you're a seasoned rider or a passionate enthusiast, our blog covers everything from cutting-edge motorcycle technology and performance reviews to thrilling ride experiences and must-have gear. Join us as we explore the fast-paced and dynamic realm of sport bikes, sharing tips, trends, and stories that ignite the passion for two-wheeled adrenaline."

![Site view across devices](static/img-readme/amiresponsivepp4.png)

The live link for "Sport Bike Blog" can be found [HERE](https://sport-bike-blog-416f164a9499.herokuapp.com/)

## Table of Contents
+ [User Stories](#user-stories)
+ [Design](#design)
  + [Wireframes](#wireframes)
  + [Database Scheme](#database-scheme)
  + [Color Scheme](#color-palette)
+ [Features](#features)
  + [CRUD](#crud)
+ [Testing](#testing)
+ [Technologies used](#technologies-used)
  + [Main Languages Used](#main-languages-used)
  + [Libraries, Frameworks and Programs](#libraries-frameworks-and-programs)
  + [Installed Packages](#installed-packages)
+ [Deployment](#deployment)
+ [Credits](#credits)

## User Stories

## Design

### Wireframes

### Database Scheme

### Color Palette
![Color Palette](static/img-readme/colorpalette.png)

## Features

#### About Page
![About Page](static/img-readme/aboutpage.png)

#### Blog Page
![Blog Page](static/img-readme/blogpage.png)

#### Events Page
![Events Page](static/img-readme/eventspage.png)

#### Log In, Sign In Page
![Log In Page](static/img-readme/loginpage.png)

### CRUD

CRUD function is avaliable in comments sections for registered and inlogged users.

All users can read blog and events posts and comments beneath them and see number of likes.

![Comments page section](static/img-readme/commentspage.png)

Only registered and inlogged users can EDIT and DELETE their comments only and LIKE or UNLIKE posts.

![Edit Page](static/img-readme/editpage2.png)


## Testing
- .html files pass through the [W3C validator](https://validator.w3.org) with no issues
  
- CSS files pass through the [Jigsaw validator](https://jigsaw.w3.org/css-validator/)
![W3C Validator](static/img-readme/w3cvalidatorpp4.png)

- page has good Accessibility rating in Lighthouse
![Accessibilty score](static/img-readme/lighthouse.png)

- Python files tested in [CI Python Linter](https://pep8ci.herokuapp.com/) with no issues
  
- All social links opens to external links as intended.


## Technologies Used
### Main Languages Used
- HTML5
- CSS3
- JavaScript
- Python
- Django
- SQL Postgres

### Libraries, Frameworks and Programs

- CodeAnywhere - IDE to create my html files & styling sheet before pushing the project to Github.
- GitHub - to store my repository.
- Django
- Bootstrap
- Google Fonts - font families.
- Font Awesome - to add icons to the social links in the footer element.
- Favicon
- Am I Responsive? - to ensure the project looked good across all devices.

### Installed Packages

- 'django' gunicorn
- dj_database_url psycopg2
- dj3-cloudinary-storage
- django-summernote [(link)](https://summernote.org/)
- django-allauth [(link)](https://django-allauth.readthedocs.io/en/latest/)
- django-crispy-forms[(link)](https://django-crispy-forms.readthedocs.io/en/latest/index.html)

## Deployment
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

## Credits

- [Lauren-Nicole Popich](https://github.com/CluelessBiker): a MENTOR!
- Tutor Support
- "I think therefore I blog", "Hello Django"
- [Start Bootstrap](<https://startbootstrap.com/theme/clean-blog>) base for blog site
- Slack

+ [Stackoverflow](https://stackoverflow.com/questions/66185424/django-how-do-i-handle-urls-with-multiple-apps) - how to connect URL paths from multiple apps
- Sean from Tutor Support with help and explaining how to make EDIT and DELETE buttons work
