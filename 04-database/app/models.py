from typing import Optional
import sqlalchemy as sa 
import sqlalchemy.orm as so 
from app import db

class User(db.Model):
    id = sa.Column(sa.Integer, primary_key=True)
    username = sa.Column(sa.String(80), unique=True, index=True)
    email = sa.Column(sa.String(120), unique=True, index=True)
    password_hash = sa.Column(sa.String(256))

    def __repr__(self):
        return '<User {}>'.format(self.username)