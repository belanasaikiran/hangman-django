# hangman-django


## For this Repository, Instructions:

```
python manage.py makemigrations  
python manage.py migrate
python manage.py runserver
```



## Django App create:

1. Create main app
```
django-admin startproject main .
```

2. sub app:
```
python manage.py startapp hangman
```
> The above command would create a new directory in the same folder


3. run migration script:
```
python manage.py migrate
```
4. to run server
```
python manage.py runserver
```

## Customizing the app:

Views: View is a function that returns output to the browser for interacting

> we can only make one project url per app


### For Demo purpose, we use SQLite, for low traffic sites that don't experience a lot of concurrency

1. First we need to register our app in our project to use its database.
2. we edit `settings.py`
3. To Add config from app to project,  find `INSTALLED_APPS` section, we add `hangman.app.HangmanConfig` to the list 


### Create Model for our site:

`hangman` > `models.py` >

> A model describes the database objects used in the site, tables and fields, etc
```
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')

```

### Next, we register the tables we created in django admin system(`admin.py`) to manage the table directly in admin page
`hangman` > `admin.py`

```
# add the following
from .models import Book # we just created this database object
admin.site.register(Book)
```

## We now need to do `Migration` before doing anything with the newly created models/model

> Luckily django does it for us, using `make migrations` command in `manage.py`

1. To do So, we run
    ```
    python manage.py makemigrations hangman
    ```
    > Each set of changes that we make to database is recorder in a separate sequence numbered file so we can migrate smoothly between schemas.

2. To apply the above changes, we use `sqlmigrate` function:
    ```
    python manage.py sqlmigrate hangman 0001
    ```

3. Finally we apply all the changes using `migrate` command
    ```
    python manage.py migrate hangman
    ```
* Now the Database and description of it are completely up-to-date with each other


### Using Database:

1. Create Administrative user which will be stored in database to perform administrative function(for adding data to database)
    ```
    python manage.py createsuperuser 
    ```
    Output would be options to create username instructions:
    ```
    Username (leave blank to use 'sanju'): 
    Email address: saikiransanju22@gmail.com
    Password: 
    Password (again): 
    Error: Your passwords didn't match.
    Password: 
    Password (again): 
    Superuser created successfully.
    ```
2. To login, run `python manage.py runserver` and go to admin screen and login
