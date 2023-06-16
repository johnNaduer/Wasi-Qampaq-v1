#!/usr/bin/python3

import json
import uuid
import models
from sys import argv
from os.path import isfile
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, DateTime
from datetime import datetime

Base = declarative_base()

class basemodel:
    __tablename__ = 'base_model'
    id = Column(String(60), primary_key=True, nullable=False)
    """
    created_at = Column(DateTime, default=datetime.utcnow)
    """
    def __init__(self, **kwargs):
        """
        self.id = str(uuid.uuid4())
        
        self.created_at = datetime.utcnow()
        """
        for key, value in kwargs.items():
            setattr(self, key, value)        
        """
        self.kwargs = kwargs
        """
        models.estorage.new(self)
