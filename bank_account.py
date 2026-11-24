class Account:
    existing=[]
    def __init__(self,acc_num,name,balance):
        if acc_num in Account.existing:
            raise ValueError("Account already exists")

        if balance < 0:
            raise ValueError("Initial balance cannot be negative")
        if balance == 0:
            raise ValueError("Account can't be created with zero balance")
        
        self.acc_num = acc_num
        self.name = name
        self.balance = balance
        Account.existing.append(acc_num)
        print("Account created successfully.")

    def deposit(self,amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero")
        self.balance+= amount
        print("Amount deposited successfully. New balance is:",self.balance)

    def withdraw(self,amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero")
        if amount>self.balance:
            print("Not enough balance")
        else:
            self.balance-=amount
            print("Amount withdrawn successfully. New balance is:",self.balance)

    def check_balance(self):
        return self.balance

    def display(self):
        print("Your account details:")
        print("Account Number:",self.acc_num)
        print("Account Holder Name:",self.name)
        print("Account Balance:",str(self.balance)+" BDT")
def main():
        acc_num=input("Enter your account number: ")
        name=input("Enter your name: ")
        balance=float(input("Enter your initial balance: "))
        

        account=Account(acc_num,name,balance)
        while True:
            print("\nMenu:")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Display Account Details")
            print("5. Exit")
            choice=int(input("Enter your choice: "))
            
            if choice==1:
                amount=float(input("Enter the amount to deposit: "))
                account.deposit(amount)

            elif choice==2:
                amount=float(input("Enter the amount to withdraw: "))
                account.withdraw(amount)


            elif choice==3:
                print("Your current balance is:",account.check_balance())

            elif choice==4:
                account.display()

            elif choice==5:
                print("You have exited the program.")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__=="__main__":
    main()