# SecretSanta


## Backend Setup
### Setup on linux
```
For Linux:
cd backend
source venv/bin/activate
pip install -r requirements.txt
```

### Setup on windows
```
cd backend
setup a virtual environment (i.e. called secretsanta)
see (https://medium.com/analytics-vidhya/virtual-environment-6ad5d9b6af59) for instructions
.\secretsanta\Scripts\activate
pip install -r requirements.txt
```

### DB Setup on Both
```
setup database by using the following command
python manage.py migrate
- your DB will be located in the \backend folder called db.sqlite3
```

### DB admin user setup
python manage.py createsuperuser
- will prompt for username, password

### Startup backend server
python manage.py runserver
- provides server with url to manage DB
- 127.0.0.1:8000 for example
- nicer user interface: 127.0.0.1:8000/admin


### SQLite app
Use the following DB Browser for SQLite
https://sqlitebrowser.org/

### Node
```
cd frontend
npm install
```