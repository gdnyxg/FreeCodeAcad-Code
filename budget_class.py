class Category:
    def __init__(self, name: str, ledger = None):
    #initialisation method
        self.name = name
        self.ledger = [] if ledger is None else ledger
        self.balance = 0.0

    def __str__(self):
        # Title line
        title = f"{self.name:*^30}\n"
        # Ledger lines
        items = ""
        for entry in self.ledger:
            # max 23 chars
            description = entry["description"][:23]  
            # format and truncate
            amount = f"{entry['amount']:.2f}"[:7]   
            items += f"{description:<23}{amount:>7}\n"
        # Total line
        total = f"Total: {self.balance:.2f}"

        return title + items + total

    def deposit(self, amount, desc = ""):
    #adds deposit info to ledger and updates balance attribute
        dep_entry = {"amount": amount,"description": desc}
        self.ledger.append(dep_entry)
        self.balance += float(amount)

    def check_funds(self, amount):
    #checks if balance is < or > than amount given
        if amount > self.balance:
            return False
        else:
            return True
        
    def withdraw(self, amount, desc = ""):
    #adds withdrawl details if the account balance is enough
        if self.check_funds(amount):
            if amount > 0:
                #store as negative number
                amount = (-1)*(amount)
            wdraw_entry = {"amount" : amount,"description" : desc}
            self.ledger.append(wdraw_entry)
            self.balance += float(amount)
            return True
        else:
            return False
        
    def get_balance(self):
        #returns current balance
        return self.balance

    def transfer(self, amount, other_catagory):
    #transfer to other catagory object
        if self.check_funds(amount):
            wdraw_string = f"Transfer to {other_catagory.name}"
            dep_string = f"Transfer from {self.name}"
            self.withdraw(amount,wdraw_string)
            other_catagory.deposit(amount,dep_string)
            return True
        else:
            return False


def create_spend_chart(categories):
    # Get total withdrawls for each category
    withdrawals = []
    for category in categories:
        total = 0
        for item in category.ledger:
            if item["amount"] < 0:
                total += -item["amount"]
        withdrawals.append(total)

    # Calculate spending percentages
    total_spent = sum(withdrawals)
    percentages = [int((w / total_spent) * 100) for w in withdrawals]

    # Round down to nearest 10
    percentages = [p - (p % 10) for p in percentages]

    # Chart header
    chart = "Percentage spent by category\n"

    # chart 
    for i in range(100, -1, -10):
        line = str(i).rjust(3) + "|"
        for p in percentages:
            if p >= i:
                line += " o "
            else:
                line += "   "
        chart += line + " \n"

    # Separator line
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # Category labels (vertical)
    max_len = max(len(cat.name) for cat in categories)
    for i in range(max_len):
        line = "     "
        for cat in categories:
            if i < len(cat.name):
                line += cat.name[i] + "  "
            else:
                line += "   "
        if i < max_len - 1:
            chart += line + "\n"
        else:
            chart += line

    return chart
