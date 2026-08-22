# File Upload Project with Django

A small Django project for learning **Django Templates (DTL), file uploads, media/static files, SQLite, URL routing, models, views, and basic CRUD operations**.

![Project Screenshot](docs/project-screenshot.png)

## Features

- Upload files through a Django form
- Store uploaded files under `media/uploads/`
- Save file metadata in SQLite
- Display uploaded files and upload time
- Delete a file from both the database and media folder
- Display uploaded images as previews
- Serve CSS through Django static files
- Simple home page and file-management page

## Tech Stack

- Python
- Django
- Django Templates (DTL)
- SQLite
- HTML/CSS
- Git/GitHub

## Project Structure

```text
file-upload-project-with-DTL/
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   ├── asgi.py
│   └── wsgi.py
├── files/
│   ├── migrations/
│   │   └── 0001_initial.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── media/
│   └── uploads/
├── static/
│   └── file-upload.css
├── templates/
│   ├── files/
│   │   └── file_upload.html
│   └── home/
│       └── index.html
├── db.sqlite3
└── manage.py
```

## How It Works

The main flow is:

```text
Browser
   ↓
URL
   ↓
files/views.py
   ↓
File model
   ↓
SQLite + media/uploads
   ↓
Django Template
   ↓
HTML response
```

### Upload

The form sends a `POST` request with `multipart/form-data`.

```python
uploaded_file = request.FILES.get('file')
if uploaded_file:
    File.objects.create(file=uploaded_file)
```

The model uses:

```python
file = models.FileField(upload_to='uploads/')
```

So uploaded files are stored under:

```text
media/uploads/
```

### Delete

The delete view removes the physical file first and then removes its database record:

```python
file.file.delete(save=False)
file.delete()
```

### Media Files

The project uses:

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

During development, `config/urls.py` serves media files when `DEBUG=True`.

### Static Files

The CSS file is located at:

```text
static/file-upload.css
```

and configured with:

```python
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / "static",
]
```

The template loads it with:

```django
{% load static %}
<link rel="stylesheet" href="{% static 'file-upload.css' %}">
```

## Run Locally

Clone the repository:

```bash
git clone https://github.com/MojiShah/file-upload-project-with-DTL.git
cd file-upload-project-with-DTL
```

Create and activate a virtual environment:

### Windows PowerShell

```powershell
python -m venv venv
.env\Scripts\Activate.ps1
```

Install Django:

```powershell
pip install django
```

Apply migrations:

```powershell
python manage.py migrate
```

Run the development server:

```powershell
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

Then open the file-management page from the home page.

## Main Model

```python
class File(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name
```

## Notes

This repository is primarily a **learning project**. It currently uses SQLite and Django's development server.

Before production deployment, the project should be improved with environment variables for secrets, a production database such as PostgreSQL, proper static/media serving, production WSGI/ASGI configuration, security settings, and a deployment setup.

> The repository currently contains a `SECRET_KEY` in `settings.py`. For a real production project, move the secret to an environment variable and never commit production secrets to Git.
