from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
 
DB_USER = 'root'
DB_PASSWORD = 'Abcdefghijklmnop_'
DB_HOST = 'localhost'
DB_PORT = '3306'
DB_NAME ='agdb1'

DB_URL = f'mysql+pymysql://root:Abcdefghijklmnop_@localhost:3306/agdb1'
 
engine = create_engine(DB_URL)
sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()