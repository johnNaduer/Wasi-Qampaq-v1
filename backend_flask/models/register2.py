#!/usr/bin/python3

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from .base_model2 import Base, basemodel


class register(basemodel, Base):
    __tablename__ = 'register2'
    name = Column(String(120), nullable=False)
    email = Column(String(60), nullable=False)
    password = Column(String(120), nullable=False)
    password_2 = Column(String(120), nullable=False)
