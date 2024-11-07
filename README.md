# Shoping

Shoping is an online shopping website built using the Django framework. It offers a complete set of features, including a product catalog, cart functionality, coupons functionality, checkout, and email invoicing.

## Demo

Watch the demo video to see **Shoping** in action:


                 
<div align="center">
    <a href="https://youtu.be/bTgNIKVai9I">
        <img src="https://img.youtube.com/vi/bTgNIKVai9I/0.jpg" alt="Watch the video" style="width:80%; max-width:600px;">
    </a>
</div>


## Key Features
- **Product Catalog**: Browse and view detailed product listings.
- **Cart Functionality**: Add, update, and remove products from the shopping cart.
- **Product Recommendation**: Uses Redis for intelligent product suggestions.
- **Coupon System**: Apply coupon codes for discounts during checkout.
- **Checkout Process**: Streamlined checkout experience.
- **Payment Integration**: Secure payments using Stripe.
- **Email Invoicing**: Automatic sending of invoices to customers via email.
- **Background Task Management**: Utilizes Celery with Redis and RabbitMQ for task handling.
- **PDF Generation**: Invoices generated in PDF format using WeasyPrint.

## Technologies Used
- **Django**
- **Celery**
- **Redis**
- **Stripe**
- **RabbitMQ**
- **WeasyPrint**

## Project Structure
```
shoping/
├── cart/
│   ├── __init__.py
│   ├── views.py
│   ├── models.py
│   ├── forms.py
│   └── ...
├── coupons/
│   ├── __init__.py
│   ├── views.py
│   ├── models.py
│   └── ...
├── orders/
│   ├── __init__.py
│   ├── views.py
│   ├── models.py
│   └── ...
├── payment/
│   ├── __init__.py
│   ├── views.py
│   ├── webhooks.py
│   └── ...
├── shop/
│   ├── __init__.py
│   ├── views.py
│   ├── recommender.py
│   ├── models.py
│   └── ...
├── static/
│   ├── admin/
│   ├── css/
│   └── img/
├── templates/
├── manage.py
├── requirements.txt
├── .env
├── venv/
└── ...
```

## Installation and Setup

### Prerequisites
- Python 3.x
- Redis server
- RabbitMQ server
- Git

### Steps to Install
1. **Clone the repository**:
   ```bash
   git clone https://github.com/tarunkeshukumar/shoping.git
   cd shoping
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   Create a `.env` file in the project root with the following variables:
   ```env
   SECRET_KEY=your_django_secret_key
   DEBUG=True
   STRIPE_SECRET_KEY=your_stripe_secret_key
   STRIPE_PUBLISHABLE_KEY=your_stripe_publishable_key
   EMAIL_HOST=smtp.your-email-provider.com
   EMAIL_PORT=587
   EMAIL_HOST_USER=your_email@example.com
   EMAIL_HOST_PASSWORD=your_email_password
   EMAIL_USE_TLS=True
   ```

5. **Apply migrations**:
   ```bash
   python manage.py migrate
   ```

6. **Run Redis and Celery**:
   - Start the Redis server:
     ```bash
     redis-server
     ```
   - Start Celery workers:
     ```bash
     celery -A shoping worker --solo=polo
     ```

7. **Run the Django development server**:
   ```bash
   python manage.py runserver
   ```

## Usage
- Visit `http://127.0.0.1:8000/` to access the website.


