#Classes: Challenge
import os
import sys

class BankAccount():
    net_pos = 0
    sum_overdraft = 0

    # initialise with defaults set at zero
    def __init__(self, account_type="", balance=0, overdraft_fees=0):
        self.account_type = account_type
        self.balance = balance
        self.overdraft_fees = overdraft_fees
        BankAccount.net_pos += balance

    def withdraw(self, amount):
        self.balance -= amount
        # if withdrawal ends with the balance below zero, overdraft is applied
        if (self.balance - self.overdraft_fees) < 0:
            self.overdraft_fees += 20
            # adds to overdraft to the combined overdraft sum
            BankAccount.sum_overdraft += 20
            BankAccount.net_pos -= (amount + 20)
        # if withdrawal ends with balance above zero, overdraft is not applied
        else:
            BankAccount.net_pos -= amount
        
    def deposit(self, amount):
        self.balance += amount
        BankAccount.net_pos += amount

def clear_screen():
    if sys.platform  == 'win32':
        clear = 'cls'
    else:
        clear = 'clear'
    return clear

# refreshes screen with current account status
def screen(accounts):
    os.system(clear_screen())   
    print("These are your accounts:")
    for key, value in accounts.items():
        if value.overdraft_fees == 0:
            print(str(value.account_type) + " = " + str(value.balance))
        else:
            print(str(value.account_type) + " = " + str(value.balance) 
                  + " plus overdraft fees of " + str(value.overdraft_fees))
    print("\nTotal overdraft fees paid =", BankAccount.sum_overdraft, 
          "\nNet position for all accounts =", BankAccount.net_pos)

def transaction():
    screen(accounts)
    line_one = "Select 0 for new account. "
    for key, value in accounts.items():
        line_one += ("Select {} for {}. ".format(key, value.account_type))
    inp_one = int(input(line_one))
    # creates new account and adds it to the accounts dictionary
    if inp_one == 0:
        new_account = BankAccount(input("Name your new account: "))
        accounts[(len(accounts) + 1)] = new_account
        inp_two = int(input(
                    "\n{} account selected\nSelect 1 to withdraw or 2 to deposit: "
                    .format(new_account.account_type)))
        if inp_two == 1:
            inp_three = float(input("How much to withdraw?: "))
            new_account.withdraw(inp_three)
        elif inp_two == 2:
            inp_three = float(input("How much to deposit?: "))
            new_account.deposit(inp_three)
    # selects an existing account from accounts dictionary
    elif inp_one in accounts:
        inp_two = int(input(accounts[inp_one].account_type 
                          + " selected\nSelect 1 to withdraw or 2 to deposit: "))
        if inp_two == 1:
            inp_three = float(input("How much to withdraw?: "))
            accounts[inp_one].withdraw(inp_three)
        elif inp_two == 2:
            inp_three = float(input("How much to deposit?: "))
            accounts[inp_one].deposit(inp_three)
    # breaks out of program
    elif inp_one == 9:
        os.exit(1)

if __name__ == "__main__":
    savings = BankAccount("Savings")
    checking = BankAccount("Checking")
    accounts = {1: savings, 2: checking}
    while True:
        transaction()