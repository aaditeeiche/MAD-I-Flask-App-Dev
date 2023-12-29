import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy import select

from sqlalchemy.orm import Session
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship

# Create Base Class for the Model
Base = DeclarativeBase()

# Create Table User as Base Class
class User(Base): # extends Base
    __tablename__ = 'user' # should be the same table name as in the database
    user_id = Column(Integer, autoincrement=True, primary_key=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)

# Create Table Article as Base Class
class Article(Base):
    __tablename__ = 'article'
    article_id = Column(Integer, autoincrement=True, primary_key=True)
    title = Column(String)
    content = Column(String)

# Create Table ArticleAuthors as Base Class
class ArticleAuthors(Base):
    __tablename__ = 'article_authors'
    user_id = Column(Integer, ForeignKey("user.user_id"), primary_key=True, nullable=False)
    article_id = Column(Integer, ForeignKey("article.article_id"), primary_key=True, nullable=False)
    # Define many-to-many relationship 
    authors = relationship("User", secondary="article_authors")

# Connect to the database by creating engine by giving us a collection pool and dialect to talk to the db
engine = create_engine("sqlite:///./testdb.sqlite3")