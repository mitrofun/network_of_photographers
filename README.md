# Network of photographers

[![Build Status](https://travis-ci.org/mitrofun/network_of_photographers.svg?branch=master)](https://travis-ci.org/mitrofun/network_of_photographers)

Test task. Make a small social network for photographers.

We have countries, cities, things, users. Each type has a different set of fields.
Each type entity can have multiple photos.
The photo can be either approved by the administrator or not.

## Installation
```bash
git clone https://github.com/mitrofun/network_of_photographers.git
```

## Run

### Local develop
```bash
cd network_of_photographers
pip3 install -r requirements.txt
```

#### Migration
After roll migration
```bash
python3 manage.py migrate
```

#### Create admin
Create administrator with username `admin` and password `admin` 
```bash
python3 manage.py createadminuser
```

#### Run develop server
After run develop server
```bash
python3 manage.py runserver
```

##Tests

For run test use the following commands
```bash
pytest
```
Check style code run command 
```bash
flake8
```

## Requirements
- python 3.6+
- Django 3+
- see all requirements in requirements.txt
