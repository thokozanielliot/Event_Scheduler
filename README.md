# Event Scheduling System API

## Overview

This a system for scheduling events. Each user is able to to add, delete, edit and view their scheduled events.
This project was built using Django and Django Rest Framework and contains the following:
- Allows new accounts registration
- Create, edit and delete any events

## Prerequisites

- Git [https://git-scm.com/downloads]
- Python version 3.10.6 [https://www.python.org/downloads/]
- VS Code [https://code.visualstudio.com/download]
- Postman [https://www.postman.com/downloads/]

Using `pip`command, install the following Python packages in the `requirements.txt` file:
```
pip install -r requirements.txt
```

## Cloning

Run the following command to clone this repository
```
git clone https://github.com/thokozanielliot/
```

## Running The Code

Navigate to the `src` folder and run the following commands:
```
cd src
python manage.py makemigrations
python manage.py migrate
```
Running the server:
```
python manage.py runserver
```

- Posting an Event Or Viewing all Events
    - `http://127.0.0.1:8000/events/`

- Editing, Deleting an Event Or Accessing an Event
    - `http://127.0.0.1:8000/events/pk`
    - Example `http://127.0.0.1:8000/events/1`
