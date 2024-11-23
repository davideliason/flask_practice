Inside flask container, we have requirements.txt which lists required modules to install. 
These include:
alembic # database migration
Faker   # fake data to populate tables
Flask   # back-end tool
Flask-Migrate 
Flask-SQLAlchemy
psycopg2-binary
SQLAlchemy

It is psycopg2 that I am looking at with this file.
$ mkdir psycopg2 & cd psycopg2
$ touch veggies.py
# inside that file, include the file code found in this subfolder
