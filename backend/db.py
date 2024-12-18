from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey, Float
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine("sqlite:///ecomnerct.db", echo=True)


SessionLocal = sessionmaker(bind=engine)


Base = declarative_base()
