# ConstructionMart — Civil Engineering Materials Purchase Website

Project engineer: Vinoth Kumar

A starter Django project for browsing construction materials, calculating prices, managing a shopping cart, and submitting sample orders.

## Features
- Product catalogue: cement, steel, bricks, sand and aggregates
- Search and category filters
- Quantity and price calculator on product cards
- Session-based shopping cart
- Demo checkout with Google Pay (UPI), PhonePe (UPI), and cash-on-delivery selection
- Order confirmation showing the selected payment method
- Admin interface for managing products and orders
- Responsive layout

## Run on Windows
1. Install Python 3.10+.
2. Extract the ZIP and open a terminal inside the `ConstructionMart` folder.
3. Create and activate a virtual environment:
   ```bat
   py -m venv venv
   venv\Scripts\activate
   ```
4. Install dependencies:
   ```bat
   pip install -r requirements.txt
   ```
5. Create the database tables:
   ```bat
   python manage.py migrate
   ```
6. Load demo products:
   ```bat
   python manage.py seed_products
   ```
7. Start the development server:
   ```bat
   python manage.py runserver
   ```
8. Open http://127.0.0.1:8000/

## Admin login
Create your own admin user with:
```bat
python manage.py createsuperuser
```
Then open http://127.0.0.1:8000/admin/

## Deploy to Render
1. Push this project to a GitHub or GitLab repository.
2. In Render, create a PostgreSQL database and copy its internal connection URL.
3. Create a Blueprint from the repository containing `render.yaml`.
4. When prompted, set `DATABASE_URL` to the PostgreSQL connection URL. Render generates `SECRET_KEY`; the Blueprint sets `DEBUG=false`.
5. Deploy. The build collects static files; the start command applies database migrations, loads the sample products, and starts Gunicorn.

The Blueprint uses Render's free web-service plan. Free services can spin down when idle, and their local filesystem is not persistent. Use PostgreSQL for data you need to keep; Render database plans and retention limits can change, so check current pricing and retention before creating a database. The payment choices are for demonstration only: Google Pay and PhonePe do not process UPI payments, and cash on delivery does not arrange a real delivery.

## Important
This is a learning/demo project. Checkout does not collect real payments and does not contact real suppliers. Prices and stock are sample values. Before production use, add authentication, payment gateway integration, delivery policies, security review, and verified supplier/material information.
