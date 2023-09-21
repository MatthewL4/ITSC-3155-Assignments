class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        ###
        coins = {"dollar": 1, "half dollar": 0.5, "quarter": 0.25, "nickel": 0.05}
        total_amount = 0
        for coin in coins:
            try:
                amount = int(input(f"How many {coin}" + "s?: "))
                total_amount += amount * coins[coin]
            except ValueError:
                pass
        return total_amount

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        ##
