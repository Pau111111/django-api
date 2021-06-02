`#python` `#django` `#api`

# Django API <!-- omit in toc -->

<p>
  <img alt="Version" src="https://img.shields.io/badge/version-1.0-blue.svg?cacheSeconds=2592000" />
</p>

> With Django, you can take Web applications from concept to launch in a matter of hours.
> Django takes care of much of the hassle of Web development, so you can focus on writing your app without needing to reinvent the wheel.
> It’s free and open source.

## Index <!-- omit in toc -->

- [Requirements](#requirements)
- [Steps](#steps)
- [API Key Middleware](#api-key-middleware)
- [Resources](#resources)

## Requirements

- [Python](https://www.python.org/downloads/)
- [Django](https://www.djangoproject.com/)
- [DBeaver](https://dbeaver.io/)

## Steps

1. Create an empty Django project: `django-admin startproject djangoAPI`
2. `cd djangoProject`
3. Start a new Django application: `py manage.py startapp djangoAPI`
4. Next steps are detailed with commits, look at this README.md when you reach the migration commits
5. Create migrations: `py manage.py makemigrations`
6. Execute migrations: `py manage.py migrate`
7. Create a super user to administrate your API: `py manage.py createsuperuser`
8. Execute your server: show DATABASE`py manage.py runserver`

## API Key Middleware

> [API Key Library](https://pypi.org/project/djangorestframework-api-key/)

- `pip install djangorestframework-api-key==2.*`
  `or`
- `pip3 install djangorestframework`

```
# settings.py

INSTALLED_APPS = [

# ...

"rest_framework",
"rest_framework_api_key",
]
```

- `python manage.py migrate`

## Resources

- [¿Cómo crear una API REST con DJANGO](https://youtu.be/XqRBb_4CLS4)
