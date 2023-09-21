### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for ingredient, quantity in ingredients.items():
            if self.machine_resources.get(ingredient) < quantity:
                return False
            return True

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
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
        if coins < cost:
            print("Sorry that is not enough money. Money refunded.")
            return False
        else:
            change = coins - cost
            if change > 0:
                print(f"Here is ${change} in change")
            return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        for ingredient, quantity in order_ingredients.items():
            self.machine_resources[ingredient] -= quantity


### Make an instance of SandwichMachine class and write the rest of the codes ###
sandwich_machine = SandwichMachine(resources)

while True:
    print("What would you like? (small/ medium/ large/ off/ report)")
    choice = input().lower()

    if choice in ["small", "medium", "large"]:
        order_ingredients = recipes[choice]["ingredients"]
        cost = recipes[choice]["cost"]
        if sandwich_machine.check_resources(order_ingredients):
            coins = sandwich_machine.process_coins()
            if sandwich_machine.transaction_result(coins, cost):
                sandwich_machine.make_sandwich(choice, order_ingredients)
                print(f"{choice} sandwich is ready. Bon appetit!")
        else:
            print("Sorry, there is not enough bread.")
    elif choice == "off":
        print("Turning off machine")
        break
    elif choice == "report":
        for ingredient, quantity in sandwich_machine.machine_resources.items():
            print(f"{ingredient}: {quantity}")
