# EShopper

EShopper is an e-commerce web application that provides a modern and user-friendly online shopping experience. This platform allows users to browse products, add items to their cart, and complete purchases securely.

## 📋 Features

- **Responsive Design**: Mobile-friendly interface that works across devices
- **Product Catalog**: Browse products by categories
- **Shopping Cart**: Add and manage items in your cart
- **User Authentication**: Create accounts and login securely
- **Product Search**: Find products quickly with search functionality
- **Order Management**: Track and manage your orders
- **Payment Integration**: Secure payment processing

## 🚀 Technology Stack

- **Frontend**: 
  - HTML (24.6%)
  - CSS (42.1%)
  - JavaScript (21.5%)
  - Bootstrap framework
  
- **Backend**:
  - Python (11.8%)
  - Django framework
  - SQLite/PostgreSQL database

## 🛠️ Installation and Setup

### Prerequisites

- Python 3.8+
- pip (Python package manager)
- Git

### Steps to Setup

1. Clone the repository
   ```
   git clone https://github.com/yehorkarabanov/EShopper.git
   cd EShopper
   ```

2. Set up Python virtual environment
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install Python dependencies
   ```
   pip install -r requirements.txt
   ```

4. Set up database
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Create an admin user
   ```
   python manage.py createsuperuser
   ```

6. Run the development server
   ```
   python manage.py runserver
   ```

7. Access the application at `http://localhost:8000`

## 📚 Usage

1. Register a new account or login with existing credentials
2. Browse products by categories
3. Use the search feature to find specific items
4. Add products to your shopping cart
5. Review your cart and proceed to checkout
6. Complete your purchase with the available payment options
7. View your order history in the user dashboard

## 🔧 Project Structure

- `/static/` - Static files (CSS, JavaScript, images)
- `/templates/` - HTML templates
- `/app/` - Django application code
- `/media/` - User-uploaded content

## 📊 Admin Dashboard

Access the admin panel at `/admin` to:
- Manage products and categories
- View and update user accounts
- Process orders
- Configure site settings

## 🧪 Testing

Run tests with the following command:
```
python manage.py test
```

## 📝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📞 Contact

Yehor Karabanov - [GitHub](https://github.com/yehorkarabanov)

Project Link: [https://github.com/yehorkarabanov/EShopper](https://github.com/yehorkarabanov/EShopper)
