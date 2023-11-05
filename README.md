On production:

gunicorn --workers=3 --bind="0.0.0.0:8000" app:app

Locally:

python app.py