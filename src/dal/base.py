#This file is used to create a base class for the database models,it's base module for SqlAlchemy ORM models.
# This module defines the `Base` class, which serves as the foundation for all ORM models
# in the project. Every model should inherit from `Base` to be automatically recognized
# by SQLAlchemy when creating or managing database tables.

from sqlalchemy.orm import declarative_base

# Create a base class for all ORM models
Base = declarative_base()