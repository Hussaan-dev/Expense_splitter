# Expense Splitter

A Django web app to split shared expenses among groups of friends. Built to track who owes who after group trips or shared bills.

**Live demo:** https://expense-splitter-hussaan.up.railway.app/

## Features

- User registration and login
- Create groups and add members
- Log expenses within a group
- Expenses split equally among group members automatically
- Balance summary showing who owes who
- Mark individual splits as paid
- Edit and delete groups and expenses
- REST API built with Django REST Framework

## Tech Stack

- Python, Django
- SQLite (PostgreSQL on production)
- Django REST Framework
- Tailwind CSS for styling
- Deployed on Railway

## How It Works

1. Create a group and add friends as members
2. Log an expense — who paid and how much
3. The amount is split equally among all members automatically
4. The group page shows who owes who, updated in real time
5. Mark a split as paid once it's settled

## Run It Locally

```bash
git clone https://github.com/Hussaan-dev/Expense_splitter.git
cd Expense_splitter
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Known Limitations

- Splits are always equal — no custom split amounts yet
- Group members can't be edited after creation (avoids breaking existing splits)
- Amounts don't support decimals (PKR doesn't typically use them)

## Notes

CSS was generated with AI assistance using Tailwind utility classes to keep focus on backend logic.

## Author

Built by Hussaan as a capstone project