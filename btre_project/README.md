# BTRE - Real Estate Property Listing Website

A comprehensive Django-based real estate platform for browsing, searching, and managing property listings with user authentication and contact management.

## Overview

BTRE is a modern real estate web application built with **Django 5.2** and **PostgreSQL**. It provides a complete platform for real estate agents and buyers to list, search, and inquire about properties. The system includes user authentication, property management, realtor profiles, and an inquiry/contact system.

## Features

### Core Features
- **Property Listings**: Browse and search residential properties with detailed information
- **Advanced Search**: Filter properties by location, price range, bedrooms, bathrooms, and more
- **Property Details**: View comprehensive property information including photos, descriptions, and realtor contact info
- **User Accounts**: User registration and authentication system
- **Contact & Inquiries**: Submit inquiries about properties to realtors
- **Realtor Profiles**: View realtor information and their listed properties
- **Responsive Design**: Mobile-friendly interface using Bootstrap

### Admin Features
- Django admin panel for managing listings, realtors, users, and inquiries
- Property image management
- User account management
- Inquiry/Contact tracking

## Project Structure

```
btre_project/
├── btre/                 # Main project configuration
│   ├── settings.py       # Django settings and configuration
│   ├── urls.py           # URL routing
│   ├── asgi.py           # ASGI configuration
│   ├── wsgi.py           # WSGI configuration
│   └── static/           # Global static files
├── pages/                # Home and about pages app
│   ├── views.py
│   ├── urls.py
│   └── templates/
├── listings/             # Property listings management app
│   ├── models.py         # Listing model
│   ├── views.py
│   ├── urls.py
│   ├── choices.py        # Predefined choices
│   └── templates/
├── realtors/             # Realtor management app
│   ├── models.py         # Realtor model
│   ├── views.py
│   ├── urls.py
│   └── templates/
├── accounts/             # User authentication app
│   ├── models.py         # User models
│   ├── views.py          # Login, register, dashboard
│   ├── urls.py
│   └── templates/
├── contacts/             # Contact/Inquiry management app
│   ├── models.py         # Contact inquiry model
│   ├── views.py
│   ├── urls.py
│   └── templates/
├── media/                # User-uploaded files (property images)
├── static/               # Static files (CSS, JS, images)
├── templates/            # HTML templates
├── manage.py             # Django management script
├── db.sqlite3            # Development database (can switch to PostgreSQL)
└── README.md             # This file
```

## Technology Stack

- **Backend**: Django 5.2
- **Database**: PostgreSQL (configured in settings)
- **Frontend**: HTML5, CSS3, Bootstrap 4/5
- **ORM**: Django ORM
- **Admin**: Django Admin Interface

## Requirements

- Python 3.8+
- Django 5.2
- PostgreSQL 12+
- pip (Python package manager)

## Installation

### 1. Clone the Repository
```bash
git clone <repository-url>
cd btre_project
```

### 2. Create a Virtual Environment
```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Database Setup

**Option A: Using PostgreSQL** (Recommended)
- Ensure PostgreSQL is installed and running
- Create a database named `btredb`:
```sql
CREATE DATABASE btredb;
CREATE USER postgres WITH PASSWORD 'postgres';
GRANT ALL PRIVILEGES ON DATABASE btredb TO postgres;
```

**Option B: Using SQLite** (Development)
- The project defaults to SQLite in `db.sqlite3`

### 5. Apply Migrations
```bash
python manage.py migrate
```

### 6. Create a Superuser (Admin Account)
```bash
python manage.py createsuperuser
```

### 7. Collect Static Files
```bash
python manage.py collectstatic
```

### 8. Run the Development Server
```bash
python manage.py runserver
```

The application will be available at `http://localhost:8000/`

## Usage

### User Workflows

**Browsing Properties**
1. Navigate to the homepage
2. Use the search bar or filters to find properties
3. Click on a property to view detailed information
4. Contact the realtor through the inquiry form

**User Registration**
1. Click "Sign Up" on the navigation bar
2. Fill in your details (name, email, password)
3. Log in with your credentials
4. Access your dashboard to manage inquiries

**Submitting Inquiries**
1. View a property listing
2. Fill in the contact form with your information
3. Submit your inquiry
4. The realtor will be notified and may contact you

### Admin Management

1. Navigate to `/admin/`
2. Log in with superuser credentials
3. Manage:
   - Listings (create, edit, delete properties)
   - Realtors (manage realtor profiles)
   - Users (manage user accounts)
   - Contacts (view and track inquiries)

## Configuration

### Key Settings (in `btre/settings.py`)

- **DEBUG**: Set to `False` in production
- **ALLOWED_HOSTS**: Add your domain(s) in production
- **DATABASE**: Configure PostgreSQL connection
- **MEDIA_ROOT**: Path for user-uploaded files
- **STATIC_ROOT**: Path for static files collection
- **SECRET_KEY**: Change this in production

### Environment Variables (Recommended)
Create a `.env` file for sensitive information:
```
SECRET_KEY=your-secret-key
DEBUG=False
DATABASE_NAME=btredb
DATABASE_USER=postgres
DATABASE_PASSWORD=your-password
DATABASE_HOST=localhost
DATABASE_PORT=5432
```

## Apps Overview

### Pages App
- Homepage
- About page
- General information pages

### Listings App
- Property model with fields for price, bedrooms, bathrooms, lot size, etc.
- Search and filter functionality
- Property detail view

### Realtors App
- Realtor profiles
- Realtor listings
- Realtor information display

### Accounts App
- User registration
- User login/logout
- User dashboard
- Profile management

### Contacts App
- Contact inquiry model
- Inquiry submission form
- Inquiry management in admin

## Database Models

### Key Models
- **User**: Django built-in User model (extended in accounts app)
- **Listing**: Property information (price, address, bedrooms, bathrooms, etc.)
- **Realtor**: Realtor profiles and information
- **Contact**: User inquiries and contact messages

## Deployment

### Production Checklist
- [ ] Set `DEBUG = False`
- [ ] Change `SECRET_KEY` to a secure value
- [ ] Update `ALLOWED_HOSTS`
- [ ] Configure PostgreSQL for production
- [ ] Set up environment variables
- [ ] Collect static files
- [ ] Set up proper logging
- [ ] Configure HTTPS/SSL
- [ ] Use a production WSGI server (Gunicorn, uWSGI)
- [ ] Set up a reverse proxy (Nginx, Apache)

### Deployment Options
- Heroku
- AWS (EC2, Elastic Beanstalk)
- DigitalOcean
- PythonAnywhere
- VPS with Nginx and Gunicorn

## Development

### Running Tests
```bash
python manage.py test
```

### Creating Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Loading Sample Data
```bash
python manage.py loaddata <fixture-file>
```

## Troubleshooting

### Database Connection Issues
- Ensure PostgreSQL is running
- Check database credentials in `settings.py`
- Verify database exists

### Static Files Not Loading
```bash
python manage.py collectstatic --clear
```

### Migration Issues
```bash
python manage.py migrate --fake-initial
```

## Future Enhancements

- [ ] Advanced search filters (school district, crime rate, etc.)
- [ ] Email notifications for new listings
- [ ] Property comparison tool
- [ ] Virtual tours/3D property views
- [ ] Reviews and ratings system
- [ ] Map integration (Google Maps)
- [ ] Mobile app
- [ ] AI-based property recommendations

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, email support@btre.com or open an issue in the repository.

## Author

Kenneth Kimosop

## Acknowledgments

- Django community
- Bootstrap for responsive design
- PostgreSQL for robust database