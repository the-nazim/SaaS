# Saas Application (API) 

## Project Structure

```bash
saas_app/
│
├── manage.py
├── requirements.txt
├── .env                 # Secrets and keys
│
├── config/              # Project settings
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── accounts/            # User registration, login, profiles
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/accounts/
│
├── billing/             # Stripe integration
│   ├── models.py        # Subscription models
│   ├── views.py
│   ├── urls.py
│   ├── stripe_webhooks.py
│   └── templates/billing/
│
├── core/                # Public pages, home, dashboard
│   ├── views.py
│   ├── urls.py
│   └── templates/core/
│
├── static/
│   └── css/, js/, images/
│
├── templates/           # Shared base templates
│   └── base.html
│
└── media/               # Uploaded files (if any)
```