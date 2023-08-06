# Nettruyen scraping

Project to scrape comic data from "nettruyen" and save data to Mysql

## Install libs

run command in your terminal

```python
pip install -r requirements.txt
```

## Setup database

change the ".env.example" file to ".env" and import environment variables in .env file

- example

```md
# Database

DB_HOST="localhost"
DB_PORT=3306
DB_USER="root"
DB_PASSWORD=""
DB_DATABASE="nettruyen_db"

# Website

WEBSITE_URL="https://www.nettruyenio.com/"
```

- Create database

Create database in Mysql with name same value of "DB_DATABASE" above

- Create tables

Run command in terminal

```python
py database/create_tables.py
```
