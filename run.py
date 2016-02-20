#!/usr/bin/env python
from os import environ

from website import app, db

db.create_all()
app.run(host='0.0.0.0', port=8000)
