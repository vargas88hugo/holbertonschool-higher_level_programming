#!/usr/bin/python3
"""
This script contains the State class
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from model_state import State

Base = declarative_base()


class City(Base):
    """
    This class links to the MySQL table cities
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, foreign_keys=("states.id"), nullable=False)
