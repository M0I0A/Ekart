# E-commerce Django App

This is a Django-based e-commerce platform where:
- Sellers can list products.
- Buyers can register, login, browse products, add them to the cart, and complete purchases.
- Buyers can also track the delivery status of their orders.

## Features

### Seller Features:
- Register and log in as a seller.
- Add, update, and delete products.
- Manage product details (price, description, and images).

### Buyer Features:
- Register and log in as a buyer.
- Browse and view available products.
- Add products to the shopping cart.
- Purchase products and view order details.
- Track the delivery status of orders.

### Order Management:
- View orders placed by the buyer.
- Track the delivery status of orders.

## Installation Guide

### Prerequisites

- Python 3.x
- Django 4.x
- PostgreSQL (or any database configured in `settings.py`)

### Installation Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/ecommerce-django-app.git
   cd ecommerce-django-app
2.**Create a virtual environment:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate  # On Windows: venv\Scripts\activate
  ```

3.**Install dependencies:**
```
pip install -r requirements.txt
```

4.**Configure the database:**

5.**Run migrations:**
```
python manage.py migrate
```

6.**Create a superuser:**
```
python manage.py createsuperuser
```

7.**Run the development server:**
```
python manage.py runserver
```

8.Open the app in your browser at http://127.0.0.1:8000/.

### Usage :
- Sellers: Register as a seller, log in, and start adding products.
- Buyers: Register as a buyer, browse products, add them to your cart, proceed to checkout, and track your orders.

### Technologies Used:
- Django: Backend framework
- PostgreSQL: Database (or any other database)
- Bootstrap: Frontend framework for responsive UI
- AWS S3: For storing product images (Optional)
- Stripe/PayPal: For payment gateway (Optional)
