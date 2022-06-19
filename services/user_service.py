from typing import Tuple
from models.db import USERS
from models.model import User

class UserService:
    def get_user(self, username: str) -> bool:
        """Gets user from database"""
        return USERS.get(username)
        
    def create_user(self, username) -> User:
        """Creates new user and saves in database"""
        print("Kindly provide your information so you can create an account.")
        first_name, last_name, email = self._get_user_details()
        name = f"{first_name} {last_name}"
        USERS[username] = User(name=name, email=email)
        return USERS[username]

    def _get_user_details(self) -> Tuple:
        """Get user details."""
        first_name = input("Kindly provide your first name: ")
        last_name = input("Kindly provide your last name: ")
        email = input("Kindly provide your email: ")
        return first_name, last_name, email