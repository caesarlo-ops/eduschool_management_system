# School Management System - Django + PostgreSQL

A complete school management system built with Django and PostgreSQL.

## Features

- **Student Management**: Add, search, and manage student records
- **Attendance Tracking**: Mark and monitor daily attendance
- **Fee Management**: Track fee payments and calculate balances
- **Payroll System**: Manage employee salaries and generate payslips
- **Dashboard**: Visual statistics and quick actions
- **Role-based Access**: Admin and Teacher roles
- **Django Admin**: Powerful admin interface for data management

## Requirements

- Python 3.10+
- PostgreSQL 12+
- pip

## Installation

### 1. Clone/Navigate to the project

```bash
cd school_management
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up PostgreSQL Database

Create a database in PostgreSQL:

```sql
CREATE DATABASE school_management;
CREATE USER postgres WITH PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE school_management TO postgres;
```

Update `config/settings.py` with your database credentials if different.

### 5. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create a superuser

```bash
python manage.py createsuperuser
```

Enter email, password, and other details when prompted.

### 7. Create User Profile for Admin

After creating the superuser, you need to create a UserProfile:

```bash
python manage.py shell
```

Then run:

```python
from django.contrib.auth.models import User
from core.models import UserProfile

user = User.objects.get(username='your_email')
UserProfile.objects.create(user=user, role='admin')
exit()
```

### 8. Run the development server

```bash
python manage.py runserver
```

### 9. Access the application

- Main Application: http://127.0.0.1:8000/
- Admin Panel: http://127.0.0.1:8000/admin/

## Default Login

- Email: (your superuser email)
- Password: (your superuser password)
- Role: Administrator

## Project Structure

```
school_management/
├── config/                 # Django project configuration
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── core/                   # Main application
│   ├── models.py          # Database models
│   ├── views.py           # View functions
│   ├── forms.py           # Django forms
│   ├── admin.py           # Admin configuration
│   └── urls.py            # URL routing
├── templates/             # HTML templates
│   ├── base.html
│   ├── login.html
│   ├── dashboard.html
│   ├── students.html
│   ├── attendance.html
│   ├── fees.html
│   ├── payroll.html
│   └── payslip.html
├── static/                # Static files (CSS, JS)
│   └── css/
│       └── styles.css
├── manage.py
└── requirements.txt
```

## Database Models

### Student
- name
- student_class
- parent_name
- contact

### Employee
- name
- position
- base_salary
- allowances
- deductions

### Fee
- student (ForeignKey)
- amount_paid
- total_fee
- balance
- payment_date

### Attendance
- student (ForeignKey)
- status (Present/Absent/Late/Excused)
- date

### UserProfile
- user (OneToOne)
- role (admin/teacher)
- phone

## Production Deployment

Before deploying to production:

1. Change `SECRET_KEY` in `config/settings.py`
2. Set `DEBUG = False`
3. Update `ALLOWED_HOSTS` with your domain
4. Configure proper database credentials
5. Set up static files with `python manage.py collectstatic`
6. Use a production WSGI server (Gunicorn, uWSGI)
7. Set up HTTPS

## License

This project is open source.
