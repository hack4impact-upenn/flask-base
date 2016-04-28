# flask-base [![Circle CI](https://circleci.com/gh/hack4impact/flask-base.svg?style=svg)](https://circleci.com/gh/hack4impact/flask-base) [![Stories in Ready](https://badge.waffle.io/hack4impact/flask-base.png?label=ready&title=Ready)](https://waffle.io/hack4impact/flask-base)

## Synopsis

A Flask application template with the boilerplate code already done for you.

## What's included?

* Blueprints
* User and permissions management
* Flask-SQLAlchemy for databases
* Flask-WTF for forms
* Flask-Assets for asset management and SCSS compilation
* Flask-Mail for sending emails
* gzip compression
* gulp autoreload for quick static page debugging

## Extensions

Other branches include even more features

* `admin-edit-static-pages`: allow administrators to edit static pages using the [ckeditor](http://ckeditor.com/) WYSIWYG editor 

## Setting up

1. Clone the repo

    ```
    $ git clone https://github.com/hack4impact/flask-base.git
    $ cd flask-base
    ```

2. Initialize a virtualenv

    ```
    $ pip install virtualenv
    $ virtualenv env
    $ source env/bin/activate
    ```

3. Install the dependencies

    ```
    $ pip install -r requirements/common.txt
    $ pip install -r requirements/dev.txt
    ```

4. Create the database

    ```
    $ python manage.py recreate_db
    ```

5. Other setup (e.g. creating roles in database)

    ```
    $ python manage.py setup_dev
    ```

6. [Optional] Add fake data to the database

    ```
    $ python manage.py add_fake_data
    ```

7. [Optional] Use gulp to live compile your files
- Install the Live Reload browser plugin from [here](http://livereload.com/)
- Run `npm install`
- Run `gulp`


## Running the app

```
$ source env/bin/activate
$ python manage.py runserver
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
```

## Project Structure


```
├── Procfile
├── README.md
├── app
│   ├── __init__.py
│   ├── account
│   │   ├── __init__.py
│   │   ├── forms.py
│   │   └── views.py
│   ├── admin
│   │   ├── __init__.py
│   │   ├── forms.py
│   │   └── views.py
│   ├── assets
│   │   ├── scripts
│   │   │   ├── app.js
│   │   │   └── vendor
│   │   │       ├── jquery.min.js
│   │   │       ├── semantic.min.js
│   │   │       └── tablesort.min.js
│   │   └── styles
│   │       ├── app.scss
│   │       └── vendor
│   │           └── semantic.min.css
│   ├── assets.py
│   ├── decorators.py
│   ├── email.py
│   ├── main
│   │   ├── __init__.py
│   │   ├── errors.py
│   │   ├── forms.py
│   │   └── views.py
│   ├── models.py
│   ├── static
│   │   ├── fonts
│   │   │   └── vendor
│   │   ├── images
│   │   └── styles
│   │       └── app.css
│   ├── templates
│   │   ├── account
│   │   │   ├── email
│   │   │   ├── login.html
│   │   │   ├── manage.html
│   │   │   ├── register.html
│   │   │   ├── reset_password.html
│   │   │   └── unconfirmed.html
│   │   ├── admin
│   │   │   ├── index.html
│   │   │   ├── manage_user.html
│   │   │   ├── new_user.html
│   │   │   └── registered_users.html
│   │   ├── errors
│   │   ├── layouts
│   │   │   └── base.html
│   │   ├── macros
│   │   │   ├── form_macros.html
│   │   │   └── nav_macros.html
│   │   ├── main
│   │   │   └── index.html
│   │   └── partials
│   │       ├── _flashes.html
│   │       └── _head.html
│   └── utils.py
├── config.py
├── manage.py
├── requirements
│   ├── common.txt
│   └── dev.txt
└── tests
    ├── test_basics.py
    └── test_user_model.py
```

## Contributing

Contributions are welcome! Please check out our [Waffle board](https://waffle.io/hack4impact/flask-base) which automatically syncs with this project's GitHub issues.

## License
[MIT License](LICENSE.md)
