# app/db/init_db.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from app.db.base import Base
from app.db.session import engine
from app.models import post

def init():
    print("📦 Creating tables...")
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init()
