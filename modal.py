class User:
    def __init__(self, user_id, name, email, password):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password

    def __str__(self):
        return f"User: {self.name} - {self.email} - {self.password}"


class Account:
    def __init__(
        self, accountId, accountNumber, routingNumber, balance, userId, accountType
    ):
        self.accountId = accountId
        self.accountNumber = accountNumber
        self.routingNumber = routingNumber
        self.balance = balance
        self.userId = userId
        self.accountType = accountType

    def __str__(self):
        return f"Account: {self.accountNumber} - {self.balance} - {self.userId} - {self.accountType}"
