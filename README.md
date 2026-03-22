# 🛒 Store Server

E-commerce web application built with Django. Features a product catalog with categories, shopping cart, Stripe checkout, user authentication with email verification, and OAuth via GitHub.

> **Note:** This was my first Django project, built as a learning exercise alongside a course. It covers the full cycle: from models and templates to production deployment with Nginx + Gunicorn.

## Features

- **Product catalog** — categories, pagination, filtering by category
- **Shopping cart** — add/remove items, quantity tracking, total calculation
- **Stripe payments** — checkout sessions, webhook for order fulfillment
- **User system** — registration, login, profile editing, avatar upload
- **Email verification** — async via Celery + Redis, 48h expiration link
- **OAuth** — GitHub login via django-allauth
- **Caching** — Redis-backed cache (django-redis)
- **Admin panel** — full Django admin for managing products, orders, users

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Framework | Django 3.2, CBV (Class-Based Views) |
| Database | PostgreSQL (psycopg2) |
| Cache & Broker | Redis (django-redis) |
| Task Queue | Celery |
| Payments | Stripe API + Webhooks |
| Auth | django-allauth (GitHub OAuth) |
| Config | django-environ (.env) |
| Code Quality | flake8, isort |
| Deploy | Nginx, Gunicorn, UFW |

## Project Structure

```
store/
├── store/               # Django project settings
│   ├── settings.py      # Config (environ, Redis, Stripe, Celery, DB)
│   ├── urls.py          # Root URL routing
│   ├── celery.py        # Celery app configuration
│   └── wsgi.py
├── products/            # Product catalog app
│   ├── models.py        # Product, ProductCategory, Basket
│   ├── views.py         # IndexView, ProductsListView, basket_add/remove
│   └── context_processors.py
├── orders/              # Order & payment app
│   ├── models.py        # Order (statuses: Created → Paid → On Way → Delivered)
│   ├── views.py         # OrderCreateView, Stripe checkout, webhook handler
│   └── forms.py
├── users/               # User management app
│   ├── models.py        # Custom User (AbstractUser), EmailVerification
│   ├── views.py         # Login, Register, Profile (CBV)
│   ├── forms.py         # UserLoginForm, UserRegistrationForm, UserProfileForm
│   └── tasks.py         # Celery task: send_email_verification
├── common/              # Shared mixins (TitleMixin)
├── static/              # CSS, JS, images
├── media/               # User uploads, product images
└── templates/           # HTML templates per app
```

## Setup

```bash
# Clone
git clone https://github.com/FluDex7/store-server.git
cd store-server/store

# Virtual environment
python -m venv venv
source venv/bin/activate

# Dependencies
pip install -r requirments.txt

# Environment variables — create .env file
cp .env.example .env  # then fill in the values below
```

### Required `.env` variables

```env
DEBUG=True
SECRET_KEY=your-secret-key
DOMAIN_NAME=http://127.0.0.1:8000

REDIS_HOST=127.0.0.1
REDIS_PORT=6379

DATABASE_NAME=store_db
DATABASE_USER=postgres
DATABASE_PASSWORD=your-password
DATABASE_HOST=127.0.0.1
DATABASE_PORT=5432

EMAIL_HOST=smtp.yandex.ru
EMAIL_PORT=465
EMAIL_HOST_USER=your-email
EMAIL_HOST_PASSWORD=your-password
EMAIL_USE_SSL=True

STRIPE_PUBLIC_KEY=pk_test_...
STRIPE_SECRET_KEY=sk_test_...
STRIPE_WEBHOOK_SECRET=whsec_...
```

### Run

```bash
# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Start Redis (in a separate terminal)
redis-server

# Start Celery worker (in a separate terminal)
celery -A store worker -l info

# Run server
python manage.py runserver
```

App available at `http://127.0.0.1:8000`
Admin panel at `http://127.0.0.1:8000/admin/`

## Topics Covered

This project was built to learn and practice:

- Django MVT architecture, Class-Based Views (ListView, CreateView, DetailView, TemplateView)
- Custom User model (AbstractUser) with email verification flow
- Stripe API integration (product sync, checkout sessions, webhooks)
- Celery async tasks with Redis as broker
- OAuth 2.0 authentication via django-allauth
- PostgreSQL setup and configuration
- Redis caching with django-redis
- Production deployment: Nginx + Gunicorn + UFW firewall + HTTPS
- Code style enforcement: flake8 + isort
