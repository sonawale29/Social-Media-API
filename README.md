# Social Media API

This is a **Social Media API** that allows users to register, login, create posts, like posts, and comment on posts. The API provides user management and post management features with authentication, authorization, and error handling.

## Table of Contents

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Postman Collection](#postman-collection)
- [Database Dump](#database-dump)
- [Contributing](#contributing)
- [License](#license)

## Description

The Social Media API allows users to:
- Register an account.
- Create, edit, and delete posts.
- Like and comment on posts.
- Retrieve user profiles and post details.

## Installation

### Prerequisites

- Python 3.x
- Django
- Django REST Framework
- PostgreSQL (or other DB)

### Steps to Install

1. Clone the repository:
   
   git clone https://github.com/sonawale29/Social-Media-API.git

2. Navigate to the project directory:
cd repository
3. Set up the virtual environment:
python -m venv venv
4. Activate the virtual environment:

.\venv\Scripts\activate
5. Install dependencies:

pip install -r requirements.txt

Run migrations:

python manage.py migrate
6. Run the development server:

python manage.py runserver
Usage
To interact with the API, you can use Postman and the provided Postman collection file.
You can make requests to the local server: http://127.0.0.1:8000/.
