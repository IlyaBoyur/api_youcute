# REST API to Youcute Service
Stack: Django, Django REST Framework, Simple-JWT, SQLite3, git


* Original project: https://github.com/IlyaBoyur/youcute
* JWT-token authentication


To test functionality:
### 1. Prepare workspace
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
### 2. Create project database and migrate it
```bash
python manage.py migrate
```
### 3. Start the app
```bash
python manage.py runserver
```
### 4. Enjoy!
See documantation to REST API on http://127.0.0.1:8000/redoc

### Deployed solution
Check documentation at [documentation root](https://api-youcute.herokuapp.com/redoc/)
Examine [API root](https://api-youcute.herokuapp.com/api/)
