# Requirements to run this repository:

1. Clone the repository:
```
git clone git@github.com:404nicolette/CRM.git
```

2. Create a python environment:
Make sure you are inside the project directory, then, create the virtual environment by typing this in the terminal.

```
python -m venv <environment_name>
```
Activate the environment.

Windows:
```
<environment_name>\Scripts\activate
```

macOS/Linux:
```
source <environment_name>/bin/activate
```

3. Set up MySQL Database:
Enter this in the terminal
```
mysql -u root -p
```
then,
```
CREATE DATABASE your_db_name;
CREATE USER '<your_db_user'@'localhost>' IDENTIFIED BY '<your_password>';
GRANT ALL PRIVILEGES ON <your_db_name>.* TO '<your_db_user'@'localhost'>;
FLUSH PRIVILEGES;
```
Make sure to update the settings.py:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

Apply the migrations:
```
python manage.py migrate
```

