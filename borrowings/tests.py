from datetime import date, timedelta

from django.test import TestCase

from books.models import Book
from borrowings.models import Borrowing

BORROWINGS_URL = "/api/borrowings/"

def sample_book(**params):
    defaults = {
        "title": "Test Book",
        "author": "Test Author",
        "cover": "SOFT",
        "inventory": 5,
        "daily_fee": 1.50,
    }
    defaults.update(params)
    return Book.objects.create(**defaults)

def sample_borrowing(user, book, **params):
    defaults = {
        "borrow_date": date.today(),
        "expected_return_date": date.today() + timedelta(days=7),
        "book": book,
        "user": user,
    }
    defaults.update(params)
    return Borrowing.objects.create(**defaults)