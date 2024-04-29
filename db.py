import mysql.connector as mysql
from modal import User, Account

# Setup connection to the database
db = mysql.connect(user="root", database="bank", password="dhruv2007")


def add_user(user: User):
    # Create cursor
    cursor = db.cursor()

    # Execute query
    query = "INSERT INTO user (name, email, password) VALUES (%s, %s, %s)"
    queryParameters = [user.name, user.email, user.password]
    cursor.execute(query, queryParameters)

    # Commit changes
    db.commit()

    # Close cursor
    cursor.close()


def get_user_by_email(email: str) -> User:
    # Create cursor
    cursor = db.cursor()

    # Execute query
    query = "SELECT * FROM user WHERE email = %s"
    cursor.execute(query, [email])

    # Get results
    result = cursor.fetchone()

    # Close cursor
    cursor.close()

    # Return result
    return User(result[0], result[1], result[2], result[3])


def create_user_account(user: User, newAccount: Account):
    # Insert the new account into our database
    cursor = db.cursor()

    # Execute query
    query = "INSERT INTO account (account_number, routing_number, balance, user_id, type) VALUES (%s, %s, %s, %s, %s)"
    queryParameters = [
        newAccount.account_number,
        newAccount.routing_number,
        newAccount.balance,
        user.user_id,
        newAccount.account_type,
    ]
    cursor.execute(query, queryParameters)

    # Commit changes
    db.commit()

    # Close cursor
    cursor.close()


def get_user_account(user: User, accountType: str) -> Account:
    # Create cursor
    cursor = db.cursor()

    # Execute query
    query = "SELECT * FROM account WHERE user_id = %s AND type = %s"
    queryParameters = [user.user_id, accountType]
    cursor.execute(query, queryParameters)

    # Get results
    result = cursor.fetchone()

    # Close cursor
    cursor.close()

    # Return result
    return Account(result[0], result[1], result[2], result[3], result[5], result[4])


def update_account_balance(accountID, newBalance):
    # Create cursor
    cursor = db.cursor()

    # Execute query
    query = "UPDATE account SET balance = %s WHERE id = %s"
    queryParameters = [newBalance, accountID]
    cursor.execute(query, queryParameters)

    # Commit changes
    db.commit()

    # Close cursor
    cursor.close()
