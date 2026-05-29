<div align="center">

# 🐦 TweetBar

### *A Twitter-inspired social platform built with Django*

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Django](https://img.shields.io/badge/Django-6.0-092E20?style=for-the-badge&logo=django&logoColor=white)](https://djangoproject.com)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)](https://getbootstrap.com)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)]()

<br/>

> 💬 **Share your thoughts. Connect with people. Explore trending conversations.**

<br/>

![TweetBar Banner](./media/tweetbar_screenshot.png)

</div>

---

## 📋 Table of Contents

- [✨ Features](#-features)
- [🛠️ Tech Stack](#️-tech-stack)
- [🚀 Getting Started](#-getting-started)
- [📁 Project Structure](#-project-structure)
- [🔗 URL Routes](#-url-routes)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)

---

## ✨ Features

| Feature | Description |
|---|---|
| 🔐 **Authentication** | Register, login & logout securely |
| 📝 **Tweet CRUD** | Create, edit, and delete your tweets |
| 👍 **Like / 👎 Dislike** | React to any tweet in real time |
| 🖼️ **Media Uploads** | Attach images to your tweets |
| 👤 **User Profiles** | Personalized user experience |
| 📱 **Responsive UI** | Mobile-friendly Bootstrap layout |
| 🔒 **Access Control** | Auth-protected routes & views |
| ⚙️ **Django Admin** | Full admin panel included |

---

## 🛠️ Tech Stack

**Backend**
- 🐍 Python 3.10+
- 🌐 Django 6.0
- 🗄️ SQLite (default) / PostgreSQL ready

**Frontend**
- 🎨 Bootstrap 5
- 🧩 Django Templates
- 🖼️ HTML5 / CSS3

**Tools & Utilities**
- 🔧 Django Auth (built-in)
- 📂 Django Media / Static Files
- 🛡️ CSRF Protection

---

## 🚀 Getting Started

### ✅ Prerequisites

Make sure you have the following installed:

- Python 3.10+
- pip
- git

### 📦 Installation

**1. Clone the repository**

```bash
git clone https://github.com/your-username/tweetbar.git
cd tweetbar
```

**2. Create and activate a virtual environment**

```bash
# On macOS/Linux
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Apply migrations**

```bash
cd twitter_app
python manage.py makemigrations
python manage.py migrate
```

**5. Create a superuser (optional)**

```bash
python manage.py createsuperuser
```

**6. Run the development server**

```bash
python manage.py runserver
```

**7. Open in browser**

```
http://127.0.0.1:8000/
```

---

## 📁 Project Structure

```
tweetbar/
│
├── twitter_app/
│   ├── manage.py                  # Django management script
│   ├── requirements.txt           # Python dependencies
│   │
│   ├── twitterapp/                # Main project config
│   │   ├── settings.py            # Project settings
│   │   ├── urls.py                # Root URL configuration
│   │   └── wsgi.py / asgi.py      # Deployment entrypoints
│   │
│   ├── tweet/                     # Core tweet application
│   │   ├── models.py              # Tweet & reaction models
│   │   ├── views.py               # View logic
│   │   ├── forms.py               # Tweet forms
│   │   ├── urls.py                # Tweet URL patterns
│   │   ├── admin.py               # Admin registration
│   │   └── templates/             # HTML templates
│   │       ├── layout.html        # Base template
│   │       ├── index.html         # Landing page
│   │       └── registration/      # Auth templates
│   │
│   └── media/                     # Uploaded media files
```

---

## 🔗 URL Routes

| Method | URL | Description |
|---|---|---|
| `GET` | `/` | 🏠 Home / Landing page |
| `GET` | `/tweet/` | 📋 View all tweets |
| `GET/POST` | `/tweet/create/` | ✏️ Create a new tweet |
| `GET/POST` | `/tweet/<id>/edit/` | 📝 Edit a tweet |
| `POST` | `/tweet/<id>/delete/` | 🗑️ Delete a tweet |
| `POST` | `/tweet/<id>/like/` | 👍 Like a tweet |
| `POST` | `/tweet/<id>/dislike/` | 👎 Dislike a tweet |
| `GET/POST` | `/register/` | 📋 User registration |
| `GET/POST` | `/login/` | 🔑 User login |
| `GET/POST` | `/logout/` | 🚪 User logout |
| `GET` | `/admin/` | ⚙️ Django admin panel |

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. 🍴 Fork the repository
2. 🌿 Create a new branch (`git checkout -b feature/your-feature`)
3. 💾 Commit your changes (`git commit -m 'Add some feature'`)
4. 📤 Push to the branch (`git push origin feature/your-feature`)
5. 🔃 Open a Pull Request

Please make sure your code follows PEP 8 standards and includes relevant tests.

---

## 🐛 Found a Bug?

If you find a bug or want to request a feature, please [open an issue](https://github.com/your-username/tweetbar/issues) with:

- 🔍 A clear description of the problem
- 🔁 Steps to reproduce
- 💻 Your environment (OS, Python version, etc.)

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 👩‍💻 Author

**Prabhleen Kaur**

[![GitHub](https://img.shields.io/badge/GitHub-Prabhleen--kaur--r-181717?style=flat-square&logo=github)](https://github.com/Prabhleen-kaur-r)
[![Email](https://img.shields.io/badge/Email-rkaurprabhleen%40gmail.com-D14836?style=flat-square&logo=gmail&logoColor=white)](mailto:rkaurprabhleen@gmail.com)

---

<div align="center">

⭐ **If you found this project useful, please consider giving it a star!** ⭐

Made with ❤️ and Django

</div>
