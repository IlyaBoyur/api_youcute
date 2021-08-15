# REST API to Youcute Service
* Original project: https://github.com/IlyaBoyur/youcute
* JWT-token authentication
Django, Django REST Framework, Simple-JWT, SQLite3, git

To test functionality:
1. Prepare workspace
```bash
python3 -m venv venv
source venv/bin/activate
```
2. Install dependencies
```bash
pip install -r requirements.txt
```
2. Start the app
```bash
python manage.py migrate
python manage.py runserver
```
3. Enjoy!
See documantation to REST API on http://127.0.0.1:8000/redoc
