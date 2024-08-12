# To run this project

1. Clone the repository:

```
git clone git@github.com:404nicolette/CRM.git
```

2. Activate the python environment:

macOS/ Linux
```
source myenv/bin/activate
```

Windows:
```
myenv\Scripts\activate
```

3. Update the settings.py
This project runs on local computer, so please update the database section in settings.py to that it matches up to your own database credentials.

This uses MySQL Database.

```
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "myproject",
        "USER": "myuser",
        "PASSWORD": "mypassword",
        "HOST": "localhost",
        "PORT": "3306",
    }
}
```

4. To login and check the admin section of Django
```
username: admin
password: mypassword
```