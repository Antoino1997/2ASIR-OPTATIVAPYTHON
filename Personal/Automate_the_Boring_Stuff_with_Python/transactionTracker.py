def after_transaction(balance, transaction):
    change = balance + transaction

    if change < 0:
        return balance
    else:
        return change

print("Balance:")
user_balance = int(input())
print("Transaction:")
user_transaction = int(input())

final_result = after_transaction(user_balance, user_transaction)

print(f"Your balance is: {final_result}")