Online Code Editor with Django & Python Execution

## Overview

This project is a simple yet functional web-based code editor built using *Django* and *Django REST Framework*. It enables users to write, execute, and save Python code directly from a browser interface.

## Features

* 🔐 *User Authentication*

  * User registration and login system
  * Authenticated users can create and view their own code snippets

* 🧠 *Code Execution*

  * Python code execution using subprocess module
  * Captures standard output and errors
  * Execution timeout protection for safety

* 💾 *Code Snippet Storage*

  * Save and retrieve previous code snippets
  * Snippets are associated with the authenticated user

* 🌐 *REST API Integration*

  * Fully functional REST API using Django REST Framework
  * Allows external apps to interact with the code editor

* 🖼️ *Simple Frontend UI*

  * HTML-based frontend for testing code execution
  * Interactive interface for submitting code and viewing output

## Tech Stack

* *Backend:* Django, Django REST Framework
* *Frontend:* HTML, JavaScript (basic)
* *Database:* PostgreSQL (or SQLite for local testing)
* *Language Support:* Python (extendable to others)

## How It Works

1. Users register or log in to the system.
2. Authenticated users can input Python code in the editor.
3. When submitted, the code is sent to the server via an API.
4. The server safely executes the code and returns the output or error.
5. Users can also view a list of their previously executed snippets.

**###Run the development server:**

   python manage.py runserver
