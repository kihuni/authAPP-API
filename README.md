# 🛡️ AuthAPI — Django REST Authentication with Djoser

This project sets up a user authentication system using **Django**, **Django REST Framework**, and **Djoser** for token-based authentication and password reset functionality.

---

## 🚀 Features (In Progress)

- ✅ User Signup
- ✅ User Login with Token Authentication
- ✅ User Logout
- ✅ Password Reset via Email (Console backend)
- 🔄 Email-based password reset confirmation via UID and token
- 🔒 Secure password hashing and write-only password field
- 📦 Djoser integrated for standardized auth endpoints

---

---

## ⚙️ Setup Instructions

### 1. Clone the repo

```
https://github.com/kihuni/authAPP-API.git
cd authapi

```
### 2. Create virtual environment & install dependencies

```
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
pip install -r requirements.txt

```
### 3 Install requirements

```
pip install -r requirements.txt

```
### 4. Run migrations

```
python manage.py makemigrations
python manage.py migrate

```
### 5. Run the server

```
python manage.py runserver

```
### 🔐 Authentication Endpoints

| Endpoint                        | Method | Description                       |
| ------------------------------- | ------ | --------------------------------- |
| `/signup/`                      | POST   | Custom user registration          |
| `/login/`                       | POST   | Custom user login (token)         |
| `/logout/`                      | POST   | Custom user logout (token delete) |
| `auth/users/reset_password/`         | POST   | Request password reset            |
| `/auth/users/reset_password/confirm/` | POST   | Reset password using token+uid    |


### 🧪 Testing Password Reset (Console)
1. Send a POST to auth/users/reset_password/ with your email.

2. Check the terminal for the reset link.

3. Extract uid and token from the link.

4. Send a POST to /auth/users/reset_password/confirm/ with:

```
{
  "uid": "<uid_from_link>",
  "token": "<token_from_link>",
  "new_password": "yourNewPassword123"
}

```

###  📬 Email Configuration (Dev)

In settings.py:

```
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

```

### 🔧 Tech Stack

- Django

- Django REST Framework

- Djoser

- SQLite (default for dev)
