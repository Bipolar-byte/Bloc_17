from app.backend.db import engine
from app.models import User, Task

from sqlalchemy import MetaData

metadata = MetaData()
metadata.create_all(bind=engine)