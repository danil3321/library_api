from datetime import date
from pydantic import BaseModel
from typing import List, Optional

class AuthorBase(BaseModel):
    name: str
    biography: Optional[str] = None
    birth_date: Optional[date] = None

class AuthorCreate(AuthorBase):
    pass

class Author(AuthorBase):
    id: int
    books: List[int] = []

    class Config:
        orm_mode = True

class BookBase(BaseModel):
    title: str
    description: Optional[str] = None
    publication_date: Optional[date] = None
    genre: Optional[str] = None
    available_copies: int

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int
    authors: List[Author] = []

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    username: str
    role: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

class BorrowingBase(BaseModel):
    user_id: int
    book_id: int
    borrow_date: date
    return_date: Optional[date] = None

class BorrowingCreate(BorrowingBase):
    pass

class Borrowing(BorrowingBase):
    id: int
    user: User
    book: Book

    class Config:
        orm_mode = True
