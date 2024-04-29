import random
from db import (
    get_user_by_email,
    create_user_account,
    add_user,
    get_user_account,
    update_account_balance,
)
from modal import Account, User


def create_new_user(user_name, user_email, user_password):
    # Create a new User model
    new_user = User(None, user_name, user_email, user_password)

    # Persist new user in the database
    add_user(new_user)

    print(f"Created new user: {new_user}")


def create_new_account(user_email, account_type):
    # Get user from the database by email
    user = get_user_by_email(user_email)

    # Generate randomized account and routing numbers
    new_account_number = str(random.randint(100000000, 999999999))
    new_routing_number = str(random.randint(100000000, 999999999))

    # Create a new Account model representing the user's new account
    new_account = Account(
        None, new_account_number, new_routing_number, 0, user.user_id, account_type
    )

    # Create user account
    create_user_account(user, new_account)

    print(f"Created new account: {new_account}")


def get_account(user_email, account_type) -> Account:
    # Get user from the database by email
    user = get_user_by_email(user_email)

    # Get account from database for the given user and account type
    return get_user_account(user, account_type)


def deposit_into_account(user_email, account_type, deposit_amount):
    # Get account from database for the given user and account type
    account = get_account(user_email, account_type)

    # Update account balance
    new_balance = account.balance + deposit_amount

    # Update account in database
    update_account_balance(account.account_id, new_balance)

    print(f"Deposited ${deposit_amount} into account {account.account_number}")
