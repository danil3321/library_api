from sqlalchemy import Column, Integer, String, ForeignKey, Date, Table
from sqlalchemy.orm import relationship
from app.database import Base

# Ассоциативная таблица для связи многие-ко-многим (книга <-> автор)
book_author = Table(
    "book_author",
    Base.metadata,
    Column("book_id", Integer, ForeignKey("books.id"), primary_key=True),
    Column("author_id", Integer, ForeignKey("authors.id"), primary_key=True),
)

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    publication_date = Column(Date)
    genre = Column(String)
    available_copies = Column(Integer, default=1)

    authors = relationship("Author", secondary=book_author, back_populates="books")

class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    biography = Column(String)
    birth_date = Column(Date)

    books = relationship("Book", secondary=book_author, back_populates="authors")

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(String, default="reader")  # "admin" или "reader"

class Borrowing(Base):
    __tablename__ = "borrowings"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    book_id = Column(Integer, ForeignKey("books.id"))
    borrow_date = Column(Date)
    return_date = Column(Date)

    user = relationship("User")
    book = relationship("Book")
