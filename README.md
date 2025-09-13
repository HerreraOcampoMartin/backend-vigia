# Core REST API for Django Projects
This is designed for utilize the basic functionalities in an application such as, log in, sign up, managing common data, etc

## Configure the virtual environment
1. Create the virtual environment:
   ```bash
   python3 -m venv virtual-env
   ```

2. Activate the venv:
   - In Linux/Mac:
     ```bash
     source virtual-env/bin/activate
     ```
   - In Windows:
     ```bash
     .\virtual-env\Scripts\activate
     ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Migrations
Before running the server in development mode, apply migrations to the database:

```bash
python manage.py makemigrations
python manage.py migrate
```

## Development mode
To run the project in development mode, use the following command:
```bash
python manage.py runserver
```

## Testing
For running all the tests in the project you should run:
```bash
coverage run --omit='*/.venv/*' manage.py test
```

For updating the coverage status run:
```bash
coverage html
```

---
