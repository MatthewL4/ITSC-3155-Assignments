import data
from sandwich_maker import SandwichMaker
from cashier import Cashier

# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()


def main():
    while True:
        print("What would you like? (small/ medium/ large/ off/ report)")
        choice = input().lower()

        if choice in ["small", "medium", "large"]:
            order_ingredients = recipes[choice]["ingredients"]
            cost = recipes[choice]["cost"]
            if sandwich_maker_instance.check_resources(order_ingredients):
                coins = cashier_instance.process_coins()
                if cashier_instance.transaction_result(coins, cost):
                    sandwich_maker_instance.make_sandwich(choice, order_ingredients)
                    print(f"{choice} sandwich is ready. Bon appetit!")
            else:
                print("Sorry, there is not enough bread.")
        elif choice == "off":
            print("Turning off machine")
            break
        elif choice == "report":
            for ingredient, quantity in sandwich_maker_instance.machine_resources.items():
                print(f"{ingredient}: {quantity}")


if __name__ == "__main__":
    main()
