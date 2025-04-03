# scraper

A Simple Selenium based program that works on scraping student data from PESU Academy for the [PES25 Bot](https://github.com/alfadelta10010/pesu-bot-2025)

## Setup
- You'll need MariaDB installed:
```bash
sudo apt install mariadb-server libmariadb-dev
sudo systemctl start mariadb
sudo systemctl enable mariadb
```
- Run the following commands to set up the python environment
```bash
pyenv virtualenv <3.x> scraper
pyenv activate scraper
pip install -r requirements.txt
```
- Run the following for database setup:
```bash
sudo mysql -u root -p
```
```sql
CREATE DATABASE pes_people;
CREATE USER 'pes_people_bot'@'localhost' IDENTIFIED BY 'super_secure_password';
SELECT User, Host FROM mysql.user WHERE User = 'pes_people_bot';
GRANT ALL PRIVILEGES ON pes_people.* TO 'pes_people_bot'@'localhost';
FLUSH PRIVILEGES;
SHOW GRANTS FOR 'pes_people_bot'@'localhost';
```
- If you change any of the names, remember to modify the [program](scraper.py)

## Usage

```bash
python3 scraper <rr or ec> <year>
```

## Tech stack

Selenium, Python

## How it works

The scraper goes to PESU Academy, uses the `Know your section` tool, and enters a PRN. Once done, it sends that, and copies details from the result table. Saves it to a SQL Database.
