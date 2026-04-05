from enum import Enum

class UserRole(str,Enum):
    ADMIN = "admin"
    ANALYST = "analyst"
    VIEWER = "viewer"

class RecordType(str, Enum):
    INCOME = "income"
    EXPENSE = "expense"


class RecordCategory(str, Enum):
    SALARY = "salary"
    INVESTMENT = "investment"
    UTILITIES = "utilities"
    RENT = "rent"
    FOOD = "food"
    TRANSPORT = "transport"
    HEALTHCARE = "healthcare"
    ENTERTAINMENT = "entertainment"
    OTHER = "other"

''' To ensure data integrity the record categories are defined by strict enums, with an 
other field in case the category is not listed'''
