# Alotr


[![Build Status](https://travis-ci.org/your-username/your-app-name.svg?branch=master)](https://travis-ci.org/your-username/your-app-name)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## Description

A course allocation and management platform for Uganda Technology And Management University.

## Table of Contents

- [Installation](##installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. First, clone this repository to your local machine:

```bash
git clone https://github.com/jod35/allotr.git
cd allotr
```


2. Set up a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

4. Apply the database migrations:
```bash

python manage.py migrate
```

5. Create a superuser (admin) to access the Django Admin interface:
```bash

python manage.py createsuperuser
```

6. Run the development server:
```bash

python manage.py runserver
```

Now your application should be up and running at ${window.location.origin}/

## Usage
Explain how to use your application here. Provide examples and screenshots if applicable.

## Configuration
List any additional configuration settings or environment variables required for your application.

## Contributing
Contributions are welcome! If you find any issues or want to add new features, please follow these steps:

- Fork the repository.
- Create a new branch for your feature: 
```bash 
git checkout -b feature-name
```
- Commit your changes: 
```bash 
git commit -m 'Add some feature'
```
- Push the branch to your fork: 
```bash 
git push origin feature-name
```
- Create a pull request.