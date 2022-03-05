# REST API to Youcute Service
Stack local: Django, Django REST Framework, Simple-JWT, SQLite3, git
Stack deploy: Django, Django REST Framework, PostgreSQL, heroku


* Original project: https://github.com/IlyaBoyur/youcute
* JWT-token authentication


To test functionality:
### 0. Clone repository to local folder and go to project directory

### 1. Prepare workspace
```bash
python3 -m venv venv
source venv/bin/activate (for WIndows Git Bash: source venv/Scripts/activate)
pip install -r requirements.txt
```

### 3. Add required environment variables
```bash
export SECRET_KEY="hhz7l-ltdismtf@bzyz+rple7*s*w$jak%whj@(@u0eok^f9k4"
export DJANGO_DEBUG_VALUE=True
```

### 4. Create project database and migrate it
```bash
python manage.py migrate
```

### 5. Load simple test data to sqlite database
```bash
python manage.py loaddata fixtures.json
```

### 6. Start the app
```bash
python manage.py runserver
```

### 7. Enjoy!
See documentation to REST API on http://127.0.0.1:8000/redoc/

### Deployed solution
Check documentation at [documentation root](https://api-youcute.herokuapp.com/redoc/)

Examine [API root](https://api-youcute.herokuapp.com/api/)
