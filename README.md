# Food Management System

A complete beginner-friendly Django Food Management System using Django Templates, Forms, Models, Views, URLs, Bootstrap 5, JavaScript, and MySQL. It does not use REST API, React, Vue, or Angular.

## Main Features

- User registration, login, logout, profile update, and change password
- Dashboard cards for total foods, categories, and orders
- Category CRUD with search
- Food CRUD with image upload, search, category filter, and pagination
- Order CRUD with automatic total price calculation
- Stock deduction on order create, stock correction on update, and stock restore on delete
- Responsive Bootstrap 5 navbar, sidebar, tables, forms, cards, modals, alerts, and footer

## Project Structure

```text
food management/
├── food_management/        Main project settings, URLs, WSGI, ASGI, and general views
├── accounts/               Authentication, profile, and password forms/views
├── categories/             Category model, forms, CRUD views, URLs, and admin
├── foods/                  Food inventory model, forms, CRUD views, URLs, and admin
├── orders/                 Order model, forms, CRUD views, URLs, and admin
├── templates/              Django templates for all pages
├── static/css/style.css    Custom responsive styling
├── static/js/main.js       Alert auto-close and order price preview
├── media/                  Uploaded food images
├── requirements.txt        Python dependencies
└── manage.py               Django management script
```

## File Guide

### Project Files

- `manage.py`: Runs Django commands such as migrations, superuser creation, and server startup.
- `food_management/settings.py`: Configures installed apps, templates, static/media files, authentication redirects, messages, and MySQL database connection.
- `food_management/urls.py`: Connects project-level pages and app URLs.
- `food_management/views.py`: Contains home, about, contact, and dashboard views.
- `food_management/wsgi.py` and `food_management/asgi.py`: Deployment entry points.

### Accounts App

- `accounts/forms.py`: Registration, login, profile, and password change forms.
- `accounts/views.py`: Handles register, login, logout, profile update, and password change.
- `accounts/urls.py`: URLs for authentication pages.
- `accounts/templatetags/form_tags.py`: Adds Bootstrap classes to Django form fields in templates.

### Categories App

- `categories/models.py`: Defines `Category` with name, description, and created date.
- `categories/forms.py`: Model form for creating and updating categories.
- `categories/views.py`: List, create, update, and delete class-based views with search.
- `categories/admin.py`: Makes categories manageable from the Django admin.

### Foods App

- `foods/models.py`: Defines `Food` with category, price, quantity, description, expiry date, image, and created date.
- `foods/forms.py`: Model form with date picker and image upload support.
- `foods/views.py`: CRUD views with search, category filtering, and pagination.
- `foods/admin.py`: Adds useful food list, filter, and search options in admin.

### Orders App

- `orders/models.py`: Defines `Order` and calculates `total_price` automatically in `save()`.
- `orders/forms.py`: Validates order quantity and available stock.
- `orders/views.py`: CRUD views that adjust stock when orders change.
- `orders/admin.py`: Adds order management in the admin panel.

### Templates and Static Files

- `templates/base.html`: Shared layout with navbar, sidebar, messages, footer, Bootstrap, CSS, and JS.
- `templates/home.html`, `about.html`, `contact.html`, `dashboard.html`: Main pages.
- `templates/accounts/*`: Login, register, profile, and password pages.
- `templates/categories/*`: Category list, form, and delete confirmation pages.
- `templates/foods/*`: Food card list, form, and delete confirmation pages.
- `templates/orders/*`: Order table list, form, and delete confirmation pages.
- `static/css/style.css`: Modern responsive UI design.
- `static/js/main.js`: Auto-dismisses alerts and previews order totals.

## Installation Steps

1. Install Python 3.11 or newer from [python.org](https://www.python.org/downloads/). During installation, check **Add Python to PATH**.
2. Install MySQL Server and create a database:

```sql
CREATE DATABASE food_management_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

3. Open a terminal in this project folder:

```powershell
cd "C:\Users\Gopika\OneDrive\Documents\food management"
```

4. Create and activate a virtual environment:

```powershell
py -m venv venv
venv\Scripts\activate
```

5. Install dependencies:

```powershell
pip install -r requirements.txt
```

6. Set MySQL password for the current terminal if your MySQL root user has one:

```powershell
$env:MYSQL_PASSWORD="your_mysql_password"
```

You can also set `MYSQL_DATABASE`, `MYSQL_USER`, `MYSQL_HOST`, and `MYSQL_PORT` if needed.

## Migration Commands

```powershell
py manage.py makemigrations
py manage.py migrate
```

## Superuser Creation

```powershell
py manage.py createsuperuser
```

## Run Server

```powershell
py manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

Admin panel:

```text
http://127.0.0.1:8000/admin/
```

## Expected Output Screens

- Home page: A professional hero section with project introduction and feature cards.
- Login/Register pages: Centered Bootstrap forms with validation errors and success messages.
- Dashboard: Three statistic cards showing total foods, total categories, and total orders, plus recent orders and low-stock foods.
- Category page: Searchable table with edit and delete modal actions.
- Food page: Responsive food cards with image, category badge, price, stock, expiry date, search, filter, and pagination.
- Order page: Table of customer orders with calculated total price and edit/delete actions.

## Common Errors and Solutions

- `No installed Python found`: Install Python from python.org and enable **Add Python to PATH**.
- `ModuleNotFoundError: No module named django`: Activate the virtual environment and run `pip install -r requirements.txt`.
- `Access denied for user 'root'@'localhost'`: Set the correct MySQL password with `$env:MYSQL_PASSWORD="password"`.
- `Unknown database 'food_management_db'`: Create the database in MySQL before running migrations.
- MySQL driver error: This project uses PyMySQL. Run `pip install -r requirements.txt` again inside the activated virtual environment.
- Food images do not show: Make sure `DEBUG=True` while developing and upload images through the food form.

## Interview Talking Points

- Uses Django MTV architecture: Models, Templates, Views.
- Uses class-based views for clean CRUD implementation.
- Uses Django forms for validation and safe user input handling.
- Uses Django messages for user feedback.
- Uses MySQL for persistent relational storage.
- Handles uploaded media with `MEDIA_ROOT` and `MEDIA_URL`.
- Calculates order totals on the server, not only in JavaScript.
- Adjusts stock when orders are created, edited, or deleted.
